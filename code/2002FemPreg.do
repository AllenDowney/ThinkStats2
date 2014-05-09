/**************************************************************************
*
* NATIONAL SURVEY OF FAMILY GROWTH
* 2002 SURVEY - PUBLIC USE FEMALE PREGNANCY FILE
*
***************************************************************************
*
* STATA SETUP FILE
*
* Please edit this file as instructed below.                            
* To execute, start Stata, change to the directory containing:          
*        - this do file                                                   
*        - the ASCII data file                                            
*        - the dictionary file                                            
*                                                                         
*   Then execute the do file (e.g., do FemPreg.do)          
*                                                                         
***************************************************************************/

/* Allocate 6 megabytes of RAM for Stata SE to read data file into memory.*/
set mem 6m

/* Prevent the Stata output viewer from pausing the process.*/
set more off                 


/**************************************************************************
*
* Section 1: File Specifications
*    This section assigns local macros to the necessary files.
*    Please edit if necessary:
*        "raw-datafile-name" ==> The name of data file downloaded from ICPSR
*        "dictionary-filename" ==> The name of the dictionary file downloaded.
*        "stata-datafile" ==> The name you wish to call your Stata data file.
*
*    Note: We assume that the raw data, dictionary, and setup (this do file) 
*          all reside in the same directory (or folder). If that is not the 
*          case you will need to include paths as well as filenames in the 
*          macros.
*
***************************************************************************/

local raw_data ".\FemPreg.dat"
local dict ".\FemPreg.dct"
local outfile ".\FemPreg.dta"


/**************************************************************************
*
* Section 2: Infile Command
*
* This section reads the raw data into Stata format.  If Section 1 was 
* defined properly there should be no reason to modify this section. These
* macros should inflate automatically.
*
***************************************************************************/

infile using `dict', using (`raw_data') clear


/**************************************************************************
*
* Section 3: Value Label Definitions
* This section defines labels for the individual values of each variable.
*
***************************************************************************/

label data "NSFG 2002 Public Use Female Pregnancy Data"

#delimit ;
 label define pregordr
   1 "1ST PREGNANCY"
   2 "2ND PREGNANCY"
   3 "3RD PREGNANCY"
   4 "4TH PREGNANCY"
   5 "5TH PREGNANCY"
   6 "6TH PREGNANCY"
   7 "7TH PREGNANCY"
   8 "8TH PREGNANCY"
   9 "9TH PREGNANCY"
  10 "10TH PREGNANCY"
  11 "11TH PREGNANCY"
  12 "12TH PREGNANCY"
  13 "13TH PREGNANCY"
  14 "14TH PREGNANCY"
  15 "15TH PREGNANCY"
  16 "16TH PREGNANCY"
  17 "17TH PREGNANCY"
  18 "18TH PREGNANCY"
  19 "19TH PREGNANCY";

 label define howpreg_p
   1 "WEEKS"
   2 "MONTHS";

 label define moscurrp
  97 "NOT ASCERTAINED";

 label define nowprgdk
   1 "FIRST TRIMESTER"
   2 "SECOND TRIMESTER"
   3 "THIRD TRIMESTER";

 label define pregend1
   1 "MISCARRIAGE"
   2 "STILLBIRTH"
   3 "ABORTION"
   4 "ECTOPIC OR TUBAL"
   5 "LIVE BIRTH BY CESAREAN SECTION"
   6 "LIVE BIRTH BY VAGINAL DELIVERY";

 label define pregend2
   1 "MISCARRIAGE"
   2 "STILLBIRTH"
   3 "ABORTION"
   4 "ECTOPIC OR TUBAL"
   5 "LIVE BIRTH BY CESAREAN SECTION"
   6 "LIVE BIRTH BY VAGINAL DELIVERY";

 label define nbrnaliv
   1 "1 BABY"
   2 "2 BABIES"
   3 "3 BABIES" 
   4 "4 BABIES" 
   5 "5 BABIES";

 label define multbrth
   1 "YES"
   5 "NO";

 label define prgoutcome
   1 "LIVE BIRTH"
   2 "PREGNANCY LOSS OR ABORTION"
   3 "CURRENT PREGNANCY";

 label define flgdkmo1
   0 "EXACT MONTH & YEAR REPORTED"
   1 "SEASON REPORTED FOR MONTH"
   2 "MONTH REPORTED AS DK/RF"
   7 "NOT ASCERTAINED";

 label define gestasun_m
  97 "NOT ASCERTAINED";

 label define mosgest
  97 "NOT ASCERTAINED";

 label define dk1gest
   1 "LESS THAN 6 MONTHS"
   2 "6 MONTHS OR MORE";

 label define dk2gest
   1 "YES"
   5 "NO";

 label define dk3gest
   1 "LESS THAN 3 MONTHS"
   2 "3 MONTHS OR MORE, BUT LESS THAN 6 MONTHS"
   3 "6 MONTHS OR MORE";

 label define bpa_bdscheck1
   0 "NEITHER BPA NOR BDS"
   1 "BPA"
   2 "BDS";

 label define bpa_bdscheck2
   0 "NEITHER BPA NOR BDS"
   1 "BPA"
   2 "BDS";

 label define bpa_bdscheck3
   0 "NEITHER BPA NOR BDS"
   1 "BPA"
   2 "BDS";

 label define babysex
   1 "MALE"
   2 "FEMALE";

 label define birthwgt_lb
   0 "LESS THAN 1 POUND"
   1 "1 POUND"
   2 "2 POUNDS"
   3 "3 POUNDS"
   4 "4 POUNDS"
   5 "5 POUNDS"
   6 "6 POUNDS"
   7 "7 POUNDS"
   8 "8 POUNDS"
   9 "9 POUNDS"
   10 "10 POUNDS"
   11 "11 POUNDS"
   12 "12 POUNDS"
   13 "13 POUNDS"
   14 "14 POUNDS"
   15 "15 POUNDS";

 label define lobthwgt
   1 "5 1/2 POUNDS OR MORE"
   2 "LESS THAN 5 1/2 POUNDS";

 label define babysex2
   1 "MALE"
   2 "FEMALE";

 label define birthwgt_lb2
   0 "LESS THAN 1 POUND"
   1 "1 POUND"
   2 "2 POUNDS"
   3 "3 POUNDS"
   4 "4 POUNDS"
   5 "5 POUNDS"
   6 "6 POUNDS"
   7 "7 POUNDS"
   8 "8 POUNDS"
   9 "9 POUNDS"
   10 "10 POUNDS"
   11 "11 POUNDS"
   12 "12 POUNDS"
   13 "13 POUNDS"
   14 "14 POUNDS"
   15 "15 POUNDS";

 label define lobthwgt2
   1 "5 1/2 POUNDS OR MORE"
   2 "LESS THAN 5 1/2 POUNDS";

 label define babysex3
   1 "MALE"
   2 "FEMALE";

 label define birthwgt_lb3
   0 "LESS THAN 1 POUND"
   1 "1 POUND"
   2 "2 POUNDS"
   3 "3 POUNDS"
   4 "4 POUNDS"
   5 "5 POUNDS"
   6 "6 POUNDS"
   7 "7 POUNDS"
   8 "8 POUNDS"
   9 "9 POUNDS"
   10 "10 POUNDS"
   11 "11 POUNDS"
   12 "12 POUNDS"
   13 "13 POUNDS"
   14 "14 POUNDS"
   15 "15 POUNDS";

 label define lobthwgt3
   1 "5 1/2 POUNDS OR MORE"
   2 "LESS THAN 5 1/2 POUNDS";

 label define birthplc
   1 "IN A HOSPITAL"
   2 "IN A BIRTHING CENTER"
   3 "IN YOUR HOME"
   4 "SOME OTHER PLACE";

 label define paybirth1
   1 "INSURANCE"
   2 "CO-PAYMENT OR OUT-OF-POCKET PAYMENT"
   3 "MEDICAID"
   4 "NO PAYMENT REQUIRED"
   5 "SOME OTHER WAY";

 label define paybirth2
   1 "INSURANCE"
   2 "CO-PAYMENT OR OUT-OF-POCKET PAYMENT"
   3 "MEDICAID"
   4 "NO PAYMENT REQUIRED"
   5 "SOME OTHER WAY";

 label define paybirth3
   1 "INSURANCE"
   2 "CO-PAYMENT OR OUT-OF-POCKET PAYMENT"
   3 "MEDICAID"
   4 "NO PAYMENT REQUIRED"
   5 "SOME OTHER WAY";

 label define trimestr
   1 "LESS THAN 3 MONTHS"
   2 "AT LEAST 3 MONTHS BUT LESS THAN 6 MONTHS"
   3 "6 OR MORE MONTHS";

 label define ltrimest
   1 "LESS THAN 3 MONTHS"
   2 "MORE THAN 3 MONTHS";

 label define priorsmk
   0 "NONE"
   1 "ABOUT ONE CIGARETTE A DAY OR LESS"
   2 "JUST A FEW CIGARETTES A DAY (2-4)"
   3 "ABOUT HALF A PACK A DAY (5-14)"
   4 "ABOUT A PACK A DAY (15-24)"
   5 "ABOUT 1 1/2 PACKS A DAY (25-34)"
   6 "ABOUT 2 PACKS A DAY (35-44)"
   7 "MORE THAN 2 PACKS A DAY (45 OR MORE)";

 label define postsmks
   1 "YES"
   5 "NO";

 label define npostsmk
   1 "ABOUT ONE CIGARETTE A DAY OR LESS"
   2 "JUST A FEW CIGARETTES A DAY (2-4)"
   3 "ABOUT HALF A PACK A DAY (5-14)"
   4 "ABOUT A PACK A DAY (15-24)"
   5 "ABOUT 1 1/2 PACKS A DAY (25-34)"
   6 "ABOUT 2 PACKS A DAY (35-44)"
   7 "MORE THAN 2 PACKS A DAY (45 OR MORE)";

 label define getprena
   1 "YES"
   5 "NO";

 label define pnctrim
   1 "LESS THAN 3 MONTHS"
   2 "AT LEAST 3 MONTHS BUT LESS THAN 6 MONTHS"
   3 "6 OR MORE MONTHS";

 label define lpnctri
   1 "LESS THAN 3 MONTHS"
   2 "MORE THAN 3 MONTHS";

 label define workpreg
   1 "YES"
   5 "NO"
   6 "R VOLUNTEERED SHE WORKED DURING PREGNANCY, BUT QUIT JOB BEFORE DELIVERY";

 label define workborn
   1 "YES"
   5 "NO";

 label define didwork
   1 "DID NOT NEED TO TAKE MATERNITY LEAVE"
   2 "WERE NOT OFFERED OR ALLOWED TO TAKE MATERNITY LEAVE"
   3 "SOME OTHER REASON";

 label define weeksdk
   1 "4 WEEKS OR LESS"
   2 "LONGER THAN 4 WEEKS";

 label define matchfound
   1 "YES"
   5 "NO";

 label define livehere
   1 "YES"
   5 "NO";

 label define alivenow
   1 "YES"
   5 "NO";

 label define wherenow
   1 "WITH BIOLOGICAL FATHER"
   2 "WITH OTHER RELATIVES"
   3 "WITH ADOPTIVE FAMILY"
   4 "AWAY AT SCHOOL/COLLEGE"
   5 "LIVING ON OWN"
   6 "OTHER";

 label define legagree
   1 "YES"
   5 "NO";

 label define parenend
   1 "YES"
   5 "NO";

 label define anynurse
   1 "YES"
   5 "NO";

 label define fedsolid
   1 "YES"
   5 "NO";

 label define frsteatd_p
   1 "MONTHS"
   2 "WEEKS"
   3 "DAYS";

 label define frsteatd
   0 "LESS THAN 1 MONTH"
   1 "1 MONTH"
   2 "2 MONTHS"
   3 "3 MONTHS"
   4 "4 MONTHS"
   5 "5 MONTHS"
   6 "6 MONTHS";

 label define quitnurs
   1 "YES"
   5 "NO";

 label define ageqtnur_p
   1 "MONTHS"
   2 "WEEKS"
   3 "DAYS";

 label define ageqtnur
   0 "LESS THAN 1 MONTH OLD";

 label define matchfound2
   1 "YES"
   5 "NO";

 label define livehere2
   1 "YES"
   5 "NO";

 label define alivenow2
   1 "YES"
   5 "NO";

 label define wherenow2
   1 "WITH BIOLOGICAL FATHER"
   2 "WITH OTHER RELATIVES"
   3 "WITH ADOPTIVE FAMILY"
   4 "AWAY AT SCHOOL/COLLEGE"
   5 "LIVING ON OWN"
   6 "OTHER";

 label define legagree2
   1 "YES"
   5 "NO";

 label define parenend2
   1 "YES"
   5 "NO";

 label define anynurse2
   1 "YES"
   5 "NO";

 label define fedsolid2
   1 "YES"
   5 "NO";

 label define frsteatd_p2
   1 "MONTHS"
   2 "WEEKS"
   3 "DAYS";

 label define frsteatd2
   0 "LESS THAN 1 MONTH"
   1 "1 MONTH"
   2 "2 MONTHS"
   3 "3 MONTHS"
   4 "4 MONTHS"
   5 "5 MONTHS"
   6 "6 MONTHS";

 label define quitnurs2
   1 "YES"
   5 "NO";

 label define ageqtnur_p2
   1 "MONTHS"
   2 "WEEKS"
   3 "DAYS";

 label define ageqtnur2
   0 "LESS THAN 1 MONTH OLD";

 label define matchfound3
   1 "YES"
   5 "NO";

 label define livehere3
   1 "YES"
   5 "NO";

 label define alivenow3
   1 "YES"
   5 "NO";

 label define wherenow3
   1 "WITH BIOLOGICAL FATHER"
   2 "WITH OTHER RELATIVES"
   3 "WITH ADOPTIVE FAMILY"
   4 "AWAY AT SCHOOL/COLLEGE"
   5 "LIVING ON OWN"
   6 "OTHER";

 label define legagree3
   1 "YES"
   5 "NO";

 label define parenend3
   1 "YES"
   5 "NO";

 label define anynurse3
   1 "YES"
   5 "NO";

 label define fedsolid3
   1 "YES"
   5 "NO";

 label define frsteatd_p3
   1 "MONTHS"
   2 "WEEKS"
   3 "DAYS";

 label define frsteatd3
   0 "LESS THAN 1 MONTH"
   1 "1 MONTH"
   2 "2 MONTHS"
   3 "3 MONTHS"
   4 "4 MONTHS"
   5 "5 MONTHS"
   6 "6 MONTHS";

 label define quitnurs3
   1 "YES"
   5 "NO";

 label define ageqtnur_p3
   1 "MONTHS"
   2 "WEEKS"
   3 "DAYS";

 label define ageqtnur3
   0 "LESS THAN 1 MONTH OLD";

 label define evuseint
   1 "YES"
   5 "NO";

 label define stopduse
   1 "YES"
   5 "NO";

 label define whystopd
   1 "YES"
   5 "NO";

 label define whatmeth01
   1 "NO METHOD USED"
   2 "OFFICE USE ONLY"
   3 "BIRTH CONTROL PILLS"
   4 "CONDOM"
   5 "PARTNER S VASECTOMY"
   6 "STERILIZING OPERATION/TUBAL LIGATION"
   7 "WITHDRAWAL, PULLING OUT"
   8 "DEPO-PROVERA, INJECTABLES (SHOT)"
   9 "NORPLANT (TM) IMPLANTS"
  10 "RHYTHM OR SAFE PERIOD BY CALENDAR"
  11 "SAFE PERIOD BY TEMPERATURE OR CERVICAL MUCUS TEST, NATURAL FAMILY PLANNING"
  12 "DIAPHRAGM"
  13 "FEMALE CONDOM, VAGINAL POUCH"
  14 "FOAM"
  15 "JELLY OR CREAM"
  16 "CERVICAL CAP"
  17 "SUPPOSITORY, INSERT"
  18 "TODAY (TM) SPONGE"
  19 "IUD, COIL, OR LOOP"
  20 "'MORNING AFTER' PILLS OR EMERGENCY CONTRACEPTION"
  21 "OTHER METHOD"
  22 "RESPONDENT WAS STERILE"
  23 "RESPONDENT'S PARTNER WAS STERILE"
  24 "LUNELLE INJECTABLE (MONTHLY SHOT)"
  25 "CONTRACEPTIVE PATCH";

 label define whatmeth02
   1 "NO METHOD USED"
   2 "OFFICE USE ONLY"
   3 "BIRTH CONTROL PILLS"
   4 "CONDOM"
   5 "PARTNER S VASECTOMY"
   6 "STERILIZING OPERATION/TUBAL LIGATION"
   7 "WITHDRAWAL, PULLING OUT"
   8 "DEPO-PROVERA, INJECTABLES (SHOT)"
   9 "NORPLANT (TM) IMPLANTS"
  10 "RHYTHM OR SAFE PERIOD BY CALENDAR"
  11 "SAFE PERIOD BY TEMPERATURE OR CERVICAL MUCUS TEST, NATURAL FAMILY PLANNING"
  12 "DIAPHRAGM"
  13 "FEMALE CONDOM, VAGINAL POUCH"
  14 "FOAM"
  15 "JELLY OR CREAM"
  16 "CERVICAL CAP"
  17 "SUPPOSITORY, INSERT"
  18 "TODAY (TM) SPONGE"
  19 "IUD, COIL, OR LOOP"
  20 "'MORNING AFTER' PILLS OR EMERGENCY CONTRACEPTION"
  21 "OTHER METHOD"
  22 "RESPONDENT WAS STERILE"
  23 "RESPONDENT'S PARTNER WAS STERILE"
  24 "LUNELLE INJECTABLE (MONTHLY SHOT)"
  25 "CONTRACEPTIVE PATCH";

 label define whatmeth03
   1 "NO METHOD USED"
   2 "OFFICE USE ONLY"
   3 "BIRTH CONTROL PILLS"
   4 "CONDOM"
   5 "PARTNER S VASECTOMY"
   6 "STERILIZING OPERATION/TUBAL LIGATION"
   7 "WITHDRAWAL, PULLING OUT"
   8 "DEPO-PROVERA, INJECTABLES (SHOT)"
   9 "NORPLANT (TM) IMPLANTS"
  10 "RHYTHM OR SAFE PERIOD BY CALENDAR"
  11 "SAFE PERIOD BY TEMPERATURE OR CERVICAL MUCUS TEST, NATURAL FAMILY PLANNING"
  12 "DIAPHRAGM"
  13 "FEMALE CONDOM, VAGINAL POUCH"
  14 "FOAM"
  15 "JELLY OR CREAM"
  16 "CERVICAL CAP"
  17 "SUPPOSITORY, INSERT"
  18 "TODAY (TM) SPONGE"
  19 "IUD, COIL, OR LOOP"
  20 "'MORNING AFTER' PILLS OR EMERGENCY CONTRACEPTION"
  21 "OTHER METHOD"
  22 "RESPONDENT WAS STERILE"
  23 "RESPONDENT'S PARTNER WAS STERILE"
  24 "LUNELLE INJECTABLE (MONTHLY SHOT)"
  25 "CONTRACEPTIVE PATCH";

 label define whatmeth04
   1 "NO METHOD USED"
   2 "OFFICE USE ONLY"
   3 "BIRTH CONTROL PILLS"
   4 "CONDOM"
   5 "PARTNER S VASECTOMY"
   6 "STERILIZING OPERATION/TUBAL LIGATION"
   7 "WITHDRAWAL, PULLING OUT"
   8 "DEPO-PROVERA, INJECTABLES (SHOT)"
   9 "NORPLANT (TM) IMPLANTS"
  10 "RHYTHM OR SAFE PERIOD BY CALENDAR"
  11 "SAFE PERIOD BY TEMPERATURE OR CERVICAL MUCUS TEST, NATURAL FAMILY PLANNING"
  12 "DIAPHRAGM"
  13 "FEMALE CONDOM, VAGINAL POUCH"
  14 "FOAM"
  15 "JELLY OR CREAM"
  16 "CERVICAL CAP"
  17 "SUPPOSITORY, INSERT"
  18 "TODAY (TM) SPONGE"
  19 "IUD, COIL, OR LOOP"
  20 "'MORNING AFTER' PILLS OR EMERGENCY CONTRACEPTION"
  21 "OTHER METHOD"
  22 "RESPONDENT WAS STERILE"
  23 "RESPONDENT'S PARTNER WAS STERILE"
  24 "LUNELLE INJECTABLE (MONTHLY SHOT)"
  25 "CONTRACEPTIVE PATCH";

 label define resnouse
   1 "YES"
   5 "NO";

 label define wantbold
   1 "YES"
   5 "NO";

 label define probbabe
   1 "PROBABLY YES"
   5 "PROBABLY NOT"
   6 "DIDN'T CARE";

 label define cnfrmno
   1 "CORRECT"
   2 "INCORRECT";

 label define wantbld2
   1 "YES"
   5 "NO"
   7 "DIDN'T CARE";

 label define timingok
   1 "TOO SOON"
   2 "RIGHT TIME"
   3 "LATER"
   4 "DIDN'T CARE";

 label define toosoon_p
   1 "MONTHS"
   2 "YEARS";

 label define wthpart1
   1 "DEFINITELY YES"
   2 "PROBABLY YES"
   3 "PROBABLY NO"
   4 "DEFINITELY NO";

 label define wthpart2
   1 "DEFINITELY YES"
   2 "PROBABLY YES"
   3 "PROBABLY NO"
   4 "DEFINITELY NO";

 label define feelinpg
   1 "VERY UNHAPPY"
   2 "2"
   3 "3"
   4 "4"
   5 "5"
   6 "6"
   7 "7"
   8 "8"
   9 "9"
  10 "VERY HAPPY";

 label define hpwnold
   1 "YES"
   5 "NO";

 label define timokhp
   1 "TOO SOON"
   2 "RIGHT TIME"
   3 "LATER"
   4 "DIDN'T CARE";

 label define cohpbeg
   1 "YES"
   5 "NO";

 label define cohpend
   1 "YES"
   5 "NO";

 label define tellfath
   1 "YES"
   5 "NO";

 label define whentell
   1 "DURING THE PREGNANCY"
   2 "AFTER THE (PREGNANCY ENDED/BABY WAS BORN)";

 label define tryscale
   0 "0"
   1 "1"
   2 "2"
   3 "3"
   4 "4"
   5 "5"
   6 "6"
   7 "7"
   8 "8"
   9 "9"
  10 "10";

 label define wantscal
   0 "0"
   1 "1"
   2 "2"
   3 "3"
   4 "4"
   5 "5"
   6 "6"
   7 "7"
   8 "8"
   9 "9"
  10 "10";

 label define whyprg1
   1 "YOUR BIRTH CONTROL METHOD FAILED"
   2 "YOU DID NOT USE YOUR BIRTH CONTROL METHOD PROPERLY"
   3 "RESPONDENT WASN'T USING A METHOD";

 label define whyprg2
   1 "YOUR BIRTH CONTROL METHOD FAILED"
   2 "YOU DID NOT USE YOUR BIRTH CONTROL METHOD PROPERLY"
   3 "RESPONDENT WASN'T USING A METHOD";

 label define whynouse1
   1 "YOU DID NOT EXPECT TO HAVE SEX"
   2 "YOU DID NOT THINK YOU COULD GET PREGNANT"
   3 "YOU DIDN T REALLY MIND IF YOU GOT PREGNANT"
   4 "YOU WERE WORRIED ABOUT THE SIDE EFFECTS OF BIRTH CONTROL"
   5 "YOUR MALE PARTNER DID NOT WANT YOU TO USE A BIRTH CONTROL METHOD"
   6 "YOUR MALE PARTNER DID NOT WANT TO USE A BIRTH CONTROL METHOD"
   7 "RESPONDENT WAS USING A METHOD";

 label define whynouse2
   1 "YOU DID NOT EXPECT TO HAVE SEX"
   2 "YOU DID NOT THINK YOU COULD GET PREGNANT"
   3 "YOU DIDN T REALLY MIND IF YOU GOT PREGNANT"
   4 "YOU WERE WORRIED ABOUT THE SIDE EFFECTS OF BIRTH CONTROL"
   5 "YOUR MALE PARTNER DID NOT WANT YOU TO USE A BIRTH CONTROL METHOD"
   6 "YOUR MALE PARTNER DID NOT WANT TO USE A BIRTH CONTROL METHOD"
   7 "RESPONDENT WAS USING A METHOD";

 label define whynouse3
   1 "YOU DID NOT EXPECT TO HAVE SEX"
   2 "YOU DID NOT THINK YOU COULD GET PREGNANT"
   3 "YOU DIDN T REALLY MIND IF YOU GOT PREGNANT"
   4 "YOU WERE WORRIED ABOUT THE SIDE EFFECTS OF BIRTH CONTROL"
   5 "YOUR MALE PARTNER DID NOT WANT YOU TO USE A BIRTH CONTROL METHOD"
   6 "YOUR MALE PARTNER DID NOT WANT TO USE A BIRTH CONTROL METHOD"
   7 "RESPONDENT WAS USING A METHOD";

 label define anyusint
   1 "YES"
   5 "NO";

 label define outcome
   1 "LIVE BIRTH"
   2 "INDUCED ABORTION"
   3 "STILLBIRTH"
   4 "MISCARRIAGE"
   5 "ECTOPIC PREGNANCY"
   6 "CURRENT PREGNANCY";

 label define birthord
   1 "1ST BIRTH"
   2 "2ND BIRTH"
   3 "3RD BIRTH"
   4 "4TH BIRTH"
   5 "5TH BIRTH"
   6 "6TH BIRTH"
   7 "7TH BIRTH"
   8 "8TH BIRTH"
   9 "9TH BIRTH"
  10 "10TH BIRTH";

 label define fmarout5
   1 "MARRIED"
   2 "DIVORCED"
   3 "WIDOWED"
   4 "SEPARATED"
   5 "NEVER MARRIED";

 label define pmarpreg
   1 "YES";

 label define rmarout6
   1 "MARRIED"
   2 "DIVORCED"
   3 "WIDOWED"
   4 "SEPARATED"
   5 "COHABITING"
   6 "NEVER MARRIED, NOT COHABITING";

 label define fmarcon5
   1 "MARRIED"
   2 "DIVORCED"
   3 "WIDOWED"
   4 "SEPARATED"
   5 "NEVER MARRIED";

 label define pncarewk
  95 "NO PRENATAL CARE FOR THIS PREGNANCY";

 label define paydeliv
   1 "OWN INCOME ONLY"
   2 "INSURANCE ONLY"
   3 "OWN INCOME & INSURANCE ONLY"
   4 "MEDICAID/GOVT ASSISTANCE MENTIONED AT ALL";

 label define lbw1
   1 "YES, LOW BIRTH WEIGHT";

 label define bfeedwks
   0 "LESS THAN 1 WEEK"
 994 "STILL BREASTFEEDING THIS CHILD";

 label define maternlv
   0 "NOT EMPLOYED DURING THIS PREGNANCY"
   1 "TOOK MATERNITY LEAVE FROM JOB HELD DURING THIS PREGNANCY"
   2 "DID NOT TAKE -- NOT NEEDED DUE TO JOB SCHEDULE OR SELF-EMPLOYMENT"
   3 "DID NOT TAKE -- NOT OFFERED OR ALLOWED BY EMPLOYER";

 label define oldwantr
   1 "LATER, OVERDUE"
   2 "RIGHT TIME"
   3 "TOO SOON, MISTIMED"
   4 "DIDN'T CARE, INDIFFERENT"
   5 "UNWANTED"
   6 "DON'T KNOW, NOT SURE";

 label define oldwantp
   1 "LATER, OVERDUE"
   2 "RIGHT TIME"
   3 "TOO SOON, MISTIMED"
   4 "DIDN'T CARE, INDIFFERENT"
   5 "UNWANTED"
   6 "DON'T KNOW, NOT SURE";

 label define wantresp
   1 "LATER, OVERDUE"
   2 "RIGHT TIME"
   3 "TOO SOON, MISTIMED"
   4 "DIDN'T CARE, INDIFFERENT"
   5 "UNWANTED"
   6 "DON'T KNOW, NOT SURE";

 label define wantpart
   1 "LATER, OVERDUE"
   2 "RIGHT TIME"
   3 "TOO SOON, MISTIMED"
   4 "DIDN'T CARE, INDIFFERENT"
   5 "UNWANTED"
   6 "DON'T KNOW, NOT SURE";

 label define ager
  15 "15 YEARS"
  16 "16 YEARS"
  17 "17 YEARS"
  18 "18 YEARS"
  19 "19 YEARS"
  20 "20 YEARS"
  21 "21 YEARS"
  22 "22 YEARS"
  23 "23 YEARS"
  24 "24 YEARS"
  25 "25 YEARS"
  26 "26 YEARS"
  27 "27 YEARS"
  28 "28 YEARS"
  29 "29 YEARS"
  30 "30 YEARS"
  31 "31 YEARS"
  32 "32 YEARS"
  33 "33 YEARS"
  34 "34 YEARS"
  35 "35 YEARS"
  36 "36 YEARS"
  37 "37 YEARS"
  38 "38 YEARS"
  39 "39 YEARS"
  40 "40 YEARS"
  41 "41 YEARS"
  42 "42 YEARS"
  43 "43 YEARS"
  44 "44 YEARS";

 label define agescrn
  15 "15 YEARS"
  16 "16 YEARS"
  17 "17 YEARS"
  18 "18 YEARS"
  19 "19 YEARS"
  20 "20 YEARS"
  21 "21 YEARS"
  22 "22 YEARS"
  23 "23 YEARS"
  24 "24 YEARS"
  25 "25 YEARS"
  26 "26 YEARS"
  27 "27 YEARS"
  28 "28 YEARS"
  29 "29 YEARS"
  30 "30 YEARS"
  31 "31 YEARS"
  32 "32 YEARS"
  33 "33 YEARS"
  34 "34 YEARS"
  35 "35 YEARS"
  36 "36 YEARS"
  37 "37 YEARS"
  38 "38 YEARS"
  39 "39 YEARS"
  40 "40 YEARS"
  41 "41 YEARS"
  42 "42 YEARS"
  43 "43 YEARS"
  44 "44 YEARS";

 label define fmarital
   1 "MARRIED"
   2 "WIDOWED"
   3 "DIVORCED"
   4 "SEPARATED"
   5 "NEVER MARRIED";

 label define rmarital
   1 "CURRENTLY MARRIED"
   2 "NOT MARRIED BUT LIVING WITH OPP SEX PARTNER"
   3 "WIDOWED"
   4 "DIVORCED"
   5 "SEPARATED FOR REASONS OF MARITAL DISCORD"
   6 "NEVER BEEN MARRIED";

 label define educat
   9 "9TH GRADE OR LESS"
  10 "10TH GRADE"
  11 "11TH GRADE"
  12 "12TH GRADE"
  13 "1 YEAR OF COLLEGE/GRAD SCHOOL"
  14 "2 YEARS OF COLLEGE/GRAD SCHOOL"
  15 "3 YEARS OF COLLEGE/GRAD SCHOOL"
  16 "4 YEARS OF COLLEGE/GRAD SCHOOL"
  17 "5 YEARS OF COLLEGE/GRAD SCHOOL"
  18 "6 YEARS OF COLLEGE/GRAD SCHOOL"
  19 "7+ YEARS OF COLLEGE/GRAD SCHOOL";

 label define hieduc
   5 "9TH GRADE OR LESS"
   6 "10TH GRADE"
   7 "11TH GRADE"
   8 "12TH GRADE, NO DIPLOMA (NOR GED)"
   9 "HIGH SCHOOL GRADUATE (DIPLOMA OR GED)"
  10 "SOME COLLEGE BUT NO DEGREE"
  11 "ASSOCIATE DEGREE IN COLLEGE/UNIVERSITY"
  12 "BACHELOR'S DEGREE"
  13 "MASTER'S DEGREE"
  14 "DOCTORATE DEGREE"
  15 "PROFESSIONAL DEGREE";

 label define race
   1 "BLACK"
   2 "WHITE"
   3 "OTHER";

 label define hispanic
   1 "YES"
   2 "NO";

 label define hisprace
   1 "HISPANIC"
   2 "NON-HISPANIC WHITE"
   3 "NON-HISPANIC BLACK"
   4 "NON-HISPANIC OTHER";

 label define rcurpreg
   1 "YES"
   2 "NO";

 label define pregnum
   1 "1 PREGNANCY"
   2 "2 PREGNANCIES"
   3 "3 PREGNANCIES"
   4 "4 PREGNANCIES"
   5 "5 PREGNANCIES"
   6 "6 PREGNANCIES"
   7 "7 PREGNANCIES" 
   8 "8 PREGNANCIES" 
   9 "9 PREGNANCIES" 
   10 "10 PREGNANCIES" 
   11 "11 PREGNANCIES" 
   12 "12 PREGNANCIES" 
   13 "13 PREGNANCIES" 
   14 "14 PREGNANCIES" 
   15 "15 PREGNANCIES" 
   16 "16 PREGNANCIES" 
   17 "17 PREGNANCIES" 
   18 "18 PREGNANCIES" 
   19 "19 PREGNANCIES";

 label define parity
   0 "0 BABIES"
   1 "1 BABY"
   2 "2 BABIES"
   3 "3 BABIES"
   4 "4 BABIES"
   5 "5 BABIES"
   6 "6 BABIES" 
   7 "7 BABIES" 
   8 "8 BABIES" 
   9 "9 BABIES" 
   10 "10 BABIES" 
   11 "11 BABIES" 
   12 "12 BABIES" 
   13 "13 BABIES" 
   14 "14 BABIES" 
   15 "15 BABIES" 
   16 "16 BABIES" 
   17 "17 BABIES" 
   18 "18 BABIES" 
   19 "19 BABIES" 
   20 "20 BABIES" 
   21 "21 BABIES" 
   22 "22 BABIES";

 label define insuranc
   1 "NOT COVERED BY ANY HEALTH INSURANCE"
   2 "COVERED BY A PRIVATE HEALTH INSURANCE PLAN ONLY"
   3 "COVERED BY MEDICAID (MENTIONED AT ALL)"
   4 "COVERED BY PUBLIC/GOVERNMENT/STATE/MILITARY HEALTH CARE (MENTIONED AT ALL)";

 label define pubassis
   1 "YES (R RECEIVED PUBLIC ASSISTANCE IN 2001)"
   2 "NO (R DID NOT RECEIVE PUBLIC ASSISTANCE IN 2001)";

 label define poverty
 500 "500 PERCENT OF POVERTY LEVEL OR GREATER";

 label define laborfor
   1 "WORKING FULL-TIME"
   2 "WORKING PART-TIME"
   3 "WORKING-TEMP ILL/ETC"
   4 "WORKING-MATERNITY OR FAMILY LEAVE"
   5 "NOT WORKING BUT LOOKING FOR WORK"
   6 "SCHOOL"
   7 "KEEPING HOUSE"
   8 "CARING FOR FAMILY"
   9 "OTHER";

 label define religion
   1 "NO RELIGION"
   2 "CATHOLIC"
   3 "PROTESTANT"
   4 "OTHER RELIGIONS";

 label define metro
   1 "MSA, CENTRAL CITY"
   2 "MSA, OTHER"
   3 "NOT MSA";

 label define brnout
   1 "YES"
   5 "NO";

 label define prglngth_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MULTIPLE REGRESSION IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define outcome_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MULTIPLE REGRESSION IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define birthord_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MULTIPLE REGRESSION IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define datend_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MULTIPLE REGRESSION IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define agepreg_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MULTIPLE REGRESSION IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define datecon_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MULTIPLE REGRESSION IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define agecon_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MULTIPLE REGRESSION IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define fmarout5_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MULTIPLE REGRESSION IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define pmarpreg_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MULTIPLE REGRESSION IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define rmarout6_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MULTIPLE REGRESSION IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define fmarcon5_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MULTIPLE REGRESSION IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define learnprg_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MULTIPLE REGRESSION IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define pncarewk_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MULTIPLE REGRESSION IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define paydeliv_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MULTIPLE REGRESSION IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define lbw1_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MULTIPLE REGRESSION IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define bfeedwks_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MULTIPLE REGRESSION IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define maternlv_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MULTIPLE REGRESSION IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define oldwantr_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MULTIPLE REGRESSION IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define oldwantp_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MULTIPLE REGRESSION IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define wantresp_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MULTIPLE REGRESSION IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define wantpart_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MULTIPLE REGRESSION IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define ager_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MULTIPLE REGRESSION IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define fmarital_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MULTIPLE REGRESSION IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define rmarital_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MULTIPLE REGRESSION IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define educat_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MULTIPLE REGRESSION IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define hieduc_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MULTIPLE REGRESSION IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define race_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MULTIPLE REGRESSION IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define hispanic_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MULTIPLE REGRESSION IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define hisprace_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MULTIPLE REGRESSION IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define rcurpreg_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MULTIPLE REGRESSION IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define pregnum_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MULTIPLE REGRESSION IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define parity_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MULTIPLE REGRESSION IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define insuranc_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MULTIPLE REGRESSION IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define pubassis_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MULTIPLE REGRESSION IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define poverty_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MULTIPLE REGRESSION IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define laborfor_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MULTIPLE REGRESSION IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define religion_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MULTIPLE REGRESSION IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define metro_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MULTIPLE REGRESSION IMPUTATION"
   2 "LOGICAL IMPUTATION";

#delimit cr

 label values pregordr pregordr
 label values howpreg_p howpreg_p
 label values moscurrp moscurrp
 label values nowprgdk nowprgdk
 label values pregend1 pregend1
 label values pregend2 pregend2
 label values nbrnaliv nbrnaliv
 label values multbrth multbrth
 label values prgoutcome prgoutcome
 label values flgdkmo1 flgdkmo1
 label values gestasun_m gestasun_m
 label values mosgest mosgest
 label values dk1gest dk1gest
 label values dk2gest dk2gest
 label values dk3gest dk3gest
 label values bpa_bdscheck1 bpa_bdscheck1
 label values bpa_bdscheck2 bpa_bdscheck2
 label values bpa_bdscheck3 bpa_bdscheck3
 label values babysex babysex
 label values birthwgt_lb birthwgt_lb
 label values lobthwgt lobthwgt
 label values babysex2 babysex2
 label values birthwgt_lb2 birthwgt_lb2
 label values lobthwgt2 lobthwgt2
 label values babysex3 babysex3
 label values birthwgt_lb3 birthwgt_lb3
 label values lobthwgt3 lobthwgt3
 label values birthplc birthplc
 label values paybirth1 paybirth1
 label values paybirth2 paybirth2
 label values paybirth3 paybirth3
 label values trimestr trimestr
 label values ltrimest ltrimest
 label values priorsmk priorsmk
 label values postsmks postsmks
 label values npostsmk npostsmk
 label values getprena getprena
 label values pnctrim pnctrim
 label values lpnctri lpnctri
 label values workpreg workpreg
 label values workborn workborn
 label values didwork didwork
 label values weeksdk weeksdk
 label values matchfound matchfound
 label values livehere livehere
 label values alivenow alivenow
 label values wherenow wherenow
 label values legagree legagree
 label values parenend parenend
 label values anynurse anynurse
 label values fedsolid fedsolid
 label values frsteatd_p frsteatd_p
 label values frsteatd frsteatd
 label values quitnurs quitnurs
 label values ageqtnur_p ageqtnur_p
 label values ageqtnur ageqtnur
 label values matchfound2 matchfound2
 label values livehere2 livehere2
 label values alivenow2 alivenow2
 label values wherenow2 wherenow2
 label values legagree2 legagree2
 label values parenend2 parenend2
 label values anynurse2 anynurse2
 label values fedsolid2 fedsolid2
 label values frsteatd_p2 frsteatd_p2
 label values frsteatd2 frsteatd2
 label values quitnurs2 quitnurs2
 label values ageqtnur_p2 ageqtnur_p2
 label values ageqtnur2 ageqtnur2
 label values matchfound3 matchfound3
 label values livehere3 livehere3
 label values alivenow3 alivenow3
 label values wherenow3 wherenow3
 label values legagree3 legagree3
 label values parenend3 parenend3
 label values anynurse3 anynurse3
 label values fedsolid3 fedsolid3
 label values frsteatd_p3 frsteatd_p3
 label values frsteatd3 frsteatd3
 label values quitnurs3 quitnurs3
 label values ageqtnur_p3 ageqtnur_p3
 label values ageqtnur3 ageqtnur3
 label values evuseint evuseint
 label values stopduse stopduse
 label values whystopd whystopd
 label values whatmeth01 whatmeth01
 label values whatmeth02 whatmeth02
 label values whatmeth03 whatmeth03
 label values whatmeth04 whatmeth04
 label values resnouse resnouse
 label values wantbold wantbold
 label values probbabe probbabe
 label values cnfrmno cnfrmno
 label values wantbld2 wantbld2
 label values timingok timingok
 label values toosoon_p toosoon_p
 label values wthpart1 wthpart1
 label values wthpart2 wthpart2
 label values feelinpg feelinpg
 label values hpwnold hpwnold
 label values timokhp timokhp
 label values cohpbeg cohpbeg
 label values cohpend cohpend
 label values tellfath tellfath
 label values whentell whentell
 label values tryscale tryscale
 label values wantscal wantscal
 label values whyprg1 whyprg1
 label values whyprg2 whyprg2
 label values whynouse1 whynouse1
 label values whynouse2 whynouse2
 label values whynouse3 whynouse3
 label values anyusint anyusint
 label values outcome outcome
 label values birthord birthord
 label values fmarout5 fmarout5
 label values pmarpreg pmarpreg
 label values rmarout6 rmarout6
 label values fmarcon5 fmarcon5
 label values pncarewk pncarewk
 label values paydeliv paydeliv
 label values lbw1 lbw1
 label values bfeedwks bfeedwks
 label values maternlv maternlv
 label values oldwantr oldwantr
 label values oldwantp oldwantp
 label values wantresp wantresp
 label values wantpart wantpart
 label values ager ager
 label values agescrn agescrn
 label values fmarital fmarital
 label values rmarital rmarital
 label values educat educat
 label values hieduc hieduc
 label values race race
 label values hispanic hispanic
 label values hisprace hisprace
 label values rcurpreg rcurpreg
 label values pregnum pregnum
 label values parity parity
 label values insuranc insuranc
 label values pubassis pubassis
 label values poverty poverty
 label values laborfor laborfor
 label values religion religion
 label values metro metro
 label values brnout brnout
 label values prglngth_i prglngth_i
 label values outcome_i outcome_i
 label values birthord_i birthord_i
 label values datend_i datend_i
 label values agepreg_i agepreg_i
 label values datecon_i datecon_i
 label values agecon_i agecon_i
 label values fmarout5_i fmarout5_i
 label values pmarpreg_i pmarpreg_i
 label values rmarout6_i rmarout6_i
 label values fmarcon5_i fmarcon5_i
 label values learnprg_i learnprg_i
 label values pncarewk_i pncarewk_i
 label values paydeliv_i paydeliv_i
 label values lbw1_i lbw1_i
 label values bfeedwks_i bfeedwks_i
 label values maternlv_i maternlv_i
 label values oldwantr_i oldwantr_i
 label values oldwantp_i oldwantp_i
 label values wantresp_i wantresp_i
 label values wantpart_i wantpart_i
 label values ager_i ager_i
 label values fmarital_i fmarital_i
 label values rmarital_i rmarital_i
 label values educat_i educat_i
 label values hieduc_i hieduc_i
 label values race_i race_i
 label values hispanic_i hispanic_i
 label values hisprace_i hisprace_i
 label values rcurpreg_i rcurpreg_i
 label values pregnum_i pregnum_i
 label values parity_i parity_i
 label values insuranc_i insuranc_i
 label values pubassis_i pubassis_i
 label values poverty_i poverty_i
 label values laborfor_i laborfor_i
 label values religion_i religion_i
 label values metro_i metro_i


/**************************************************************************
*
* Section 4: Save Outfile
*
* This section saves a Stata system format file. If Section 1 was defined
* properly there should be no reason to modify this section. These macros
* should inflate automatically.
*
***************************************************************************/

save `outfile', replace
