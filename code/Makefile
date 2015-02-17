FILES = \
analytic.py    chap06soln.py     first.py       populations.py \
brfss.py       chap07soln.py     hinc2.py       probability.py \
chap01ex.py    chap08soln.py     hinc.py        regression.py \
chap09soln.py     hinc_soln.py   relay.py \
chap01soln.py  chap12soln.py     hypothesis.py  relay_soln.py \
chap02ex.py    chap13soln.py     linear.py      survival.py \
cumulative.py     mystery.py     test_models.py thinkplot.py \
chap02soln.py  density.py        normal.py      thinkstats2.py \
chap03soln.py  nsfg2.py       thinkstats2_test.py \
estimation.py     nsfg.py        timeseries.py \
chap01ex.ipynb    chap02soln.ipynb  chap04ex.ipynb    chap05soln.ipynb \
chap01soln.ipynb  chap03ex.ipynb    chap04soln.ipynb  chap10soln.ipynb \
chap02ex.ipynb    chap03soln.ipynb  chap05ex.ipynb    chap11soln.ipynb \
chap14soln.py    Makefile

DATA = \
1995FemRespData.dat.gz  2002Male.dat.gz           2006_2010_Male.dat.gz \
2002FemPreg.dat.gz      2006_2010_FemPreg.dat.gz  \
2002FemResp.dat.gz      2006_2010_FemResp.dat.gz  CDBRFS08.ASC.gz \
hinc06.csv    PEP_2012_PEPANNRES_metadata.csv  populations.csv \
PEP_2012_PEPANNRES_with_ann.csv 		babyboom.dat   \
Apr25_27thAn_set1.shtml
# mj-clean.csv  


git:
	git add $(FILES) $(DATA)


DEST = /home/downey/public_html/greent/thinkstats2

distrib:
	rsync *.html $(DEST)
	cd /home/downey/public_html/greent; sh back

FIGS = observed_speeds.* \
pareto_cdf.* \
pareto_height.* \
linear5.* \
populations.*             estimation1.*           linear4.* \
hypothesis1.*           linear3.* \
linear1.*               linear2.* \
example_cdf.*             scatter1.*              scatter2.*\
expo_cdf.*                nsfg_birthwgt_pmf.*     scatter3.*\
nsfg_diffs.*            \
nsfg_hist.*             \
nsfg_pmf.*              \
pdf_example.* 	          correlate1.* \
first_wgt_lb_hist.*       first_wgt_oz_hist.*     first_agepreg_hist.* \
first_prglngth_hist.*	  first_nsfg_hist.*       \
probability_nsfg_diffs.*  probability_nsfg_pmf.* \
class_size1.* \
cumulative_birthwgt_cdf.*  cumulative_example_cdf.*   cumulative_random.* \
cumulative_birthwgt_pmf.*  cumulative_prglngth_cdf.* \
analytic_birthwgt_model.* \
analytic_birthwgt_normal.* analytic_pareto_cdf.* \
analytic_expo_cdf.*        analytic_pareto_height.* \
analytic_interarrivals.*   analytic_interarrivals_logy.* \
analytic_normal_prob_example.* \
brfss_weight.*	 	   brfss_weight_normal.* \
populations_normal.*       populations_pareto.* \
density_totalwgt_kde.*     density_wtkg2_kde.* \
timeseries1.*              timeseries2.*               timeseries3.* \
timeseries4.*		   timeseries8.*               timeseries10.* \
timeseries9.*              timeseries5.*               survival1.* \
survival2.*                survival3.*                 survival4.* \
survival5.*                survival6.* 	               normal1.* \
normal2.*                  normal3.*                   normal4.* \
normal5.*

all_figs:
	# TODO: update this
	python descriptive.py
	python cumulative.py
	python babyboom.py
	python continuous.py
	python hypothesis.py
	python locomotive.py
	python brfss_figs.py
	python brfss_scatter.py

FIGDEST = ../book/figs

figs:
	rsync -a $(FIGS) $(FIGDEST)


DOCS = thinkstats2.html thinkplot.html

DOCPY = thinkstats2.py thinkplot.py

%.html: %.py
	pydoc -w $<

.PHONY: docs $(DOCPY)

docs: $(DOCPY)

$(DOCPY):
	pydoc -w ./$@

