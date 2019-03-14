# Exploring OxyContin Use in the United States 
## Abstract
## Introduction
The primary focus of this investigation was to investigate and interpret information in the NSDUH data set on medical and non-medical OxyContin use.  [According to the CDC](https://www.cdc.gov/drugoverdose/opioids/prescribed.html), OxyContin is among the most common prescription opioids involved in overdose death. OxyContin was approved for use by the FDA in 1995. The FDA at the time believed that because the drug was formulated to be slowly released in the body it would be less easy to abuse. However, since its approval OxyContin became the center of the opioid problem ([source](https://www.fda.gov/downloads/Drugs/DrugSafety/InformationbyDrugClass/UCM566985.pdf)).

## The Data Set

For this exploration, I chose to look at data from the 2014 National Survey on Drug Use and Health (NSDUH). This survey includes a number of questions asking participants about their history of OxyContin use, among other painkillers. NSDUH surveys after this year scaled back their specific OxyContin-related questions, so I chose to use the most recent survey in this study that provided a fair amount of information.

According to the [Substance Abuse and Mental Health Data Archive's page on the NSDUH data set](https://www.datafiles.samhsa.gov/study-series/national-survey-drug-use-and-health-nsduh-nid13517),

> "The National Survey on Drug Use and Health (NSDUH) series, formerly titled National Household Survey on Drug Abuse, is a major source of statistical information on the use of illicit drugs, alcohol, and tobacco and on mental health issues among U.S. civilians who are non-institutional population aged 12 or older. The survey tracks trends in specific substance use and mental illness measures and assesses the consequences of these conditions by examining mental and/or substance use disorders and treatment for these disorders."

This data set can be used to identify demographics of people at risk for abusing drugs and to find links between mental health and drug use.

The terms of use for using this data can be found on the [SAMDHA terms of use page](https://www.datafiles.samhsa.gov/info/terms-use-nid3422). One of the primary terms of use is that this data cannot be used to identify individuals who participated in the survey. I have not provided any identifying information about participants in this study.

### Study Details
The codebook for the 2014 NSDUH study can be found [here](http://samhda.s3-us-gov-west-1.amazonaws.com/s3fs-public/field-uploads-protected/studies/NSDUH-2014/NSDUH-2014-datasets/NSDUH-2014-DS0001/NSDUH-2014-DS0001-info/NSDUH-2014-DS0001-info-codebook.pdf).

The target demographic of the survey is the civilian, noninstitutionalized population of the United States who were 12 years of age or older at the time of the survey. The sample population includes the household population of all 50 states and the District of Columbia. Along with households, residents of non-institutional group quarters, such as dormitories, and people with no permanent resisdence. States with larger populations had larger sample sizes than smaller states and the District of Columbia. The sample allocations for the age groups susrveyed are as follows: 25% for 12-17 year olds, 25% for 18-25 year olds, 15% for 26-34 year olds, 20% for 35-49 year olds, and 15% for adults over 50 years old.

The study was conducted using computer-assisted-interviewing (CAI) methods. This includes both computer-assisted personal interviews, and computer-assited self interviews. The core of the study includes questions on the use of tobacco, alcohol, marijuana, cocaine, crack cocaine, heroine, hallucinogens, inhalents, pain relieves, tranquilizers, stimulants, and sedatives. There are also supplemental questions on demographics and mental health.

There are limitations of the 2014 survey listed in the codebook for this survey, which are important to note:
1. The data in the survey is self-reported, which means that it relies on the memory and truthfulness of the respondents' answers.
2. The survey is cross-sectional. Pariticpants were interviewed once and not followed for additional interviews in the future, so the survey does not provide information on how an individual's drug use changes over time.
3. The survey targets the civilian population of the United States, so active-duty military and individuals in institutional group quarters such as prisons and nursing homes are excluded. The codebook estimates that about 3% of the US population is excluded for this year.

### Survey Variables Used in Study
The 2014 NSDUH survey includes several variables pertaining to OxyContin use. I decided to use the following questions:

1. OXYCAGE: AGE WHEN FIRST USED OXYCONTIN NONMEDICALLY
    -How old were you the first time you used OxyContin that was not prescribed for you or that you took only for the experience or feeling it caused?
2. OXYCREC: TIME SINCE LAST USED OXYCONTIN NONMEDICALLY*
    -How long has it been since you last used OxyContin that was not prescribed for you or that you took only for the experience or feeling it caused?
3. OXYYRTOT: TOTAL # DAYS USED OXYCONTIN PAST 12 MONTHS
    -Total number of days used OxyContin in the past 12 months.
4. OXDAYPYR: # DAYS USED OXYCONTIN "NM" PAST 12 MONTHS
    -On how may days in the past 12 months did you use OxyContin that was not prescribed for you or that you took only for the experience or feeling it caused?

It is important here to define the term *non-medically* as "use of the substance that was not prescribed for the respondent, or that the respondent took only for the experience or feeling it caused. I will be using this term frequently throughout this report.

All of these questions came from the painreliver section of the self-administered substance use questions of the data set. Some logical editing was performed on these questions. The full procedure can be found in the codebook under the Logical Editing section, but in summary, variables were reassigned for consistency across respondent answers. an example is if the respondent answered that they have never used a particular drug, but later listed a version of that drug as something they had used, their answer to the first question was logically assigned to be that they had used it at some point.

Along with the OxyContin-specific questions, I also looked at a variable relating to the age of the participants.
1. AGE2: RECODE - FINAL EDITED AGE

This variable was determined using the respondents' answers reported age, birthday, and the time the study was conducted. It groups respondents into 17 age groups, with the range of ages in each group varying.

Finally, I also used the final person-level weights calculated for each participant for resampling ('ANALWT_C'). This variable indicates the number of people one respondent represents in the study.

#### Preparing the Data for Analysis
To create a more manageable amount of data for analysis, I created a DataFrame that only contained the columns of the 2014 NSDUH survey that I wanted to analyze (the questions listed in the previous section), the sample weights ('ANALWT\_C'), the age group of the respondent ('AGE2'), and the year of the survey, which I added as a column to the data. Because the data was given categorically, I converted it to numeric values as well.

To clean the data, I replaced several categorical codes to answers with NaNs, or with 0s, depending on the question's application. Below is a list of the variables, the codes that were replaced by another value, and the values that were substituted. These codes come from the codebooks for each survey year.:
- OXCNNMAGE:
    - 981: NEVER USED PAIN RLVRS Logically assigned -> NaN
    - 985: BAD DATA Logically assigned -> NaN
    - 991: NEVER USED/MISUSED PAIN RELIEVERS -> NaN
    - 993: DID NOT USE IN THE PAST 12 MONTHS -> NaN
    - 994: DON'T KNOW -> NaN
    - 997: REFUSED -> NaN
    - 998: BLANK (NO ANSWER) -> NaN
- OXYCAGE:
    - 981: NEVER USED OXYCONTIN Logically assigned -> NaN
    - 985: BAD DATA Logically assigned -> NaN
    - 991: NEVER USED OXYCONTIN -> NaN
    - 994: DON'T KNOW -> NaN
    - 997: REFUSED -> NaN
    - 998: BLANK (NO ANSWER) -> NaN
- OXYCREC:
    - 85: BAD DATA Logically assigned -> NaN
    - 97: REFUSED -> NaN
    - 98: BLANK (NO ANSWER) -> NaN
- OXYYRTOT:
    - 981: NEVER USED OXYCONTIN Logically assigned -> 0
    - 985: BAD DATA Logically assigned -> NaN
    - 991: NEVER USED OXYCONTIN -> 0
    - 993: DID NOT USE OXYCONTIN IN THE PAST 12 MOS -> 0
    - 994: DON'T KNOW -> NaN
    - 997: REFUSED -> NaN
    - 998: BLANK (NO ANSWER) -> NaN
- OXDAYPYR:
    - 981: NEVER USED OXYCONTIN Logically assigned -> 0
    - 985: BAD DATA Logically assigned -> NaN
    - 989: LEGITIMATE SKIP Logically assigned -> NaN
    - 991: NEVER USED OXYCONTIN -> 0
    - 993: DID NOT USE OXYCONTIN IN THE PAST 12 MOS -> 0
    - 997: REFUSED -> NaN
    - 998: BLANK (NO ANSWER) -> NaN
    - 999: LEGITIMATE SKIP -> NaN
    
I chose to replace some codes in the last two variables with 0s because respondents could either give a number of days or answer that they never used OxyContin in the last 12 months or ever. I wanted to make it easier to visulalize these answers along with the responses from people who had used OxyContin in the past year, so I converted them to a usable numeric value. This has the added benefit of being very easy to filter out when looking at only the people who used OxyContin in the 12 months prior to the survey.

Finally, I resampled the cleaned data using the person-level sample weights.

## Analysis of the Data

### Individual Variables
I started my analysis by looking at the individual varibles to get an idea of the responses to the survey and to pull out any information that may generate more analysis questions.

#### Age of Respondents.

The 'AGE2' variable groups respondents into 17 categories:
1. Respondent is 12 years old
2. Respondent is 13 years old
3. Respondent is 14 years old
4. Respondent is 15 years old
5. Respondent is 16 years old
6. Respondent is 17 years old
7. Respondent is 18 years old
8. Respondent is 19 years old
9. Respondent is 20 years old
10. Respondent is 21 years old
11. Respondent is 22 or 23 years old
12. Respondent is 24 or 25 years old
13. Respondent is between 26 and 29 years old
14. Respondent is between 30 and 34 years old
15. Respondent is between 35 and 49 years old
16. Respondent is between 50 and 64 years old
17. Respondent is 65 years old or older

The PMF and CDF of the ages are shown below.
![PMF of AGE2](figures/age2_pmf.png)
![CDF of AGE2](figures/age2_cdf.png)

To get a better idea of the age distribution, I compressed the younger age groups. The new age groups I made are:
1. Respondent is between 12 and 19 years old
2. Respondent is between 20 and 29 years old
3. Respondent is between 30 and 34 years old
4. Respondent is between 35 and 49 years old
5. Respondent is between 50 and 64 years old
6. Respondent is 65 years old or older

The PMF and CDF of the new groupings are shown below.
![PMF of AGE2](figures/age2_grouped_pmf.png)
![CDF of AGE2](figures/age2_grouped_cdf.png)

#### Age of First Trying OxyContin Non-medically
#### Time Since Last Trying OxyContin Non-medically
#### Total Number of Days Using OxyContin in 12 Months Prior to Survey
#### Number of Days Using OxyContin Non-Medically in 12 Months Prior to Survey


#### Age of First Try By Grouped by Age of Respondent
In order to get a better idea of the trend in ages that people try OxyContin non-medically for the first time, I created histograms for age groupings. These are shown below.

For the most part, I chose to use the age groupings that the survey put respondents into initially. However, for the younger ages, I decided to further group them together. The groupings I chose to look at were:
* Ages 12 - 19
* Ages 20 - 25
* Ages 26 - 29
* Ages 30 - 34
* Ages 35 - 49
* Ages 50 - 64
* Ages 65 and over

![histogram of ages 12-19](figures/age12_19.png)
![histogram of ages 20-25](figures/age20_25.png)
![histogram of ages 26-29](figures/age26_29.png)
![histogram of ages 30-34](figures/age30_34.png)
![histogram of ages 30-34](figures/age30_34.png)
![histogram of ages 35-49](figures/age35-49.png)
![histogram of ages 50-64](figures/age50_64.png)
![histogram of ages 65 and over](figures/age65_over.png)

I was very puzzled by the fact that in all age groups, the majority of the respondents reported trying OxyContin for the first time non-medically in their 40s and 50s, which doesn't make sense because this is older than the age of the respondents reporting it. I can't find anything in the codebook to indicate why this would be the case, but it may be related to the observation I made that none of the respondents reported first trying OxyContin in their 20s and 30s. I'm hesitant to draw any conclusions from this analysis because the data doesn't seem to make sense. However, one interesting thing to note is that for younger respondents, there are more people who reported trying OxyContin between the ages of 8 and 25. I wonder if there is some trend in that data that is being obscured by the strange cluster around 50 years.

### Frequency of Using OxyContin Non-medically
I chose to also explore the frequency that people used OxyContin in addition to the age at which they first tried it non-medically. This is important to understand because it points to the severity of the problem. If someone tried OxyContin once non-medically and never tried it again, I would not be concerned for that person, but if they are a frequent or regular user, that is a much stronger indicator of there being a problem. The questions I analyzed in this section all came from the 2007 - 2014 surveys because the more recent surveys do not include similar questions or information.

#### Last Time Using OxyContin Non-medically
I first wanted to look at the last time people who took OxyContin non-medically used it. The histogram of some of the responses to OXYCREC is shown below.

![histogram of last time using oxy](figures/last_use.png)

This is only representative of the people who used OxyContin non-medically at all. In the data I cleaned, there appear to be no responses coded for people who never used OxyContin non-medically or ever, which is inconsistent with what is reported in the codebooks. However, I couldn't find the reason for the missing data. It appears that most people who had ever taken OxyContin non-medically took it within 12 months of the survey, which could make sense given that opioids are highly addictive, and if someone were to use them non-medically, they would be likely to use them frequently. The large majority reported using OxyContin at least a month prior to the survey.

#### Total Days Using OxyContin in the Last Year
I next wanted to look at the total number of days that people used OxyContin in the last year to get a better indicator of the frequency of use. The PMF and CDF of the responses to OXDAYPYR are shown below

![pmf of total days using OxyContin in last year](figures/days_pmf.png)
![cdf of total days using OxyContin in last year](figures/days_cdf.png)

The first thing I noticed is that very few people reported 0 days of use in the past year, which is highly improbable considering that so many of the people surveyed were children, and even among adults, I wouldn't expect to see close to everyone having taken OxyContin in the last year at some point. This is, however, probably indicative of the fact that there seem to be missing respondents in the data who have never taken OxyContin, as discussed in the previous section. The likelihood of a respondent having taken OxyContin at least 30 days in the last year is close to 50%. Another indicator that this data is not correct is that no respondents took OxyContin for more than 50 days in the year prior to the survey. This is confusing because I would expect at least a handful of respondent to have reported using OxyContin nearly every day in the year. Given these observations about the data, I cannot confidently draw any hypotheses or conclusions from these distributions.

## Conclusion
I ended up not coming to a great number of conclusions based on this data. Although I could not pinpoint a specific reason, the responses to the questions I was looking at did not make sense or were missing large pieces of information. Some trends I observed that could merit future analysis were that young people were more likely to try OxyContin non-medically earlier than the age of 20, and that most people who used OxyContin non-medically at some point in their lives had also used it non-medically in the year prior to the survey they participated in.

## Future Work
Although this analysis yielded very little useful information, I still believe that there is a lot to be learned from the NSDUH data set with some more understanding of how responses to questions were recorded and coded. In addition to making sure data was interpreted and collected correctly, I would be interested in the future to dive deeper into the relationship between the age of respondents and the age at which they first tried OxyContin.

Finally, I think that it is important in future work to look at the relationship between OxyContin use and other opioid use. I do not think that OxyContin alone is representative of opioid use in the United States, and I would be especially interested to see how prescription and non prescriptions opioids like heroine are related.
