# Exploring Opioid Use in the NSDUH data set
The primary focus of this investigation was to investigate and interpret findings in the NSDUH data set on Oxycontin use.

## The Data Set

For this exploration, I chose to look at data from the National Survey on Drug Use and Health from 2007 to 2017.

According to the [Substance Abuse and Mental Health Data Archive's page on the NSDUH data set](https://www.datafiles.samhsa.gov/study-series/national-survey-drug-use-and-health-nsduh-nid13517),

> "The National Survey on Drug Use and Health (NSDUH) series, formerly titled National Household Survey on Drug Abuse, is a major source of statistical information on the use of illicit drugs, alcohol, and tobacco and on mental health issues among members of the U.S. civilian, non-institutional population aged 12 or older. The survey tracks trends in specific substance use and mental illness measures and assesses the consequences of these conditions by examining mental and/or substance use disorders and treatment for these disorders."

This data set can be used to identify the risk of populations abusing drugs and to find links between mental health and drug use.

The terms of use for using this data can be found on the [SAMDHA terms of use page](https://www.datafiles.samhsa.gov/info/terms-use-nid3422).

### Opioid Use.
#### Questions
I chose to look at patterns in prescription opioid use. The NSDUH series provides several questions about oxycontin use under the painkillers category relating to oxycontin use. Oxycontin is one of the most commonly used prescription opioids [according to the CDC](https://www.cdc.gov/drugoverdose/opioids/prescribed.html). The questions related to Oxycontin use in the 2007 - 2014 surveys differ from the questions in the 2015 - 2017 surveys. For the earlier surveys, I decided to use the following questions:

1. OXYCAGE: How old were you the first time you used Oxycontin that was not prescribed for you or that you took only for the experience or feeling it caused?
2. OXYCREC: How long has it been since you last used OxyContin that was not prescribed for you or that you took only for the experience or feeling it caused?
3. OXYYRTOT: Total number of days used Oxycontin in the past 12 months.
4. OXDAYPYR: On how may days in the past 12 months did you use Oxycontin that was not presctibed for you or that you took only for the experience or feeling it caused?

For the later surveys, I decided to look at the following question:

1. OXCNNMAGE: How old were you when you first used Oxycontin in a way a doctor did not direct you to use it?

Although the wording of the question changed, I chose to treat the answers to OXYCAGE and OXCNNMAGE as answers to the same question.

#### Preparing the Data for Analysis
To create a more manageable amount of data for analysis, I created a dataframe that just contained the columns I wanted to analyze (the questions listed in the previous section), the sample weights ('ANALWT\_C'), the age group of the respondant ('AGE2'), and the year of the survey, which I added as a column to the data.

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

Due to time constraints, I chose not to resample the data, however, I provided a column of weights in order to resample the data in future analysis.

After the data was cleaned, I saved the new data frame to `oxy.hdf5` under the key `oxycontin` in order to more quickly load the relevant data in the furture.

## Analysis of the Data

### Age of First Use
The age at which people first try a drug can say a lot about which demographics are at a high risk of choosing to use the drug. I decided to look at the distribution of the age of the respondants, the distribution of ages that respondants first tried oxycontin nonmedically, and the breakdown of that distribution by age group.

#### Distribution of Age of Respondants
To get an idea of the distribution of the ages of respondants, I made a histogram of the age groups, which can be seen below.
![histogram of age group distribution](figures/age_group_dist.png)

#### Distribution of Age of First Trying Oxycontin Nonmedically

#### Distribution of Age of First Try By Age of Respondant
