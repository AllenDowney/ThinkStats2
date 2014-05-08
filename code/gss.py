"""This file contains code related to "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

"""
Data Files:
http://sda.berkeley.edu/cgi-bin/hsda2?setupfile=harcsda&datasetname=gss10&ui=2&action=subset

"""

import bisect
import copy
import csv
import HTML
import math
import random
import re
import shelve

import columns
import glm
import thinkstats2
import thinkplot

import numpy as np
import matplotlib.pyplot as pyplot

import rpy2
import rpy2.robjects as robjects
import rpy2.rinterface as rinterface


ORDER_NA = ['prot', 'cath', 'jew', 'other', 'none', 'NA']
ORDER = ['prot', 'cath', 'jew', 'other', 'none']

COLORS = ['orange', 'green', 'blue', 'yellow', 'red']
ALPHAS = [0.5,      0.5,      0.5,    0.8,      0.5]


PROPER_NAME = dict(prot='Protestant', cath='Catholic', jew='Jewish', 
                   other='Other', none='None', any='Any')

USE_PARENT_DATA = True


def clean_var(val, na_codes):
    """Replaces invalid codes with NA."""
    if val in na_codes:
        return 'NA'
    else:
        return val


def meets_thresh(val, thresh):
    """Returns NA if val is NA, 1 if the value meets or exceeds thresh, 
    0 otherwise.

    val: value
    thresh: threshold
    """
    if val == 'NA':
        return 'NA'
    if val >= thresh:
        return 1
    return 0


class Respondent(object):
    """Represents a survey respondent.

    Attributes are set in columns.read_csv.
    """ 
    # map from field name to conversion function
    convert = dict(compwt=float, sei=float, masei=float, pasei=float)

    # divide Protestants into denominations?
    divide_prot = False

    # code table for relig and related attributes
    religions = {
        0:'NA',
        1:'prot',
        2:'cath',
        3:'jew',
        4:'none',
        5:'other',
        6:'other',
        7:'other',
        8:'other',
        9:'other',
        10:'other',
        11:'prot',
        12:'other',
        13:'other',
        98:'NA',
        99:'NA',
        }

    # code table for Protestant denominations
    denoms = dict(
        bap = range(10, 20),
        meth = range(20, 30),
        luth = range(30, 40),
        pres = range(40, 50),
        episc = range(50, 60),
        )

    switch_dict = dict(
        prot = (100000, 200000),
        cath = (200000, 300000),
        jew = (300000, 400000),
        none = (400000, 500000),
        other = (500000, 600000),
        )

    switwhy_dict = {
        10: 'marriage',
        20: 'friends',
        30: 'family',
        40: 'location',
        50: 'theological',
        77: 'positive beliefs',
        0: 'NA',
        99: 'NA',
        }

    # codes for marelkid and parelkid
    relkid_dict = {
        0: 'NA',
        1: 'prot',
        2: 'cath',
        3: 'jew',
        4: 'other',
        5: 'other',
        6: 'other',
        7: 'none',
        8: 'NA',
        9: 'NA',
        }
    
    def clean(self):
        """Cleans respondent data."""
        self.clean_relig()

        if self.age > 89:
            self.yrborn = 'NA'
            self.decade = 'NA'
            self.age_group = 'NA'
            self.age_from_30 = 'NA'
            self.born_from_1960 = 'NA'
            self.age2 = 'NA'
        else:
            self.yrborn = self.year - self.age
            self.decade = int(self.yrborn / 10) * 10
            self.age_group = int(self.age / 10) * 10
            self.age_from_30 = self.age - 30
            self.born_from_1960 = self.yrborn - 1960
            self.age2 = self.age**2

        for method in [self.clean_socioeconomic,
                       self.clean_attend,
                       self.clean_internet,
                       self.clean_children,
                       self.clean_switch,
                       ]:
            try:
                method()
            except AttributeError:
                pass

    def is_complete(self, attrs):
        """Checks whether a respondent has all required variables.

        attrs: list of attributes

        Returns: boolean
        """
        t = [getattr(self, attr) for attr in attrs]
        complete = ('NA' not in t)
        return complete

    def clean_random(self):
        for attr in ['rand1', 'rand2']:
            x = random.randint(0, 1)
            setattr(self, attr, x)

    def clean_children(self):
        """Cleans data about the children.

        Only collected in 1994
        """
        # loop through the children to get the years they were born
        for i in range(1, 10):
            attr = 'kdyrbrn%d' % i
            year = getattr(self, attr)
            if year == 0 or year > 9995:
                setattr(self, attr, 'NA')

    def clean_socioeconomic(self):
        """Clean socioeconomic data.
        """
        self.income = clean_var(self.income, [0, 13, 98, 99])
        self.rincome = clean_var(self.rincome, [0, 13, 98, 99])
        self.top75_income = meets_thresh(self.income, 12)

        self.educ = clean_var(self.educ, [97, 98, 99])
        if self.educ == 'NA':
            self.educ_from_12 = 'NA'
        else:
            self.educ_from_12 = self.educ - 12

        self.college = 1 if self.educ >= 16 else 0
        self.high_school = 1 if self.educ >= 12 else 0

        self.sei = clean_var(self.sei, [-1, 99.8, 99.9])

        self.srcbelt = clean_var(self.srcbelt, [0])
        self.urban = 1 if self.srcbelt in [1] else 0
        self.rural = 1 if self.srcbelt in [6] else 0

        # these are last because they might be absent
        #self.paeduc = clean_var(self.paeduc, [97, 98, 99])
        #self.maeduc = clean_var(self.maeduc, [97, 98, 99])
        #self.pasei = clean_var(self.pasei, [-1, 99.8, 99.9])
        #self.masei = clean_var(self.masei, [-1, 99.8, 99.9])

    def clean_relig(self):
        """Clean religious data."""
        self.relig_name = self.lookup_religion(self.relig)
        self.relig16_name = self.lookup_religion(self.relig16)
        self.sprelig_name = self.lookup_religion(self.sprel)

        if self.year in [1991, 1998, 2008]:
            self.parelig_name = self.relkid_dict[self.parelkid]
            self.marelig_name = self.relkid_dict[self.marelkid]
        elif self.year in [1988]:
            self.parelig_name = self.lookup_religion(self.parelig)
            self.marelig_name = self.lookup_religion(self.marelig)
        else:
            self.parelig_name = 'NA'
            self.marelig_name = 'NA'

        def has_religion(name):
            """Returns 1 if name is a religion, 0 if it is none, NA otherwise.
            """
            if name == 'NA':
                return name
            if name == 'none':
                return 0
            return 1

        self.has_relig = has_religion(self.relig_name)
        self.had_relig = has_religion(self.relig16_name)
        self.pa_has = has_religion(self.parelig_name)
        self.ma_has = has_religion(self.marelig_name)
        self.sp_has = has_religion(self.sprelig_name)

        # do the parents have the same religion?
        if self.pa_has==1 and self.parelig_name==self.marelig_name:
            self.par_same = 1
        else:
            self.par_same = 0

        # raised in one of the parents' religions?
        if ((self.pa_has==1 and self.parelig_name==self.relig16_name) or
            (self.ma_has==1 and self.marelig_name==self.relig16_name)):
            self.raised = 1
        else:
            self.raised = 0

        # married in the same religion?
        if 'NA' in [self.relig_name, self.sprelig_name]:
            self.married_in = 'NA'
        else:
            if self.has_relig==1 and self.relig_name==self.sprelig_name:
                self.married_in = 1
            else:
                self.married_in = 0

    def clean_attend(self):
        """Clean data on church attendance."""
        if self.year in [1991, 1998, 2008]:
            self.attendpa = clean_var(self.attendpa, [0, 10, 98, 99])
            self.attendma = clean_var(self.attendma, [0, 10, 98, 99])
            thresh = 7   # nearly every week
        else:
            self.attendpa = 'NA'
            self.attendma = 'NA'
            self.attendkid = 'NA'
            return

        self.attendkid = 0
        if meets_thresh(self.attendpa, thresh):
            self.attendkid = 1
        if meets_thresh(self.attendma, thresh):
            self.attendkid = 1

    def clean_lib(self):
        """Clean data on how liberal the religions are.
        """
        self.lib = self.code_lib(self.relig_name, self.fund)
        self.pa_lib = self.code_lib(self.parelig_name, self.pafund)
        self.ma_lib = self.code_lib(self.marelig_name, self.mafund)

    def clean_internet(self):

        # replace several invalid codes with 'NA'
        self.compuse = clean_var(self.compuse, [0, 8, 9])
        self.webtv = clean_var(self.webtv, [0, 8, 9])
        self.webmob = clean_var(self.webmob, [0, 8, 9])
        self.emailhr = clean_var(self.emailhr, [-1, 998, 999])
        self.emailmin = clean_var(self.emailmin, [-1, 98, 99])
        self.usewww = clean_var(self.usewww, [0, 9])
        self.wwwhr = clean_var(self.wwwhr, [-1, 998, 999])
        self.wwwmin = clean_var(self.wwwmin, [-1, 98, 99])

        # the logic for cleaning these variables comes from
        # personal correspondence with J. Son at NORC.
        if self.year in [2000, 2002]:
            if self.compuse == 2 and self.webtv == 2:
                if self.wwwhr not in [0, 'NA']:
                    print 'anomaly1', self.year, self.caseid, self.compuse, 
                    print self.webtv, self.usewww, self.wwwhr
                else:
                    self.wwwhr = self.wwwmin = 0
            elif self.usewww == 2:
                assert self.wwwhr in [0, 'NA']
                self.wwwhr = self.wwwmin = 0

        if self.year == 2004:
            if self.compuse == 2 or self.usewww == 2:
                assert self.wwwhr in [0, 'NA']
                self.wwwhr = self.wwwmin = 0

        # in 2010 and 2012, wwwhr was only asked for respondents
        # who reported no email use, which is a bizarre subset.
        # I don't know what they were thinking!
        if self.year in [2010, 2012]:
            #if self.wwwhr not in [0, 'NA']:
            #    print 'anomaly2', self.year, self.caseid, self.compuse, 
            #    print self.webmob, self.emailhr, self.usewww, self.wwwhr

            if self.compuse == 2 and self.webmob == 2:
                if self.wwwhr not in [0, 'NA']:
                    print 'anomaly3', self.year, self.caseid, self.compuse, 
                    print self.webmob, self.usewww, self.wwwhr
                else:
                    self.wwwhr = self.wwwmin = 0

            elif self.usewww == 2:
                assert self.wwwhr in [0, 'NA']
                self.wwwhr = self.wwwmin = 0

        self.recode_internet()

    def recode_internet(self):
        """Computes wwwhr and related variables."""

        # add wwwmin into wwwhr as a fraction
        if 'NA' not in [self.wwwhr, self.wwwmin]:
            self.wwwhr += self.wwwmin / 60.0
             
        self.www2 = meets_thresh(self.wwwhr, 2)
        self.www7 = meets_thresh(self.wwwhr, 7)
        self.www14 = meets_thresh(self.wwwhr, 14)
        self.www20 = meets_thresh(self.wwwhr, 20)
        
    def clean_income(self):
        """Computes income-related variables."""
        try:
            self.orig_income = int(self.orig_income)
        except ValueError:
            self.orig_income = 'NA'
        self.top50_income = meets_thresh(self.orig_income, 21)
        
    def code_lib(self, relig_name, fund):
        """Code how liberal a relion is."""
        if relig_name == 'none':
            return 4
        if fund in [1,2,3]:
            return fund
        else:
            return 'NA'
                
    def clean_switch(self):
        """Clean data on switching religions."""
        self.switch1 = self.lookup_switch(self.switch1)
        self.switch2 = self.lookup_switch(self.switch2)
        self.switch3 = self.lookup_switch(self.switch3)
        self.switwhy1 = self.lookup_switwhy(self.switwhy1)
        self.switwhy2 = self.lookup_switwhy(self.switwhy2)

    def lookup_religion(self, relig, denom=None):
        """Converts religion codes to string names.

        relig: code from relig and related fields
        denom: code from denom and related fields

        Returns: string
        """
        relname = relig

        if relig in self.religions:
            relname = self.religions[relig]

        if self.divide_prot and relig == 1:
            for denom_name, codes in self.denoms.iteritems():
                if denom in codes:
                    relname = denom_name

        return relname

    def lookup_switch(self, switch):
        """Converts religion codes to string names.

        switch: code from one of the switch fields

        Returns: string
        """
        if switch in [0, 999999]:
            return 'NA'

        for name, (low, high) in self.switch_dict.iteritems():
            if low <= switch < high:
                return name

        return '?'

    def lookup_switwhy(self, switwhy):
        """Converts reason codes to text.

        switch: code from one of the switwhy fields

        Returns: string
        """
        try:
            return self.switwhy_dict[switwhy]
        except KeyError:
            return 'other'

    def ages_when_child_born(self):
        """Returns a list of the respondent's age when children were born."""
        ages = []
        for i in range(1, self.childs+1):
            attr = 'kdyrbrn%d' % i
            child_born = getattr(self, attr)
            if child_born == 'NA':
                return 'NA'
            age_when_born = child_born - self.yrborn
            ages.append(age_when_born)

        return ages

    def make_child(self, yrborn, trans_model):
        """Generates a child based on the attributes of the parent.

        yrborn: int, year the child is born
        trans_model: TransitionModel

        Returns: Respondent
        """
        child = Respondent()
        child.parent = self
        child.get_next_id()
        child.compwt = self.compwt
        child.yrborn = yrborn
        
        child.relig16_name = trans_model.choose_upbringing(yrborn,
                                                           self.relig_name)
        child.relig_name = trans_model.choose_transmission(yrborn,
                                                           child.relig16_name) 
        return child

    def get_next_id(self, t=[90000]):
        """Assigns the next available case ID.

        t = list containing the next availabe ID
        """
        self.caseid = t[0]
        t[0] += 1


def read_survey(filename):
    survey = Survey()
    survey.read_csv(filename, Respondent)
    return survey


class Survey(object):
    """Represents a set of respondents as a map from caseid to Respondent."""

    def __init__(self, rs=None):
        if rs is None:
            self.rs = {}
        else:
            self.rs = rs
        self.cdf = None

    def add_respondent(self, r):
        """Adds a respondent to this survey."""
        self.rs[r.caseid] = r

    def add_respondents(self, rs):
        """Adds respondents to this survey."""
        [self.add_respondent(r) for r in rs]

    def len(self):
        """Number of respondents."""
        return len(self.rs)

    def respondents(self):
        """Returns an iterator over the respondents."""
        return self.rs.itervalues()

    def lookup(self, caseid):
        """Looks up a caseid and returns the Respondent object."""
        return self.rs[caseid]

    def read_csv(self, filename, constructor):
        """Reads a CSV file, return the header line and a list of objects.

        filename: string filename
        """
        objs = columns.read_csv(filename, constructor)
        for obj in objs:
            self.rs[obj.caseid] = obj

    def get_income_data(self, filename='gss.income_data.db'):
        income_data = IncomeData(filename)
        for r in self.respondents():
            r.orig_income = income_data.lookup(r.year, r.id)
            r.clean_income()
        income_data.close()

    def make_pmf(self, attr, na_flag=False):
        """Make a PMF for an attribute.  Uses compwt to weight respondents.

        attr: string attr name
        na_flag: boolean, whether to remove NAs

        Returns: normalized PMF
        """
        pmf = thinkstats2.Pmf()
        for r in self.respondents():
            val = getattr(r, attr)
            wt = r.compwt
            pmf.Incr(val, wt)

        if na_flag:
            pmf.Set('NA', 0)

        pmf.Normalize()
        return pmf

    def print_pmf(self, attr):
        """Print the PMF of an attribute.

        attr: sting attribute name
        """
        print attr
        pmf = self.make_pmf(attr)
        print_pmf_sorted(pmf)

    def summarize_binary_attrs(self, attrs):
        """Summarize survey attributes.

        Prints the probability that the val is 1.

        attrs: list of string attr names
        """
        for attr in attrs:
            try:
                pmf = self.make_pmf(attr)
                percent = pmf.Prob(1) * 100
                print '%11s\t%0.1f' % (attr, percent)
            except ValueError:
                print '%11s\tNA' % (attr)

    def make_age_pmf(self, survey_year):
        """Make a PMF for an attribute.  Uses compwt to weight respondents.

        survey_year: when the respondent is asked his or her age

        Returns: normalized PMF
        """
        pmf = thinkstats2.Pmf()
        for r in self.respondents():
            if r.yrborn == 'NA':
                continue

            age = survey_year - r.yrborn
            wt = r.compwt
            pmf.Incr(age, wt)

        pmf.Normalize()
        return pmf

    def self_information_partition(self, attr, model):
        """Computes the self information of a partition.

        Does not take into account compwt

        attr: string binary attribute
        model: object with a fit_prob method that takes a respondent

        Returns: float number of bits
        """
        def log2(x, denom=math.log(2)):
            return math.log(x) / denom

        total = 0.0
        n = 0.0
        for r in self.respondents():
            x = getattr(r, attr)
            if x == 'NA':
                # if we don't know the answer, we got zero bits of info
                continue

            p = model.fit_prob(r)
            assert p != 'NA'

            if x == 1:
                total += -log2(p)
            elif x == 0:
                total += -log2(1-p)
            else:
                raise ValueError('Values must be 0, 1 or NA')

        return total

    def make_cdf(self):
        """Makes a CDF with caseids and weights.

        Cdf.Random() selects from this CDF in proportion to compwt
        """
        items = [(caseid, r.compwt) for caseid, r in self.rs.iteritems()]
        self.cdf = thinkstats2.MakeCdfFromItems(items)

    def partition_by_attr(self, attr):
        """Makes a map from year to Survey.

        attr: string attribute to be used as a key
        """
        surveys = {}
        for r in self.respondents():
            val = getattr(r, attr)
            if val == 'NA':
                continue

            if val not in surveys:
                surveys[val] = Survey()
            surveys[val].add_respondent(r)
        return surveys

    def make_series(self, attr):
        """Makes a times series for the given attribute.

        attr: string attribute name
        
        Returns: Series
        """
        d = {}
        for r in self.respondents():
            val = getattr(r, attr)
            if r.year not in d:
                d[r.year] = thinkstats2.Pmf()
            d[r.year].Incr(val, r.compwt)

        for pmf in d.itervalues():
            pmf.Normalize()

        return Series(d)

    def cross_tab(self, attr1, attr2):
        """Cross tabulates two attributes.

        attr1: string attribute name
        attr2: string attribute name

        Returns: Table
        """
        table = {}
        hist = thinkstats2.Hist()

        for name in ORDER:
            table[name] = thinkstats2.Pmf()

        for r in self.respondents():
            x = getattr(r, attr1)
            y = getattr(r, attr2)
            if x=='NA' or y=='NA':
                continue

            table[x].Incr(y, r.compwt)
            hist.Incr(x, r.compwt)

        normalize_table(table)
        return Table(table, hist)

    def make_religiosity_curves(self):
        """Makes religiosity curves for each of the religions."""
        surveys = self.partition_by_attr('relig16_name')

        curves = []
        for name in ORDER:
            survey = surveys[name]
            curve = survey.make_religiosity_curve()
            curves.append(curve)

        pyplot.clf()
        plot_relig_curves(curves)
        thinkplot.Show()

    def make_religiosity_curves_by_decade(self, relig_name, age_flag=True):
        """Plots fraction with religion as a function of age.

        Partitioned by decade of birth.

        relig_name: string religion name to plot
        age_flag: whether to use age or year of survey as x-axis
        """
        surveys = self.partition_by_attr('decade')

        curves = []
        labels = []
        for decade, survey in sorted(surveys.iteritems()):
            if decade in [1890, 1980] or survey.len() < 300:
                continue
            curve = survey.make_religiosity_curve(age_flag)
            labels.append(str(decade))
            if not age_flag:
                curve = normalize_curve(curve, 1990)
            curves.append(curve)

        if age_flag:
            root = 'gss.religiosity.%s' % relig_name
            xlabel = 'Age when surveyed'
        else:
            root = 'gss.religiosity.by.year.normalized.%s' % relig_name
            xlabel = 'Survey year'
            
        title = 'Religiosity curves, %s' % PROPER_NAME[relig_name]

        pyplot.clf()
        plot_curves(curves, labels)
        thinkplot.Save(root=root,
                    title=title,
                    xlabel=xlabel,
                    ylabel='Fraction with any religion',
                    )

    def make_religiosity_contour_by_decade(self, relig_name):
        """Plots fraction with religion as a function of age.

        Partitioned by decade of birth.

        relig_name: string religion name to plot
        """
        surveys = self.partition_by_attr('decade')

        d = {}
        for decade, survey in sorted(surveys.iteritems()):
            if decade in [1890, 1980] or survey.len() < 300:
                continue
            curve = survey.make_religiosity_curve()

            for year, z in zip(*curve):
                d[year, decade] = z

        root = 'gss.contour.%s' % relig_name
        title = 'Religiosity contour, %s' % PROPER_NAME[relig_name]

        pyplot.clf()
        thinkplot.Contour(d)
        thinkplot.Save(root=root,
                    title=title,
                    xlabel='Year surveyed',
                    ylabel='Decade born',
                    )

    def make_religiosity_curve(self, age_flag=True):
        """Makes a religiosity curve.

        Fraction with some religion vs. age when surveyed.

        age_flag: whether to use age or year surveyed as the x-axis

        Returns: curve (pair of lists)
        """
        d = {}
        for r in self.respondents():
            if r.relig_name == 'NA':
                continue

            if age_flag:
                x = r.age_group
            else:
                x = (r.year / 5) * 5

            if x not in d:
                d[x] = thinkstats2.Hist()
                
            d[x].Incr(r.relig_name != 'none')

        rows = []
        for x, hist in sorted(d.iteritems()):
            if hist.Total() < 30:
                continue
            fraction = fraction_true(hist)
            rows.append((x, fraction))

        curve = zip(*rows)
        return curve

    def deepcopy(self):
        return copy.deepcopy(self)

    def resample(self, n=None):
        """Form a new cohort by resampling from this survey.

        n: number of respondents in new sample
        """
        if self.cdf is None:
            self.make_cdf()

        n = n or len(self.rs)
        resample = self.resample_by_cdf(self.cdf, n)
        
        # after resampling, all respondents have the same weight
        [setattr(r, 'compwt', 1) for r in resample.respondents()]

        return resample

    def resample_by_age(self, n, year, age_pmf):
        """Form a new cohort by resampling from this survey.

        n: number of respondents in new sample
        """
        current_age_pmf = self.make_age_pmf(year)

        items = []
        for caseid, r in self.rs.iteritems():
            if r.yrborn == 'NA':
                continue

            age = year - r.yrborn
            weight = age_pmf.Prob(age) / current_age_pmf.Prob(age)
            items.append((caseid, weight))
        
        cdf = thinkstats2.MakeCdfFromItems(items)
        return self.resample_by_cdf(cdf, n)

    def resample_by_cdf(self, cdf, n):
        """Form a new cohort by drawing from the given CDF.

        cdf: CDF of caseids
        n: sample size
        """
        ids = cdf.Sample(n)
        rs = dict((i, self.rs[caseid]) for i, caseid in enumerate(ids))
        return Survey(rs)

    def subsample(self, filter_func):
        """Form a new cohort by filtering respondents

        filter_func: function that takes a respondent and returns boolean

        Returns: Survey
        """
        pairs = [(r.caseid, r) for r in self.respondents() if filter_func(r)]
        rs = dict(pairs)
        return Survey(rs)

    def counterfactual(self, modify_func):
        """Form a new cohort by applying a function to all respondents

        modify_func: function that takes a respondent, modifies it
                     and returns it

        Returns: Survey
        """
        pairs = [(r.caseid, modify_func(r)) for r in self.respondents()]
        rs = dict(pairs)
        return Survey(rs)

    def simulate_model(self, model):
        """Counts the number of respondents with some property, under a model.

        model: any object with a fit_prob function

        Returns: float, fraction of respondents with the property
        """
        count = 0.0
        total = 0.0
        for r in self.respondents():
            p = model.fit_prob(r)
            count += p * r.compwt
            total += r.compwt

        return count / total

    def investigate_conversions(self, old, new):
        switches = []

        for r in self.respondents():
            if r.relig16_name != old or r.relig_name != new:
                continue
            
            print r.switch1, r.switch2, r.switch3

    def investigate_switches(self, old, new):
        switches = []

        for r in self.respondents():
            switch1 = Switch(r.switch1, r.switch2,
                             r.switage1, r.switwhy1)
            switch2 = Switch(r.switch2, r.switch3,
                             r.switage2, r.switwhy2)

            if switch1.match(old, new):
                switches.append(switch1)

            if switch2.match(old, new):
                switches.append(switch2)

        for switch in switches:
            print switch.age, switch.why


    def partition_by_yrborn(self, attr, bin_size=10):
        """Partition the sample by binning birthyear.

        attr: which attribute to collect
        bin_size: number of years in each bin

        Returns: map from decade year to Pmf of values
        """
        d = {}
        for r in self.respondents():
            if r.yrborn == 'NA':
                continue

            decade = r.decade
            if decade not in d:
                d[decade] = thinkstats2.Pmf()
            val = getattr(r, attr)
            d[decade].Incr(val, r.compwt)

        for pmf in d.itervalues():
            pmf.Normalize()

        return d

    def count_partition(self, d, val):
        """Returns a time series of probabilities for the given value.

        d: map from decade year to Pmf of values
        val: which value to select

        Returns: list of (year, prob) pairs
        """
        rows = []
        for year, pmf in sorted(d.iteritems()):
            p = pmf.Prob(val)
            rows.append((year, p))
        return rows

    def regress_by_yrborn(self, attr, val):
        """Performs a regression on a variable vs year born.

        Logistic regression of the fraction where the given
        attribute has the given value.

        attr: dependent variable
        val: value of the variable

        Returns a Regression object.
        """
        rows = []

        for r in self.respondents():
            if r.yrborn == 'NA':
                continue

            y = 1 if getattr(r, attr) == val else 0
            x = r.yrborn - 1900

            rows.append((y, x))

        ys, xs = zip(*rows)
        x2s = [x**2 for x in xs]
        col_dict = dict(y=ys, x=xs, x2=x2s)
        glm.inject_col_dict(col_dict)

        return Regression(xs)

    def logistic_regression(self, model, print_flag=False):
        """Performs a regression.

        model: string model in r format
        print_flag: boolean, whether to print results

        Returns: LogRegression object
        """
        def clean(attr):
            m = re.match('as.factor\((.*)\)', attr)
            if m:
                return m.group(1)
            return attr
                
        # pull out the attributes in the model
        rows = []
        t = model.split()
        attrs = [clean(attr) for attr in model.split() if len(attr)>1]

        for r in self.respondents():
            row = [getattr(r, attr) for attr in attrs]
            rows.append(row)

        rows = [row for row in rows if 'NA' not in row]

        # inject the data and runs the model
        col_dict = dict(zip(attrs, zip(*rows)))
        glm.inject_col_dict(col_dict)

        res = glm.logit_model(model, print_flag=print_flag)

        return LogRegression(res)

    def make_logistic_regression(self, dep, control, exp_vars=[]):
        """Runs a logistic regression.

        dep: string dependent variable name
        control: list of string control variables
        exp_vars: list of string independent variable names

        Returns: LogRegression object
        """
        s = ' + '.join(control + exp_vars)
        model = '%s ~ %s' % (dep, s)

        reg = self.logistic_regression(model)

        null_model = make_null_model(self, dep)
        reg.null_sip = self.self_information_partition(dep, null_model)

        reg.model_sip = self.self_information_partition(dep, reg)
        reg.sip = reg.null_sip - reg.model_sip

        print reg.null_sip, reg.model_sip, reg.sip

        return reg

    def make_logistic_regressions(self, dep, control, exp_vars):
        """Runs multiple logistic regressions.

        Prints results

        dep: string dependent variable name
        control: list of string control variables
        exp_vars: list of string independent variable names

        Returns: list of LogRegression objects
        """
        regs = []

        # run the control model
        if control:
            reg = self.make_logistic_regression(dep, control)
            regs.append(reg)

        # run each explanatory model
        for attr in exp_vars:
            reg = self.make_logistic_regression(dep, control, [attr])
            regs.append(reg)

        return regs

    def iterate_respondent_child_ages(self):
        """Loops through respondents and generates (respondent, ages) pairs.

        Where ages is the list of ages at which this parent had children.

        Skips parents with unknown year of birth or any children with
        unknown year of birth.
        """
        for r in self.respondents():
            if r.yrborn == 'NA':
                continue

            ages = r.ages_when_child_born()
            if ages == 'NA':
                continue

            yield r, ages

    def plot_child_curves(self):
        """Makes a plot showing child curves for parent's decade of birth."""
        d = {}
        for r, ages in self.iterate_respondent_child_ages():
            for age in range(13, r.age):
                if (r.decade, age) not in d:
                    d[r.decade, age] = thinkstats2.Hist()
                # record whether this person had a child at this age
                d[r.decade, age].Incr(age in ages)

        table = np.zeros(shape=(8,90), dtype=np.float)
        for (decade, age), hist in sorted(d.iteritems()):
            index = (decade-1900)/10
            table[index, age] = fraction_true(hist)

        self.child_table = table

        decades, all_ages = zip(*d.iterkeys())
        decades = set(decades)
        ages = [age for age in set(all_ages) if age < 50]
        ages.sort()

        options = dict(lw=3, alpha=0.5)

        for decade in sorted(decades):
            if decade < 1930:
                continue
            label = str(decade)
            index = (decade-1900)/10
            ys = np.cumsum([table[index, age] for age in ages])
            thinkplot.Plot(ages, ys, label=label, **options)

        thinkplot.Save(root='gss4',
                    xlabel='Age of parent',
                    ylabel='Cumulative number of children',
                    )

    def plot_child_curve(self):
        """Makes a plot showing cumulative children vs age.
        """
        model = self.make_birth_model()
        ages = [age for age in model.all_ages if age < 50]
        ages.sort()

        table = model.table
        ps = [table[age] for age in ages]
        ys = np.cumsum(ps)
        thinkplot.Plot(ages, ys, color='purple', 
                    lw=3, alpha=0.5, linestyle='dashed', label='model')

        thinkplot.Save(root='gss5',
                    xlabel='Age of parent',
                    ylabel='Cumulative number of children',
                    )

    def make_birth_model(self):
        """Makes a model of the probability of having a child at a given age.

        Returns: BirthModel object
        """
        d = {}
        for r, ages in self.iterate_respondent_child_ages():
            if r.decade < 1940:
                continue

            # loop through the ages we know about for this respondent
            for age in range(13, r.age):
                if age not in d:
                    d[age] = thinkstats2.Hist()
                # record whether this person had a child at this age
                d[age].Incr(age in ages)

        table = np.zeros(shape=(90), dtype=np.float)
        for age, hist in sorted(d.iteritems()):
            table[age] = fraction_true(hist)

        all_ages = set(d.iterkeys())
        return BirthModel(all_ages, table)

    def age_cohort(self, val, start, end):
        """Runs one simulation of the aging cohort.

        val: which religion name to track
        start: low end of the range of year to age by
        end: high end of the range of year to age by

        Returns: a time series of (year, fraction) pairs
        """
        # resample and estimate a linear model
        resampled = self.resample()
        reg = resampled.regress_by_yrborn('relig_name', val)
        fit = reg.linear_model()

        # resample again before aging
        cohort = self.resample()

        # loop through the years and accumulate results
        series = []
        for delta in range(start, end+1):

            total = 0
            count = 0
            for r in cohort.respondents():
                year = r.year + delta
                fake_yrborn = year - r.age
                p = reg.fit_prob(fake_yrborn)

                total += 1
                if random.random() <= p:
                    count += 1

            fraction = float(count) / total
            series.append((year, fraction))

        return series

    def simulate_aging_cohort(self, val, start, end, n=20):
        """Simulates the aging of the cohort for one year
 
        Generates a plot of the results.

        val: which religion name to track
        start: low end of the range of year to age by
        end: high end of the range of year to age by
        n: how many simulations to run
        """
        pyplot.clf()
        random.seed(17)

        # run the simulation
        all_ps = {}
        for i in range(n):
            series = self.age_cohort(val, start, end)
            for x, p in series:
                all_ps.setdefault(x, []).append(p)

        # plot the simulated data
        xs, means = plot_interval(all_ps, color='0.9')
        thinkplot.Plot(xs, means, color='blue', lw=3, alpha=0.5)

        # plot the real data
        series = Series()
        data = get_series_for_val(series, val)
        xs, ps = zip(*data)
        thinkplot.Plot(xs, ps, color='red', lw=3, alpha=0.5)

        axes = dict(
            none=[1968, 2011, 0, 0.16],
            prot=[1968, 2011, 0, 1],
            cath=[1968, 2011, 0, 0.5],
            jew=[1968, 2011, 0, 0.2],
            other=[1968, 2011, 0, 0.2],
            )

        thinkplot.Save(root='gss2',
                    xlabel='Year of survey',
                    ylabel='Fraction with relig=%s' % val,
                    axis=axes[val]
                    )

    def plot_relig_vs_yrborn(self, val):
        """Makes a plot of religious preference by year.

        val: string, which religion name to track.
        """
        random.seed(19)

        # plot some resampled fits
        all_ps = {}
        all_rows = {}
        for i in range(4):
            print i
            resampled = self.resample()

            # collect the partitioned estimates
            d = resampled.partition_by_yrborn('relig_name')
            rows = resampled.count_partition(d, val)
            for x, p in rows:
                all_rows.setdefault(x, []).append(p)

            # collect the resampled values
            reg = resampled.regress_by_yrborn('relig_name', val)
            fit = reg.linear_model()
            for x, p in fit:
                all_ps.setdefault(x, []).append(p)

        plot_interval(all_ps, color='0.9')

        # plot the real fit
        reg = self.regress_by_yrborn('relig_name', val)
        fit = reg.linear_model()
        xs, ps = zip(*fit)
        thinkplot.Plot(xs, ps, lw=3, color='blue', alpha=0.5)

        # plot the real data with error bars
        d = self.partition_by_yrborn('relig_name')
        rows = self.count_partition(d, val)
        xs, ps = zip(*rows[1:-1])

        plot_errorbars(all_rows, lw=1, color='red', alpha=0.5)
        thinkplot.Plot(xs, ps, marker='s', markersize=8, 
                    lw=0, color='red', alpha=0.5)

        axes = dict(
            none=[1875, 1995, 0, 0.4],
            prot=[1895, 1965, 0, 1],
            cath=[1895, 1965, 0, 0.5],
            jew=[1895, 1965, 0, 0.2],
            other=[1865, 1995, 0, 0.5],
            )

        # make the figure
        thinkplot.Save(root='gss1',
                    xlabel='Year born',
                    ylabel='Prob of relig=%s' % val,
                    axis=axes[val])

    def run_transition_model(self, model_factory, n=20):
        """Runs a model based on given transition data.

        model_factory: function that returns a resampled transition model
        n: number of iterations

        Returns: list of (mean, span) pairs
        """
        before = self.print_state_vector()

        data = []
        for i in range(n):
            trans_model = model_factory()
            next_gen = trans_model.next_gen(self, resample_flag=True)
            after = next_gen.print_state_vector(head_flag=False)
            data.append(after)

        preds = self.extract_predictions(data)
        return preds

    def extract_predictions(self, data):
        """Gets predictions from simulation results.
        
        data: list of state vectors (5-tuples)
        
        Returns: list of (mean, span) pairs
        """
        cols = zip(*data)

        preds = []
        for col in cols:
            mean = thinkstats2.Mean(col)
            col = list(col)
            col.sort()
            span = col[1], col[-2]
            preds.append((mean, span))

        return preds
            
    def print_state_vector(self, attr='relig_name', head_flag=True):
        """Prints the state of the given attribute.

        attr: string attribute name
        head_flag: boolean, whether to print the header line

        Returns: np state array
        """
        pmf = self.make_pmf(attr)
        vector = pmf_to_vector(pmf)
        print_vector(vector, head_flag)
        return vector


def normalize_curve(curve, year):
    years, ys = curve
    index = bisect.bisect(years, year) - 1
    denom = ys[index]
    ys = [y/denom for y in ys]
    return years, ys


class TransitionModel2(object):
    def __init__(self, survey, decade_flag=False):
        """Makes the simplified transition model.

        survey: Survey object
        """
        self.decade_flag = decade_flag

        self.up_table = survey.cross_tab('parelig_name', 'relig16_name')
        self.trans_table = survey.cross_tab('relig16_name', 'relig_name')

        surveys = survey.partition_by_attr('decade')
        self.up_tables = make_cross_tabs(surveys, 
                                         'parelig_name', 'relig16_name')
        self.trans_tables = make_cross_tabs(surveys, 
                                            'relig16_name', 'relig_name')

    def extend_tables(self, attr, source_year, dest_years):
        """Copies tables from the source_year into the dest_years.

        source_year: int
        dest_years: list of int
        """
        tables = getattr(self, attr)
        if True:
            print attr
            for year, table in sorted(tables.iteritems()):
                print year, table.hist.Total()
            print source_year, dest_years

        source = tables[source_year]
        for dest_year in dest_years:
            tables[dest_year] = source

    def choose_upbringing(self, yrborn, relig_name):
        """Choose how a parent will raise a child.

        yrborn: year the child is born
        relig_name: parent's religion

        Returns: string relig name
        """
        if self.decade_flag:
            decade = int(yrborn/10) * 10
            table = self.up_tables[decade]
            try:
                return table.choose(relig_name)
            except EmptyPmfError:
                return self.up_table.choose(relig_name)
        else:
            return self.up_table.choose(relig_name)

    def choose_transmission(self, yrborn, relig_name):
        """Choose the child's religion.

        yrborn: year the child is born
        relig_name: string name of religion child raised in

        Returns: string relig name
        """
        if self.decade_flag:
            decade = int(yrborn/10) * 10
            table = self.trans_tables[decade]
            return table.choose(relig_name)
        else:
            return self.trans_table.choose(relig_name)

    def plot_upbringing_elements(self):
        """Plots elements from upbringing tables as a time series.
        """
        for name in ['prot', 'cath', 'none']:
            plot_element(self.up_tables, name)
            root = 'gss.upbringing.%s' % name
            title = "Parent's religion %s" % PROPER_NAME[name]
            thinkplot.Save(root=root,
                        xlabel='Decade respondent born',
                        ylabel='Religious upbringing of respondent',
                        title=title,
                        )

    def plot_transmission_elements(self):
        """Plots elements from transmission tables as a time series.
        """
        for name in ['prot', 'cath', 'none']:
            plot_element(self.trans_tables, name)
            root = 'gss.transmission.%s' % name
            title = 'People raised %s' % PROPER_NAME[name]
            thinkplot.Save(root=root,
                        xlabel='Decade respondent born',
                        ylabel='Religious preference as adults',
                        title=title,
                        )

    def simulate_generation(self, survey, birth_model):
        """Generates one child for each respondent.

        survey: cohort of parents
        birth_model: BirthModel

        Returns: Survey
        """
        next_gen = Survey()
        for parent in survey.respondents():
            if 'NA' in [parent.relig_name, parent.yrborn]:
                continue

            age_when_born = birth_model.random_age()
            yrborn = parent.yrborn + age_when_born
            child = parent.make_child(yrborn, self)
            next_gen.add_respondent(child)

            # print parent.relig_name, child.relig_name

        return next_gen


class TransitionModel(object):
    """Represents the more detailed transition model."""
    
    def __init__(self, survey, resample_flag=False):
        """Makes and runs the transition model.

        Returns a vector of predictions.

        survey: Survey object
        resample_flag: boolean, whether to resample
        """
        if resample_flag:
            survey = survey.resample()

        self.spouse_table = SpouseTable(survey)
        self.env_table = EnvironmentTable(survey)
        self.trans_table = TransitionTable(survey, 'Transition table')

    def next_gen(self, survey, resample_flag=False):
        # generate the next generation
        next_gen = self.simulate_transition(survey, resample_flag)

        # compute the generation table (from parent to child religion)
        self.gen_table = TransitionTable(next_gen, 'Generation table',
                                    'fake_parent_relig_name', 'relig_name')

        return next_gen

    def simulate_transition(self, survey, resample_flag):
        """Simulates one generation.

        resample: boolean, whether to resample
        spouse_table: map from r's religion to Pmf of spouse's religion
        env_table: map from (ma, pa) religion to "raised religion"
        trans_table: map from raised religion to r's religion

        Returns: Survey object with next generation
        """
        if resample_flag:
            survey = survey.resample()

        next_gen = {}

        for r in survey.respondents():
            if r.relig_name == 'NA':
                continue

            # choose a random spouse
            sprelig_name = self.spouse_table.generate_spouse(r)

            # choose how to raise the child
            if r.sex == 1:
                raised = self.env_table.generate_raised(sprelig_name, 
                                                        r.relig_name)
            else:
                raised = self.env_table.generate_raised(r.relig_name, 
                                                        sprelig_name)

            # determine the child's religion
            relig_name = self.trans_table.generate_relig(raised)

            # make a Respondent object for the child
            child = copy.copy(r)
            child.fake_parent_relig_name = r.relig_name
            child.relig16_name = raised 
            child.relig_name = relig_name
            next_gen[child.caseid] = child

        return Survey(next_gen)

    def print_model(self):
        print 'prob same', self.spouse_table.prob_same()
        self.spouse_table.print_table()
        self.spouse_table.write_html_table()

        self.env_table.write_combined_table()
        for name in ORDER:
            print 'parent table (%s)' % name
            self.env_table.print_table(name)
            self.env_table.write_html_table(name)

        print 'trans table'
        self.trans_table.print_table()
        self.trans_table.write_html_table()

        print 'gen table'
        self.gen_table.print_table()
        self.gen_table.write_html_table()


class Series(object):
    """Represents a times series of PMFs."""

    def __init__(self, d):
        """Makes a Series.

        d: map from year to Pmf
        """
        self.d = d

    def print_series(self):
        """Prints a series of Pmfs."""
        for year, pmf in sorted(self.d.iteritems()):
            print year,
            for val, prob in sorted(pmf.Items()):
                percent = '%0.0f' % (prob * 100)
                print val, percent, 
            print

    def get_ratios(self, val1=1, val2=0):
        """Gets the ratios of two values in the PMFs.

        val1: value in Pmf
        val2: value in Pmf

        Returns: times series of float
        """
        rows = []
        for year, pmf in sorted(self.d.iteritems()):
            yes, no = pmf.Prob(val1), pmf.Prob(val2)
            if yes + no:
                percent = yes / (yes + no) * 100
                rows.append((year, percent))
            else:
                rows.append((year, None))                

        return rows

    def plot_series(self, val1=1, val2=0, label=''):
        """Plots rows.

        rows: list of (year, y) pairs
        """
        rows = self.get_ratios(val1, val2)
        years, ys = zip(*rows)
        thinkplot.Plot(years, ys, label=label)


def make_spouse_series():
    """Plots the fraction of spouses with the same religion."""
    survey = Survey()
    survey.read_csv('gss.series.csv', Respondent)
    
    series = survey.make_series('married_in')
    series.plot_series()
    thinkplot.Save(root='gss.spouse.series',
                title='Spouses with same religion',
                xlabel='Survey year',
                ylabel='% of respondents')


def make_spouse_table(low=1972, high=2010):
    """Makes the spouse tables reading data from the given year.

    low: int year
    high: int year

    Returns: SpouseTable
    """
    def filter_func(r):
        return low <= r.year <= high

    survey = Survey()
    survey.read_csv('gss.series.csv', Respondent)
    subsample = survey.subsample(filter_func)
    spouse_table = SpouseTable(subsample)
    return spouse_table


def make_env_table(year):
    """Makes the environment table reading data from the given year.

    year: int

    Returns: EnvironmentTable
    """
    survey = Survey()
    filename = 'gss%d.csv' % year
    survey.read_csv(filename, Respondent)
    env_table = EnvironmentTable(survey)
    return env_table


def make_trans_table(year):
    """Makes the transition table reading data from the given year.

    year: int

    Returns: TransitionTable
    """
    survey = Survey()
    filename = 'gss%d.csv' % year
    survey.read_csv(filename, Respondent)
    trans_table = TransitionTable(survey, 'Transition table')
    return trans_table


class Switch(object):
    """Encapsulates data about a religious conversion."""
    def __init__(self, old, new, age, why):
        self.old = old
        self.new = new
        self.age = age
        self.why = why

    def match(self, old, new):
        return self.old==old and self.new==new


class BirthModel(object):
    """Model of the probability of having a child at a given age."""
    def __init__(self, all_ages, table):
        self.all_ages = all_ages
        self.table = table

        self.age_pmf = self.get_pmf()
        self.age_cdf = thinkstats2.MakeCdfFromPmf(self.age_pmf)

    def get_pmf(self):
        """Gets the distribution of parents age.

        Returns: pmf object
        """
        pmf = thinkstats2.Pmf()
        for age in self.all_ages:
            pmf.Incr(age, self.table[age])
        pmf.Normalize()
        return pmf

    def random_age(self):
        """Chooses a random age for a parent."""
        return self.age_cdf.Random()

    def prob(self, age):
        """Returns the probability of having a child at a given age."""
        return self.table[age]


class Regression(object):
    """Represents the result of a regression."""
    def __init__(self, xs):
        self.xs = xs

    def linear_model(self, print_flag=False):
        """Runs a linear model and returns fitted values.

        print_flag: boolean, whether to print the R results

        Returns a list of (x, fitted y) pairs
        """
        res = glm.logit_model('y ~ x', print_flag=print_flag)
        estimates, aic = glm.get_coeffs(res)

        self.inter = estimates['(Intercept)'][0]
        self.slope = estimates['x'][0]

        xs = np.array(sorted(set(self.xs)))
        log_odds = self.inter + self.slope * xs
        odds = np.exp(log_odds)
        ps = odds / (1 + odds)

        fit = []
        for x, p in zip(xs, ps):
            fit.append((x+1900, p))

        self.fit = fit
        return fit

    def quadratic_model(self, print_flag=False):
        """Runs a quadratic model and returns fitted values.

        print_flag: boolean, whether to print the R results

        Returns a list of (x, fitted y) pairs
        """
        res = glm.logit_model('y ~ x + x2', print_flag=print_flag)
        estimates, aic = glm.get_coeffs(res)

        self.inter = estimates['(Intercept)'][0]
        self.slope = estimates['x'][0]
        self.slope2 = estimates['x2'][0]

        xs = np.array(sorted(set(xs)))
        log_odds = self.inter + self.slope * xs + self.slope2 * xs**2
        odds = np.exp(log_odds)
        ps = odds / (1 + odds)

        fit = []
        for x, p in zip(xs, ps):
            fit.append((x+1900, p))

        self.fit = fit
        return fit

    def fit_prob(self, x):
        """Computes the fitted value of y for a given x.

        Only works with the linear model.

        x: float value of x

        Returns: float value of y
        """
        log_odds = self.inter + self.slope * (x-1900)
        odds = math.exp(log_odds)
        p = odds / (1 + odds)
        return p
    

class NullModel(object):
    def __init__(self, p):
        """Make a NullModel.

        p: probability that a respondent has some property
        """
        self.p = p

    def fit_prob(self, r):
        """Computes the fitted probability for the given respondent.

        r: Respondent

        Returns: float prob
        """
        return self.p


class LogRegression(object):
    def __init__(self, res):
        """Makes a LogRegression object

        res: result object from rpy2
        estimates: list of (name, est, error, z)
        """
        self.res = res
        self.estimates, self.aic = glm.get_coeffs(res)

    def fit_prob(self, r):
        """Computes the fitted probability for the given respondent.

        r: Respondent

        Returns: float prob
        """
        log_odds = 0
        for name, est, error, z in self.estimates:
            if name == '(Intercept)':
                log_odds += est
            else:
                x = getattr(r, name)
                if x == 'NA':
                    print name
                    return 'NA'
                log_odds += est * x

        odds = math.exp(log_odds)
        p = odds / (1 + odds)
        return p

    def validate(self, respondents, attr):
        for r in respondents:
            dv = getattr(r, attr)
            p = self.fit_prob(r)
            #print r.caseid, dv, p

    def report(self):
        """Prints a summary of the glm results."""
        if self.res is None:
            print 'No summary'
        glm.print_summary(self.res)

    def report_odds(self, means):
        """Prints a summary of the estimated parameters.

        Iterates the attributes and computes the odds ratio, for
        the given value, and the probability that corresponds to
        the cumulative odds.

        means: map from attribute to value
        """
        cumulative = cumulative_odds(self.estimates, means)
        print_cumulative_odds(cumulative)

    def make_pickleable(self):
        self.res = None


def trans_to_matrix(trans):
    """Converts a transition table to a matrix.

    trans: map from explanatory values to Pmf of outcomes.

    Returns: numpy array of float
    """
    n = len(ORDER)
    matrix = np.empty(shape=(n, n), dtype=np.float)

    for i, x in enumerate(ORDER):
        for j, y in enumerate(ORDER):
            percent = trans[x].Prob(y)
            matrix[i][j] = percent

    return np.transpose(matrix)


def fraction_true(hist):
    yes, no = hist.Freq(True), hist.Freq(False)
    return float(yes) / (yes+no)

def fraction_one(pmf):
    yes, no = pmf.Prob(1), pmf.Prob(0)
    return float(yes) / (yes+no)


def print_pmf_sorted(pmf):
    """Prints the values in the Pmf in ascending order by value.

    pmf: Pmf object
    """
    for val, prob in sorted(pmf.Items()):
        print val, prob * 100


def print_pmf_sorted_by_prob(pmf):
    """Prints the values in the Pmf in descending order of prob.

    pmf: Pmf object
    """
    pvs = [(prob, val) for val, prob in pmf.Items()]
    pvs.sort(reverse=True)
    for prob, val in pvs:
        print val, prob * 100


def print_pmf(pmf):
    """Prints the Pmf with values in the given ORDER.

    pmf: Pmf object
    """
    for x in ORDER:
        print '%s\t%0.0f' % (x, pmf.Prob(x) * 100)


def pmf_to_vector(pmf):
    """Converts a Pmf to a vector of probabilites.

    pmf: Pmf object

    Returns: numpy array of float
    """
    t = [pmf.Prob(x) for x in ORDER]
    return np.array(t)


def print_vector(vector, head_flag=True):
    """Prints a 1-D numpy array.

    vector: numpy array
    head_flag: boolean whether to print a header line
    """
    if head_flag:
        for x in ORDER:
            print x, '\t',
        print

    for i, x in enumerate(ORDER):
        percent = vector[i] * 100
        print '%0.1f\t' % percent,
    print


def step(matrix, vector):
    """Advance the simulation by one generation.

    matrix: numpy transition matrix
    vector: numpy state vector

    Returns: new numpy vector
    """
    new = np.dot(matrix, vector)
    return new


def normalize_vector(vector, total=1.0):
    """Normalizes a numpy array to add to total.

    Modifies the array.

    vector: numpy array
    total: float
    """
    vector *= total / np.sum(vector)


class Model(object):
    
    def run_nonlinear(self, matrix, vector):
        """Runs the nonlinear model where the number of conversions depends
        on the prevalance of each category.

        matrix: numpy transition matrix
        vector: numpy state vector
        """
        conversions = matrix / vector

        state = vector
        print_vector(state, True)

        for i in range(10):
            trans = conversions * state
            state = step(trans, state)
            normalize_vector(state)
            print_vector(state, False)

    def run_linear(self, matrix, vector, steps=1):
        """Runs the linear model where the rate of conversions is constant.

        matrix: numpy transition matrix
        vector: numpy state vector
        """
        print_vector(vector, True)

        for i in range(steps):
            vector = step(matrix, vector)
            print_vector(vector, False)

        return vector


class ReligSeries(object):
    def __init__(self, filename='GSS_relig_time_series.csv'):
        """Reads data from CSV file and returns map from year to Pmf of relig.

        filename: string
        """
        fp = open(filename)
        reader = csv.reader(fp)

        header1 = reader.next()[1:]
        header2 = reader.next()[1:]

        self.data = {}
        for t in reader:
            year = int(t[0])
            total = float(t[-1])
            row = [float(x)/total for x in t[1:-1]]
            pmf = combine_row(row, header2)

            # normalizing shouldn't be necessary, but the totals tend
            # to be off in the third decimal place, so I'm cleaning that up
            pmf.Normalize()

            self.data[year] = pmf

        fp.close()

    def plot_time_series_stack(self):
        plot_time_series_stack(self.data)
        thinkplot.Save(root='gss0',
                    xlabel='Year of survey',
                    ylabel='Fraction of population',
                    legend=True,
                    axis=[1972, 2010, 0, 100.5])
            
    def plot_changes(self, low, high, 
                     change_flag=True,
                     preds=None,
                     spans=None):
        """Makes a plot of changes in religious preference.

        low, high: range of years to plot
        change_flag: boolean: whether to normalize by first year value
        preds: vector of predicted values (should only be used
                     with change_flag=True)
        spans: error ranges for the predictions
        """
        pyplot.clf()
        years = self.get_years(low, high)
        ys = np.zeros(len(years))

        rows = []
        for name in ORDER:
            ys = [self.data[year].Prob(name) * 100  for year in years]
            rows.append(ys)

        stretch = 4 if preds else 1

        for i in range(len(rows)):
            ys = rows[i]
            if change_flag:
                baseline = ys[0]
                ys = [100.0 * y / baseline for y in ys]
                axis = [low-1, high+stretch, 50, 260]
            else:
                axis = [low-1, high+stretch, 0, 90]

            thinkplot.Plot(years, ys,
                        label=ORDER[i],
                        linewidth=3,
                        color=COLORS[i],
                        alpha=ALPHAS[i])

            xloc = high + 0.6 * (i+1)

            if spans is not None:
                low_span = 100.0 * 100.0 * spans[i][0] / baseline
                high_span = 100.0 * 100.0 * spans[i][1] / baseline
                thinkplot.Plot([xloc, xloc], [low_span, high_span],
                            linewidth=3,
                            color=COLORS[i],
                            alpha=ALPHAS[i])

            if preds is not None:
                pred = 100.0 * 100.0 * preds[i] / baseline
                thinkplot.Plot(xloc, pred, 
                            marker='s',
                            markersize=10,
                            markeredgewidth=0,
                            color=COLORS[i],
                            alpha=ALPHAS[i])

        if change_flag:
            if preds is None:
                root = 'gss.change.%d-%d' % (low, high)
            else:
                root = 'gss.pred.%d-%d' % (low, high)
                
            ylabel = '%% change since %d' % low
        else:
            root = 'gss.%d-%d' % (low, high)
            ylabel = '% of respondents'

        thinkplot.Save(root=root,
                    xlabel='Survey year',
                    ylabel=ylabel,
                    legend=True,
                    axis=axis)

    def get_years(self, low, high):
        years = self.data.keys()
        years.sort()
        years = [year for year in years if low <= year <= high]
        return years

    def test_significance(self, relig_name, low, high):
        """Run a linear regression on market share vs year.

        Prints the results

        series: map from year to Pmf of religions
        relig_name: string, which religion to test
        """
        years = self.get_years(low, high)
        ys = [self.data[year].Prob(relig_name) * 100  for year in years]
        d = dict(years=years, ys=ys)
        glm.inject_col_dict(d)
        glm.linear_model('ys ~ years')

    def get_series_for_val(self, val):
        """Gets the time series for a particular value.

        series: map from year to Pmf of religious preference.
        val: string religion name to track

        Returns: list of (year, fraction) pairs
        """
        res = []
        for year, pmf in sorted(self.data.iteritems()):
            p = pmf.Prob(val)
            res.append((year, p))
        return res


def plot_time_series_stack(data):
    """Makes a plot of the actual data and the model predictions.

    data: map from year to Pmf
    """
    years = data.keys()
    years.sort()

    ys = np.zeros(len(years))

    rows = []
    for name in ORDER:
        for i, year in enumerate(years):
            percent = data[year].Prob(name) * 100
            ys[i] += percent

        rows.append(np.copy(ys))

    for i in range(len(rows)-1, -1, -1):
        ys = rows[i]
        if i == 0:
            prev = np.zeros(len(years))
        else:
            prev = rows[i-1]

        pyplot.fill_between(years, prev, ys, 
                            color=COLORS[i],
                            alpha=0.2)


def combine_row(row, header):
    """Makes a row into a PMF.

    row: list of float data
    header: category each datum should be added to

    Returns: Pmf that maps categories to probs (or fraction of pop)
    """
    pmf = thinkstats2.Pmf()
    pmf.Incr('NA', 0)
    for name, prob in zip(header, row):
        pmf.Incr(name, prob)
    return pmf


class SpouseTable(object):
    def __init__(self, survey):

        self.sp_female = {}
        self.sp_male = {}
        self.sp_same = {1:thinkstats2.Hist(), 2:thinkstats2.Hist()}

        for name in ORDER:
            self.sp_female[name] = thinkstats2.Pmf()
            self.sp_male[name] = thinkstats2.Pmf()

        for r in survey.respondents():
            if USE_PARENT_DATA:
                attr1='marelig_name'
                attr2='parelig_name'
            elif r.sex == 1:
                attr1='sprelig_name'
                attr2='relig_name'
            else:
                attr1='relig_name'
                attr2='sprelig_name'

            ma = getattr(r, attr1)
            pa = getattr(r, attr2)
            if ma=='NA' or pa=='NA':
                continue

            self.sp_same[r.sex].Incr(ma==pa)
            self.sp_female[ma].Incr(pa, r.compwt)
            self.sp_male[pa].Incr(ma, r.compwt)

        normalize_table(self.sp_female)
        normalize_table(self.sp_male)

    def print_table(self):
        print 'prob same', self.prob_same()

        for attr in ['sp_male', 'sp_female']:
            print attr
            table = getattr(self, attr)
            print_table(table)

    def prob_same(self):
        t = [fraction_true(self.sp_same[sex]) for sex in [1, 2]]
        return t

    def write_html_table(self):
        for attr in ['sp_male', 'sp_female']:
            table = getattr(self, attr)
            rows, header_row = get_table_rows(table)
            filename = 'gss.%s.html' % attr
            write_html_table(filename, rows, header_row, 'Spouse Table')

    def print_pmf(self, pmf):
        for name in ORDER:
            percent = pmf.Prob(name) * 100
            print '%s %0.0f\t' % (name, percent)

    def generate_spouse(self, r):
        if r.sex == 1:
            pmf = self.sp_male[r.relig_name]
        else:
            pmf = self.sp_female[r.relig_name]
        return pmf.Random()


class EnvironmentTable(object):
    def __init__(self, survey):
        """Makes a 

        Returns map from (marelig, parelig) to normalized Pmf of which
        religion the child is raised in.

        order: string list of relig_names
        """
        self.table = {}
        self.hist = thinkstats2.Hist()

        for ma in ORDER:
            for pa in ORDER:
                self.table[ma, pa] = thinkstats2.Pmf()

        for r in survey.respondents():
            ma = r.marelig_name
            pa = r.parelig_name
            raised = r.relig16_name
            if 'NA' in [ma, pa, raised]:
                continue

            self.table[ma, pa].Incr(raised, r.compwt)
            self.hist.Incr((ma, pa))

        normalize_table(self.table)

    def print_table(self, relig_name):
        """Prints a table of mother's religion x father's religion.

        Each row is mother's religion, each column is father's.

        Each entry is the fraction of children raised in relig_name.

        relig_name: string name of religion
        """
        print '\t',
        for y in ORDER:
            print y, '\t',
        print

        for ma in ORDER:
            print ma, '\t', 
            for pa in ORDER:
                pmf = self.table[ma, pa]
                percent = pmf.Prob(relig_name) * 100
                print '%0.0f\t' % percent,
            print

    def write_html_table(self, relig_name):
        """Prints a table of mother's religion x father's religion.

        Each row is mother's religion, each column is father's.

        Each entry is the fraction of children raised in relig_name.

        relig_name: string name of religion
        """
        header_row = ['']
        header_row.extend(ORDER)

        rows = []
        for ma in ORDER:
            row = [ma]
            for pa in ORDER:
                pmf = self.table[ma, pa]
                percent = pmf.Prob(relig_name) * 100
                row.append('%0.0f' % percent)
            rows.append(row)

        filename = 'gss.par.%s.html' % relig_name
        title = 'Parent table (%s)' % relig_name
        write_html_table(filename, rows, header_row, title)

    def print_combined_table(self):
        """Prints a table of mother's religion x father's religion.
        """
        print '\t\t',
        for y in ORDER:
            print y, '\t',
        print

        for ma in ORDER:
            for pa in ORDER:
                print '%4.4s-%4.4s\t' % (ma, pa),
                pmf = self.table[ma, pa]
                for name in ORDER:
                    percent = pmf.Prob(name) * 100
                    print '%0.0f\t' % percent,
                print self.hist.Freq((ma, pa))

    def diff_combined_table(self, other):
        """Prints a table of mother's religion x father's religion.
        """
        print '\t\t',
        for y in ORDER:
            print y, '\t',
        print
        
        total = 0
        for ma in ORDER:
            for pa in ORDER:
                print '%4.4s-%4.4s\t' % (ma, pa),
                pmf = self.table[ma, pa]
                pmf2 = other.table[ma, pa]
                freq = self.hist.Freq((ma, pa))

                for name in ORDER:
                    percent = pmf.Prob(name) * 100
                    percent2 = pmf2.Prob(name) * 100
                    change = percent2 - percent
                    print '%0.0f\t' % percent2,
                    if name == 'none':
                        print '%+0.0f\t' % change,
                        excess = change/100 * freq
                        total += excess
                print '%d\t%0.1f' % (freq, excess)
        print total

    def write_combined_table(self):
        """Prints a table of mother's religion x father's religion.
        """
        header_row = ['parents']
        header_row.extend(ORDER)

        rows = []
        for ma in ORDER:
            for pa in ORDER:
                row = ['%s-%s' % (ma, pa)]
                pmf = self.table[ma, pa]
                for name in ORDER:
                    percent = pmf.Prob(name) * 100
                    row.append('%0.0f' % percent)
                rows.append(row)

        filename = 'gss.parent.html'
        title = 'Parent table'
        write_html_table(filename, rows, header_row, title)

    def generate_raised(self, ma, pa):
        """Chooses a random religion to raise a child in.

        ma: mother's religion
        pa: father's religion

        Returns: string religion name
        """
        pmf = self.table[ma, pa]
        if pmf.Total():
            return pmf.Random()
        else:
            return random.choice([ma, pa])


class TransitionTable(object):
    def __init__(self, survey, title,
                 attr1='relig16_name', attr2='relig_name'):
        """Makes a transition table.

        Returns map from attr1 to normalized Pmf of outcomes.

        attr1: explanatory variable
        attr2: dependent variable
        """
        self.title = title
        self.attr1 = attr1
        self.attr2 = attr2

        self.table = {}
        self.hist = thinkstats2.Hist()

        for name in ORDER:
            self.table[name] = thinkstats2.Pmf()

        for r in survey.respondents():
            x = getattr(r, attr1)
            y = getattr(r, attr2)
            if x=='NA' or y=='NA':
                continue

            self.table[x].Incr(y, r.compwt)
            self.hist.Incr(x)

        normalize_table(self.table)

    def print_table(self):
        print_table(self.table)

    def diff_table(self, other):
        """Prints a table of ...
        """
        print '\t',
        for y in ORDER:
            print y, '\t',
        print
        
        total = 0
        for raised in ORDER:
            print raised, '\t',
            pmf = self.table[raised]
            pmf2 = other.table[raised]
            freq = self.hist.Freq(raised)

            for name in ORDER:
                percent = pmf.Prob(name) * 100
                percent2 = pmf2.Prob(name) * 100
                change = percent2 - percent
                print '%0.0f\t' % percent2,
                if name == 'none':
                    print '%+0.0f\t' % change,
                    excess = change/100 * freq
                    total += excess
            print '%d\t%0.1f' % (freq, excess)
        print total

    def write_html_table(self):
        rows, header_row = get_table_rows(self.table)
        filename = 'gss.%s.html' % '.'.join(self.title.lower().split())
        write_html_table(filename, rows, header_row, self.title)

    def generate_relig(self, raised):
        """Chooses a random religious preference.

        raised: string religion raised in

        Returns: string religion name
        """
        pmf = self.table[raised]
        return pmf.Random()


class EmptyPmfError(ValueError):
    """Raised if the PMF has no values."""


class Table(object):
    def __init__(self, table, hist):
        self.table = table
        self.hist = hist

    def get_pmf(self, key):
        return self.table[key]

    def choose(self, key):
        pmf = self.get_pmf(key)
        if pmf.Total() == 0:
            print 'EmptyPmfError'
            raise EmptyPmfError()
        val = pmf.Random()
        return val


def print_table(table):
    """Prints a transition table.

    table: map from explanatory values to Pmf of outcomes.
    """
    print '\t',
    for y in ORDER:
        print y, '\t',
    print

    for x in ORDER:
        print x, '\t', 
        for y in ORDER:
            percent = table[x].Prob(y) * 100
            print '%0.0f\t' % percent,
        print


def get_table_rows(table):
    header_row = ['']
    header_row.extend(ORDER)

    rows = []
    for x in ORDER:
        row = [x]
        for y in ORDER:
            percent = table[x].Prob(y) * 100
            row.append('%0.0f' % percent)
        rows.append(row)

    return rows, header_row


def write_html_table(filename, rows, header_row, title=''):
    """Writes a transition table to a file.

    table: map from explanatory values to Pmf of outcomes.
    """
    print 'Writing', filename
    fp = open(filename, 'w')
    fp.write('<div>\n<h3>%s</h3>\n' % title)

    htmlcode = HTML.table(rows, header_row=header_row)
    fp.write(htmlcode)
    fp.write('</div>\n\n')
 
    fp.close()


def normalize_table(table):
    """Normalize the pmfs in this table."""
    for pmf in table.itervalues():
        if pmf.Total():
            pmf.Normalize()


def make_matrix_model():
    pmf = survey88.make_pmf('relig_name')
    vector = pmf_to_vector(pmf)

    print 'relig16_name'
    trans = survey88.make_trans('relig16_name', 'relig_name')
    print_trans(trans)

    matrix = trans_to_matrix(trans)

    print
    model = Model()
    preds = model.run_linear(matrix, vector, steps=1)

    series = ReligSeries()
    series.plot_changes(1988, 2010, preds=preds)


def plot_time_series():
    """Make time series plots."""
    series = ReligSeries()
    #series.plot_time_series_stack()
    series.plot_changes(1972, 2010, change_flag=False)
    series.plot_changes(1972, 1988)
    series.plot_changes(1988, 2010)


def print_time_series():
    """Print time series data."""
    series = ReligSeries()
    for year, pmf in series.data.iteritems():
        print year
        print_pmf(pmf)


def test_significance():
    series = ReligSeries()
    for name in ORDER:
        print name
        series.test_significance(name, 1972, 2010)
        series.test_significance(name, 1988, 2010)


def plot_interval(all_ps, **options):
    """Plot a 2-standard error interval.

    all_ps: map from x value to list of y values
    options: keyword options passed along to pyplot.fill_between
    """
    xs = all_ps.keys()
    xs.sort()
    columns = [all_ps[x] for x in xs]
    stats = [thinkstats2.MeanVar(ys) for ys in columns]
    min_ps = [mu - 2 * math.sqrt(var) for mu, var in stats]
    max_ps = [mu + 2 * math.sqrt(var) for mu, var in stats]
    mean_ps = [mu for mu, var in stats]

    pyplot.fill_between(xs, min_ps, max_ps, linewidth=0, **options)
    return xs, mean_ps


def plot_errorbars(all_ps, n=1, **options):
    """Plot error bars spanning all but n values from the top and bottom.

    all_ps: map from x value to list of y values
    options: keyword options passed along to pyplot.fill_between
    """
    xs = all_ps.keys()
    xs.sort()

    lows = []
    highs = []
    for x in xs:
        col = all_ps[x]
        col.sort()
        low = col[n]
        high = col[-(n+1)]
        lows.append(low)
        highs.append(high)

    for x, low, high in zip(xs, lows, highs):
        thinkplot.Plot([x, x], [low, high], **options)


def print_transition_model():
    survey88 = Survey()
    survey88.read_csv('gss1988.csv', Respondent)
    trans_model = TransitionModel(survey88)
    next_gen = trans_model.next_gen(survey88)
    trans_model.print_model()


class ModelFactory(object):
    def __init__(self, survey, spouse_flag, env_flag, trans_flag):
        self.survey1 = survey
        self.spouse_flag = spouse_flag
        self.env_flag = env_flag
        self.trans_flag = trans_flag

        if self.any_flag():
            self.survey2 = Survey()
            self.survey2.read_csv('gss2008.csv', Respondent)

    def any_flag(self):
        return self.spouse_flag or self.env_flag or self.trans_flag

    def __call__(self):
        trans_model = TransitionModel(self.survey1,
                                      resample_flag=True)

        if self.any_flag():
            trans_model2 = TransitionModel(self.survey2,
                                           resample_flag=True)

        if self.spouse_flag:
            trans_model.spouse_table = trans_model2.spouse_table

        if self.env_flag:
            trans_model.env_table = trans_model2.env_table

        if self.trans_flag:
            trans_model.trans_table = trans_model2.trans_table

        return trans_model


def run_transition_model(spouse_flag=False, env_flag=False, trans_flag=False):
    """
    
    spouse_flag: boolean, whether to use 2004-2010 spouse tables
    env_flag: boolean, whether to use 2008 parent table
    """
    random.seed(17)

    survey88 = Survey()
    survey88.read_csv('gss1988.csv', Respondent)

    factory = ModelFactory(survey88, spouse_flag, env_flag, trans_flag)
    res = survey88.run_transition_model(factory)
    
    preds, spans = zip(*res)
    for name, pred, span in zip(ORDER, preds, spans):
        print name, '%0.1f (%0.1f %0.1f)' % (pred*100, span[0]*100, span[1]*100)

    series = ReligSeries()
    series.plot_changes(1988, 2010, preds=preds, spans=spans)


def plot_none_vs_yrborn():
    survey = Survey()
    survey.read_csv('gss.series.csv', Respondent)

    def filter_func(r):
        return 1900 <= r.yrborn <= 1990

    subsample = survey.subsample(filter_func)
    subsample.plot_relig_vs_yrborn('none')


def plot_none_vs_year():
    survey = Survey()
    survey.read_csv('gss.series.csv', Respondent)

    surveys = survey.partition_by_attr('year')
    
    for year in [1990, 2010]:
        print year
        sub = surveys[year]
        sub.print_pmf('relig_name')
        print

    years = []
    ps = []
    for year, sub in surveys.iteritems():
        pmf = sub.make_pmf('relig_name')
        pmf.Set('NA', 0)
        pmf.Normalize()
        years.append(year)
        prob = pmf.Prob('none')
        ps.append(prob * 100)

    thinkplot.Plot(years, ps, color='red', label='% unaffiliated')
    pyplot.axis([1971, 2011, 0, 20])


def plot_internet_users():
    """Plots World Bank data, number of Internet users in U.S. over time."""
    filename = 'IT.NET.USER.P2_Indicator_MetaData_en_EXCEL.csv'
    fp = open(filename)
    reader = csv.reader(fp)
    
    header = reader.next()[32:-1]
    years = [int(x) for x in header]

    for t in reader:
        if t[0] == 'United States':
            ys = [float(y) for y in t[32:-1]]
            thinkplot.Plot(years, ys, label='Internet users per 100')

    pyplot.axis([1971, 2011, 0, 80])
    pyplot.legend(loc=2)
    pyplot.title('Prevalence of Internet use and non-affiliation')


def plot_internet_users_and_nones():
    pyplot.subplot(2, 1, 1)
    plot_internet_users()

    pyplot.subplot(2, 1, 2)
    plot_none_vs_year()

    thinkplot.Save(root='gss.internet', xlabel='Year')


def investigate_switches():
    survey = Survey()
    survey.read_csv('gss1988.csv', Respondent)

    surveys = survey.partition_by_attr('relig16_name')
    prot = surveys['prot'].subsample(lambda r: r.relig_name != 'prot')

    rows = []
    for r in prot.respondents():
        row = (r.relig16_name, r.relig_name, 
               r.switch1, r.switwhy1, r.switch2, r.switch3)
        rows.append(row)

    rows.sort()
    for row in rows:
        print row

    return
    for name in ORDER:
        survey = surveys[name]
        survey.make_pmg
        print name, survey.len()

    return
    pmf = survey88.make_pmf('switch1')
    pmf.Set('NA', 0)
    pmf.Normalize()
    for val, prob in sorted(pmf.Items()):
        print val, prob

    survey88.investigate_switches('prot', 'none')


def make_time_series(filename, cutoff=None):
    """Makes a map from decade born to Survey.

    filename: file to read
    cutoff: survey year to cut off results

    Returns: a map from decade born to Survey.
    """
    survey = Survey()
    survey.read_csv(filename, Respondent)

    if cutoff:
        survey = survey.subsample(lambda r: r.year<=cutoff)

    surveys = survey.partition_by_attr('decade')
    return surveys


def make_cross_tabs(surveys, attr1, attr2):
    """Makes a cross tabulation for each year.
    
    surveys: a map from decade born to Survey.
    attr1: string attribute name
    attr2: string attribute name

    Returns: map from year to Table object
    """
    tables = {}
    for year, survey in surveys.iteritems():
        table = survey.cross_tab(attr1, attr2)
        tables[year] = table
    return tables


def plot_element(tables, relig_name):
    """Plots an element of a table as a time series.

    tables: map from year to Table object
    relig_name: string name of relig to plot
    """
    # collect the data
    years = []
    rows = []
    for year, table in sorted(tables.iteritems()):
        if table.hist.Total() < 100:
            continue
        
        row = []
        pmf = table.get_pmf(relig_name)
        for name in ORDER:
            percent = pmf.Prob(name) * 100
            row.append(percent)

        years.append(year)
        rows.append(row)

    # plot it
    cols = zip(*rows)
    plot_relig_series(years, cols)


def plot_relig_series(years, cols):
    """Plots a set of lines, color coded for religions.

    years: sequence of years
    cols: list of columns, one for each religion, in standard order
    """
    for i, col in enumerate(cols):
        thinkplot.Plot(years, col,
                    label=ORDER[i],
                    color=COLORS[i],
                    alpha=ALPHAS[i])


def plot_relig_curves(curves, indices=range(6), **options):
    """Plots a set of lines, color coded for religions.

    curves: list of (xs, ys) pairs
    """
    for i, curve in enumerate(curves):
        if i not in indices:
            continue

        xs, ys = curve
        thinkplot.Plot(xs, ys,
                    label=ORDER[i],
                    color=COLORS[i],
                    alpha=ALPHAS[i],
                    **options)


def plot_simulated_relig_curves(curves, indices=range(6), **options):
    """Plots a set of lines, color coded for religions.

    curves: list of (xs, ys) pairs
    """
    for i, curve in enumerate(curves):
        if i not in indices:
            continue

        xs, ys = curve
        thinkplot.Plot(xs, ys,
                    lw=1,
                    color=COLORS[i],
                    alpha=ALPHAS[i],
                    **options)


def plot_curves(curves, labels):
    """Plots a set of lines.

    curves: list of (xs, ys) pairs
    """
    for curve, label in zip(curves, labels):
        xs, ys = curve
        thinkplot.Plot(xs, ys, label=label)


def make_stack_series(tables, name):
    pmfs = {}
    for year, table in tables.iteritems():
        pmf = table.get_pmf(name)
        pmfs[year] = pmf

    plot_time_series_stack(pmfs)
    thinkplot.Save(root='gss_stack_%s' % name,
                xlabel='Year of survey',
                ylabel='Fraction of population',
                legend=True,
                axis=[1972, 2010, 0, 100.5])


def part_three():
    # print the environment tables
    env_table = make_env_table(1988)
    env_table.print_combined_table()

    env_table2 = make_env_table(2008)
    env_table.diff_combined_table(env_table2)

    # print the transmission tables
    trans_table = make_trans_table(1988)
    trans_table.print_table()

    trans_table2 = make_trans_table(2008)
    trans_table2.print_table()
    trans_table.diff_table(trans_table2)

    # plot the model
    run_transition_model(spouse_flag=False, env_flag=False, trans_flag=True)
    return

    # part three
    make_spouse_series()


def part_four():
    survey = Survey()
    survey.read_csv('gss.series.csv', Respondent)
    
    raised = survey.subsample(lambda r: r.had_relig)
    raised.make_religiosity_curves_by_decade('any', age_flag=False)

    surveys = survey.partition_by_attr('relig16_name')
    for relig_name in ['prot', 'cath', 'none']:
        subsurvey = surveys[relig_name]
        #subsurvey.make_religiosity_curves_by_decade(relig_name)
        subsurvey.make_religiosity_curves_by_decade(relig_name, age_flag=False)
        #subsurvey.make_religiosity_contour_by_decade(relig_name)

    # sadly, this looks useless
    #investigate_switches()


def part_six():
    random.seed(21)

    #plot_simulation_predictions(cutoff=2010)
    #plot_simulation_predictions(cutoff=1988)
    plot_simulation_predictions(cutoff=2010, start_year=2010, end_year=2050)


def plot_simulation_predictions(cutoff=2010,
                                start_year=1988,
                                end_year=2010):
    whole_survey = Survey()
    whole_survey.read_csv('gss.series.csv', Respondent)

    # surveys is a map from year to actual Survey
    surveys = whole_survey.partition_by_attr('year')
    start_survey = surveys[start_year]
    
    available_survey = whole_survey.subsample(lambda r: r.year<=cutoff)

    # each simulation is a map from year to simulated Survey
    simulations = []
    for i in range(5):
        print i+1
        resample = available_survey.resample()
        cohort = Cohort(resample, cutoff=cutoff, decade_flag=True)
        simulation = cohort.run_simulation(start_year, end_year)
        simulations.append(simulation)

    root = 'gss.model.%d.%d.pcn' % (cutoff, end_year)
    plot_real_and_simulated(surveys, simulations, [0,1,4], root)

    root = 'gss.model.%d.%d.oj' % (cutoff, end_year)
    plot_real_and_simulated(surveys, simulations, [2,3], root)


def plot_real_and_simulated(surveys, simulations, indices, root):
    """Plots actual times series and simulations.

    surveys: map from year to Survey
    simulations: list of simulations ()
    indices: list in int, which lines to draw
    root: string filename for output
    """
    pyplot.clf()

    for simulation in simulations:
        plot_surveys_relig(simulation, indices, real_flag=False)
        
    # plot the real data
    plot_surveys_relig(surveys, indices)
    thinkplot.Save(root=root,
                xlabel='Survey year',
                ylabel='fraction of population'
                )


def plot_surveys_relig(surveys, indices, real_flag=True):
    """Plots a time series for each religion.

    surveys: map from year to Survey
    """
    pmf_series = PmfSeries(surveys, 'relig_name')

    curves = []
    for name in ORDER:
        curve = pmf_series.get_curve(name)
        curves.append(curve)

    if real_flag:
        plot_relig_curves(curves, indices)
    else:
        plot_simulated_relig_curves(curves, indices)


class PmfSeries(object):
    """Stores a series of PMFs."""
    def __init__(self, surveys, attr):
        self.pmfs = {}
        for key, survey in surveys.iteritems():
            self.pmfs[key] = survey.make_pmf(attr)

    def get_curve(self, val):
        """Gets the times series for a given value.

        Returns: (years, probs) tuple
        """
        data = []
        for key, pmf in sorted(self.pmfs.iteritems()):
            data.append((key, pmf.Prob(val)))
        return zip(*data)


class Cohort(object):
    def __init__(self, survey, cutoff=None, decade_flag=False):
        """Makes a cohort.

        survey: Survey object
        cutoff: what's the latest data we're allowed to use?
        decade_flag: whether to use a different transition model for
                     each decade of birth
        """
        self.survey = survey
        self.trans_model = TransitionModel2(survey, decade_flag)

        source_years = {
            1988: 1960,
            2010: 1980,
            }
        source_year = source_years[cutoff]
        self.extrapolate_transition_model(cutoff, source_year)

        self.birth_model = self.make_birth_model()

    def extrapolate_transition_model(self, cutoff, source_year):
        """Extrapolates from the real data to later decades.

        cutoff: last year of data we're using
        source_year: year we're copying
        """
        dest_years = range(source_year+10, 2050, 10)

        self.trans_model.extend_tables('up_tables', source_year, dest_years)
        self.trans_model.extend_tables('trans_tables', source_year, dest_years)

    def make_birth_model(self, plot_flag=False):
        """Makes the birth model.

        Uses data from 1994.

        plot_flag: whether to make the plots

        Returns: BirthModel
        """
        survey = Survey()
        survey.read_csv('gss1994.csv', Respondent)

        if plot_flag:
            survey.plot_child_curves()
            survey.plot_child_curve()

        birth_model = survey.make_birth_model()
        return birth_model

    def plot_elements(self):
        """Plot the elements of the transmission and upbringing tables.
        """
        self.trans_model.plot_transmission_elements()
        self.trans_model.plot_upbringing_elements()

    def make_next_generation(self, survey_year, survey):
        """Makes a simulated survey of the children of the respondents.

        survey_year: what year to use for the hypothetical parents

        Returns: Generation
        """
        if False:
            survey = Survey()
            filename = 'gss%d.csv' % survey_year
            survey.read_csv(filename, Respondent)
            survey = survey.resample()

        print 'Start survey N =', survey.len()

        n = survey.len()
        age_pmf = survey.make_age_pmf(survey_year)

        # simulate the next generation
        next_gen = self.trans_model.simulate_generation(survey,
                                                        self.birth_model)
        # add the current generation in with the next
        next_gen.add_respondents(survey.respondents())

        return Generation(next_gen, n, age_pmf)

    def run_simulation(self, start_year, end_year, plot_flag=False):
        """Simulate the evolution of the cohort over time.

        start_year: int year
        end_year: int year
        plot_flag: whether to make the plot showing age_pmfs

        Returns: map from year to Survey
        """
        start_survey = self.survey.subsample(lambda r: r.year==start_year)
        generation = self.make_next_generation(start_year, start_survey)

        if plot_flag:
            pmfs = []
            pmfs.append(('original', generation.age_pmf))

        surveys = {}
        for year in range(start_year, end_year+1):
            simulated = generation.simulate(year)
            if plot_flag:
                pmf = simulated.make_age_pmf(predict_year)
                name = 'predict%d' % predict_year
                pmfs.append((name, pmf))
            surveys[year] = simulated

        if plot_flag:
            plot_pmfs(pmfs)
        return surveys


def plot_pmfs(pmfs):
    """Plots one CDF for each PMF.

    pmfs: list of Pmf objects
    """
    for name, pmf in pmfs:
        cdf = thinkstats2.MakeCdfFromPmf(pmf, name=name)
        thinkplot.Cdf(cdf)
    thinkplot.Show()


class Generation(object):
    """Encapsulates a cohort we can evolve over time.
    """
    def __init__(self, survey, n, age_pmf):
        """Makes a Generation.

        survey: Survey with original respondents and simulated children
        n: number of respondents to resample
        age_pmf: distribution of ages to match
        """
        self.survey = survey
        self.n = n
        self.age_pmf = age_pmf

    def simulate(self, predict_year):
        """Generates a resample of the survey with the right age distribution.

        predict_year: the future year we are simulating
        """
        resample = self.survey.resample_by_age(self.n, 
                                               predict_year, 
                                               self.age_pmf)
        return resample


def how_many_fake(survey):
    """How many of the resampled respondents are fake?

    survey: Survey

    Returns: int
    """
    fake = survey.subsample(lambda r:r.caseid >= 90000)
    return fake.len()


class Locker(object):
    def __init__(self, shelf_file):
        self.shelf = shelve.open(shelf_file)
        try:
            self.get_next()
        except KeyError:
            self.set_next(0)

    def close(self):
        self.shelf.close()

    def get_next(self):
        return self.shelf['next']

    def set_next(self, i):
        self.shelf['next'] = i

    def get(self, i):
        return self.shelf[str(i)]

    def generate(self):
        for i in range(self.get_next()):
            yield self.get(i)

    def put(self, item):
        i = self.get_next()
        self.shelf[str(i)] = item
        self.set_next(i+1)


def make_null_model(survey, attr):
    """Computes the self information of an attribute.

    Total surprisal of the attr if we knew nothing about the respondents.

    survey: Survey
    attr: string attribute name
    """
    pmf = survey.make_pmf(attr)
    p = fraction_one(pmf)
    model = NullModel(p)
    return model


def investigate_compuse():
    survey = read_survey('gss.2000-2010.csv')
    survey = survey.subsample(lambda r: r.wwwhr == -1)
    surveys = survey.partition_by_attr('year')

    attr = 'usewww'
    for year, survey in sorted(surveys.iteritems()):
        print '\n', year, survey.len()
        pmf = survey.print_pmf(attr)
        #print attr, fraction_one(pmf)


def run_models(survey, version):
    nones = simulate_nones(survey, version)
    print '%5.5g' % (nones * 100)

    surveys = survey.partition_by_attr('year')
    for year, sub in sorted(surveys.iteritems()):
        nones = simulate_nones(sub, version)
        print '%5.5g' % (nones * 100),
    print


def simulate_nones(survey, version):
    """Fits a model to the data and computes the fraction of nones if
    the model were perfect.

    survey: Survey
    version: which version of the model to run

    Returns: float fraction
    """
    regs = run_regression(survey, version=version)
    model = regs.get(0)
    frac = 1 - survey.simulate_model(model)
    return frac


def make_www_series(survey):
    surveys = survey.partition_by_attr('year')
    for year, sub in sorted(surveys.iteritems()):
        print '\n', year
        for attr in ['www2', 'www7', 'www14']:
            pmf = sub.make_pmf(attr)
            print attr, fraction_one(pmf)

    for attr in ['www2', 'www7', 'www14']:
        series = survey.make_series(attr)
        series.plot_series(label=attr)
    
    thinkplot.Save(root='gss.www.series',
                xlabel='Survey year',
                ylabel='Percent of respondents'
                )


def odds_ratio(p1, p2):
    """Computes the odds ratio of p1 relative to p2.

    p1, p2: float probabilities

    Returns: float odds ratio
    """
    return p1 * (1-p2) / p2 / (1-p1)

def odds(p):
    """Computes the odds corresponding to probability p."""
    return p / (1 - p)

def prob(odds):
    """Computes the probability corresponding to odds."""
    return odds / (1 + odds)


def part_nine(n=3, version=2):
    # compute odds ratios to rewind to the 1980s
    print odds_ratio(0.033, 0.077)   # raised none
    print odds_ratio(0.174, 0.272)   # college

    random.seed(18)
    survey, complete = read_complete(version)

    rows = []
    for i in range(n):
        resample = complete.resample()

        regs = run_regression(resample, version)
        model = regs.get(0)
        model.report()
        
        x1 = estimate_upbringing_effect(complete, model)
        x2 = estimate_college_effect(complete, model)
        x3 = estimate_internet_effect(complete, model)
        x4 = estimate_generational_effect(complete, model)

        rows.append((x1, x2, x3, x4))

    cols = zip(*rows)
    names = ['upbringing', 'college', 'internet', 'generation']

    rows = []
    for col, name in zip(cols, names):
        ci, pval = compute_ci(col)
        millions = format_range(ci, 3)
        fractions = [val / 25.0 * 100 for val in ci]
        percentages = format_range(fractions, 3)
        row = [name, millions, percentages]
        rows.append(rows)

    header = ['Factor',
              'Millions',
              'Percentage']

    filename = 'gss.factor_table.tex'
    fp = open(filename, 'w')
    format = '|l|r|r|'
    write_latex_table(fp, header, rows, format)
    fp.close()


def estimate_internet_effect(survey, model):
    """Estimate the effect of the Internet on the population of unaffiliated.

    survey: Survey
    model: LogRegression
    odds_ratio: float, observed change in the explanatory variable

    Returns: float, number of people explained by the Internet effect
    """
    def counter_func(r):
        r.wwwhr = 0
        r.wwwmin = 0
        r.recode_internet()
        return r

    cf = Counterfactual(survey, model, attr='www2')
    return cf.run_counterfactuals(counter_func)


def estimate_generational_effect(survey, model):
    """Estimate the generational effect on the population of unaffiliated.

    survey: Survey
    model: LogRegression
    odds_ratio: float, observed change in the explanatory variable

    Returns: float, number of people explained by generational replacement
    """
    def counter_func(r):
        r.born_from_1960 -= 20
        return r

    cf = Counterfactual(survey, model, attr='born_from_1960')
    return cf.run_counterfactuals(counter_func)


def compute_adjustment_ratio(survey, attr, odds_ratio, flag=False):
    """Computes the fractions of As to convert to Bs to get the
    desired odds ratio.

    survey: Survey
    attr: string attribute name
    odds_ratio: float
    flag: boolean, whether to invert the "before" probability

    Returns: float
    """
    pmf = survey.make_pmf(attr)
    before = fraction_one(pmf)
    if flag:
        before = 1 - before

    after = prob(odds(before) * odds_ratio)
    adjustment_ratio = (before - after) / before
    return adjustment_ratio


def estimate_college_effect(survey, model, odds_ratio=0.56):
    """Estimate the effect of college on the population of unaffiliated.

    survey: Survey
    model: LogRegression
    odds_ratio: float, observed change in the explanatory variable

    Returns: float, number of people explained by college effect
    """
    def counter_func(r):
        if r.educ > 12:
            if random.random() < adjustment_ratio:
                r.educ = 12
        r.clean_socioeconomic()
        return r

    attr = 'college'
    adjustment_ratio = compute_adjustment_ratio(survey, attr, odds_ratio)

    cf = Counterfactual(survey, model, attr)
    return cf.run_counterfactuals(counter_func)


def estimate_upbringing_effect(survey, model, odds_ratio=0.41):
    """Estimate the effect of upbringing on the population of unaffiliated.

    survey: Survey
    model: LogRegression
    odds_ratio: float, observed change in the explanatory variable

    Returns: float, number of people explained by religious upbringing
    """
    def counter_func(r):
        if r.had_relig == 0:
            if random.random() < adjustment_ratio:
                r.had_relig = 1
        return r

    attr = 'had_relig'
    adjustment_ratio = compute_adjustment_ratio(survey, attr, odds_ratio, True)

    cf = Counterfactual(survey, model, attr)
    return cf.run_counterfactuals(counter_func)


class Counterfactual(object):
    def __init__(self, survey, model, attr):
        # make a safety copy before we go modifying anything
        self.survey = survey.deepcopy()
        self.model = model
        self.attr = attr

    def run_one_counterfactual(self, survey):
        pmf = survey.make_pmf(self.attr)
        p1 = fraction_one(pmf) * 100
        print '%3.3g' % (p1)

        frac = 1 - survey.simulate_model(self.model)

        return frac

    def run_counterfactuals(self, counter_func):
        print '-act\t',
        actual = self.run_one_counterfactual(self.survey)

        counterfactual = self.survey.counterfactual(counter_func)
        print '-cf\t',
        counter = self.run_one_counterfactual(counterfactual)

        print 'actual\t %3.3g' % (actual*100)
        print 'counter\t %3.3g' % (counter*100)

        diff1 = actual - counter
        print 'Difference in percentage points', 100 * diff1

        # http://2010.census.gov/news/releases/operations/cb10-cn93.html
        population_mil = 309

        excess = diff1 * population_mil
        print 'Diff counter - actual (mil)', excess

        # data from GSS tables
        diff3 = 0.153 - 0.071
        print 'Fraction explained', diff1 / diff3

        return excess

def part_eight():
    regs1 = run_many_regressions(n=0, version=1)
    regs11 = run_many_regressions(n=0, version=11, clean_version=1)
    regs2 = run_many_regressions(n=0, version=2)
    regs22 = run_many_regressions(n=0, version=22, clean_version=2)
    regs3 = run_many_regressions(n=0, version=3)
    regs33 = run_many_regressions(n=0, version=33, clean_version=3)
    regs333 = run_many_regressions(n=0, version=333, clean_version=3)

    print 'pval 1>11', compare_sips(regs1, regs11)
    print 'pval 2>22', compare_sips(regs2, regs22)
    print 'pval 2>1', compare_sips(regs2, regs1)
    print 'pval 3>33', compare_sips(regs3, regs33)
    print 'pval 3>333', compare_sips(regs3, regs333)


def run_many_regressions(n=0, version=1, clean_version=None):
    """Runs regressions and store the results.

    n: int, number of regression
    version: which model to use
    clean_version: which model to use to clean the survey
    """
    locker_file = 'gss.regress.%d.db' % version
    print locker_file

    means = dict(educ_from_12=4,
                 born_from_1960=10)

    if n > 0 :
        if clean_version is None:
            clean_version = version

        survey, complete = read_complete(clean_version)

        if version in [3, 33, 333]:
            complete = complete.subsample(lambda r: r.had_relig == 1)

        load_locker(complete, locker_file, n, version)

    regs = summarize_locker(locker_file, means)
    return regs


def compare_sips(regs1, regs2):
    """Computes the pvalue for the hypothesis that regs0 > regs1.

    regs0: Regressions object
    regs1: Regressions object
    """
    count = 0.0
    total = 0.0
    for sip1, sip2 in zip(regs1.sips, regs2.sips):
        total += 1
        if sip1 < sip2:
            count += 1
    return count / total


def load_locker(survey, locker_file, n=11, version=1):
    """Runs resampled regressions and stores the results.

    survey: Survey
    locker_file: place to store results
    n: number of regressions to run
    version: int, which model to run
    """
    dep, control = get_version(version)
    locker = Locker(locker_file)

    print 'N', survey.len()
    for i in range(n):
        index = locker.get_next()
        print i, index

        random.seed(index)
        resample = survey.resample()
        [r.clean_random() for r in resample.respondents()]

        reg = resample.make_logistic_regression(dep, control)
        reg.make_pickleable()
        locker.put(reg)

    locker.close()


def summarize_locker(locker_file, means):
    locker = Locker(locker_file)
    print locker.get_next()
    regs = Regressions(list(locker.generate()))
    locker.close()

    regs.summarize(means)
    regs.print_table()

    filename = locker_file + '.tex'
    print 'Writing', filename
    regs.write_table(filename)

    return regs


def auxiliary_models():
    means = dict(educ_from_12=4,
                 born_from_1960=10)

    version = 6
    survey, complete = read_complete(version)
    run_regression_and_print(complete, version, means=means)

    version = 5
    survey, complete = read_complete(version)
    run_regression_and_print(complete, version, means=means)


def compare_survey_and_complete(survey, complete):
    """Looks for the effect of selecting only complete records.

    survey: all respondents
    complete: only complete respondents (for a particular version)
    """
    for s in [survey, complete]:
        pmf = s.make_pmf('has_relig')
        frac = fraction_one(pmf)
        print 'has_relig', frac

        pmf = s.make_pmf('had_relig')
        frac = fraction_one(pmf)
        print 'had_relig', frac

        pmf = s.make_pmf('top75_income')
        frac = fraction_one(pmf)
        print 'top75_income', frac

        pmf = s.make_pmf('born_from_1960')
        try:
            pmf.Remove('NA')
        except:
            pass
        pmf.Normalize()
        print 'mean born_from_1960', pmf.Mean()

        pmf = s.make_pmf('college')
        frac = fraction_one(pmf)
        print 'college', frac


def test_models(version=2, resample_flag=False):
    means = dict(educ_from_12=4,
                 born_from_1960=10)

    # read the survey
    survey, complete = read_complete(version)
    subset = complete.subsample(lambda r: r.had_relig==1)

    compare_survey_and_complete(survey, complete)

    print 'all respondents', survey.len()
    print_fraction_none(survey)

    print 'complete', complete.len()
    print_fraction_none(complete)

    print 'subset', subset.len()
    print_fraction_none(subset)

    # print the distribution of years
    print '\nDistribution of survey years'
    pmf = survey.make_pmf('year')
    for val, prob in sorted(pmf.Items()):
        print val, prob

    # summarize the variables
    print '\nVariables:'
    dep, control = get_version(version)
    attrs = [dep] + control
    complete.summarize_binary_attrs(attrs)

    # resample
    if resample_flag:
        random.seed(0)
        resample = complete.resample()
    else:
        resample = complete

    # run_regression_and_print(complete, version=0, means=means)

    # run the models
    for version in [1, 2]:
        run_regression_and_print(resample, version=version, means=means)

    run_regression_and_print(subset, version=3, means=means)

    subset2 = complete.subsample(lambda r: r.had_relig==0)
    run_regression_and_print(subset2, version=4, means=means)


def read_complete(version):
    survey = read_survey('gss.2000-2010.csv')

    # select just the years we want
    years = [2000, 2002, 2004, 2006, 2010]
    survey = survey.subsample(lambda r: r.year in years)
    #survey.get_income_data()

    # give respondents random values
    random.seed(17)
    [r.clean_random() for r in survey.respondents()]

    # select complete records
    dep, control = get_version(version)
    #for var in [dep] + control:
    #    print r'\verb"%s",' % var

    attrs = [dep] + control
    complete = survey.subsample(lambda r: r.is_complete(attrs))

    return survey, complete


def run_regression_and_print(survey, version, means):
    """Runs a logistic regression and prints results

    survey: Survey
    version: which model to run
    means: map from variables to nominal values
    """
    print 'Version', version
    print 'N', survey.len()
    regs = run_regression(survey, version)
    regs.print_regression_reports(means)
    print
    regs.summarize(means)


def run_regression(survey, version):
    """Runs logistic regressions.

    survey: Survey
    version: which model to run

    Returns: Regressions object
    """
    dep, control = get_version(version)
    print dep, control
    reg = survey.make_logistic_regression(dep, control)
    return Regressions([reg])


def get_version(version):
    """Gets the variables for different versions of the model.

    version: int

    Returns: string, list of strings
    """
    dep = 'has_relig'

    if version == 0:
        control = ['had_relig', 'top75_income', 'top50_income',
                   'born_from_1960',
                   'educ_from_12']

    if version == 1:
        control = ['had_relig', 'top75_income',
                   'born_from_1960',
                   'educ_from_12', 'www2']

    if version == 11:
        control = ['had_relig', 'top75_income',
                   'born_from_1960',
                   'educ_from_12', 'rand1']

    if version == 2:
        control = ['had_relig', 'top75_income',
                   'born_from_1960',
                   'educ_from_12', 'www2', 'www7']

    if version == 22:
        control = ['had_relig', 'top75_income',
                   'born_from_1960',
                   'educ_from_12', 'www2', 'rand1']

    if version == 3:
        control = ['top75_income', 'born_from_1960',
                   'educ_from_12', 'www2', 'www7']

    if version == 33:
        control = ['top75_income', 'born_from_1960',
                   'educ_from_12', 'rand1', 'rand2']

    if version == 333:
        control = ['top75_income', 'born_from_1960',
                   'educ_from_12', 'www2', 'rand1']

    if version == 4:
        control = ['top75_income', 'born_from_1960',
                   'educ_from_12', 'www7']

    if version == 5:
        dep = 'college'
        control = ['had_relig', 'top75_income', 'born_from_1960',
                   'sei', 'urban', 'rural']

    if version == 6:
        dep = 'www2'
        control = ['had_relig', 'top75_income', 'born_from_1960',
                   'sei', 'urban', 'rural']

    return dep, control
    

def fraction_none(survey):
    pmf = survey.make_pmf('relig_name')
    #pmf.Set('NA', 0)
    #pmf.Normalize()
    frac = pmf.Prob('none')
    actual = frac * 100
    return '%3.3g' % actual


def print_fraction_none(survey):
    print fraction_none(survey)
    surveys = survey.partition_by_attr('year')
    for year, sub in sorted(surveys.iteritems()):
        print fraction_none(sub),
    print


def part_seven():
    plot_internet_users()

    # run one regression
    survey = read_survey('gss.2000-2010.csv')
    survey = survey.resample()
    regs = run_regression(survey)
    print_regression_reports(regs, means)

    return


def summarize_survey(survey):
    print 'N', survey.len()
    return
    attr_pairs = [
        ('relig', 'has_relig'),
        ('relig16', 'had_relig'),
        ('yrborn', 'born_from_1960'),
        ('educ', 'educ_from_12'),
        ('income', 'top75_income'),
        ]
    for attr1, attr2 in attr_pairs:
        survey.print_pmf(attr1)
        print
        survey.print_pmf(attr2)
        print

    survey.print_pmf('compuse')
    print
    survey.print_pmf('usewww')
    print
    survey.print_pmf('wwwhr')
    print
    survey.print_pmf('www2')
    print
    survey.print_pmf('www7')
    print
    survey.print_pmf('www14')


class Regressions(object):
    def __init__(self, regs):
        self.regs = regs
        reg = regs[0]
        self.names = [name for name, _, _, _ in reg.estimates]
        
    def get(self, i):
        return self.regs[i]

    def print_regression_reports(self, means):
        for reg in self.regs:
            reg.report()
            reg.report_odds(means)
            print 'AIC', reg.aic
            print 'SIP', reg.sip

    def median_model(self):
        rows = []

        # for each regression, make a list of estimates
        for reg in self.regs:
            row = [est for name, est, _, _ in reg.estimates]
            rows.append(row)

        # cols is one column per variable
        cols = zip(*rows)

        # compute cis for the estimates
        medians = []
        for col in cols:
            ci, pval = compute_ci(col)
            median, low, high = ci
            medians.append(median)

        for name, median in zip(self.names, medians):
            print name, median

    def summarize(self, means):
        self.summarize_estimates(means)
        self.summarize_cumulatives(means)
        self.summarize_information()
        
    def summarize_estimates(self, means):
        """Generate summary statistics for a set of regressions.

        regs: list of LogRegression
        means: map from variable to reference value
        """
        rows = []

        # for each regression, make a list of estimates
        for reg in self.regs:
            row = [est * means.get(name, 1) 
                   for name, est, _, _ in reg.estimates]
            rows.append(row)

        # cols is one column per variable
        cols = zip(*rows)

        # compute cis for the estimates
        cis = []
        pvals = []
        for col in cols:
            ci, pval = compute_ci(col)
            cis.append(ci)
            pvals.append(pval)

        self.estimate_cis = cis
        self.pvals = pvals

    def summarize_cumulatives(self, means):
        """Generate summary statistics for a set of regressions.

        means: map from variable to reference value
        """
        rows = []

        for reg in self.regs:
            cumulative = cumulative_odds(reg.estimates, means)
            rows.append([p for _, _, p in cumulative])

        # compute cis for the cumulative probabilities
        cols = zip(*rows)
        cis = []
        for col in cols:
            ci, pval = compute_ci(col)
            cis.append(ci)

        self.cumulative_cis = cis

    def summarize_information(self):
        """Generate summary statistics for a set of regressions.

        regs: list of LogRegression
        means: map from variable to reference value
        """
        self.aics = [reg.aic for reg in self.regs]
        self.sips = [reg.sip for reg in self.regs]

    def print_table(self):
        """Prints the table in human-readable form."""

        data = zip(self.names, 
                   self.estimate_cis, 
                   self.pvals,
                   self.cumulative_cis)

        for name, ci, pval, cumulative in data:
            odds_ci = np.exp(ci)
            print '%15.15s  \t' % name,
            print format_range(odds_ci), '  \t',
            print format_range(cumulative), '\t',
            print format_pvalue(pval)

        ci, pval = compute_ci(self.sips)
        print 'SIP:', format_range(ci, 3), format_pvalue(pval)

    def write_table(self, filename):
        """Writes the table in latex."""

        data = zip(self.names, 
                   self.estimate_cis, 
                   self.pvals,
                   self.cumulative_cis)

        header = ['Variable',
                  'Odds ratio',
                  'Probability',
                  'p-value',
                  ]

        rows = []
        for name, ci, pval, cumulative in data:
            odds_ci = np.exp(ci)
            row = [
                r'\verb"%s"' % name,
                format_range(odds_ci),
                format_range(cumulative),
                format_pvalue(pval),
                ]
            rows.append(row)

        fp = open(filename, 'w')
        format = '|l|r|r|r|'
        write_latex_table(fp, header, rows, format)
        fp.close()

def format_range(triple, digits=2, format='%0.*g (%0.*g, %0.*g)'):
    mean, low, high = triple
    if high < low:
        low, high = high, low

    return format % (digits, mean, digits, low, digits, high)


def format_pvalue(pval, min_val=0.001):
    if pval < min_val:
        return '*'
    else:
        return '%0.2g' % pval


def compute_ci(col):
    """Computes a 95% confidence interval.

    col: sequence of values

    Returns: CI tuple, p-value
    """
    n = len(col)
    index = n / 40
    mid = n / 2

    t = list(col)
    t.sort()
    median = t[mid]
    
    pval = compute_pvalue(median, t)

    low, high = t[index], t[-index-1]
    ci = np.array([median, low, high])

    return ci, pval


def compute_pvalue(median, t):
    """Computes the p-value for a list of outcomes.

    Counts the fraction of outcomes with the opposite sign from the median
    (or 0).

    median: median value from the list
    t: list of outcomes

    Returns: float prob
    """
    if median > 0:
        opp = [x for x in t if x <= 0]
    else:
        opp = [x for x in t if x >= 0]

    fraction = float(len(opp)) / len(t)
    return fraction
        

def cumulative_odds(estimates, means):
    """Computes cumulative odds based on a sequence of estimates.

    Iterates the attributes and computes the odds ratio, for
    the given value, and the probability that corresponds to
    the cumulative odds.

    estimates: list of (name, est, error, z)
    means: map from attribute to value

    Returns: list of (name, odds, p)
    """
    total_odds = 1.0
    res = []

    for name, est, _, _ in estimates:
        mean = means.get(name, 1)
        odds = math.exp(est * mean)
        total_odds *= odds
        p = 100 * total_odds / (1 + total_odds)
        res.append((name, odds, p))

    return res


def print_cumulative_odds(cumulative_odds):
    """Prints a summary of the estimated parameters.

    cumulative_odds: list of (name, odds, p)
    """
    print '\t\todds\tcumulative'
    print '\t\tratio\tprobability\tdiff'
    prev = None

    for name, odds, p in cumulative_odds:
        if prev:
            diff = p - prev
            print '%11s\t%0.2g\t%0.2g\t%0.2g' % (name, odds, p, diff)
        else:
            print '%11s\t%0.2g\t%0.2g' % (name, odds, p)
        prev = p


def write_latex_table(fp, header, rows, format):
    """Writes the data in a LaTeX table.

    """
    fp.write(r'\begin{tabular}{%s}' % format)
    fp.write(r'\hline' '\n')
    header = '&'.join(header)
    fp.write(header + r'\\' '\n')
    fp.write(r'\hline' '\n')

    for row in rows:
        row = '&'.join(row)
        fp.write(row + r'\\' '\n')
    
    fp.write(r'\hline' '\n')
    fp.write(r'\end{tabular}' '\n')


class SimpleRespondent(object):
    convert = dict()

    def clean(self):
        pass

class IncomeData(object):
    def __init__(self, shelf_file):
        self.shelf = shelve.open(shelf_file)

    def read_year_file(self, year):
        filename = 'gss.%d.csv' % year
        objs = columns.read_csv(filename, SimpleRespondent)

        if year in [2000, 2002, 2004]:
            attr = 'income98'
        elif year in [2006, 2010]:
            attr = 'income06'

        for obj in objs:
            income = getattr(obj, attr)
            print obj.year, obj.id, income
            key = '%d.%d' % (obj.year, obj.id)
            self.shelf[key] = income

    def close(self):
        self.shelf.close()

    def lookup(self, year, orig_id):
        key = '%d.%d' % (year, orig_id)
        return self.shelf.get(key)


def main(script):
    test_models()
    return

    income_data = IncomeData('gss.income_data.db')
    for year in [2004, 2002, 2000]:
        income_data.read_year_file(year)
    return

    auxiliary_models()
    return

    part_eight()
    return

    part_nine()
    return
    
    part_seven()
    return

    part_six()
    return

    part_four()
    return

    part_three()
    return



if __name__ == '__main__':
    import sys
    main(*sys.argv)

