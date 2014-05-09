/**************************************************************************
*
* NATIONAL SURVEY OF FAMILY GROWTH
* 2002 SURVEY - PUBLIC USE MALE RESPONDENT FILE
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
*   Then execute the do file (e.g., do Male.do)          
*                                                                         
***************************************************************************/

/* Allocate 20 megabytes of RAM for Stata SE to read data file into memory.*/
set mem 20m

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

local raw_data ".\Male.dat"
local dict ".\Male.dct"
local outfile ".\Male.dta"


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

label data "NSFG 2002 Public Use Male Respondent Data"

#delimit ;
 label define rscrinf
   1 "YES"
   5 "NO";

 label define rdormres
   1 "YES"
   5 "NO";

 label define rostscrn
   1 "1 HOUSEHOLD MEMBER"
   2 "2 HOUSEHOLD MEMBERS"
   3 "3 HOUSEHOLD MEMBERS"
   4 "4 HOUSEHOLD MEMBERS"
   5 "5 HOUSEHOLD MEMBERS"
   6 "6 HOUSEHOLD MEMBERS"
   7 "7 HOUSEHOLD MEMBERS"
   8 "8 OR MORE HOUSEHOLD MEMBERS";

 label define rscreenhisp
   1 "YES"
   5 "NO";

 label define rscreenrace
   1 "AMERICAN INDIAN OR ALASKA NATIVE"
   2 "ASIAN"
   3 "NATIVE HAWAIIAN OR OTHER PACIFIC ISLANDER"
   4 "BLACK OR AFRICAN AMERICAN"
   5 "WHITE";

 label define age_a
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
  44 "44 YEARS"
  45 "45 YEARS";

 label define age_r
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
  44 "44 YEARS"
  45 "45 YEARS";

 label define marstat
   1 "MARRIED"
   2 "NOT MARRIED BUT LIVING TOGETHER WITH A PARTNER OF THE OPPOSITE SEX"
   3 "WIDOWED"
   4 "DIVORCED"
   5 "SEPARATED, BECAUSE YOU AND YOUR SPOUSE ARE NOT GETTING ALONG"
   6 "NEVER BEEN MARRIED";

 label define fmarstat
   3 "WIDOWED"
   4 "DIVORCED"
   5 "SEPARATED, BECAUSE YOU AND YOUR SPOUSE ARE NOT GETTING ALONG"
   6 "HAVE YOU NEVER BEEN MARRIED";

 label define hisp
   1 "YES"
   5 "NO";

 label define hispgrp
   1 "MEXICAN OR MEXICAN-AMERICAN"
   2 "ANOTHER HISPANIC OR LATINO GROUP";

 label define numrace
   1 "SINGLE RACE REPORTED"
   2 "2 OR MORE RACES REPORTED";

 label define wplocale
   1 "W/P LIVES IN HOUSEHOLD WITH R"
   2 "W/P DOES NOT LIVE IN HOUSEHOLD WITH R";

 label define womrel
   1 "WIFE"
   2 "PARTNER";

 label define fl_rage
   0 "NO"
   1 "YES";

 label define fl_rrace
   0 "NO"
   1 "YES";

 label define fl_rhisp
   0 "NO"
   1 "YES";

 label define goschol
   1 "YES"
   5 "NO";

 label define vaca
   1 "YES"
   5 "NO";

 label define higrade
   9 "9TH GRADE OR LESS"
  10 "10TH GRADE"
  11 "11TH GRADE"
  12 "12TH GRADE"
  13 "1 YEAR OF COLLEGE OR LESS"
  14 "2 YEARS OF COLLEGE"
  15 "3 YEARS OF COLLEGE"
  16 "4 YEARS OF COLLEGE/GRAD SCHOOL"
  17 "5 YEARS OF COLLEGE/GRAD SCHOOL"
  18 "6 YEARS OF COLLEGE/GRAD SCHOOL"
  19 "7 OR MORE YEARS OF COLLEGE AND/OR GRAD SCHOOL"
  99 "DON'T KNOW";

 label define compgrd
   1 "YES"
   5 "NO";

 label define havedip
   1 "YES"
   5 "NO";

 label define dipged
   1 "HIGH SCHOOL DIPLOMA"
   2 "GED"
   3 "BOTH";

 label define havedeg
   1 "YES"
   5 "NO";

 label define degrees
   1 "ASSOCIATE'S DEGREE"
   2 "BACHELOR'S DEGREE"
   3 "MASTER'S DEGREE"
   4 "DOCTORATE DEGREE"
   5 "PROFESSIONAL SCHOOL DEGREE";

 label define wthparnw
   1 "R LIVES WITH BOTH BIOLOGICAL OR ADOPTIVE PARENTS"
   2 "R LIVES WITH OTHER OR NO PARENTAL FIGURES";

 label define onown
   1 "YES"
   5 "NO";

 label define intact
   1 "YES"
   5 "NO";

 label define parmarr
   1 "YES"
   5 "NO";

 label define lvsit14f
   1 "BIOLOGICAL MOTHER"
   2 "OTHER MOTHER-FIGURE"
   3 "NO MOTHER-FIGURE";

 label define lvsit14m
   1 "BIOLOGICAL FATHER"
   2 "STEPFATHER"
   3 "NO FATHER-FIGURE PRESENT"
   4 "OTHER";

 label define womrasdu
   1 "BIOLOGICAL MOTHER"
   2 "OTHER MOTHER-FIGURE"
   3 "NO MOTHER-FIGURE";

 label define momdegre
   1 "LESS THAN HIGH SCHOOL"
   2 "HIGH SCHOOL GRAD OR GED"
   3 "SOME COLLEGE"
   4 "BACHELOR'S DEGREE OR HIGHER";

 label define momworkd
   1 "FULL-TIME"
   2 "PART-TIME"
   3 "EQUAL AMOUNTS FULL-TIME AND PART-TIME"
   4 "NOT AT ALL (FOR PAY)";

 label define momchild
   0 "NO CHILDREN"
   1 "1 CHILD"
   2 "2 CHILDREN"
   3 "3 CHILDREN"
   4 "4 CHILDREN"
   5 "5 CHILDREN"
   6 "6 OR MORE CHILDREN VALUE HIGRADE"
   9 "9TH GRADE OR LESS"
  10 "10TH GRADE"
  11 "11TH GRADE"
  12 "12TH GRADE"
  13 "1 YEAR OF COLLEGE OR LESS"
  14 "2 YEARS OF COLLEGE"
  15 "3 YEARS OF COLLEGE"
  16 "4 YEARS OF COLLEGE/GRAD SCHOOL"
  17 "5 YEARS OF COLLEGE/GRAD SCHOOL"
  18 "6 YEARS OF COLLEGE/GRAD SCHOOL"
  19 "7 OR MORE YEARS OF COLLEGE AND/OR GRAD SCHOOL";

 label define momfstch
   1 "LESS THAN 18 YEARS"
   2 "18-19 YEARS"
   3 "20-24 YEARS"
   4 "25-29 YEARS"
   5 "30 OR OLDER";

 label define mom18
   1 "UNDER 18"
   2 "18-19"
   3 "20-24"
   4 "25 OR OLDER";

 label define manrasdu
   1 "BIOLOGICAL FATHER"
   2 "STEPFATHER"
   3 "NO FATHER-FIGURE PRESENT"
   4 "OTHER";

 label define daddegre
   1 "LESS THAN HIGH SCHOOL"
   2 "HIGH SCHOOL GRAD OR GED"
   3 "SOME COLLEGE"
   4 "BACHELOR'S DEGREE OR HIGHER";

 label define bothbiol
   0 "NO"
   1 "YES";

 label define intact18
   1 "YES"
   5 "NO";

 label define onown18
   1 "YES"
   5 "NO";

 label define timesmar
   1 "1 TIME MARRIED"
   2 "2 TIMES MARRIED"
   3 "3 TIMES MARRIED";

 label define evcohab1
   1 "YES"
   5 "NO";

 label define numcoh1
   1 "1 PARTNER"
   2 "2 PARTNERS"
   3 "3 PARTNERS"
   4 "4 PARTNERS"
   5 "5 PARTNERS";

 label define evcohab2
   1 "YES"
   5 "NO";

 label define numcoh2
   1 "1 PARTNER"
   2 "2 PARTNERS"
   3 "3 PARTNERS"
   4 "4 PARTNERS"
   5 "5 PARTNERS";

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

 label define fmarit
   0 "DK/RF"
   1 "MARRIED"
   2 "WIDOWED"
   3 "DIVORCED"
   4 "SEPARATED"
   5 "NEVER MARRIED";

 label define evrmarry
   0 "NEVER MARRIED"
   1 "EVER MARRIED";

 label define roscnt
   1 "1 HOUSEHOLD MEMBER"
   2 "2 HOUSEHOLD MEMBERS"
   3 "3 HOUSEHOLD MEMBERS"
   4 "4 HOUSEHOLD MEMBERS"
   5 "5 HOUSEHOLD MEMBERS"
   6 "6 HOUSEHOLD MEMBERS"
   7 "7 HOUSEHOLD MEMBERS"
   8 "8 OR MORE HOUSEHOLD MEMBERS";

 label define evrcohab
   0 "NO"
   1 "YES";

 label define numwife
   0 "NEVER MARRIED"
   1 "1 TIME MARRIED"
   2 "2 TIMES MARRIED"
   3 "3 TIMES MARRIED";

 label define numcohab
   0 "NO PARTNERS"
   1 "1 PARTNER"
   2 "2 PARTNERS"
   3 "3 PARTNERS"
   4 "4 PARTNERS"
   5 "5 PARTNERS";

 label define talkpar1
   1 "HOW TO SAY NO TO SEX"
   2 "METHODS OF BIRTH CONTROL"
   3 "WHERE TO GET BIRTH CONTROL"
   4 "SEXUALLY TRANSMITTED DISEASES"
   5 "HOW TO USE A CONDOM"
   6 "NONE OF THE ABOVE";

 label define talkpar2
   1 "HOW TO SAY NO TO SEX"
   2 "METHODS OF BIRTH CONTROL"
   3 "WHERE TO GET BIRTH CONTROL"
   4 "SEXUALLY TRANSMITTED DISEASES"
   5 "HOW TO USE A CONDOM";

 label define talkpar3
   1 "HOW TO SAY NO TO SEX"
   2 "METHODS OF BIRTH CONTROL"
   3 "WHERE TO GET BIRTH CONTROL"
   4 "SEXUALLY TRANSMITTED DISEASES"
   5 "HOW TO USE A CONDOM";

 label define talkpar4
   1 "HOW TO SAY NO TO SEX"
   2 "METHODS OF BIRTH CONTROL"
   3 "WHERE TO GET BIRTH CONTROL"
   4 "SEXUALLY TRANSMITTED DISEASES"
   5 "HOW TO USE A CONDOM";

 label define talkpar5
   1 "HOW TO SAY NO TO SEX"
   2 "METHODS OF BIRTH CONTROL"
   3 "WHERE TO GET BIRTH CONTROL"
   4 "SEXUALLY TRANSMITTED DISEASES"
   5 "HOW TO USE A CONDOM";

 label define sedno
   1 "YES"
   5 "NO";

 label define sednog
   1 "1ST GRADE"
   2 "2ND GRADE"
   3 "3RD GRADE"   
   4 "4TH GRADE" 
   5 "5TH GRADE"
   6 "6TH GRADE"
   7 "7TH GRADE"
   8 "8TH GRADE"
   9 "9TH GRADE"
   10 "10TH GRADE"
   11 "11TH GRADE"
   12 "12TH GRADE"
  96 "NOT IN SCHOOL AT THE TIME OF INSTRUCTION";

 label define sedbc
   1 "YES"
   5 "NO";

 label define sedbcg
   4 "4TH GRADE"
   5 "5TH GRADE"
   6 "6TH GRADE"
   7 "7TH GRADE"
   8 "8TH GRADE"
   9 "9TH GRADE"
   10 "10TH GRADE"
   11 "11TH GRADE"
   12 "12TH GRADE"
  96 "NOT IN SCHOOL AT THE TIME OF INSTRUCTION";

 label define pledge
   1 "YES"
   5 "NO";

 label define everoper
   1 "YES"
   5 "NO";

 label define typeoper
   1 "VASECTOMY"
   2 "OTHER OPERATION"
   3 "VASECTOMY FAILED"
   4 "VASECTOMY ALREADY SURGICALLY REVERSED";

 label define steroper
   1 "YES"
   5 "NO";

 label define plcstrop
   1 "PRIVATE DOCTOR'S OFFICE"
   2 "HMO FACILITY"
   3 "COMMUNITY HEALTH CLINIC, COMMUNITY CLINIC, PUBLIC HEALTH CLINIC"
   4 "FAMILY PLANNING OR PLANNED PARENTHOOD CLINIC"
   5 "EMPLOYER OR COMPANY CLINIC"
   6 "SCHOOL OR SCHOOL-BASED CLINIC"
   7 "HOSPITAL OUTPATIENT CLINIC"
   8 "HOSPITAL EMERGENCY ROOM"
   9 "HOSPITAL REGULAR ROOM"
  10 "URGENT CARE CENTER, URGI-CARE, OR WALK-IN FACILITY"
  20 "SOME OTHER PLACE";

 label define rvrsvas
   1 "YES"
   5 "NO";

 label define rsurgstr
   0 "NO"
   1 "YES";

 label define fathposs
   1 "YES"
   5 "NO";

 label define fathdiff
   1 "YES"
   5 "NO";

 label define rstrstat
   0 "NOT STERILE"
   1 "SURGICALLY STERILE"
   2 "NONSURGICALLY STERILE";

 label define eversex
   1 "YES"
   5 "NO";

 label define rhadsex
   1 "YES"
   2 "NO";

 label define sxmtonce
   1 "YES"
   5 "NO";

 label define ynosex
   1 "AGAINST RELIGION OR MORALS"
   2 "DON T WANT TO GET A FEMALE PREGNANT"
   3 "DON T WANT TO GET A SEXUALLY TRANSMITTED DISEASE"
   4 "HAVEN T FOUND THE RIGHT PERSON YET"
   5 "IN A RELATIONSHIP, BUT WAITING FOR THE RIGHT TIME"
   6 "OTHER";

 label define evrchil
   1 "YES"
   5 "NO";

 label define evrchiln
   1 "1 CHILD"
   2 "2 CHILDREN"
   3 "3 CHILDREN";

 label define father
   0 "NO"
   1 "YES";

 label define lifeprt
   1 "ONE"
   2 "TWO"
   3 "THREE"
   4 "FOUR"
   5 "FIVE"
   6 "SIX"
   7 "SEVEN OR MORE";

 label define lifeprts
   0 "NONE"
   1 "ONE"
   2 "TWO"
   3 "THREE"
   4 "FOUR"
   5 "FIVE"
   6 "SIX"
   7 "SEVEN OR MORE";

 label define sxmon12
   1 "YES"
   5 "NO";

 label define mon12prt
   0 "NONE"
   1 "ONE"
   2 "TWO"
   3 "THREE"
   4 "FOUR"
   5 "FIVE"
   6 "SIX"
   7 "SEVEN OR MORE";

 label define mon12prts
   0 "NONE"
   1 "ONE"
   2 "TWO"
   3 "THREE"
   4 "FOUR"
   5 "FIVE"
   6 "SIX"
   7 "SEVEN OR MORE";

 label define sexstat
   0 "NEVER HAD SEX"
   1 "1 PARTNER EVER/SEX IN LAST 12 MOS/SEX ONLY ONCE"
   2 "1 PARTNER EVER/SEX IN LAST 12 MOS/SEX > ONCE"
   3 "1 PARTNER EVER/NO SEX IN LAST 12 MOS/SEX ONLY ONCE"
   4 "1 PARTNER EVER/NO SEX IN LAST 12 MOS/SEX > ONCE"
   5 ">1 PARTNER EVER/NO SEX IN LAST 12 MOS"
   6 ">1 PARTNER EVER/SEX IN LAST 12 MOS";

 label define biokids
   0 "NONE"
   1 "1 CHILD"
   2 "2 CHILDREN"
   3 "3 CHILDREN";

 label define adopkids
   0 "NONE";

 label define currpreg
   0 "INAPP/DK/RF"
   1 "YES";

 label define currprts
   0 "INAPP/DK/RF"
   1 "1 PARTNER"
   2 "2 PARTNERS"
   3 "3 PARTNERS";

 label define pregsnow
   0 "INAPP/DK/RF";

 label define sexfreq
   0 "NONE"
   1 "1"
   2 "2"
   3 "3"
   4 "4"
   5 "5";

 label define confreq
   0 "NONE"
   1 "1"
   2 "2"
   3 "3"
   4 "4"
   5 "5";

 label define p1rltn1
   1 "YES"
   5 "NO";

 label define p1currwife
   1 "YES"
   5 "NO";

 label define p1currsep
   1 "YES"
   5 "NO";

 label define p1rltn2
   1 "YES"
   5 "NO";

 label define p1cohabit
   1 "YES"
   5 "NO";

 label define p2rltn1
   1 "YES"
   5 "NO";

 label define p2currwife
   1 "YES"
   5 "NO";

 label define p2currsep
   1 "YES"
   5 "NO";

 label define p2rltn2
   1 "YES"
   5 "NO";

 label define p2cohabit
   1 "YES"
   5 "NO";

 label define p3rltn1
   1 "YES"
   5 "NO";

 label define p3currwife
   1 "YES"
   5 "NO";

 label define p3currsep
   1 "YES"
   5 "NO";

 label define p3rltn2
   1 "YES"
   5 "NO";

 label define p3cohabit
   1 "YES"
   5 "NO";

 label define p1relation
   0 "INAPPLICABLE/NOT ASCERTAINED"
   1 "EVER MARRIED TO HER"
   2 "EVER COHABITED WITH HER"
   3 "NEVER MARRIED NOR COHABITED WITH HER";

 label define p2relation
   0 "INAPPLICABLE/NOT ASCERTAINED"
   1 "EVER MARRIED TO HER"
   2 "EVER COHABITED WITH HER"
   3 "NEVER MARRIED NOR COHABITED WITH HER";

 label define p3relation
   0 "INAPPLICABLE/NOT ASCERTAINED"
   1 "EVER MARRIED TO HER"
   2 "EVER COHABITED WITH HER"
   3 "NEVER MARRIED NOR COHABITED WITH HER";

 label define first
   1 "YES"
   5 "NO";

 label define livtogwf
   1 "YES"
   5 "NO";

 label define engathen
   1 "YES"
   5 "NO";

 label define willmarr
   1 "NO CHANCE"
   2 "A LITTLE CHANCE"
   3 "50-50 CHANCE"
   4 "A PRETTY GOOD CHANCE"
   5 "AN ALMOST CERTAIN CHANCE";

 label define cwphisp
   1 "YES"
   5 "NO";

 label define cwprace1
   1 "AMERICAN INDIAN OR ALASKA NATIVE"
   2 "ASIAN"
   3 "NATIVE HAWAIIAN OR OTHER PACIFIC ISLANDER"
   4 "BLACK OR AFRICAN AMERICAN"
   5 "WHITE";

 label define cwprace2
   1 "AMERICAN INDIAN OR ALASKA NATIVE"
   2 "ASIAN"
   3 "NATIVE HAWAIIAN OR OTHER PACIFIC ISLANDER"
   4 "BLACK OR AFRICAN AMERICAN"
   5 "WHITE";

 label define cwprace3
   1 "AMERICAN INDIAN OR ALASKA NATIVE"
   2 "ASIAN"
   3 "NATIVE HAWAIIAN OR OTHER PACIFIC ISLANDER"
   4 "BLACK OR AFRICAN AMERICAN"
   5 "WHITE";

 label define cwpraceb
   1 "AMERICAN INDIAN OR ALASKA NATIVE"
   2 "ASIAN"
   3 "NATIVE HAWAIIAN OR OTHER PACIFIC ISLANDER"
   4 "BLACK OR AFRICAN AMERICAN"
   5 "WHITE";

 label define cwpeducn
   1 "LESS THAN HIGH SCHOOL"
   2 "HIGH SCHOOL GRADUATE OR GED"
   3 "SOME COLLEGE BUT NO DEGREE"
   4 "2-YEAR COLLEGE DEGREE (E G , ASSOCIATES DEGREE)"
   5 "4-YEAR COLLEGE GRADUATE (E G , BA, BS)"
   6 "GRADUATE OR PROFESSIONAL SCHOOL";

 label define cwpborn
   1 "YES"
   5 "NO";

 label define cwpmarbf
   1 "YES"
   5 "NO";

 label define cwpsx1rl
   1 "MARRIED TO HER"
   2 "ENGAGED TO HER"
   3 "LIVING TOGETHER IN A SEXUAL RELATIONSHIP, BUT NOT ENGAGED"
   4 "GOING WITH HER OR GOING STEADY"
   5 "GOING OUT WITH HER ONCE IN A WHILE"
   6 "JUST FRIENDS"
   7 "HAD JUST MET HER"
   8 "SOMETHING ELSE";

 label define cwpfuse
   1 "YES"
   5 "NO";

 label define cwpfmet01
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define cwpfmet02
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define cwpfmet03
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define cwpfmet04
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define cwpopstr
   1 "YES"
   5 "NO";

 label define cwptypop1
   1 "TUBAL LIGATION OR TUBAL STERILIZATION"
   2 "HYSTERECTOMY"
   3 "SOMETHING ELSE";

 label define cwptypop2
   1 "TUBAL LIGATION OR TUBAL STERILIZATION"
   2 "HYSTERECTOMY"
   3 "SOMETHING ELSE";

 label define cwptotst
   1 "YES"
   5 "NO";

 label define cwprevst
   1 "YES"
   5 "NO";

 label define psurgstr
   0 "NO"
   1 "YES";

 label define cwpposs
   1 "YES"
   5 "NO";

 label define cwpdiff
   1 "YES"
   5 "NO";

 label define pstrstat
   0 "NOT STERILE"
   1 "SURGICALLY STERILE"
   2 "NONSURGICALLY STERILE";

 label define cwplstsx
   1 "WITHIN THE LAST WEEK"
   2 "WITHIN THE LAST FOUR WEEKS"
   3 "MORE THAN FOUR WEEKS AGO";

 label define cwpluse
   1 "YES"
   5 "NO";

 label define cwplmet01
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define cwplmet02
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define cwplmet03
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define cwplmet04
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define cwpluse1
   1 "YES"
   5 "NO";

 label define cwplmet11
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
  10 "SOMETHING ELSE";

 label define cwplmet12
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
  10 "SOMETHING ELSE";

 label define cwplmet13
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
  10 "SOMETHING ELSE";

 label define cwplmet14
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
  10 "SOMETHING ELSE";

 label define cwpluse2
   1 "YES"
   5 "NO";

 label define cwplmet21
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define cwplmet22
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define cwplmet23
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define cwplmet24
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define cwprecbc
   1 "YES"
   5 "NO";

 label define cwpallbc01
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define cwpallbc02
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define cwpallbc03
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define cwpallbc04
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define cwpallbc05
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define cwpallbc06
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define cwplsxuse
   0 "NONE OR NO METHOD IDENTIFIED"
   1 "ANY METHOD IDENTIFIED";

 label define cwpbcmst
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define cwpnofrq
   1 "EVERY TIME"
   2 "MOST OF THE TIME"
   3 "ABOUT HALF OF THE TIME"
   4 "SOME OF THE TIME"
   5 "NONE OF THE TIME";

 label define cwpbiokd
   1 "YES"
   5 "NO";

 label define partfath
   0 "NO"
   1 "YES";

 label define bkidagegp21
   0 "NOT ASCERTAINED"
   1 "UNDER 5 YEARS"
   2 "5-18 YEARS"
   3 "19 OR OLDER";

 label define bkidhh21
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define bkidmar21
   0 "NO"
   1 "YES";

 label define cwpchsex
   1 "MALE"
   2 "FEMALE";

 label define cwpchmar
   1 "YES"
   5 "NO";

 label define cwpchres
   1 "YES"
   5 "NO";

 label define cwpchlrn
   1 "DURING THE PREGNANCY"
   2 "AFTER THE CHILD WAS BORN";

 label define cwpchliv1
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "AWAY AT SCHOOL OR COLLEGE"
   4 "LIVING ON OWN"
   5 "LIVING WITH OTHER RELATIVES"
   6 "DECEASED"
   7 "PLACED FOR ADOPTION OR ADOPTED"
   8 "PLACED IN FOSTER CARE"
   9 "SOMEPLACE ELSE";

 label define cwpchliv2
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "AWAY AT SCHOOL OR COLLEGE"
   4 "LIVING ON OWN"
   5 "LIVING WITH OTHER RELATIVES"
   6 "DECEASED"
   7 "PLACED FOR ADOPTION OR ADOPTED"
   8 "PLACED IN FOSTER CARE"
   9 "SOMEPLACE ELSE";

 label define cwpchage
   1 "LESS THAN 5 YEARS OLD"
   2 "5-18 YEARS OLD"
   3 "19 YEARS OR OLDER";

 label define cwpchleg
   1 "YES"
   5 "NO";

 label define cwpchhop
   1 "YES"
   5 "NO";

 label define cwpchevr
   1 "YES"
   5 "NO";

 label define cwpchwnt
   1 "DEFINITELY YES"
   2 "PROBABLY YES"
   3 "PROBABLY NO"
   4 "DEFINITELY NO";

 label define cwpchson
   1 "TOO SOON"
   2 "RIGHT TIME"
   3 "LATER"
   4 "DIDN'T CARE";

 label define bkidagegp22
   0 "NOT ASCERTAINED"
   1 "UNDER 5 YEARS"
   2 "5-18 YEARS"
   3 "19 OR OLDER";

 label define bkidhh22
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define bkidmar22
   0 "NO"
   1 "YES";

 label define cwpchsex2
   1 "MALE"
   2 "FEMALE";

 label define multbirt2
   1 "YES"
   5 "NO";

 label define cwpchmar2
   1 "YES"
   5 "NO";

 label define cwpchres2
   1 "YES"
   5 "NO";

 label define cwpchlrn2
   1 "DURING THE PREGNANCY"
   2 "AFTER THE CHILD WAS BORN";

 label define cwpchliv10
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "AWAY AT SCHOOL OR COLLEGE"
   4 "LIVING ON OWN"
   5 "LIVING WITH OTHER RELATIVES"
   6 "DECEASED"
   7 "PLACED FOR ADOPTION OR ADOPTED"
   8 "PLACED IN FOSTER CARE"
   9 "SOMEPLACE ELSE";

 label define cwpchliv11
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "AWAY AT SCHOOL OR COLLEGE"
   4 "LIVING ON OWN"
   5 "LIVING WITH OTHER RELATIVES"
   6 "DECEASED"
   7 "PLACED FOR ADOPTION OR ADOPTED"
   8 "PLACED IN FOSTER CARE"
   9 "SOMEPLACE ELSE";

 label define cwpchage2
   1 "LESS THAN 5 YEARS OLD"
   2 "5-18 YEARS OLD"
   3 "19 YEARS OR OLDER";

 label define cwpchleg2
   1 "YES"
   5 "NO";

 label define cwpchhop2
   1 "YES"
   5 "NO";

 label define cwpchevr2
   1 "YES"
   5 "NO";

 label define cwpchwnt2
   1 "DEFINITELY YES"
   2 "PROBABLY YES"
   3 "PROBABLY NO"
   4 "DEFINITELY NO";

 label define cwpchson2
   1 "TOO SOON"
   2 "RIGHT TIME"
   3 "LATER"
   4 "DIDN'T CARE";

 label define bkidagegp23
   0 "NOT ASCERTAINED"
   1 "UNDER 5 YEARS"
   2 "5-18 YEARS"
   3 "19 OR OLDER";

 label define bkidhh23
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define bkidmar23
   0 "NO"
   1 "YES";

 label define cwpchsex3
   1 "MALE"
   2 "FEMALE";

 label define multbirt3
   1 "YES"
   5 "NO";

 label define cwpchmar3
   1 "YES"
   5 "NO";

 label define cwpchres3
   1 "YES"
   5 "NO";

 label define cwpchlrn3
   1 "DURING THE PREGNANCY"
   2 "AFTER THE CHILD WAS BORN";

 label define cwpchliv19
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "AWAY AT SCHOOL OR COLLEGE"
   4 "LIVING ON OWN"
   5 "LIVING WITH OTHER RELATIVES"
   6 "DECEASED"
   7 "PLACED FOR ADOPTION OR ADOPTED"
   8 "PLACED IN FOSTER CARE"
   9 "SOMEPLACE ELSE";

 label define cwpchage3
   1 "LESS THAN 5 YEARS OLD"
   2 "5-18 YEARS OLD"
   3 "19 YEARS OR OLDER";

 label define cwpchleg3
   1 "YES"
   5 "NO";

 label define cwpchhop3
   1 "YES"
   5 "NO";

 label define cwpchevr3
   1 "YES"
   5 "NO";

 label define cwpchwnt3
   1 "DEFINITELY YES"
   2 "PROBABLY YES"
   3 "PROBABLY NO"
   4 "DEFINITELY NO";

 label define cwpchson3
   1 "TOO SOON"
   2 "RIGHT TIME"
   3 "LATER"
   4 "DIDN'T CARE";

 label define bkidagegp24
   0 "NOT ASCERTAINED"
   1 "UNDER 5 YEARS"
   2 "5-18 YEARS"
   3 "19 OR OLDER";

 label define bkidhh24
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define bkidmar24
   0 "NO"
   1 "YES";

 label define cwpchsex4
   1 "MALE"
   2 "FEMALE";

 label define multbirt4
   1 "YES"
   5 "NO";

 label define cwpchres4
   1 "YES"
   5 "NO";

 label define cwpchlrn4
   1 "DURING THE PREGNANCY"
   2 "AFTER THE CHILD WAS BORN";

 label define cwpchliv28
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "AWAY AT SCHOOL OR COLLEGE"
   4 "LIVING ON OWN"
   5 "LIVING WITH OTHER RELATIVES"
   6 "DECEASED"
   7 "PLACED FOR ADOPTION OR ADOPTED"
   8 "PLACED IN FOSTER CARE"
   9 "SOMEPLACE ELSE";

 label define cwpchleg4
   1 "YES"
   5 "NO";

 label define cwpchhop4
   1 "YES"
   5 "NO";

 label define cwpchevr4
   1 "YES"
   5 "NO";

 label define cwpchwnt4
   1 "DEFINITELY YES"
   2 "PROBABLY YES"
   3 "PROBABLY NO"
   4 "DEFINITELY NO";

 label define cwpchson4
   1 "TOO SOON"
   2 "RIGHT TIME"
   3 "LATER"
   4 "DIDN'T CARE";

 label define bkidagegp25
   1 "UNDER 5 YEARS"
   2 "5-18 YEARS"
   3 "19 OR OLDER";

 label define bkidhh25
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define bkidmar25
   0 "NO"
   1 "YES";

 label define cwpchsex5
   1 "MALE"
   2 "FEMALE";

 label define multbirt5
   1 "YES"
   5 "NO";

 label define cwpchres5
   1 "YES"
   5 "NO";

 label define cwpchlrn5
   1 "DURING THE PREGNANCY"
   2 "AFTER THE CHILD WAS BORN";

 label define cwpchliv37
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "AWAY AT SCHOOL OR COLLEGE"
   4 "LIVING ON OWN"
   5 "LIVING WITH OTHER RELATIVES"
   6 "DECEASED"
   7 "PLACED FOR ADOPTION OR ADOPTED"
   8 "PLACED IN FOSTER CARE"
   9 "SOMEPLACE ELSE";

 label define cwpchleg5
   1 "YES"
   5 "NO";

 label define cwpchhop5
   1 "YES"
   5 "NO";

 label define cwpchevr5
   1 "YES"
   5 "NO";

 label define cwpchwnt5
   1 "DEFINITELY YES"
   2 "PROBABLY YES"
   3 "PROBABLY NO"
   4 "DEFINITELY NO";

 label define cwpchson5
   1 "TOO SOON"
   2 "RIGHT TIME"
   3 "LATER"
   4 "DIDN'T CARE";

 label define bkidagegp26
   1 "UNDER 5 YEARS"
   2 "5-18 YEARS"
   3 "19 OR OLDER";

 label define bkidhh26
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define bkidmar26
   0 "NO"
   1 "YES";

 label define cwpchsex6
   1 "MALE"
   2 "FEMALE";

 label define multbirt6
   1 "YES"
   5 "NO";

 label define cwpchres6
   1 "YES"
   5 "NO";

 label define cwpchliv46
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "AWAY AT SCHOOL OR COLLEGE"
   4 "LIVING ON OWN"
   5 "LIVING WITH OTHER RELATIVES"
   6 "DECEASED"
   7 "PLACED FOR ADOPTION OR ADOPTED"
   8 "PLACED IN FOSTER CARE"
   9 "SOMEPLACE ELSE";

 label define bkidagegp27
   1 "UNDER 5 YEARS"
   2 "5-18 YEARS"
   3 "19 OR OLDER";

 label define bkidhh27
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define bkidmar27
   0 "NO"
   1 "YES";

 label define cwpchsex7
   1 "MALE"
   2 "FEMALE";

 label define multbirt7
   1 "YES"
   5 "NO";

 label define cwpchliv55
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "AWAY AT SCHOOL OR COLLEGE"
   4 "LIVING ON OWN"
   5 "LIVING WITH OTHER RELATIVES"
   6 "DECEASED"
   7 "PLACED FOR ADOPTION OR ADOPTED"
   8 "PLACED IN FOSTER CARE"
   9 "SOMEPLACE ELSE";

 label define cwpprgnw
   1 "YES"
   5 "NO";

 label define cwptrypg
   1 "YES"
   5 "NO";

 label define cwpcpwnt
   1 "DEFINITELY YES"
   2 "PROBABLY YES"
   3 "PROBABLY NO"
   4 "DEFINITELY NO";

 label define cwpcpson
   1 "TOO SOON"
   2 "RIGHT TIME"
   3 "LATER"
   4 "DIDN'T CARE";

 label define cwpotkid
   1 "YES"
   5 "NO";

 label define cwpokad
   1 "YES"
   5 "NO";

 label define akidagegp21
   1 "UNDER 5 YEARS"
   2 "5-18 YEARS"
   3 "19 OR OLDER";

 label define akidhh21
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define cwpoksex
   1 "MALE"
   2 "FEMALE";

 label define cwpokliv1
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "AWAY AT SCHOOL OR COLLEGE"
   4 "LIVING ON OWN"
   5 "LIVING WITH OTHER RELATIVES"
   6 "DECEASED"
   7 "SOMEPLACE ELSE";

 label define akidagegp22
   1 "UNDER 5 YEARS"
   2 "5-18 YEARS"
   3 "19 OR OLDER";

 label define akidhh22
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define cwpoksex2
   1 "MALE"
   2 "FEMALE";

 label define cwpokliv8
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "AWAY AT SCHOOL OR COLLEGE"
   4 "LIVING ON OWN"
   5 "LIVING WITH OTHER RELATIVES"
   6 "DECEASED"
   7 "SOMEPLACE ELSE";

 label define akidagegp23
   1 "UNDER 5 YEARS"
   2 "5-18 YEARS"
   3 "19 OR OLDER";

 label define akidhh23
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define cwpoksex3
   1 "MALE"
   2 "FEMALE";

 label define cwpokliv15
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "AWAY AT SCHOOL OR COLLEGE"
   4 "LIVING ON OWN"
   5 "LIVING WITH OTHER RELATIVES"
   6 "DECEASED"
   7 "SOMEPLACE ELSE";

 label define cwpnbevr
   1 "YES"
   5 "NO";

 label define cwpnbrel
   1 "YES"
   5 "NO";

 label define cwpnbfos
   1 "YES"
   5 "NO";

 label define cwpnbad
   1 "YES"
   5 "NO";

 label define akidhh31
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define cwpnbsex
   1 "MALE"
   2 "FEMALE";

 label define cwpnbliv1
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "AWAY AT SCHOOL OR COLLEGE"
   4 "LIVING ON OWN"
   5 "LIVING WITH OTHER RELATIVES"
   6 "DECEASED"
   7 "SOMEPLACE ELSE";

 label define akidagegp31
   1 "UNDER 5 YEARS"
   2 "5-18 YEARS"
   3 "19 OR OLDER";

 label define akidhh32
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define cwpnbsex2
   1 "MALE"
   2 "FEMALE";

 label define cwpnbliv8
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "AWAY AT SCHOOL OR COLLEGE"
   4 "LIVING ON OWN"
   5 "LIVING WITH OTHER RELATIVES"
   6 "DECEASED"
   7 "SOMEPLACE ELSE";

 label define akidagegp32
   1 "UNDER 5 YEARS"
   2 "5-18 YEARS"
   3 "19 OR OLDER";

 label define c_nbakids
   0 "NONE";

 label define thiswom
   1 "YES"
   5 "NO";

 label define pxrelat
   1 "YES"
   5 "NO";

 label define pxrelat2
   1 "YES, MARRIED TO"
   2 "YES, LIVED TOGETHER WITH"
   5 "NO";

 label define livtogn
   1 "YES"
   5 "NO";

 label define engagthn
   1 "YES"
   5 "NO";

 label define marrend
   1 "DEATH OF WIFE"
   2 "DIVORCE"
   3 "ANNULMENT"
   4 "SEPARATION";

 label define pxcurr
   1 "YES"
   5 "NO";

 label define p1currprt
   0 "NO"
   1 "YES";

 label define pxmarry
   1 "NO CHANCE"
   2 "A LITTLE CHANCE"
   3 "50-50 CHANCE"
   4 "A PRETTY GOOD CHANCE"
   5 "AN ALMOST CERTAIN CHANCE";

 label define pxlast
   1 "WITHIN THE LAST WEEK"
   2 "WITHIN THE LAST FOUR WEEKS"
   3 "MORE THAN FOUR WEEKS AGO";

 label define pxluse
   1 "YES"
   5 "NO";

 label define pxlmeth01
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define pxlmeth02
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define pxlmeth03
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define pxlmeth04
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define pxlruse
   1 "YES"
   5 "NO";

 label define pxlrmeth1
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
  10 "SOMETHING ELSE";

 label define pxlrmeth2
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
  10 "SOMETHING ELSE";

 label define pxlrmeth3
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
  10 "SOMETHING ELSE";

 label define pxlrmeth4
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
  10 "SOMETHING ELSE";

 label define pxlpuse
   1 "YES"
   5 "NO";

 label define pxlpmeth1
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define pxlpmeth2
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define pxlpmeth3
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define pxlpmeth4
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define lsxusep
   0 "NONE OR NO METHOD IDENTIFIED"
   1 "ANY METHOD IDENTIFIED";

 label define pxlsxprb
   1 "YES"
   5 "NO";

 label define pxmtonce
   1 "YES"
   5 "NO";

 label define mtoncep
   0 "NOT ASCERTAINED?"
   1 "YES (MORE THAN ONCE)"
   2 "NO (ONCE)";

 label define pxrelage
   1 "OLDER"
   2 "YOUNGER"
   3 "SAME AGE";

 label define pxrelyrs
   1 "1-2 YEARS"
   2 "3-5 YEARS"
   3 "6-10 YEARS"
   4 "MORE THAN 10 YEARS";

 label define pxfrltn1
   1 "MARRIED TO HER"
   2 "ENGAGED TO HER"
   3 "LIVING TOGETHER IN A SEXUAL RELATIONSHIP, BUT NOT ENGAGED"
   4 "GOING WITH HER OR GOING STEADY"
   5 "GOING OUT WITH HER ONCE IN A WHILE"
   6 "JUST FRIENDS"
   7 "HAD JUST MET HER"
   8 "SOMETHING ELSE";

 label define pxhisp
   1 "YES"
   5 "NO";

 label define pxrace1
   1 "AMERICAN INDIAN OR ALASKA NATIVE"
   2 "ASIAN"
   3 "NATIVE HAWAIIAN OR OTHER PACIFIC ISLANDER"
   4 "BLACK OR AFRICAN AMERICAN"
   5 "WHITE";

 label define pxrace2
   1 "AMERICAN INDIAN OR ALASKA NATIVE"
   2 "ASIAN"
   3 "NATIVE HAWAIIAN OR OTHER PACIFIC ISLANDER"
   4 "BLACK OR AFRICAN AMERICAN"
   5 "WHITE";

 label define pxrace3
   1 "AMERICAN INDIAN OR ALASKA NATIVE"
   2 "ASIAN"
   3 "NATIVE HAWAIIAN OR OTHER PACIFIC ISLANDER"
   4 "BLACK OR AFRICAN AMERICAN"
   5 "WHITE";

 label define pxbest
   1 "AMERICAN INDIAN OR ALASKA NATIVE"
   2 "ASIAN"
   3 "NATIVE HAWAIIAN OR OTHER PACIFIC ISLANDER"
   4 "BLACK OR AFRICAN AMERICAN"
   5 "WHITE";

 label define pxdob_m
   1 "JANUARY"
   2 "FEBRUARY"
   3 "MARCH"
   4 "APRIL"
   5 "MAY"
   6 "JUNE"
   7 "JULY"
   8 "AUGUST"
   9 "SEPTEMBER"
  10 "OCTOBER"
  11 "NOVEMBER"
  12 "DECEMBER"
  13 "WINTER"
  14 "SPRING"
  15 "SUMMER"
  16 "FALL";

 label define pxeduc
   1 "LESS THAN HIGH SCHOOL"
   2 "HIGH SCHOOL GRADUATE OR GED"
   3 "SOME COLLEGE BUT NO DEGREE"
   4 "2-YEAR COLLEGE DEGREE (E G , ASSOCIATES DEGREE)"
   5 "4-YEAR COLLEGE GRADUATE (E G , BA, BS)"
   6 "GRADUATE OR PROFESSIONAL SCHOOL";

 label define pxmarbf
   1 "YES"
   5 "NO";

 label define pxanych
   1 "YES"
   5 "NO";

 label define pxanychn
   1 "1 CHILD"
   2 "2 CHILDREN";

 label define pxablech
   1 "YES"
   5 "NO";

 label define pxfrltn2
   1 "MARRIED TO HER"
   2 "ENGAGED TO HER"
   3 "LIVING TOGETHER IN A SEXUAL RELATIONSHIP, BUT NOT ENGAGED"
   4 "GOING WITH HER OR GOING STEADY"
   5 "GOING OUT WITH HER ONCE IN A WHILE"
   6 "JUST FRIENDS"
   7 "HAD JUST MET HER"
   8 "SOMETHING ELSE";

 label define pxfuse
   1 "YES"
   5 "NO";

 label define pxfmeth01
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define pxfmeth02
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define pxfmeth03
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define pxfmeth04
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define pxfmeth05
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define pxanyuse
   1 "YES"
   5 "NO";

 label define pxmethod01
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define pxmethod02
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define pxmethod03
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define pxmethod04
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define pxmethod05
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define pxmethod06
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define pxmstuse
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define pxnofreq
   1 "EVERY TIME"
   2 "MOST OF THE TIME"
   3 "ABOUT HALF OF THE TIME"
   4 "SOME OF THE TIME"
   5 "NONE OF THE TIME";

 label define pxchild
   1 "YES"
   5 "NO";

 label define pxcxsex
   1 "MALE"
   2 "FEMALE";

 label define kidmar
   0 "NO"
   1 "YES";

 label define kidagegp
   1 "UNDER 5 YEARS"
   2 "5-18 YEARS"
   3 "19 OR OLDER";

 label define kidliv
   0 "NO"
   1 "YES";

 label define kidhh
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define pxcxmarb
   1 "YES"
   5 "NO";

 label define pxcxres
   1 "YES"
   5 "NO";

 label define pxcxknow
   1 "DURING THE PREGNANCY"
   2 "AFTER THE CHILD WAS BORN";

 label define pxcxliv01
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "WITH HIS/HER MOTHER"
   4 "AWAY AT SCHOOL OR COLLEGE"
   5 "LIVING ON OWN"
   6 "LIVING WITH OTHER RELATIVES"
   7 "DECEASED"
   8 "PLACED FOR ADOPTION OR ADOPTED"
   9 "PLACED IN FOSTER CARE"
  10 "SOMEPLACE ELSE";

 label define pxcxliv02
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "WITH HIS/HER MOTHER"
   4 "AWAY AT SCHOOL OR COLLEGE"
   5 "LIVING ON OWN"
   6 "LIVING WITH OTHER RELATIVES"
   7 "DECEASED"
   8 "PLACED FOR ADOPTION OR ADOPTED"
   9 "PLACED IN FOSTER CARE"
  10 "SOMEPLACE ELSE";

 label define pxcxage
   1 "LESS THAN 5 YEARS OLD"
   2 "5-18 YEARS OLD"
   3 "19 YEARS OR OLDER";

 label define pxcxlaw
   1 "YES"
   5 "NO";

 label define pxcxhop
   1 "YES"
   5 "NO";

 label define pxcxever
   1 "YES"
   5 "NO";

 label define pxwant
   1 "DEFINITELY YES"
   2 "PROBABLY YES"
   3 "PROBABLY NO"
   4 "DEFINITELY NO";

 label define pxsoon
   1 "TOO SOON"
   2 "RIGHT TIME"
   3 "LATER"
   4 "DIDN'T CARE";

 label define pxcxsex2
   1 "MALE"
   2 "FEMALE";

 label define kidmar2
   0 "NO"
   1 "YES";

 label define kidagegp2
   1 "UNDER 5 YEARS"
   2 "5-18 YEARS"
   3 "19 OR OLDER";

 label define kidliv2
   0 "NO"
   1 "YES";

 label define kidhh2
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define multbirt12
   1 "YES"
   5 "NO";

 label define pxcxres2
   1 "YES"
   5 "NO";

 label define pxcxknow2
   1 "DURING THE PREGNANCY"
   2 "AFTER THE CHILD WAS BORN";

 label define pxcxliv11
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "WITH HIS/HER MOTHER"
   4 "AWAY AT SCHOOL OR COLLEGE"
   5 "LIVING ON OWN"
   6 "LIVING WITH OTHER RELATIVES"
   7 "DECEASED"
   8 "PLACED FOR ADOPTION OR ADOPTED"
   9 "PLACED IN FOSTER CARE"
  10 "SOMEPLACE ELSE";

 label define pxcxliv12
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "WITH HIS/HER MOTHER"
   4 "AWAY AT SCHOOL OR COLLEGE"
   5 "LIVING ON OWN"
   6 "LIVING WITH OTHER RELATIVES"
   7 "DECEASED"
   8 "PLACED FOR ADOPTION OR ADOPTED"
   9 "PLACED IN FOSTER CARE"
  10 "SOMEPLACE ELSE";

 label define pxcxlaw2
   1 "YES"
   5 "NO";

 label define pxcxhop2
   1 "YES"
   5 "NO";

 label define pxcxever2
   1 "YES"
   5 "NO";

 label define pxwant2
   1 "DEFINITELY YES"
   2 "PROBABLY YES"
   3 "PROBABLY NO"
   4 "DEFINITELY NO";

 label define pxsoon2
   1 "TOO SOON"
   2 "RIGHT TIME"
   3 "LATER"
   4 "DIDN'T CARE";

 label define pxcxsex3
   1 "MALE"
   2 "FEMALE";

 label define kidmar3
   0 "NO"
   1 "YES";

 label define kidagegp3
   1 "UNDER 5 YEARS"
   2 "5-18 YEARS"
   3 "19 OR OLDER";

 label define kidliv3
   0 "NO"
   1 "YES";

 label define kidhh3
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define multbirt13
   1 "YES"
   5 "NO";

 label define pxcxres3
   1 "YES"
   5 "NO";

 label define pxcxknow3
   1 "DURING THE PREGNANCY"
   2 "AFTER THE CHILD WAS BORN";

 label define pxcxliv21
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "WITH HIS/HER MOTHER"
   4 "AWAY AT SCHOOL OR COLLEGE"
   5 "LIVING ON OWN"
   6 "LIVING WITH OTHER RELATIVES"
   7 "DECEASED"
   8 "PLACED FOR ADOPTION OR ADOPTED"
   9 "PLACED IN FOSTER CARE"
  10 "SOMEPLACE ELSE";

 label define pxcxliv22
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "WITH HIS/HER MOTHER"
   4 "AWAY AT SCHOOL OR COLLEGE"
   5 "LIVING ON OWN"
   6 "LIVING WITH OTHER RELATIVES"
   7 "DECEASED"
   8 "PLACED FOR ADOPTION OR ADOPTED"
   9 "PLACED IN FOSTER CARE"
  10 "SOMEPLACE ELSE";

 label define pxcxlaw3
   1 "YES"
   5 "NO";

 label define pxcxhop3
   1 "YES"
   5 "NO";

 label define pxcxever3
   1 "YES"
   5 "NO";

 label define pxwant3
   1 "DEFINITELY YES"
   2 "PROBABLY YES"
   3 "PROBABLY NO"
   4 "DEFINITELY NO";

 label define pxsoon3
   1 "TOO SOON"
   2 "RIGHT TIME"
   3 "LATER"
   4 "DIDN'T CARE";

 label define pxcxsex4
   1 "MALE"
   2 "FEMALE";

 label define kidmar4
   0 "NO"
   1 "YES";

 label define kidagegp4
   1 "UNDER 5 YEARS"
   2 "5-18 YEARS"
   3 "19 OR OLDER";

 label define kidliv4
   0 "NO"
   1 "YES";

 label define kidhh4
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define pxcxknow4
   1 "DURING THE PREGNANCY"
   2 "AFTER THE CHILD WAS BORN";

 label define pxcxliv31
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "WITH HIS/HER MOTHER"
   4 "AWAY AT SCHOOL OR COLLEGE"
   5 "LIVING ON OWN"
   6 "LIVING WITH OTHER RELATIVES"
   7 "DECEASED"
   8 "PLACED FOR ADOPTION OR ADOPTED"
   9 "PLACED IN FOSTER CARE"
  10 "SOMEPLACE ELSE";

 label define pxwant4
   1 "DEFINITELY YES"
   2 "PROBABLY YES"
   3 "PROBABLY NO"
   4 "DEFINITELY NO";

 label define pxsoon4
   1 "TOO SOON"
   2 "RIGHT TIME"
   3 "LATER"
   4 "DIDN'T CARE";

 label define pxcpreg
   1 "YES"
   5 "NO";

 label define pxtrying
   1 "YES"
   5 "NO";

 label define pxrwant
   1 "DEFINITELY YES"
   2 "PROBABLY YES"
   3 "PROBABLY NO"
   4 "DEFINITELY NO";

 label define pxrsoon
   1 "TOO SOON"
   2 "RIGHT TIME"
   3 "LATER"
   4 "DIDN'T CARE";

 label define pxotkid
   1 "YES"
   5 "NO";

 label define pxokad
   1 "YES"
   5 "NO";

 label define akidhh41
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define akidagegp41
   1 "UNDER 5 YEARS"
   2 "5-18 YEARS"
   3 "19 OR OLDER";

 label define pxoksex
   1 "MALE"
   2 "FEMALE";

 label define pxokliv1
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "WITH HIS/HER MOTHER"
   4 "AWAY AT SCHOOL OR COLLEGE"
   5 "LIVING ON OWN"
   6 "LIVING WITH OTHER RELATIVES"
   7 "DECEASED"
   8 "SOMEPLACE ELSE";

 label define pxokliv2
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "WITH HIS/HER MOTHER"
   4 "AWAY AT SCHOOL OR COLLEGE"
   5 "LIVING ON OWN"
   6 "LIVING WITH OTHER RELATIVES"
   7 "DECEASED"
   8 "SOMEPLACE ELSE";

 label define pxnbevr
   1 "YES"
   5 "NO";

 label define pxnbrel
   1 "YES"
   5 "NO";

 label define pxnbfos
   1 "YES"
   5 "NO";

 label define pxnbad
   1 "YES"
   5 "NO";

 label define pxnbxsex
   1 "MALE"
   2 "FEMALE";

 label define pxnbliv1
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "WITH HIS/HER MOTHER"
   4 "AWAY AT SCHOOL OR COLLEGE"
   5 "LIVING ON OWN"
   6 "LIVING WITH OTHER RELATIVES"
   7 "DECEASED"
   8 "SOMEPLACE ELSE";

 label define akidhh51
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define akidagegp51
   1 "UNDER 5 YEARS"
   2 "5-18 YEARS"
   3 "19 OR OLDER";

 label define pxnbxsex2
   1 "MALE"
   2 "FEMALE";

 label define pxnbliv9
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "WITH HIS/HER MOTHER"
   4 "AWAY AT SCHOOL OR COLLEGE"
   5 "LIVING ON OWN"
   6 "LIVING WITH OTHER RELATIVES"
   7 "DECEASED"
   8 "SOMEPLACE ELSE";

 label define akidhh52
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define akidagegp52
   1 "UNDER 5 YEARS"
   2 "5-18 YEARS"
   3 "19 OR OLDER";

 label define d_nbakids
   0 "NONE";

 label define thiswom2
   1 "YES"
   5 "NO";

 label define pxrelat3
   1 "YES"
   5 "NO";

 label define pxrelat4
   1 "YES, MARRIED TO"
   2 "YES, LIVED TOGETHER WITH"
   5 "NO";

 label define livtogn2
   1 "YES"
   5 "NO";

 label define engagthn2
   1 "YES"
   5 "NO";

 label define marrend2
   1 "DEATH OF WIFE"
   2 "DIVORCE"
   3 "ANNULMENT"
   4 "SEPARATION";

 label define pxcurr2
   1 "YES"
   5 "NO";

 label define p2currprt
   0 "NO"
   1 "YES";

 label define pxmarry2
   1 "NO CHANCE"
   2 "A LITTLE CHANCE"
   3 "50-50 CHANCE"
   4 "A PRETTY GOOD CHANCE"
   5 "AN ALMOST CERTAIN CHANCE";

 label define pxlast2
   1 "WITHIN THE LAST WEEK"
   2 "WITHIN THE LAST FOUR WEEKS"
   3 "MORE THAN FOUR WEEKS AGO";

 label define pxluse2
   1 "YES"
   5 "NO";

 label define pxlmeth11
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define pxlmeth12
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define pxlmeth13
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define pxlmeth14
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define pxlruse2
   1 "YES"
   5 "NO";

 label define pxlrmeth5
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
  10 "SOMETHING ELSE";

 label define pxlrmeth6
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
  10 "SOMETHING ELSE";

 label define pxlrmeth7
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
  10 "SOMETHING ELSE";

 label define pxlrmeth8
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
  10 "SOMETHING ELSE";

 label define pxlpuse2
   1 "YES"
   5 "NO";

 label define pxlpmeth8
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define pxlpmeth9
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define pxlpmeth10
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define pxlpmeth11
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define lsxusep2
   0 "NONE OR NO METHOD IDENTIFIED"
   1 "ANY METHOD IDENTIFIED";

 label define pxlsxprb2
   1 "YES"
   5 "NO";

 label define pxmtonce2
   1 "YES"
   5 "NO";

 label define mtoncep2
   0 "NOT ASCERTAINED?"
   1 "YES (MORE THAN ONCE)"
   2 "NO (ONCE)";

 label define pxrelage2
   1 "OLDER"
   2 "YOUNGER"
   3 "SAME AGE";

 label define pxrelyrs2
   1 "1-2 YEARS"
   2 "3-5 YEARS"
   3 "6-10 YEARS"
   4 "MORE THAN 10 YEARS";

 label define pxfrltn3
   1 "MARRIED TO HER"
   2 "ENGAGED TO HER"
   3 "LIVING TOGETHER IN A SEXUAL RELATIONSHIP, BUT NOT ENGAGED"
   4 "GOING WITH HER OR GOING STEADY"
   5 "GOING OUT WITH HER ONCE IN A WHILE"
   6 "JUST FRIENDS"
   7 "HAD JUST MET HER"
   8 "SOMETHING ELSE";

 label define pxhisp2
   1 "YES"
   5 "NO";

 label define pxrace6
   1 "AMERICAN INDIAN OR ALASKA NATIVE"
   2 "ASIAN"
   3 "NATIVE HAWAIIAN OR OTHER PACIFIC ISLANDER"
   4 "BLACK OR AFRICAN AMERICAN"
   5 "WHITE";

 label define pxrace7
   1 "AMERICAN INDIAN OR ALASKA NATIVE"
   2 "ASIAN"
   3 "NATIVE HAWAIIAN OR OTHER PACIFIC ISLANDER"
   4 "BLACK OR AFRICAN AMERICAN"
   5 "WHITE";

 label define pxbest2
   1 "AMERICAN INDIAN OR ALASKA NATIVE"
   2 "ASIAN"
   3 "NATIVE HAWAIIAN OR OTHER PACIFIC ISLANDER"
   4 "BLACK OR AFRICAN AMERICAN"
   5 "WHITE";

 label define pxdob_m2
   1 "JANUARY"
   2 "FEBRUARY"
   3 "MARCH"
   4 "APRIL"
   5 "MAY"
   6 "JUNE"
   7 "JULY"
   8 "AUGUST"
   9 "SEPTEMBER"
  10 "OCTOBER"
  11 "NOVEMBER"
  12 "DECEMBER"
  13 "WINTER"
  14 "SPRING"
  15 "SUMMER"
  16 "FALL";

 label define pxeduc2
   1 "LESS THAN HIGH SCHOOL"
   2 "HIGH SCHOOL GRADUATE OR GED"
   3 "SOME COLLEGE BUT NO DEGREE"
   4 "2-YEAR COLLEGE DEGREE (E G , ASSOCIATES DEGREE)"
   5 "4-YEAR COLLEGE GRADUATE (E G , BA, BS)"
   6 "GRADUATE OR PROFESSIONAL SCHOOL";

 label define pxmarbf2
   1 "YES"
   5 "NO";

 label define pxanych2
   1 "YES"
   5 "NO";

 label define pxanychn2
   1 "1 CHILD"
   2 "2 CHILDREN";

 label define pxablech2
   1 "YES"
   5 "NO";

 label define pxfrltn4
   1 "MARRIED TO HER"
   2 "ENGAGED TO HER"
   3 "LIVING TOGETHER IN A SEXUAL RELATIONSHIP, BUT NOT ENGAGED"
   4 "GOING WITH HER OR GOING STEADY"
   5 "GOING OUT WITH HER ONCE IN A WHILE"
   6 "JUST FRIENDS"
   7 "HAD JUST MET HER"
   8 "SOMETHING ELSE";

 label define pxfuse2
   1 "YES"
   5 "NO";

 label define pxfmeth11
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define pxfmeth12
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define pxfmeth13
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define pxfmeth14
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define pxfmeth15
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define pxanyuse2
   1 "YES"
   5 "NO";

 label define pxmethod11
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define pxmethod12
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define pxmethod13
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define pxmethod14
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define pxmethod15
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define pxmethod16
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define pxmstuse2
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define pxnofreq2
   1 "EVERY TIME"
   2 "MOST OF THE TIME"
   3 "ABOUT HALF OF THE TIME"
   4 "SOME OF THE TIME"
   5 "NONE OF THE TIME";

 label define pxchild2
   1 "YES"
   5 "NO";

 label define pxcxsex11
   1 "MALE"
   2 "FEMALE";

 label define kidmar11
   0 "NO"
   1 "YES";

 label define kidagegp11
   1 "UNDER 5 YEARS"
   2 "5-18 YEARS"
   3 "19 OR OLDER";

 label define kidliv11
   0 "NO"
   1 "YES";

 label define kidhh11
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define pxcxres11
   1 "YES"
   5 "NO";

 label define pxcxknow11
   1 "DURING THE PREGNANCY"
   2 "AFTER THE CHILD WAS BORN";

 label define pxcxliv101
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "WITH HIS/HER MOTHER"
   4 "AWAY AT SCHOOL OR COLLEGE"
   5 "LIVING ON OWN"
   6 "LIVING WITH OTHER RELATIVES"
   7 "DECEASED"
   8 "PLACED FOR ADOPTION OR ADOPTED"
   9 "PLACED IN FOSTER CARE"
  10 "SOMEPLACE ELSE";

 label define pxcxliv102
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "WITH HIS/HER MOTHER"
   4 "AWAY AT SCHOOL OR COLLEGE"
   5 "LIVING ON OWN"
   6 "LIVING WITH OTHER RELATIVES"
   7 "DECEASED"
   8 "PLACED FOR ADOPTION OR ADOPTED"
   9 "PLACED IN FOSTER CARE"
  10 "SOMEPLACE ELSE";

 label define pxcxage11
   1 "LESS THAN 5 YEARS OLD"
   2 "5-18 YEARS OLD"
   3 "19 YEARS OR OLDER";

 label define pxcxlaw11
   1 "YES"
   5 "NO";

 label define pxcxhop11
   1 "YES"
   5 "NO";

 label define pxcxever11
   1 "YES"
   5 "NO";

 label define pxwant11
   1 "DEFINITELY YES"
   2 "PROBABLY YES"
   3 "PROBABLY NO"
   4 "DEFINITELY NO";

 label define pxsoon11
   1 "TOO SOON"
   2 "RIGHT TIME"
   3 "LATER"
   4 "DIDN'T CARE";

 label define pxcxsex12
   1 "MALE"
   2 "FEMALE";

 label define kidmar12
   0 "NO"
   1 "YES";

 label define kidagegp12
   1 "UNDER 5 YEARS"
   2 "5-18 YEARS"
   3 "19 OR OLDER";

 label define kidliv12
   0 "NO"
   1 "YES";

 label define kidhh12
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define multbirt22
   1 "YES"
   5 "NO";

 label define pxcxres12
   1 "YES"
   5 "NO";

 label define pxcxknow12
   1 "DURING THE PREGNANCY"
   2 "AFTER THE CHILD WAS BORN";

 label define pxcxliv111
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "WITH HIS/HER MOTHER"
   4 "AWAY AT SCHOOL OR COLLEGE"
   5 "LIVING ON OWN"
   6 "LIVING WITH OTHER RELATIVES"
   7 "DECEASED"
   8 "PLACED FOR ADOPTION OR ADOPTED"
   9 "PLACED IN FOSTER CARE"
  10 "SOMEPLACE ELSE";

 label define pxcxage12
   1 "LESS THAN 5 YEARS OLD"
   2 "5-18 YEARS OLD"
   3 "19 YEARS OR OLDER";

 label define pxcxlaw12
   1 "YES"
   5 "NO";

 label define pxcxhop12
   1 "YES"
   5 "NO";

 label define pxcxever12
   1 "YES"
   5 "NO";

 label define pxwant12
   1 "DEFINITELY YES"
   2 "PROBABLY YES"
   3 "PROBABLY NO"
   4 "DEFINITELY NO";

 label define pxsoon12
   1 "TOO SOON"
   2 "RIGHT TIME"
   3 "LATER"
   4 "DIDN'T CARE";

 label define pxcxsex13
   1 "MALE"
   2 "FEMALE";

 label define kidmar13
   0 "NO"
   1 "YES";

 label define kidagegp13
   1 "UNDER 5 YEARS"
   2 "5-18 YEARS"
   3 "19 OR OLDER";

 label define kidliv13
   0 "NO"
   1 "YES";

 label define kidhh13
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define pxcxres13
   1 "YES"
   5 "NO";

 label define pxcxknow13
   1 "DURING THE PREGNANCY"
   2 "AFTER THE CHILD WAS BORN";

 label define pxcxliv121
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "WITH HIS/HER MOTHER"
   4 "AWAY AT SCHOOL OR COLLEGE"
   5 "LIVING ON OWN"
   6 "LIVING WITH OTHER RELATIVES"
   7 "DECEASED"
   8 "PLACED FOR ADOPTION OR ADOPTED"
   9 "PLACED IN FOSTER CARE"
  10 "SOMEPLACE ELSE";

 label define pxcxlaw13
   1 "YES"
   5 "NO";

 label define pxcxhop13
   1 "YES"
   5 "NO";

 label define pxwant13
   1 "DEFINITELY YES"
   2 "PROBABLY YES"
   3 "PROBABLY NO"
   4 "DEFINITELY NO";

 label define pxsoon13
   1 "TOO SOON"
   2 "RIGHT TIME"
   3 "LATER"
   4 "DIDN'T CARE";

 label define pxcxsex14
   1 "MALE"
   2 "FEMALE";

 label define kidmar14
   0 "NO"
   1 "YES";

 label define kidagegp14
   1 "UNDER 5 YEARS"
   2 "5-18 YEARS"
   3 "19 OR OLDER";

 label define kidliv14
   0 "NO"
   1 "YES";

 label define kidhh14
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define pxcxres14
   1 "YES"
   5 "NO";

 label define pxcxknow14
   1 "DURING THE PREGNANCY"
   2 "AFTER THE CHILD WAS BORN";

 label define pxcxliv131
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "WITH HIS/HER MOTHER"
   4 "AWAY AT SCHOOL OR COLLEGE"
   5 "LIVING ON OWN"
   6 "LIVING WITH OTHER RELATIVES"
   7 "DECEASED"
   8 "PLACED FOR ADOPTION OR ADOPTED"
   9 "PLACED IN FOSTER CARE"
  10 "SOMEPLACE ELSE";

 label define pxcxlaw14
   1 "YES"
   5 "NO";

 label define pxcxhop14
   1 "YES"
   5 "NO";

 label define pxwant14
   1 "DEFINITELY YES"
   2 "PROBABLY YES"
   3 "PROBABLY NO"
   4 "DEFINITELY NO";

 label define pxsoon14
   1 "TOO SOON"
   2 "RIGHT TIME"
   3 "LATER"
   4 "DIDN'T CARE";

 label define pxcpreg2
   1 "YES"
   5 "NO";

 label define pxtrying2
   1 "YES"
   5 "NO";

 label define pxrwant2
   1 "DEFINITELY YES"
   2 "PROBABLY YES"
   3 "PROBABLY NO"
   4 "DEFINITELY NO";

 label define pxrsoon2
   1 "TOO SOON"
   2 "RIGHT TIME"
   3 "LATER"
   4 "DIDN'T CARE";

 label define pxotkid2
   1 "YES"
   5 "NO";

 label define pxokad2
   1 "YES"
   5 "NO";

 label define pxnbevr2
   1 "YES"
   5 "NO";

 label define pxnbrel2
   1 "YES"
   5 "NO";

 label define pxnbfos2
   1 "YES"
   5 "NO";

 label define pxnbad2
   1 "YES"
   5 "NO";

 label define d_nbakids2
   0 "NONE";

 label define thiswom3
   1 "YES"
   5 "NO";

 label define pxrelat5
   1 "YES"
   5 "NO";

 label define pxrelat6
   1 "YES, MARRIED TO"
   2 "YES, LIVED TOGETHER WITH"
   5 "NO";

 label define livtogn3
   1 "YES"
   5 "NO";

 label define engagthn3
   1 "YES"
   5 "NO";

 label define marrend3
   1 "DEATH OF WIFE"
   2 "DIVORCE"
   3 "ANNULMENT"
   4 "SEPARATION";

 label define pxcurr3
   1 "YES"
   5 "NO";

 label define p3currprt
   0 "NO"
   1 "YES";

 label define pxmarry3
   1 "NO CHANCE"
   2 "A LITTLE CHANCE"
   3 "50-50 CHANCE"
   4 "A PRETTY GOOD CHANCE"
   5 "AN ALMOST CERTAIN CHANCE";

 label define pxlast3
   1 "WITHIN THE LAST WEEK"
   2 "WITHIN THE LAST FOUR WEEKS"
   3 "MORE THAN FOUR WEEKS AGO";

 label define pxluse3
   1 "YES"
   5 "NO";

 label define pxlmeth21
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define pxlmeth22
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define pxlmeth23
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define pxlmeth24
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define pxlruse3
   1 "YES"
   5 "NO";

 label define pxlrmeth9
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
  10 "SOMETHING ELSE";

 label define pxlrmeth10
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
  10 "SOMETHING ELSE";

 label define pxlrmeth11
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
  10 "SOMETHING ELSE";

 label define pxlrmeth12
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
  10 "SOMETHING ELSE";

 label define pxlpuse3
   1 "YES"
   5 "NO";

 label define pxlpmeth15
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define pxlpmeth16
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define pxlpmeth17
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define pxlpmeth18
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define lsxusep3
   0 "NONE OR NO METHOD IDENTIFIED"
   1 "ANY METHOD IDENTIFIED";

 label define pxlsxprb3
   1 "YES"
   5 "NO";

 label define pxmtonce3
   1 "YES"
   5 "NO";

 label define mtoncep3
   0 "NOT ASCERTAINED?"
   1 "YES (MORE THAN ONCE)"
   2 "NO (ONCE)";

 label define pxrelage3
   1 "OLDER"
   2 "YOUNGER"
   3 "SAME AGE";

 label define pxrelyrs3
   1 "1-2 YEARS"
   2 "3-5 YEARS"
   3 "6-10 YEARS"
   4 "MORE THAN 10 YEARS";

 label define pxfrltn5
   1 "MARRIED TO HER"
   2 "ENGAGED TO HER"
   3 "LIVING TOGETHER IN A SEXUAL RELATIONSHIP, BUT NOT ENGAGED"
   4 "GOING WITH HER OR GOING STEADY"
   5 "GOING OUT WITH HER ONCE IN A WHILE"
   6 "JUST FRIENDS"
   7 "HAD JUST MET HER"
   8 "SOMETHING ELSE";

 label define pxhisp3
   1 "YES"
   5 "NO";

 label define pxrace11
   1 "AMERICAN INDIAN OR ALASKA NATIVE"
   2 "ASIAN"
   3 "NATIVE HAWAIIAN OR OTHER PACIFIC ISLANDER"
   4 "BLACK OR AFRICAN AMERICAN"
   5 "WHITE";

 label define pxrace12
   1 "AMERICAN INDIAN OR ALASKA NATIVE"
   2 "ASIAN"
   3 "NATIVE HAWAIIAN OR OTHER PACIFIC ISLANDER"
   4 "BLACK OR AFRICAN AMERICAN"
   5 "WHITE";

 label define pxbest3
   1 "AMERICAN INDIAN OR ALASKA NATIVE"
   2 "ASIAN"
   3 "NATIVE HAWAIIAN OR OTHER PACIFIC ISLANDER"
   4 "BLACK OR AFRICAN AMERICAN"
   5 "WHITE";

 label define pxdob_m3
   1 "JANUARY"
   2 "FEBRUARY"
   3 "MARCH"
   4 "APRIL"
   5 "MAY"
   6 "JUNE"
   7 "JULY"
   8 "AUGUST"
   9 "SEPTEMBER"
  10 "OCTOBER"
  11 "NOVEMBER"
  12 "DECEMBER"
  13 "WINTER"
  14 "SPRING"
  15 "SUMMER"
  16 "FALL";

 label define pxeduc3
   1 "LESS THAN HIGH SCHOOL"
   2 "HIGH SCHOOL GRADUATE OR GED"
   3 "SOME COLLEGE BUT NO DEGREE"
   4 "2-YEAR COLLEGE DEGREE (E G , ASSOCIATES DEGREE)"
   5 "4-YEAR COLLEGE GRADUATE (E G , BA, BS)"
   6 "GRADUATE OR PROFESSIONAL SCHOOL";

 label define pxmarbf3
   1 "YES"
   5 "NO";

 label define pxanych3
   1 "YES"
   5 "NO";

 label define pxanychn3
   1 "1 CHILD"
   2 "2 CHILDREN";

 label define pxablech3
   1 "YES"
   5 "NO";

 label define pxfrltn6
   1 "MARRIED TO HER"
   2 "ENGAGED TO HER"
   3 "LIVING TOGETHER IN A SEXUAL RELATIONSHIP, BUT NOT ENGAGED"
   4 "GOING WITH HER OR GOING STEADY"
   5 "GOING OUT WITH HER ONCE IN A WHILE"
   6 "JUST FRIENDS"
   7 "HAD JUST MET HER"
   8 "SOMETHING ELSE";

 label define pxfuse3
   1 "YES"
   5 "NO";

 label define pxfmeth21
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define pxfmeth22
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define pxfmeth23
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define pxfmeth24
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define pxfmeth25
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define pxanyuse3
   1 "YES"
   5 "NO";

 label define pxmethod21
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define pxmethod22
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define pxmethod23
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define pxmethod24
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define pxmethod25
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define pxmethod26
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define pxmstuse3
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define pxnofreq3
   1 "EVERY TIME"
   2 "MOST OF THE TIME"
   3 "ABOUT HALF OF THE TIME"
   4 "SOME OF THE TIME"
   5 "NONE OF THE TIME";

 label define pxchild3
   1 "YES"
   5 "NO";

 label define pxcxsex21
   1 "MALE"
   2 "FEMALE";

 label define kidmar21
   0 "NO"
   1 "YES";

 label define kidagegp21
   1 "UNDER 5 YEARS"
   2 "5-18 YEARS"
   3 "19 OR OLDER";

 label define kidliv21
   0 "NO"
   1 "YES";

 label define kidhh21
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define pxcxmarb21
   1 "YES"
   5 "NO";

 label define pxcxres21
   1 "YES"
   5 "NO";

 label define pxcxknow21
   1 "DURING THE PREGNANCY"
   2 "AFTER THE CHILD WAS BORN";

 label define pxcxliv201
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "WITH HIS/HER MOTHER"
   4 "AWAY AT SCHOOL OR COLLEGE"
   5 "LIVING ON OWN"
   6 "LIVING WITH OTHER RELATIVES"
   7 "DECEASED"
   8 "PLACED FOR ADOPTION OR ADOPTED"
   9 "PLACED IN FOSTER CARE"
  10 "SOMEPLACE ELSE";

 label define pxcxliv202
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "WITH HIS/HER MOTHER"
   4 "AWAY AT SCHOOL OR COLLEGE"
   5 "LIVING ON OWN"
   6 "LIVING WITH OTHER RELATIVES"
   7 "DECEASED"
   8 "PLACED FOR ADOPTION OR ADOPTED"
   9 "PLACED IN FOSTER CARE"
  10 "SOMEPLACE ELSE";

 label define pxcxage21
   1 "LESS THAN 5 YEARS OLD"
   2 "5-18 YEARS OLD"
   3 "19 YEARS OR OLDER";

 label define pxcxlaw21
   1 "YES"
   5 "NO";

 label define pxcxhop21
   1 "YES"
   5 "NO";

 label define pxcxever21
   1 "YES"
   5 "NO";

 label define pxwant21
   1 "DEFINITELY YES"
   2 "PROBABLY YES"
   3 "PROBABLY NO"
   4 "DEFINITELY NO";

 label define pxsoon21
   1 "TOO SOON"
   2 "RIGHT TIME"
   3 "LATER"
   4 "DIDN'T CARE";

 label define pxcxsex22
   1 "MALE"
   2 "FEMALE";

 label define kidmar22
   0 "NO"
   1 "YES";

 label define kidagegp22
   1 "UNDER 5 YEARS"
   2 "5-18 YEARS"
   3 "19 OR OLDER";

 label define kidliv22
   0 "NO"
   1 "YES";

 label define kidhh22
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define pxcxres22
   1 "YES"
   5 "NO";

 label define pxcxknow22
   1 "DURING THE PREGNANCY"
   2 "AFTER THE CHILD WAS BORN";

 label define pxcxliv211
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "WITH HIS/HER MOTHER"
   4 "AWAY AT SCHOOL OR COLLEGE"
   5 "LIVING ON OWN"
   6 "LIVING WITH OTHER RELATIVES"
   7 "DECEASED"
   8 "PLACED FOR ADOPTION OR ADOPTED"
   9 "PLACED IN FOSTER CARE"
  10 "SOMEPLACE ELSE";

 label define pxcxlaw22
   1 "YES"
   5 "NO";

 label define pxcxhop22
   1 "YES"
   5 "NO";

 label define pxwant22
   1 "DEFINITELY YES"
   2 "PROBABLY YES"
   3 "PROBABLY NO"
   4 "DEFINITELY NO";

 label define pxcpreg3
   1 "YES"
   5 "NO";

 label define pxtrying3
   1 "YES"
   5 "NO";

 label define pxrwant3
   1 "DEFINITELY YES"
   2 "PROBABLY YES"
   3 "PROBABLY NO"
   4 "DEFINITELY NO";

 label define pxrsoon3
   1 "TOO SOON"
   2 "RIGHT TIME"
   3 "LATER"
   4 "DIDN'T CARE";

 label define pxotkid3
   1 "YES"
   5 "NO";

 label define pxokad3
   1 "YES"
   5 "NO";

 label define pxnbevr3
   1 "YES"
   5 "NO";

 label define pxnbrel3
   1 "YES"
   5 "NO";

 label define pxnbfos3
   1 "YES"
   5 "NO";

 label define pxnbad3
   1 "YES"
   5 "NO";

 label define d_nbakids3
   0 "NONE";

 label define fpage18
   1 "LESS THAN 18"
   2 "18 YEARS OR OLDER";

 label define fpage15
   1 "LESS THAN 15"
   2 "15 YEARS OR OLDER";

 label define fpage20
   1 "LESS THAN 20"
   2 "20 YEARS OR OLDER";

 label define fprelage
   1 "OLDER"
   2 "YOUNGER"
   3 "SAME AGE";

 label define fprelyrs
   1 "1-2 YEARS"
   2 "3-5 YEARS"
   3 "6-10 YEARS"
   4 "MORE THAN 10 YEARS";

 label define fprltn
   1 "MARRIED TO HER"
   2 "ENGAGED TO HER"
   3 "LIVING TOGETHER IN A SEXUAL RELATIONSHIP, BUT NOT ENGAGED"
   4 "GOING WITH HER OR GOING STEADY"
   5 "GOING OUT WITH HER ONCE IN A WHILE"
   6 "JUST FRIENDS"
   7 "HAD JUST MET HER"
   8 "SOMETHING ELSE";

 label define fpuse
   1 "YES"
   5 "NO";

 label define fpmeth01
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define fpmeth02
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define fpmeth03
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define fpmeth04
   1 "CONDOM OR RUBBER"
   2 "WITHDRAWAL OR PULLING OUT"
   3 "VASECTOMY OR MALE STERILIZATION"
   4 "PILL"
   5 "TUBAL LIGATION (TUBES TIED) OR FEMALE STERILIZATION"
   6 "INJECTION (DEPO-PROVERA OR LUNELLE)"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT (NORPLANT (TM))"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE";

 label define fpprobe
   1 "YES"
   5 "NO";

 label define fwverify
   1 "YES"
   5 "NO";

 label define fwver
   0 "NO"
   1 "YES";

 label define fwverify2
   1 "YES"
   5 "NO";

 label define fwver2
   0 "NO"
   1 "YES";

 label define fwverify3
   1 "YES"
   5 "NO";

 label define fwver3
   0 "NO"
   1 "YES";

 label define fcverify
   1 "YES"
   5 "NO";

 label define fcver
   0 "NO"
   1 "YES";

 label define exrelation
   0 "FORMER COHAB PARTNER"
   1 "FORMER WIFE";

 label define livtogn4
   1 "YES"
   5 "NO";

 label define engagthn4
   1 "YES"
   5 "NO";

 label define marrend4
   1 "DEATH OF WIFE"
   2 "DIVORCE"
   3 "ANNULMENT"
   4 "SEPARATION";

 label define fwpdob_m
   1 "JANUARY"
   2 "FEBRUARY"
   3 "MARCH"
   4 "APRIL"
   5 "MAY"
   6 "JUNE"
   7 "JULY"
   8 "AUGUST"
   9 "SEPTEMBER"
  10 "OCTOBER"
  11 "NOVEMBER"
  12 "DECEMBER"
  13 "WINTER"
  14 "SPRING"
  15 "SUMMER"
  16 "FALL";

 label define fwphisp
   1 "YES"
   5 "NO";

 label define fwprace1
   1 "AMERICAN INDIAN OR ALASKA NATIVE"
   2 "ASIAN"
   3 "NATIVE HAWAIIAN OR OTHER PACIFIC ISLANDER"
   4 "BLACK OR AFRICAN AMERICAN"
   5 "WHITE";

 label define fwprace2
   1 "AMERICAN INDIAN OR ALASKA NATIVE"
   2 "ASIAN"
   3 "NATIVE HAWAIIAN OR OTHER PACIFIC ISLANDER"
   4 "BLACK OR AFRICAN AMERICAN"
   5 "WHITE";

 label define fwpraceb
   1 "AMERICAN INDIAN OR ALASKA NATIVE"
   2 "ASIAN"
   3 "NATIVE HAWAIIAN OR OTHER PACIFIC ISLANDER"
   4 "BLACK OR AFRICAN AMERICAN"
   5 "WHITE";

 label define fwpmarbf
   1 "YES"
   5 "NO";

 label define fwpbiokd
   1 "YES"
   5 "NO";

 label define kidliv31
   0 "NO"
   1 "YES";

 label define kidagegp31
   1 "UNDER 5 YEARS"
   2 "5-18 YEARS"
   3 "19 OR OLDER";

 label define kidhh31
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define kidmar31
   0 "NO"
   1 "YES";

 label define fwpchsex
   1 "MALE"
   2 "FEMALE";

 label define fwchmarb
   1 "YES"
   5 "NO";

 label define fwpchres
   1 "YES"
   5 "NO";

 label define fwpchlrn
   1 "DURING THE PREGNANCY"
   2 "AFTER THE CHILD WAS BORN";

 label define fwpchliv01
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "WITH HIS/HER MOTHER"
   4 "AWAY AT SCHOOL OR COLLEGE"
   5 "LIVING ON OWN"
   6 "LIVING WITH OTHER RELATIVES"
   7 "DECEASED"
   8 "PLACED FOR ADOPTION OR ADOPTED"
   9 "PLACED IN FOSTER CARE"
  10 "SOMEPLACE ELSE";

 label define fwpchliv02
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "WITH HIS/HER MOTHER"
   4 "AWAY AT SCHOOL OR COLLEGE"
   5 "LIVING ON OWN"
   6 "LIVING WITH OTHER RELATIVES"
   7 "DECEASED"
   8 "PLACED FOR ADOPTION OR ADOPTED"
   9 "PLACED IN FOSTER CARE"
  10 "SOMEPLACE ELSE";

 label define fwpchage
   1 "LESS THAN 5 YEARS OLD"
   2 "5-18 YEARS OLD"
   3 "19 YEARS OR OLDER";

 label define fwpchleg
   1 "YES"
   5 "NO";

 label define fwpchhop
   1 "YES"
   5 "NO";

 label define fwpchevr
   1 "YES"
   5 "NO";

 label define fwprwant
   1 "DEFINITELY YES"
   2 "PROBABLY YES"
   3 "PROBABLY NO"
   4 "DEFINITELY NO";

 label define fwpsoon
   1 "TOO SOON"
   2 "RIGHT TIME"
   3 "LATER"
   4 "DIDN'T CARE";

 label define kidliv32
   0 "NO"
   1 "YES";

 label define kidagegp32
   1 "UNDER 5 YEARS"
   2 "5-18 YEARS"
   3 "19 OR OLDER";

 label define kidhh32
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define kidmar32
   0 "NO"
   1 "YES";

 label define fwpchsex2
   1 "MALE"
   2 "FEMALE";

 label define fwchmarb2
   1 "YES"
   5 "NO";

 label define fwpchres2
   1 "YES"
   5 "NO";

 label define fwpchlrn2
   1 "DURING THE PREGNANCY"
   2 "AFTER THE CHILD WAS BORN";

 label define fwpchliv11
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "WITH HIS/HER MOTHER"
   4 "AWAY AT SCHOOL OR COLLEGE"
   5 "LIVING ON OWN"
   6 "LIVING WITH OTHER RELATIVES"
   7 "DECEASED"
   8 "PLACED FOR ADOPTION OR ADOPTED"
   9 "PLACED IN FOSTER CARE"
  10 "SOMEPLACE ELSE";

 label define fwpchliv12
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "WITH HIS/HER MOTHER"
   4 "AWAY AT SCHOOL OR COLLEGE"
   5 "LIVING ON OWN"
   6 "LIVING WITH OTHER RELATIVES"
   7 "DECEASED"
   8 "PLACED FOR ADOPTION OR ADOPTED"
   9 "PLACED IN FOSTER CARE"
  10 "SOMEPLACE ELSE";

 label define fwpchage2
   1 "LESS THAN 5 YEARS OLD"
   2 "5-18 YEARS OLD"
   3 "19 YEARS OR OLDER";

 label define fwpchleg2
   1 "YES"
   5 "NO";

 label define fwpchhop2
   1 "YES"
   5 "NO";

 label define fwpchevr2
   1 "YES"
   5 "NO";

 label define fwprwant2
   1 "DEFINITELY YES"
   2 "PROBABLY YES"
   3 "PROBABLY NO"
   4 "DEFINITELY NO";

 label define fwpsoon2
   1 "TOO SOON"
   2 "RIGHT TIME"
   3 "LATER"
   4 "DIDN'T CARE";

 label define kidliv33
   0 "NO"
   1 "YES";

 label define kidagegp33
   1 "UNDER 5 YEARS"
   2 "5-18 YEARS"
   3 "19 OR OLDER";

 label define kidhh33
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define kidmar33
   0 "NO"
   1 "YES";

 label define fwpchsex3
   1 "MALE"
   2 "FEMALE";

 label define fwpchres3
   1 "YES"
   5 "NO";

 label define fwpchlrn3
   1 "DURING THE PREGNANCY"
   2 "AFTER THE CHILD WAS BORN";

 label define fwpchliv21
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "WITH HIS/HER MOTHER"
   4 "AWAY AT SCHOOL OR COLLEGE"
   5 "LIVING ON OWN"
   6 "LIVING WITH OTHER RELATIVES"
   7 "DECEASED"
   8 "PLACED FOR ADOPTION OR ADOPTED"
   9 "PLACED IN FOSTER CARE"
  10 "SOMEPLACE ELSE";

 label define fwpchliv22
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "WITH HIS/HER MOTHER"
   4 "AWAY AT SCHOOL OR COLLEGE"
   5 "LIVING ON OWN"
   6 "LIVING WITH OTHER RELATIVES"
   7 "DECEASED"
   8 "PLACED FOR ADOPTION OR ADOPTED"
   9 "PLACED IN FOSTER CARE"
  10 "SOMEPLACE ELSE";

 label define fwpchage3
   1 "LESS THAN 5 YEARS OLD"
   2 "5-18 YEARS OLD"
   3 "19 YEARS OR OLDER";

 label define fwpchleg3
   1 "YES"
   5 "NO";

 label define fwpchhop3
   1 "YES"
   5 "NO";

 label define fwpchevr3
   1 "YES"
   5 "NO";

 label define fwprwant3
   1 "DEFINITELY YES"
   2 "PROBABLY YES"
   3 "PROBABLY NO"
   4 "DEFINITELY NO";

 label define fwpsoon3
   1 "TOO SOON"
   2 "RIGHT TIME"
   3 "LATER"
   4 "DIDN'T CARE";

 label define kidmar34
   0 "NO"
   1 "YES";

 label define kidagegp34
   1 "UNDER 5 YEARS"
   2 "5-18 YEARS"
   3 "19 OR OLDER";

 label define kidhh34
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define kidliv34
   0 "NO"
   1 "YES";

 label define fwpchsex4
   1 "MALE"
   2 "FEMALE";

 label define multbirt44
   1 "YES"
   5 "NO";

 label define fwpchres4
   1 "YES"
   5 "NO";

 label define fwpchliv31
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "WITH HIS/HER MOTHER"
   4 "AWAY AT SCHOOL OR COLLEGE"
   5 "LIVING ON OWN"
   6 "LIVING WITH OTHER RELATIVES"
   7 "DECEASED"
   8 "PLACED FOR ADOPTION OR ADOPTED"
   9 "PLACED IN FOSTER CARE"
  10 "SOMEPLACE ELSE";

 label define fwpchage4
   1 "LESS THAN 5 YEARS OLD"
   2 "5-18 YEARS OLD"
   3 "19 YEARS OR OLDER";

 label define fwpchleg4
   1 "YES"
   5 "NO";

 label define fwpchhop4
   1 "YES"
   5 "NO";

 label define fwpchevr4
   1 "YES"
   5 "NO";

 label define fwprwant4
   1 "DEFINITELY YES"
   2 "PROBABLY YES"
   3 "PROBABLY NO"
   4 "DEFINITELY NO";

 label define kidmar35
   0 "NO"
   1 "YES";

 label define kidagegp35
   1 "UNDER 5 YEARS"
   2 "5-18 YEARS"
   3 "19 OR OLDER";

 label define kidhh35
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define kidliv35
   0 "NO"
   1 "YES";

 label define fwpchsex5
   1 "MALE"
   2 "FEMALE";

 label define fwpchliv41
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "WITH HIS/HER MOTHER"
   4 "AWAY AT SCHOOL OR COLLEGE"
   5 "LIVING ON OWN"
   6 "LIVING WITH OTHER RELATIVES"
   7 "DECEASED"
   8 "PLACED FOR ADOPTION OR ADOPTED"
   9 "PLACED IN FOSTER CARE"
  10 "SOMEPLACE ELSE";

 label define fwpchage5
   1 "LESS THAN 5 YEARS OLD"
   2 "5-18 YEARS OLD"
   3 "19 YEARS OR OLDER";

 label define fwpchleg5
   1 "YES"
   5 "NO";

 label define fwpchhop5
   1 "YES"
   5 "NO";

 label define fwpchevr5
   1 "YES"
   5 "NO";

 label define fwpotkid
   1 "YES"
   5 "NO";

 label define fwpokad
   1 "YES"
   5 "NO";

 label define akidhh101
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define fwpoksex
   1 "MALE"
   2 "FEMALE";

 label define fwpokliv1
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "WITH HIS/HER MOTHER"
   4 "AWAY AT SCHOOL OR COLLEGE"
   5 "LIVING ON OWN"
   6 "LIVING WITH OTHER RELATIVES"
   7 "DECEASED"
   8 "SOMEPLACE ELSE";

 label define fwpokliv2
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "WITH HIS/HER MOTHER"
   4 "AWAY AT SCHOOL OR COLLEGE"
   5 "LIVING ON OWN"
   6 "LIVING WITH OTHER RELATIVES"
   7 "DECEASED"
   8 "SOMEPLACE ELSE";

 label define akidagegp101
   1 "UNDER 5 YEARS"
   2 "5-18 YEARS"
   3 "19 OR OLDER";

 label define akidagegp102
   1 "UNDER 5 YEARS"
   2 "5-18 YEARS"
   3 "19 OR OLDER";

 label define akidhh102
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define fwpoksex2
   1 "MALE"
   2 "FEMALE";

 label define fwpokliv9
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "WITH HIS/HER MOTHER"
   4 "AWAY AT SCHOOL OR COLLEGE"
   5 "LIVING ON OWN"
   6 "LIVING WITH OTHER RELATIVES"
   7 "DECEASED"
   8 "SOMEPLACE ELSE";

 label define akidagegp103
   1 "UNDER 5 YEARS"
   2 "5-18 YEARS"
   3 "19 OR OLDER";

 label define akidhh103
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define fwpoksex3
   1 "MALE"
   2 "FEMALE";

 label define fwpokliv17
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "WITH HIS/HER MOTHER"
   4 "AWAY AT SCHOOL OR COLLEGE"
   5 "LIVING ON OWN"
   6 "LIVING WITH OTHER RELATIVES"
   7 "DECEASED"
   8 "SOMEPLACE ELSE";

 label define fwpnbevr
   1 "YES"
   5 "NO";

 label define fwpnbrel
   1 "YES"
   5 "NO";

 label define fwpnbfos
   1 "YES"
   5 "NO";

 label define fwpnbad
   1 "YES"
   5 "NO";

 label define akidagegp111
   1 "UNDER 5 YEARS"
   2 "5-18 YEARS"
   3 "19 OR OLDER";

 label define akidhh111
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define fwpnbsex
   1 "MALE"
   2 "FEMALE";

 label define akidagegp112
   1 "UNDER 5 YEARS"
   2 "5-18 YEARS"
   3 "19 OR OLDER";

 label define akidhh112
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define fwpnbsex2
   1 "MALE"
   2 "FEMALE";

 label define fwpnbliv9
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "WITH HIS/HER MOTHER"
   4 "AWAY AT SCHOOL OR COLLEGE"
   5 "LIVING ON OWN"
   6 "LIVING WITH OTHER RELATIVES"
   7 "DECEASED"
   8 "SOMEPLACE ELSE";

 label define e_okakids
   0 "NONE";

 label define exrelation2
   0 "FORMER COHAB PARTNER"
   1 "FORMER WIFE";

 label define livtogn5
   1 "YES"
   5 "NO";

 label define engagthn5
   1 "YES"
   5 "NO";

 label define marrend5
   1 "DEATH OF WIFE"
   2 "DIVORCE"
   3 "ANNULMENT"
   4 "SEPARATION";

 label define fwpdob_m2
   1 "JANUARY"
   2 "FEBRUARY"
   3 "MARCH"
   4 "APRIL"
   5 "MAY"
   6 "JUNE"
   7 "JULY"
   8 "AUGUST"
   9 "SEPTEMBER"
  10 "OCTOBER"
  11 "NOVEMBER"
  12 "DECEMBER"
  13 "WINTER"
  14 "SPRING"
  15 "SUMMER"
  16 "FALL";

 label define fwpmarbf2
   1 "YES"
   5 "NO";

 label define fwpbiokd2
   1 "YES"
   5 "NO";

 label define kidmar41
   0 "NO"
   1 "YES";

 label define kidagegp41
   1 "UNDER 5 YEARS"
   2 "5-18 YEARS"
   3 "19 OR OLDER";

 label define kidhh41
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define kidliv41
   0 "NO"
   1 "YES";

 label define fwpchsex11
   1 "MALE"
   2 "FEMALE";

 label define fwpchres11
   1 "YES"
   5 "NO";

 label define fwpchlrn11
   1 "DURING THE PREGNANCY"
   2 "AFTER THE CHILD WAS BORN";

 label define fwpchliv101
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "WITH HIS/HER MOTHER"
   4 "AWAY AT SCHOOL OR COLLEGE"
   5 "LIVING ON OWN"
   6 "LIVING WITH OTHER RELATIVES"
   7 "DECEASED"
   8 "PLACED FOR ADOPTION OR ADOPTED"
   9 "PLACED IN FOSTER CARE"
  10 "SOMEPLACE ELSE";

 label define fwpchliv102
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "WITH HIS/HER MOTHER"
   4 "AWAY AT SCHOOL OR COLLEGE"
   5 "LIVING ON OWN"
   6 "LIVING WITH OTHER RELATIVES"
   7 "DECEASED"
   8 "PLACED FOR ADOPTION OR ADOPTED"
   9 "PLACED IN FOSTER CARE"
  10 "SOMEPLACE ELSE";

 label define fwpchage11
   1 "LESS THAN 5 YEARS OLD"
   2 "5-18 YEARS OLD"
   3 "19 YEARS OR OLDER";

 label define fwpchleg11
   1 "YES"
   5 "NO";

 label define fwpchhop11
   1 "YES"
   5 "NO";

 label define fwpchevr11
   1 "YES"
   5 "NO";

 label define fwprwant11
   1 "DEFINITELY YES"
   2 "PROBABLY YES"
   3 "PROBABLY NO"
   4 "DEFINITELY NO";

 label define fwpsoon11
   1 "TOO SOON"
   2 "RIGHT TIME"
   3 "LATER"
   4 "DIDN'T CARE";

 label define kidmar42
   0 "NO"
   1 "YES";

 label define kidagegp42
   1 "UNDER 5 YEARS"
   2 "5-18 YEARS"
   3 "19 OR OLDER";

 label define kidhh42
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define kidliv42
   0 "NO"
   1 "YES";

 label define fwpchsex12
   1 "MALE"
   2 "FEMALE";

 label define fwpchres12
   1 "YES"
   5 "NO";

 label define fwpchliv111
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "WITH HIS/HER MOTHER"
   4 "AWAY AT SCHOOL OR COLLEGE"
   5 "LIVING ON OWN"
   6 "LIVING WITH OTHER RELATIVES"
   7 "DECEASED"
   8 "PLACED FOR ADOPTION OR ADOPTED"
   9 "PLACED IN FOSTER CARE"
  10 "SOMEPLACE ELSE";

 label define fwpchage12
   1 "LESS THAN 5 YEARS OLD"
   2 "5-18 YEARS OLD"
   3 "19 YEARS OR OLDER";

 label define fwpchleg12
   1 "YES"
   5 "NO";

 label define fwpchhop12
   1 "YES"
   5 "NO";

 label define kidmar43
   0 "NO"
   1 "YES";

 label define kidagegp43
   1 "UNDER 5 YEARS"
   2 "5-18 YEARS"
   3 "19 OR OLDER";

 label define kidhh43
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define kidliv43
   0 "NO"
   1 "YES";

 label define fwpchsex13
   1 "MALE"
   2 "FEMALE";

 label define fwpchliv121
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "WITH HIS/HER MOTHER"
   4 "AWAY AT SCHOOL OR COLLEGE"
   5 "LIVING ON OWN"
   6 "LIVING WITH OTHER RELATIVES"
   7 "DECEASED"
   8 "PLACED FOR ADOPTION OR ADOPTED"
   9 "PLACED IN FOSTER CARE"
  10 "SOMEPLACE ELSE";

 label define kidmar44
   0 "NO"
   1 "YES";

 label define kidagegp44
   1 "UNDER 5 YEARS"
   2 "5-18 YEARS"
   3 "19 OR OLDER";

 label define kidhh44
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define kidliv44
   0 "NO"
   1 "YES";

 label define fwpchsex14
   1 "MALE"
   2 "FEMALE";

 label define fwpchliv131
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "WITH HIS/HER MOTHER"
   4 "AWAY AT SCHOOL OR COLLEGE"
   5 "LIVING ON OWN"
   6 "LIVING WITH OTHER RELATIVES"
   7 "DECEASED"
   8 "PLACED FOR ADOPTION OR ADOPTED"
   9 "PLACED IN FOSTER CARE"
  10 "SOMEPLACE ELSE";

 label define fwpotkid2
   1 "YES"
   5 "NO";

 label define fwpokad2
   1 "YES"
   5 "NO";

 label define akidagegp121
   1 "UNDER 5 YEARS"
   2 "5-18 YEARS"
   3 "19 OR OLDER";

 label define akidhh121
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define fwpoksex11
   1 "MALE"
   2 "FEMALE";

 label define fwpokliv81
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "WITH HIS/HER MOTHER"
   4 "AWAY AT SCHOOL OR COLLEGE"
   5 "LIVING ON OWN"
   6 "LIVING WITH OTHER RELATIVES"
   7 "DECEASED"
   8 "SOMEPLACE ELSE";

 label define fwpnbevr2
   1 "YES"
   5 "NO";

 label define fwpnbrel2
   1 "YES"
   5 "NO";

 label define fwpnbfos2
   1 "YES"
   5 "NO";

 label define fwpnbad2
   1 "YES"
   5 "NO";

 label define akidagegp131
   1 "UNDER 5 YEARS"
   2 "5-18 YEARS"
   3 "19 OR OLDER";

 label define akidhh131
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define fwpnbsex11
   1 "MALE"
   2 "FEMALE";

 label define fwpnbliv81
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "WITH HIS/HER MOTHER"
   4 "AWAY AT SCHOOL OR COLLEGE"
   5 "LIVING ON OWN"
   6 "LIVING WITH OTHER RELATIVES"
   7 "DECEASED"
   8 "SOMEPLACE ELSE";

 label define e_okakids2
   0 "NONE";

 label define exrelation3
   0 "FORMER COHAB PARTNER"
   1 "FORMER WIFE";

 label define livtogn6
   1 "YES"
   5 "NO";

 label define engagthn6
   1 "YES"
   5 "NO";

 label define marrend6
   1 "DEATH OF WIFE"
   2 "DIVORCE"
   3 "ANNULMENT"
   4 "SEPARATION";

 label define fwpdob_m3
   1 "JANUARY"
   2 "FEBRUARY"
   3 "MARCH"
   4 "APRIL"
   5 "MAY"
   6 "JUNE"
   7 "JULY"
   8 "AUGUST"
   9 "SEPTEMBER"
  10 "OCTOBER"
  11 "NOVEMBER"
  12 "DECEMBER"
  13 "WINTER"
  14 "SPRING"
  15 "SUMMER"
  16 "FALL";

 label define fwpmarbf3
   1 "YES"
   5 "NO";

 label define fwpbiokd3
   1 "YES"
   5 "NO";

 label define kidmar51
   0 "NO"
   1 "YES";

 label define kidagegp51
   1 "UNDER 5 YEARS"
   2 "5-18 YEARS"
   3 "19 OR OLDER";

 label define kidhh51
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define kidliv51
   0 "NO"
   1 "YES";

 label define fwpchsex21
   1 "MALE"
   2 "FEMALE";

 label define fwpchres21
   1 "YES"
   5 "NO";

 label define fwpchlrn21
   1 "DURING THE PREGNANCY"
   2 "AFTER THE CHILD WAS BORN";

 label define fwpchliv201
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "WITH HIS/HER MOTHER"
   4 "AWAY AT SCHOOL OR COLLEGE"
   5 "LIVING ON OWN"
   6 "LIVING WITH OTHER RELATIVES"
   7 "DECEASED"
   8 "PLACED FOR ADOPTION OR ADOPTED"
   9 "PLACED IN FOSTER CARE"
  10 "SOMEPLACE ELSE";

 label define fwpchage21
   1 "LESS THAN 5 YEARS OLD"
   2 "5-18 YEARS OLD"
   3 "19 YEARS OR OLDER";

 label define fwpchleg21
   1 "YES"
   5 "NO";

 label define fwpchhop21
   1 "YES"
   5 "NO";

 label define fwpchevr21
   1 "YES"
   5 "NO";

 label define fwprwant21
   1 "DEFINITELY YES"
   2 "PROBABLY YES"
   3 "PROBABLY NO"
   4 "DEFINITELY NO";

 label define fwpotkid3
   1 "YES"
   5 "NO";

 label define fwpokad3
   1 "YES"
   5 "NO";

 label define fwpnbevr3
   1 "YES"
   5 "NO";

 label define fwpnbrel3
   1 "YES"
   5 "NO";

 label define fwpnbfos3
   1 "YES"
   5 "NO";

 label define fwpnbad3
   1 "YES"
   5 "NO";

 label define e_okakids3
   0 "NONE";

 label define exrelation11
   0 "FORMER COHAB PARTNER"
   1 "FORMER WIFE";

 label define fstunion
   1 "FIRST COHAB"
   2 "FIRST WIFE";

 label define engagthn14
   1 "YES"
   5 "NO";

 label define fwphisp11
   1 "YES"
   5 "NO";

 label define fwprace51
   1 "AMERICAN INDIAN OR ALASKA NATIVE"
   2 "ASIAN"
   3 "NATIVE HAWAIIAN OR OTHER PACIFIC ISLANDER"
   4 "BLACK OR AFRICAN AMERICAN"
   5 "WHITE";

 label define fwprace52
   1 "AMERICAN INDIAN OR ALASKA NATIVE"
   2 "ASIAN"
   3 "NATIVE HAWAIIAN OR OTHER PACIFIC ISLANDER"
   4 "BLACK OR AFRICAN AMERICAN"
   5 "WHITE";

 label define fwprace53
   1 "AMERICAN INDIAN OR ALASKA NATIVE"
   2 "ASIAN"
   3 "NATIVE HAWAIIAN OR OTHER PACIFIC ISLANDER"
   4 "BLACK OR AFRICAN AMERICAN"
   5 "WHITE";

 label define fwprace54
   1 "AMERICAN INDIAN OR ALASKA NATIVE"
   2 "ASIAN"
   3 "NATIVE HAWAIIAN OR OTHER PACIFIC ISLANDER"
   4 "BLACK OR AFRICAN AMERICAN"
   5 "WHITE";

 label define fwpraceb11
   1 "AMERICAN INDIAN OR ALASKA NATIVE"
   2 "ASIAN"
   3 "NATIVE HAWAIIAN OR OTHER PACIFIC ISLANDER"
   4 "BLACK OR AFRICAN AMERICAN"
   5 "WHITE";

 label define fwpmarbf11
   1 "YES"
   5 "NO";

 label define fwpbiokd11
   1 "YES"
   5 "NO";

 label define kidagegp131
   1 "UNDER 5 YEARS"
   2 "5-18 YEARS"
   3 "19 OR OLDER";

 label define kidhh131
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define kidliv131
   0 "NO"
   1 "YES";

 label define fwpchsex101
   1 "MALE"
   2 "FEMALE";

 label define fwpchres101
   1 "YES"
   5 "NO";

 label define fwpchlrn101
   1 "DURING THE PREGNANCY"
   2 "AFTER THE CHILD WAS BORN";

 label define fwpchliv1001
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "WITH HIS/HER MOTHER"
   4 "AWAY AT SCHOOL OR COLLEGE"
   5 "LIVING ON OWN"
   6 "LIVING WITH OTHER RELATIVES"
   7 "DECEASED"
   8 "PLACED FOR ADOPTION OR ADOPTED"
   9 "PLACED IN FOSTER CARE"
  10 "SOMEPLACE ELSE";

 label define fwpchliv1002
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "WITH HIS/HER MOTHER"
   4 "AWAY AT SCHOOL OR COLLEGE"
   5 "LIVING ON OWN"
   6 "LIVING WITH OTHER RELATIVES"
   7 "DECEASED"
   8 "PLACED FOR ADOPTION OR ADOPTED"
   9 "PLACED IN FOSTER CARE"
  10 "SOMEPLACE ELSE";

 label define fwpchage101
   1 "LESS THAN 5 YEARS OLD"
   2 "5-18 YEARS OLD"
   3 "19 YEARS OR OLDER";

 label define fwpchleg101
   1 "YES"
   5 "NO";

 label define fwpchhop101
   1 "YES"
   5 "NO";

 label define fwpchevr101
   1 "YES"
   5 "NO";

 label define fwprwant101
   1 "DEFINITELY YES"
   2 "PROBABLY YES"
   3 "PROBABLY NO"
   4 "DEFINITELY NO";

 label define fwpsoon101
   1 "TOO SOON"
   2 "RIGHT TIME"
   3 "LATER"
   4 "DIDN'T CARE";

 label define kidagegp132
   1 "UNDER 5 YEARS"
   2 "5-18 YEARS"
   3 "19 OR OLDER";

 label define kidhh132
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define kidliv132
   0 "NO"
   1 "YES";

 label define fwpchsex102
   1 "MALE"
   2 "FEMALE";

 label define fwpchres102
   1 "YES"
   5 "NO";

 label define fwpchlrn102
   1 "DURING THE PREGNANCY"
   2 "AFTER THE CHILD WAS BORN";

 label define fwpchliv1011
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "WITH HIS/HER MOTHER"
   4 "AWAY AT SCHOOL OR COLLEGE"
   5 "LIVING ON OWN"
   6 "LIVING WITH OTHER RELATIVES"
   7 "DECEASED"
   8 "PLACED FOR ADOPTION OR ADOPTED"
   9 "PLACED IN FOSTER CARE"
  10 "SOMEPLACE ELSE";

 label define fwpchliv1012
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "WITH HIS/HER MOTHER"
   4 "AWAY AT SCHOOL OR COLLEGE"
   5 "LIVING ON OWN"
   6 "LIVING WITH OTHER RELATIVES"
   7 "DECEASED"
   8 "PLACED FOR ADOPTION OR ADOPTED"
   9 "PLACED IN FOSTER CARE"
  10 "SOMEPLACE ELSE";

 label define fwpchage102
   1 "LESS THAN 5 YEARS OLD"
   2 "5-18 YEARS OLD"
   3 "19 YEARS OR OLDER";

 label define fwpchleg102
   1 "YES"
   5 "NO";

 label define fwpchhop102
   1 "YES"
   5 "NO";

 label define fwpchevr102
   1 "YES"
   5 "NO";

 label define fwprwant102
   1 "DEFINITELY YES"
   2 "PROBABLY YES"
   3 "PROBABLY NO"
   4 "DEFINITELY NO";

 label define fwpsoon102
   1 "TOO SOON"
   2 "RIGHT TIME"
   3 "LATER"
   4 "DIDN'T CARE";

 label define kidagegp133
   1 "UNDER 5 YEARS"
   2 "5-18 YEARS"
   3 "19 OR OLDER";

 label define kidhh133
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define kidliv133
   0 "NO"
   1 "YES";

 label define fwpchsex103
   1 "MALE"
   2 "FEMALE";

 label define multbirt143
   1 "YES"
   5 "NO";

 label define fwpchres103
   1 "YES"
   5 "NO";

 label define fwpchlrn103
   1 "DURING THE PREGNANCY"
   2 "AFTER THE CHILD WAS BORN";

 label define fwpchliv1021
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "WITH HIS/HER MOTHER"
   4 "AWAY AT SCHOOL OR COLLEGE"
   5 "LIVING ON OWN"
   6 "LIVING WITH OTHER RELATIVES"
   7 "DECEASED"
   8 "PLACED FOR ADOPTION OR ADOPTED"
   9 "PLACED IN FOSTER CARE"
  10 "SOMEPLACE ELSE";

 label define fwpchage103
   1 "LESS THAN 5 YEARS OLD"
   2 "5-18 YEARS OLD"
   3 "19 YEARS OR OLDER";

 label define fwpchleg103
   1 "YES"
   5 "NO";

 label define fwpchhop103
   1 "YES"
   5 "NO";

 label define fwprwant103
   1 "DEFINITELY YES"
   2 "PROBABLY YES"
   3 "PROBABLY NO"
   4 "DEFINITELY NO";

 label define kidagegp134
   1 "UNDER 5 YEARS"
   2 "5-18 YEARS"
   3 "19 OR OLDER";

 label define kidhh134
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define kidliv134
   0 "NO"
   1 "YES";

 label define fwpchsex104
   1 "MALE"
   2 "FEMALE";

 label define fwpchres104
   1 "YES"
   5 "NO";

 label define fwpchliv1031
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "WITH HIS/HER MOTHER"
   4 "AWAY AT SCHOOL OR COLLEGE"
   5 "LIVING ON OWN"
   6 "LIVING WITH OTHER RELATIVES"
   7 "DECEASED"
   8 "PLACED FOR ADOPTION OR ADOPTED"
   9 "PLACED IN FOSTER CARE"
  10 "SOMEPLACE ELSE";

 label define fwpchleg104
   1 "YES"
   5 "NO";

 label define fwpchhop104
   1 "YES"
   5 "NO";

 label define kidagegp135
   1 "UNDER 5 YEARS"
   2 "5-18 YEARS"
   3 "19 OR OLDER";

 label define kidhh135
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define kidliv135
   0 "NO"
   1 "YES";

 label define fwpchsex105
   1 "MALE"
   2 "FEMALE";

 label define fwpchres105
   1 "YES"
   5 "NO";

 label define fwpchliv1041
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "WITH HIS/HER MOTHER"
   4 "AWAY AT SCHOOL OR COLLEGE"
   5 "LIVING ON OWN"
   6 "LIVING WITH OTHER RELATIVES"
   7 "DECEASED"
   8 "PLACED FOR ADOPTION OR ADOPTED"
   9 "PLACED IN FOSTER CARE"
  10 "SOMEPLACE ELSE";

 label define fwpchleg105
   1 "YES"
   5 "NO";

 label define fwpchhop105
   1 "YES"
   5 "NO";

 label define fwpotkid11
   1 "YES"
   5 "NO";

 label define fwpokad11
   1 "YES"
   5 "NO";

 label define akidagegp301
   1 "UNDER 5 YEARS"
   2 "5-18 YEARS"
   3 "19 OR OLDER";

 label define akidhh301
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define fwpoksex101
   1 "MALE"
   2 "FEMALE";

 label define fwpokliv801
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "WITH HIS/HER MOTHER"
   4 "AWAY AT SCHOOL OR COLLEGE"
   5 "LIVING ON OWN"
   6 "LIVING WITH OTHER RELATIVES"
   7 "DECEASED"
   8 "SOMEPLACE ELSE";

 label define fwpnbevr11
   1 "YES"
   5 "NO";

 label define fwpnbrel11
   1 "YES"
   5 "NO";

 label define fwpnbfos11
   1 "YES"
   5 "NO";

 label define fwpnbad11
   1 "YES"
   5 "NO";

 label define e_okakids11
   0 "NONE";

 label define otbchil
   1 "YES"
   5 "NO";

 label define otbprobe
   1 "YES"
   5 "NO";

 label define otbchiln
   1 "1 CHILD";

 label define otbsame
   1 "YES"
   5 "NO";

 label define obcsexx
   1 "MALE"
   2 "FEMALE";

 label define obcmliv
   1 "YES"
   5 "NO";

 label define obcknowx
   1 "DURING THE PREGNANCY"
   2 "AFTER THE CHILD WAS BORN";

 label define obclivex01
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "WITH HIS/HER MOTHER"
   4 "AWAY AT SCHOOL OR COLLEGE"
   5 "LIVING ON OWN"
   6 "LIVING WITH OTHER RELATIVES"
   7 "DECEASED"
   8 "PLACED FOR ADOPTION OR ADOPTED"
   9 "PLACED IN FOSTER CARE"
  10 "SOMEPLACE ELSE";

 label define obclivex02
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "WITH HIS/HER MOTHER"
   4 "AWAY AT SCHOOL OR COLLEGE"
   5 "LIVING ON OWN"
   6 "LIVING WITH OTHER RELATIVES"
   7 "DECEASED"
   8 "PLACED FOR ADOPTION OR ADOPTED"
   9 "PLACED IN FOSTER CARE"
  10 "SOMEPLACE ELSE";

 label define obclivex03
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "WITH HIS/HER MOTHER"
   4 "AWAY AT SCHOOL OR COLLEGE"
   5 "LIVING ON OWN"
   6 "LIVING WITH OTHER RELATIVES"
   7 "DECEASED"
   8 "PLACED FOR ADOPTION OR ADOPTED"
   9 "PLACED IN FOSTER CARE"
  10 "SOMEPLACE ELSE";

 label define obcage
   1 "LESS THAN 5 YEARS OLD"
   2 "5-18 YEARS OLD"
   3 "19 YEARS OR OLDER";

 label define kidagegp141
   1 "UNDER 5 YEARS"
   2 "5-18 YEARS"
   3 "19 OR OLDER";

 label define kidliv141
   0 "NO"
   1 "YES";

 label define kidhh141
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define obclawx
   1 "YES"
   5 "NO";

 label define obchopx
   1 "YES"
   5 "NO";

 label define obceverx
   1 "YES"
   5 "NO";

 label define obcrwanx
   1 "DEFINITELY YES"
   2 "PROBABLY YES"
   3 "PROBABLY NO"
   4 "DEFINITELY NO";

 label define obcsoonx
   1 "TOO SOON"
   2 "RIGHT TIME"
   3 "LATER"
   4 "DIDN'T CARE";

 label define obcsexx2
   1 "MALE"
   2 "FEMALE";

 label define multbirt152
   1 "YES"
   5 "NO";

 label define obcmliv2
   1 "YES"
   5 "NO";

 label define obcknowx2
   1 "DURING THE PREGNANCY"
   2 "AFTER THE CHILD WAS BORN";

 label define obclivex11
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "WITH HIS/HER MOTHER"
   4 "AWAY AT SCHOOL OR COLLEGE"
   5 "LIVING ON OWN"
   6 "LIVING WITH OTHER RELATIVES"
   7 "DECEASED"
   8 "PLACED FOR ADOPTION OR ADOPTED"
   9 "PLACED IN FOSTER CARE"
  10 "SOMEPLACE ELSE";

 label define obcage2
   1 "LESS THAN 5 YEARS OLD"
   2 "5-18 YEARS OLD"
   3 "19 YEARS OR OLDER";

 label define kidagegp142
   1 "UNDER 5 YEARS"
   2 "5-18 YEARS"
   3 "19 OR OLDER";

 label define kidliv142
   0 "NO"
   1 "YES";

 label define kidhh142
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define obclawx2
   1 "YES"
   5 "NO";

 label define obchopx2
   1 "YES"
   5 "NO";

 label define obceverx2
   1 "YES"
   5 "NO";

 label define obcrwanx2
   1 "DEFINITELY YES"
   2 "PROBABLY YES"
   3 "PROBABLY NO"
   4 "DEFINITELY NO";

 label define obcsoonx2
   1 "TOO SOON"
   2 "RIGHT TIME"
   3 "LATER"
   4 "DIDN'T CARE";

 label define obcsexx3
   1 "MALE"
   2 "FEMALE";

 label define multbirt153
   1 "YES"
   5 "NO";

 label define obcmliv3
   1 "YES"
   5 "NO";

 label define obcknowx3
   1 "DURING THE PREGNANCY"
   2 "AFTER THE CHILD WAS BORN";

 label define obclivex21
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "WITH HIS/HER MOTHER"
   4 "AWAY AT SCHOOL OR COLLEGE"
   5 "LIVING ON OWN"
   6 "LIVING WITH OTHER RELATIVES"
   7 "DECEASED"
   8 "PLACED FOR ADOPTION OR ADOPTED"
   9 "PLACED IN FOSTER CARE"
  10 "SOMEPLACE ELSE";

 label define obcage3
   1 "LESS THAN 5 YEARS OLD"
   2 "5-18 YEARS OLD"
   3 "19 YEARS OR OLDER";

 label define kidagegp143
   1 "UNDER 5 YEARS"
   2 "5-18 YEARS"
   3 "19 OR OLDER";

 label define kidliv143
   0 "NO"
   1 "YES";

 label define kidhh143
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define obclawx3
   1 "YES"
   5 "NO";

 label define obchopx3
   1 "YES"
   5 "NO";

 label define obceverx3
   1 "YES"
   5 "NO";

 label define obcrwanx3
   1 "DEFINITELY YES"
   2 "PROBABLY YES"
   3 "PROBABLY NO"
   4 "DEFINITELY NO";

 label define obcsoonx3
   1 "TOO SOON"
   2 "RIGHT TIME"
   3 "LATER"
   4 "DIDN'T CARE";

 label define obcsexx4
   1 "MALE"
   2 "FEMALE";

 label define multbirt154
   1 "YES"
   5 "NO";

 label define obcmliv4
   1 "YES"
   5 "NO";

 label define obcknowx4
   1 "DURING THE PREGNANCY"
   2 "AFTER THE CHILD WAS BORN";

 label define obclivex31
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "WITH HIS/HER MOTHER"
   4 "AWAY AT SCHOOL OR COLLEGE"
   5 "LIVING ON OWN"
   6 "LIVING WITH OTHER RELATIVES"
   7 "DECEASED"
   8 "PLACED FOR ADOPTION OR ADOPTED"
   9 "PLACED IN FOSTER CARE"
  10 "SOMEPLACE ELSE";

 label define obcage4
   1 "LESS THAN 5 YEARS OLD"
   2 "5-18 YEARS OLD"
   3 "19 YEARS OR OLDER";

 label define kidagegp144
   1 "UNDER 5 YEARS"
   2 "5-18 YEARS"
   3 "19 OR OLDER";

 label define kidliv144
   0 "NO"
   1 "YES";

 label define kidhh144
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define obclawx4
   1 "YES"
   5 "NO";

 label define obchopx4
   1 "YES"
   5 "NO";

 label define obceverx4
   1 "YES"
   5 "NO";

 label define obcrwanx4
   1 "DEFINITELY YES"
   2 "PROBABLY YES"
   3 "PROBABLY NO"
   4 "DEFINITELY NO";

 label define obcsoonx4
   1 "TOO SOON"
   2 "RIGHT TIME"
   3 "LATER"
   4 "DIDN'T CARE";

 label define obcsexx5
   1 "MALE"
   2 "FEMALE";

 label define obcmliv5
   1 "YES"
   5 "NO";

 label define obcknowx5
   1 "DURING THE PREGNANCY"
   2 "AFTER THE CHILD WAS BORN";

 label define obclivex41
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "WITH HIS/HER MOTHER"
   4 "AWAY AT SCHOOL OR COLLEGE"
   5 "LIVING ON OWN"
   6 "LIVING WITH OTHER RELATIVES"
   7 "DECEASED"
   8 "PLACED FOR ADOPTION OR ADOPTED"
   9 "PLACED IN FOSTER CARE"
  10 "SOMEPLACE ELSE";

 label define obcage5
   1 "LESS THAN 5 YEARS OLD"
   2 "5-18 YEARS OLD"
   3 "19 YEARS OR OLDER";

 label define kidagegp145
   1 "UNDER 5 YEARS"
   2 "5-18 YEARS"
   3 "19 OR OLDER";

 label define kidliv145
   0 "NO"
   1 "YES";

 label define kidhh145
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define obclawx5
   1 "YES"
   5 "NO";

 label define obchopx5
   1 "YES"
   5 "NO";

 label define obceverx5
   1 "YES"
   5 "NO";

 label define obcrwanx5
   1 "DEFINITELY YES"
   2 "PROBABLY YES"
   3 "PROBABLY NO"
   4 "DEFINITELY NO";

 label define obcsoonx5
   1 "TOO SOON"
   2 "RIGHT TIME"
   3 "LATER"
   4 "DIDN'T CARE";

 label define obcsexx6
   1 "MALE"
   2 "FEMALE";

 label define obcmliv6
   1 "YES"
   5 "NO";

 label define obcknowx6
   1 "DURING THE PREGNANCY"
   2 "AFTER THE CHILD WAS BORN";

 label define obclivex51
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "WITH HIS/HER MOTHER"
   4 "AWAY AT SCHOOL OR COLLEGE"
   5 "LIVING ON OWN"
   6 "LIVING WITH OTHER RELATIVES"
   7 "DECEASED"
   8 "PLACED FOR ADOPTION OR ADOPTED"
   9 "PLACED IN FOSTER CARE"
  10 "SOMEPLACE ELSE";

 label define kidagegp146
   1 "UNDER 5 YEARS"
   2 "5-18 YEARS"
   3 "19 OR OLDER";

 label define kidliv146
   0 "NO"
   1 "YES";

 label define kidhh146
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define obclawx6
   1 "YES"
   5 "NO";

 label define obchopx6
   1 "YES"
   5 "NO";

 label define obceverx6
   1 "YES"
   5 "NO";

 label define obcrwanx6
   1 "DEFINITELY YES"
   2 "PROBABLY YES"
   3 "PROBABLY NO"
   4 "DEFINITELY NO";

 label define obcsoonx6
   1 "TOO SOON"
   2 "RIGHT TIME"
   3 "LATER"
   4 "DIDN'T CARE";

 label define otachil
   1 "YES"
   5 "NO";

 label define otachiln
   1 "1 CHILD";

 label define otnbrel
   1 "YES"
   5 "NO";

 label define otnbfos
   1 "YES"
   5 "NO";

 label define otnbad
   1 "YES"
   5 "NO";

 label define f_akids
   0 "NONE";

 label define otnbsex
   1 "MALE"
   2 "FEMALE";

 label define otnbliv1
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "WITH HIS/HER MOTHER"
   4 "AWAY AT SCHOOL OR COLLEGE"
   5 "LIVING ON OWN"
   6 "LIVING WITH OTHER RELATIVES"
   7 "DECEASED"
   8 "SOMEPLACE ELSE";

 label define akidhh321
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define akidagegp321
   1 "UNDER 5 YEARS"
   2 "5-18 YEARS"
   3 "19 OR OLDER";

 label define otnbsex2
   1 "MALE"
   2 "FEMALE";

 label define otnbliv9
   1 "IN THIS HOUSEHOLD FULL-TIME"
   2 "IN THIS HOUSEHOLD PART-TIME"
   3 "WITH HIS/HER MOTHER"
   4 "AWAY AT SCHOOL OR COLLEGE"
   5 "LIVING ON OWN"
   6 "LIVING WITH OTHER RELATIVES"
   7 "DECEASED"
   8 "SOMEPLACE ELSE";

 label define akidhh322
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define akidagegp322
   1 "UNDER 5 YEARS"
   2 "5-18 YEARS"
   3 "19 OR OLDER";

 label define otpreg
   1 "YES"
   5 "NO";

 label define otprgprb
   1 "YES"
   5 "NO";

 label define otprgn
   1 "1 PREGNANCY"
   2 "2 PREGNANCIES";

 label define otprgend
   1 "MISCARRIAGE"
   2 "STILLBIRTH"
   3 "ABORTION";

 label define otmsn
   0 "NONE";

 label define otstn
   0 "NONE";

 label define otabn
   0 "NONE";

 label define totprg
   0 "NONE"
   1 "1 PREGNANCY"
   2 "2 PREGNANCIES"
   3 "3 PREGNANCIES"
   4 "4 PREGNANCIES"
   5 "5 PREGNANCIES";

 label define numlife
  50 "50 OR MORE PARTNERS";

 label define otpregs
   0 "NONE"
   1 "1 PREGNANCY"
   2 "2 PREGNANCIES";

 label define totpregs_c
   0 "NONE"
   1 "1 PREGNANCY"
   2 "2 PREGNANCIES"
   3 "3 PREGNANCIES"
   4 "4 PREGNANCIES"
   5 "5 PREGNANCIES";

 label define totpregs_r
   0 "NONE"
   1 "1 PREGNANCY"
   2 "2 PREGNANCIES"
   3 "3 PREGNANCIES"
   4 "4 PREGNANCIES"
   5 "5 PREGNANCIES";

 label define anykids
   0 "NO"
   1 "YES";

 label define bkidliv
   0 "NO"
   1 "YES";

 label define bkidliv2
   0 "NO"
   1 "YES";

 label define bkidliv3
   0 "NO"
   1 "YES";

 label define bkidliv4
   0 "NO"
   1 "YES";

 label define bkidliv5
   0 "NO"
   1 "YES";

 label define bkidliv6
   0 "NO"
   1 "YES";

 label define bkidliv7
   0 "NO"
   1 "YES";

 label define bkidliv8
   0 "NO"
   1 "YES";

 label define bkidliv9
   0 "NO"
   1 "YES";

 label define bkidliv10
   0 "NO"
   1 "YES";

 label define biosex1
   1 "MALE"
   2 "FEMALE";

 label define biosex2
   1 "MALE"
   2 "FEMALE";

 label define biosex3
   1 "MALE"
   2 "FEMALE";

 label define biosex4
   1 "MALE"
   2 "FEMALE";

 label define biosex5
   1 "MALE"
   2 "FEMALE";

 label define biosex6
   1 "MALE"
   2 "FEMALE";

 label define biosex7
   1 "MALE"
   2 "FEMALE";

 label define biosex8
   1 "MALE"
   2 "FEMALE";

 label define biosex9
   1 "MALE"
   2 "FEMALE";

 label define biosex10
   1 "MALE"
   2 "FEMALE";

 label define biohh1
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define biohh2
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define biohh3
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define biohh4
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define biohh5
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define biohh6
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define biohh7
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define biohh8
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define biohh9
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define biohh10
   1 "IN HH"
   2 "ALIVE, NOT ADOPTED/FOSTER, BUT NOT IN HH"
   3 "DEAD OR ADOPTED/FOSTER OR DK/RF";

 label define biomar1
   0 "NO"
   1 "YES";

 label define biomar2
   0 "NO"
   1 "YES";

 label define biomar3
   0 "NO"
   1 "YES";

 label define biomar4
   0 "NO"
   1 "YES";

 label define biomar5
   0 "NO"
   1 "YES";

 label define biomar6
   0 "NO"
   1 "YES";

 label define biomar7
   0 "NO"
   1 "YES";

 label define biomar8
   0 "NO"
   1 "YES";

 label define biomar9
   0 "NO"
   1 "YES";

 label define biomar10
   0 "NO"
   1 "YES";

 label define biocohb1
   0 "NO"
   1 "YES";

 label define biocohb2
   0 "NO"
   1 "YES";

 label define biocohb3
   0 "NO"
   1 "YES";

 label define biocohb4
   0 "NO"
   1 "YES";

 label define biocohb5
   0 "NO"
   1 "YES";

 label define biocohb6
   0 "NO"
   1 "YES";

 label define biocohb7
   0 "NO"
   1 "YES";

 label define biocohb8
   0 "NO"
   1 "YES";

 label define biocohb9
   0 "NO"
   1 "YES";

 label define biocohb10
   0 "NO"
   1 "YES";

 label define biolrnpg1
   1 "DURING THE PREGNANCY"
   2 "AFTER THE CHILD WAS BORN";

 label define biolrnpg2
   1 "DURING THE PREGNANCY"
   2 "AFTER THE CHILD WAS BORN";

 label define biolrnpg3
   1 "DURING THE PREGNANCY"
   2 "AFTER THE CHILD WAS BORN";

 label define biolrnpg4
   1 "DURING THE PREGNANCY"
   2 "AFTER THE CHILD WAS BORN";

 label define biolrnpg5
   1 "DURING THE PREGNANCY"
   2 "AFTER THE CHILD WAS BORN";

 label define biolrnpg6
   1 "DURING THE PREGNANCY"
   2 "AFTER THE CHILD WAS BORN";

 label define biolrnpg7
   1 "DURING THE PREGNANCY"
   2 "AFTER THE CHILD WAS BORN";

 label define biolrnpg8
   1 "DURING THE PREGNANCY"
   2 "AFTER THE CHILD WAS BORN";

 label define biolrnpg9
   1 "DURING THE PREGNANCY"
   2 "AFTER THE CHILD WAS BORN";

 label define biolrnpg10
   1 "DURING THE PREGNANCY"
   2 "AFTER THE CHILD WAS BORN";

 label define biolgpat1
   1 "YES"
   5 "NO";

 label define biolgpat2
   1 "YES"
   5 "NO";

 label define biolgpat3
   1 "YES"
   5 "NO";

 label define biolgpat4
   1 "YES"
   5 "NO";

 label define biolgpat5
   1 "YES"
   5 "NO";

 label define biolgpat6
   1 "YES"
   5 "NO";

 label define biolgpat7
   1 "YES"
   5 "NO";

 label define biolgpat8
   1 "YES"
   5 "NO";

 label define biolgpat9
   1 "YES"
   5 "NO";

 label define biolgpat10
   1 "YES"
   5 "NO";

 label define biohspat1
   1 "YES"
   5 "NO";

 label define biohspat2
   1 "YES"
   5 "NO";

 label define biohspat3
   1 "YES"
   5 "NO";

 label define biohspat4
   1 "YES"
   5 "NO";

 label define biohspat5
   1 "YES"
   5 "NO";

 label define biohspat6
   1 "YES"
   5 "NO";

 label define biohspat7
   1 "YES"
   5 "NO";

 label define biohspat8
   1 "YES"
   5 "NO";

 label define biohspat9
   1 "YES"
   5 "NO";

 label define biohspat10
   1 "YES"
   5 "NO";

 label define biolvevr1
   1 "YES"
   5 "NO";

 label define biolvevr2
   1 "YES"
   5 "NO";

 label define biolvevr3
   1 "YES"
   5 "NO";

 label define biolvevr4
   1 "YES"
   5 "NO";

 label define biolvevr5
   1 "YES"
   5 "NO";

 label define biolvevr6
   1 "YES"
   5 "NO";

 label define biolvevr7
   1 "YES"
   5 "NO";

 label define biolvevr8
   1 "YES"
   5 "NO";

 label define biolvevr9
   1 "YES"
   5 "NO";

 label define biolvevr10
   1 "YES"
   5 "NO";

 label define biowant1
   1 "DEFINITELY YES"
   2 "PROBABLY YES"
   3 "PROBABLY NO"
   4 "DEFINITELY NO";

 label define biowant2
   1 "DEFINITELY YES"
   2 "PROBABLY YES"
   3 "PROBABLY NO"
   4 "DEFINITELY NO";

 label define biowant3
   1 "DEFINITELY YES"
   2 "PROBABLY YES"
   3 "PROBABLY NO"
   4 "DEFINITELY NO";

 label define biowant4
   1 "DEFINITELY YES"
   2 "PROBABLY YES"
   3 "PROBABLY NO"
   4 "DEFINITELY NO";

 label define biowant5
   1 "DEFINITELY YES"
   2 "PROBABLY YES"
   3 "PROBABLY NO"
   4 "DEFINITELY NO";

 label define biowant6
   1 "DEFINITELY YES"
   2 "PROBABLY YES"
   3 "PROBABLY NO"
   4 "DEFINITELY NO";

 label define biowant7
   1 "DEFINITELY YES"
   2 "PROBABLY YES"
   3 "PROBABLY NO"
   4 "DEFINITELY NO";

 label define biowant8
   1 "DEFINITELY YES"
   2 "PROBABLY YES"
   3 "PROBABLY NO"
   4 "DEFINITELY NO";

 label define biowant9
   1 "DEFINITELY YES"
   2 "PROBABLY YES"
   3 "PROBABLY NO"
   4 "DEFINITELY NO";

 label define biowant10
   1 "DEFINITELY YES"
   2 "PROBABLY YES"
   3 "PROBABLY NO"
   4 "DEFINITELY NO";

 label define biohsoon1
   1 "TOO SOON"
   2 "RIGHT TIME"
   3 "LATER"
   4 "DIDN'T CARE";

 label define biohsoon2
   1 "TOO SOON"
   2 "RIGHT TIME"
   3 "LATER"
   4 "DIDN'T CARE";

 label define biohsoon3
   1 "TOO SOON"
   2 "RIGHT TIME"
   3 "LATER"
   4 "DIDN'T CARE";

 label define biohsoon4
   1 "TOO SOON"
   2 "RIGHT TIME"
   3 "LATER"
   4 "DIDN'T CARE";

 label define biohsoon5
   1 "TOO SOON"
   2 "RIGHT TIME"
   3 "LATER"
   4 "DIDN'T CARE";

 label define biohsoon6
   1 "TOO SOON"
   2 "RIGHT TIME"
   3 "LATER"
   4 "DIDN'T CARE";

 label define biohsoon7
   1 "TOO SOON"
   2 "RIGHT TIME"
   3 "LATER"
   4 "DIDN'T CARE";

 label define biohsoon8
   1 "TOO SOON"
   2 "RIGHT TIME"
   3 "LATER"
   4 "DIDN'T CARE";

 label define biohsoon9
   1 "TOO SOON"
   2 "RIGHT TIME"
   3 "LATER"
   4 "DIDN'T CARE";

 label define biohsoon10
   1 "TOO SOON"
   2 "RIGHT TIME"
   3 "LATER"
   4 "DIDN'T CARE";

 label define crall
   0 "NONE"
   1 "1 CHILD"
   2 "2 CHILDREN"
   3 "3 CHILDREN";

 label define crallu5
   0 "NONE"
   1 "1 CHILD"
   2 "2 CHILDREN";

 label define crall518
   0 "NONE"
   1 "1 CHILD"
   2 "2 CHILDREN"
   3 "3 CHILDREN";

 label define crmalu5
   0 "NONE"
   1 "1 CHILD";

 label define crmal518
   0 "NONE"
   1 "1 CHILD"
   2 "2 CHILDREN";

 label define crfemu5
   0 "NONE"
   1 "1 CHILD";

 label define crfem518
   0 "NONE"
   1 "1 CHILD"
   2 "2 CHILDREN";

 label define ncall
   0 "NONE"
   1 "1 CHILD"
   2 "2 CHILDREN"
   3 "3 CHILDREN";

 label define ncallu5
   0 "NONE"
   1 "1 CHILD";

 label define ncall518
   0 "NONE"
   1 "1 CHILD"
   2 "2 CHILDREN"
   3 "3 CHILDREN";

 label define ncmalu5
   0 "NONE"
   1 "1 CHILD";

 label define ncmal518
   0 "NONE"
   1 "1 CHILD";

 label define ncfemu5
   0 "NONE"
   1 "1 CHILD";

 label define ncfem518
   0 "NONE"
   1 "1 CHILD"
   2 "2 CHILDREN";

 label define croutg
   0 "NOT AT ALL"
   1 "ONCE OR TWICE DURING THE YEAR"
   2 "SEVERAL TIMES DURING THE YEAR"
   3 "1-3 TIMES PER MONTH"
   4 "ABOUT ONCE A WEEK"
   5 "SEVERAL TIMES A WEEK"
   6 "EVERY DAY";

 label define crrelg
   0 "NOT AT ALL"
   1 "ONCE OR TWICE DURING THE YEAR"
   2 "SEVERAL TIMES DURING THE YEAR"
   3 "1-3 TIMES PER MONTH"
   4 "ABOUT ONCE A WEEK"
   5 "SEVERAL TIMES A WEEK"
   6 "EVERY DAY";

 label define crpta
   1 "YES"
   5 "NO";

 label define introga4
   1 "QUALIFIED FOR INTRO - DID NOT RESPOND 96"
  96 "NO CONTACT WITH THESE CHILDREN IN THE LAST 4 WEEKS";

 label define crhelp
   1 "NOT AT ALL"
   2 "LESS THAN ONCE A WEEK"
   3 "ABOUT ONCE A WEEK"
   4 "SEVERAL TIMES A WEEK"
   5 "EVERY DAY (AT LEAST ONCE A DAY)"
   7 "NOT ASCERTAINED";

 label define crtalk
   1 "NOT AT ALL"
   2 "LESS THAN ONCE A WEEK"
   3 "ABOUT ONCE A WEEK"
   4 "SEVERAL TIMES A WEEK"
   5 "EVERY DAY (AT LEAST ONCE A DAY)"
   7 "NOT ASCERTAINED";

 label define crtake
   1 "NOT AT ALL"
   2 "LESS THAN ONCE A WEEK"
   3 "ABOUT ONCE A WEEK"
   4 "SEVERAL TIMES A WEEK"
   5 "EVERY DAY (AT LEAST ONCE A DAY)"
   7 "NOT ASCERTAINED";

 label define crmeal
   1 "NOT AT ALL"
   2 "LESS THAN ONCE A WEEK"
   3 "ABOUT ONCE A WEEK"
   4 "SEVERAL TIMES A WEEK"
   5 "EVERY DAY (AT LEAST ONCE A DAY)"
   7 "NOT ASCERTAINED";

 label define introga9
   1 "QUALIFIED FOR INTRO - DID NOT RESPOND 96"
  96 "NO CONTACT WITH THESE CHILDREN IN THE LAST 4 WEEKS";

 label define crfeed
   1 "NOT AT ALL"
   2 "LESS THAN ONCE A WEEK"
   3 "ABOUT ONCE A WEEK"
   4 "SEVERAL TIMES A WEEK"
   5 "EVERY DAY (AT LEAST ONCE A DAY)";

 label define crbath
   1 "NOT AT ALL"
   2 "LESS THAN ONCE A WEEK"
   3 "ABOUT ONCE A WEEK"
   4 "SEVERAL TIMES A WEEK"
   5 "EVERY DAY (AT LEAST ONCE A DAY)";

 label define crplay
   1 "NOT AT ALL"
   2 "LESS THAN ONCE A WEEK"
   3 "ABOUT ONCE A WEEK"
   4 "SEVERAL TIMES A WEEK"
   5 "EVERY DAY (AT LEAST ONCE A DAY)";

 label define crread
   1 "NOT AT ALL"
   2 "LESS THAN ONCE A WEEK"
   3 "ABOUT ONCE A WEEK"
   4 "SEVERAL TIMES A WEEK"
   5 "EVERY DAY (AT LEAST ONCE A DAY)";

 label define crgood
   1 "A VERY GOOD JOB"
   2 "A GOOD JOB"
   3 "AN OKAY JOB"
   4 "NOT A VERY GOOD JOB"
   5 "A BAD JOB";

 label define ncvisit
   0 "NOT AT ALL"
   1 "ONCE OR TWICE DURING THE YEAR"
   2 "SEVERAL TIMES DURING THE YEAR"
   3 "1-3 TIMES PER MONTH"
   4 "ABOUT ONCE A WEEK"
   5 "SEVERAL TIMES A WEEK"
   6 "EVERY DAY";

 label define ncsatvis
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

 label define ncoutg
   0 "NOT AT ALL"
   1 "ONCE OR TWICE DURING THE YEAR"
   2 "SEVERAL TIMES DURING THE YEAR"
   3 "1-3 TIMES PER MONTH"
   4 "ABOUT ONCE A WEEK"
   5 "SEVERAL TIMES A WEEK"
   6 "EVERY DAY";

 label define ncrelg
   0 "NOT AT ALL"
   1 "ONCE OR TWICE DURING THE YEAR"
   2 "SEVERAL TIMES DURING THE YEAR"
   3 "ONE TO THREE TIMES PER MONTH"
   4 "ABOUT ONCE A WEEK"
   5 "SEVERAL TIMES A WEEK"
   6 "EVERY DAY"
  96 "NO CONTACT IN 12 MONTHS";

 label define ncpta
   1 "YES"
   5 "NO";

 label define introgb6
   1 "QUALIFIED FOR INTRO - DID NOT RESPOND 96"
  96 "NO CONTACT WITH THESE CHILDREN IN THE LAST 4 WEEKS";

 label define nchelp
   1 "NOT AT ALL"
   2 "LESS THAN ONCE A WEEK"
   3 "ABOUT ONCE A WEEK"
   4 "SEVERAL TIMES A WEEK"
   5 "EVERY DAY (AT LEAST ONCE A DAY)";

 label define nctalk
   1 "NOT AT ALL"
   2 "LESS THAN ONCE A WEEK"
   3 "ABOUT ONCE A WEEK"
   4 "SEVERAL TIMES A WEEK"
   5 "EVERY DAY (AT LEAST ONCE A DAY)";

 label define nctake
   1 "NOT AT ALL"
   2 "LESS THAN ONCE A WEEK"
   3 "ABOUT ONCE A WEEK"
   4 "SEVERAL TIMES A WEEK"
   5 "EVERY DAY (AT LEAST ONCE A DAY)";

 label define ncmeal
   1 "NOT AT ALL"
   2 "LESS THAN ONCE A WEEK"
   3 "ABOUT ONCE A WEEK"
   4 "SEVERAL TIMES A WEEK"
   5 "EVERY DAY (AT LEAST ONCE A DAY)";

 label define introgb11
   1 "QUALIFIED FOR INTRO - DID NOT RESPOND 96"
  96 "NO CONTACT WITH THESE CHILDREN IN THE LAST 4 WEEKS";

 label define ncfeed
   1 "NOT AT ALL"
   2 "LESS THAN ONCE A WEEK"
   3 "ABOUT ONCE A WEEK"
   4 "SEVERAL TIMES A WEEK"
   5 "EVERY DAY (AT LEAST ONCE A DAY)"
   7 "NOT ASCERTAINED";

 label define ncbath
   1 "NOT AT ALL"
   2 "LESS THAN ONCE A WEEK"
   3 "ABOUT ONCE A WEEK"
   4 "SEVERAL TIMES A WEEK"
   5 "EVERY DAY (AT LEAST ONCE A DAY)"
   7 "NOT ASCERTAINED";

 label define ncplay
   1 "NOT AT ALL"
   2 "LESS THAN ONCE A WEEK"
   3 "ABOUT ONCE A WEEK"
   4 "SEVERAL TIMES A WEEK"
   5 "EVERY DAY (AT LEAST ONCE A DAY)"
   7 "NOT ASCERTAINED";

 label define ncread
   1 "NOT AT ALL"
   2 "LESS THAN ONCE A WEEK"
   3 "ABOUT ONCE A WEEK"
   4 "SEVERAL TIMES A WEEK"
   5 "EVERY DAY (AT LEAST ONCE A DAY)"
   7 "NOT ASCERTAINED";

 label define ncgood
   1 "A VERY GOOD JOB"
   2 "A GOOD JOB"
   3 "AN OKAY JOB"
   4 "NOT A VERY GOOD JOB"
   5 "A BAD JOB";

 label define ncmoney
   1 "YES"
   5 "NO";

 label define ncreg
   1 "REGULAR BASIS"
   2 "ONCE IN A WHILE";

 label define chsuppyr
   0 "NONE/NOT REPORTED"
   1 "$1-$3,000"
   2 "$3,001-$5,000"
   3 "$5,001-$9,000"
   4 "MORE THAN $9,000";

 label define ncagree
   1 "YES"
   5 "NO";

 label define ncagreen
   0 "NONE"
   1 "1 CHILD"
   2 "2 CHILDREN"
   3 "3 CHILDREN";

 label define rwant
   1 "YES"
   5 "NO";

 label define probwant
   1 "PROBABLY WANT"
   2 "PROBABLY DO NOT WANT"
   3 "IF R INSISTS: DONT KNOW/NOT SURE";

 label define jintend
   1 "YES"
   5 "NO";

 label define jsureint
   1 "VERY SURE"
   2 "SOMEWHAT SURE"
   3 "NOT AT ALL SURE";

 label define jintendn
   0 "NONE"
   1 "1 CHILD"
   2 "2 CHILDREN"
   3 "3 CHILDREN";

 label define jexpectl
   0 "NONE"
   1 "1 CHILD";

 label define jexpects
   0 "NONE"
   1 "1 CHILD";

 label define intend
   1 "DEFINITELY YES"
   2 "PROBABLY YES"
   3 "PROBABLY NO"
   4 "DEFINITELY NO";

 label define intendn
   0 "NONE"
   1 "1 CHILD"
   2 "2 CHILDREN"
   3 "3 CHILDREN";

 label define expectl
   0 "NONE"
   1 "1 CHILD"
   2 "2 CHILDREN"
   3 "3 CHILDREN";

 label define expects
   0 "NONE"
   1 "1 CHILD";

 label define usualcar
   1 "YES"
   5 "NO";

 label define uslplace
   1 "PRIVATE DOCTOR'S OFFICE"
   2 "HMO FACILITY"
   3 "COMMUNITY HEALTH CLINIC, COMMUNITY CLINIC, PUBLIC HEALTH CLINIC"
   4 "FAMILY PLANNING OR PLANNED PARENTHOOD CLINIC"
   5 "EMPLOYER OR COMPANY CLINIC"
   6 "SCHOOL OR SCHOOL-BASED CLINIC"
   7 "HOSPITAL OUTPATIENT CLINIC"
   8 "HOSPITAL EMERGENCY ROOM"
   9 "HOSPITAL REGULAR ROOM"
  10 "URGENT CARE CENTER, URGI-CARE, OR WALK-IN FACILITY"
  20 "SOME OTHER PLACE";

 label define cover12
   1 "YES"
   5 "NO";

 label define numnocov
   1 "1 MONTH"
   2 "2 MONTHS"
   3 "3 MONTHS"
   4 "4 MONTHS"
   5 "5 MONTHS"
   6 "6 MONTHS"
   7 "7 MONTHS"
   8 "8 MONTHS"
   9 "9 MONTHS"
  10 "10 MONTHS"
  11 "11 MONTHS"
  12 "12 MONTHS";

 label define coverhow01
   1 "PRIVATE HEALTH INSURANCE PLAN"
   2 "MEDICAID"
   3 "MEDICARE"
   4 "MEDI-GAP"
   5 "MILITARY HEALTH CARE"
   6 "INDIAN HEALTH SERVICE"
   7 "CHIP (CHILDREN'S HEALTH INSURANCE PROGRAM)"
   8 "SINGLE-SERVICE PLAN (E.G., DENTAL, VISION, PRESCRIPTIONS)"
   9 "STATE-SPONSORED HEALTH PLAN"
  10 "OTHER GOVERNMENT HEALTH CARE";

 label define coverhow02
   1 "PRIVATE HEALTH INSURANCE PLAN"
   2 "MEDICAID"
   3 "MEDICARE"
   4 "MEDI-GAP"
   5 "MILITARY HEALTH CARE"
   6 "INDIAN HEALTH SERVICE"
   7 "CHIP (CHILDREN'S HEALTH INSURANCE PROGRAM)"
   8 "SINGLE-SERVICE PLAN (E.G., DENTAL, VISION, PRESCRIPTIONS)"
   9 "STATE-SPONSORED HEALTH PLAN"
  10 "OTHER GOVERNMENT HEALTH CARE";

 label define coverhow03
   1 "PRIVATE HEALTH INSURANCE PLAN"
   2 "MEDICAID"
   3 "MEDICARE"
   4 "MEDI-GAP"
   5 "MILITARY HEALTH CARE"
   6 "INDIAN HEALTH SERVICE"
   7 "CHIP (CHILDREN'S HEALTH INSURANCE PROGRAM)"
   8 "SINGLE-SERVICE PLAN (E.G., DENTAL, VISION, PRESCRIPTIONS)"
   9 "STATE-SPONSORED HEALTH PLAN"
  10 "OTHER GOVERNMENT HEALTH CARE";

 label define coverhow04
   1 "PRIVATE HEALTH INSURANCE PLAN"
   2 "MEDICAID"
   3 "MEDICARE"
   4 "MEDI-GAP"
   5 "MILITARY HEALTH CARE"
   6 "INDIAN HEALTH SERVICE"
   7 "CHIP (CHILDREN'S HEALTH INSURANCE PROGRAM)"
   8 "SINGLE-SERVICE PLAN (E.G., DENTAL, VISION, PRESCRIPTIONS)"
   9 "STATE-SPONSORED HEALTH PLAN"
  10 "OTHER GOVERNMENT HEALTH CARE";

 label define nowcover01
   1 "PRIVATE HEALTH INSURANCE PLAN"
   2 "MEDICAID"
   3 "MEDICARE"
   4 "MEDI-GAP"
   5 "MILITARY HEALTH CARE"
   6 "INDIAN HEALTH SERVICE"
   7 "CHIP (CHILDREN'S HEALTH INSURANCE PROGRAM)"
   8 "SINGLE-SERVICE PLAN (E.G., DENTAL, VISION, PRESCRIPTIONS)"
   9 "STATE-SPONSORED HEALTH PLAN"
  10 "OTHER GOVERNMENT HEALTH CARE"
  11 "NOT COVERED BY ANY INSURANCE";

 label define nowcover02
   1 "PRIVATE HEALTH INSURANCE PLAN"
   2 "MEDICAID"
   3 "MEDICARE"
   4 "MEDI-GAP"
   5 "MILITARY HEALTH CARE"
   6 "INDIAN HEALTH SERVICE"
   7 "CHIP (CHILDREN'S HEALTH INSURANCE PROGRAM)"
   8 "SINGLE-SERVICE PLAN (E.G., DENTAL, VISION, PRESCRIPTIONS)"
   9 "STATE-SPONSORED HEALTH PLAN"
  10 "OTHER GOVERNMENT HEALTH CARE"
  11 "NOT COVERED BY ANY INSURANCE";

 label define nowcover03
   1 "PRIVATE HEALTH INSURANCE PLAN"
   2 "MEDICAID"
   3 "MEDICARE"
   4 "MEDI-GAP"
   5 "MILITARY HEALTH CARE"
   6 "INDIAN HEALTH SERVICE"
   7 "CHIP (CHILDREN'S HEALTH INSURANCE PROGRAM)"
   8 "SINGLE-SERVICE PLAN (E.G., DENTAL, VISION, PRESCRIPTIONS)"
   9 "STATE-SPONSORED HEALTH PLAN"
  10 "OTHER GOVERNMENT HEALTH CARE"
  11 "NOT COVERED BY ANY INSURANCE";

 label define gofpcwgf
   1 "YES"
   5 "NO";

 label define whengogf
   1 "IN THE LAST 12 MONTHS"
   2 "MORE THAN 12 MONTHS AGO";

 label define yougofpc
   1 "YES"
   5 "NO";

 label define whengofp
   1 "IN THE LAST 12 MONTHS"
   2 "MORE THAN 12 MONTHS AGO";

 label define youfpsvc1
   1 "PHYSICAL EXAM"
   2 "BIRTH CONTROL COUNSELING OR METHODS, INCLUDING CONDOMS"
   3 "TESTING OR TREATMENT FOR SEXUALLY TRANSMITTED INFECTION OTHER THAN HIV"
   4 "HIV TESTING"
   5 "ABORTION ADVICE OR COUNSELING"
   6 "OTHER";

 label define youfpsvc2
   1 "PHYSICAL EXAM"
   2 "BIRTH CONTROL COUNSELING OR METHODS, INCLUDING CONDOMS"
   3 "TESTING OR TREATMENT FOR SEXUALLY TRANSMITTED INFECTION OTHER THAN HIV"
   4 "HIV TESTING"
   5 "ABORTION ADVICE OR COUNSELING"
   6 "OTHER";

 label define youfpsvc3
   1 "PHYSICAL EXAM"
   2 "BIRTH CONTROL COUNSELING OR METHODS, INCLUDING CONDOMS"
   3 "TESTING OR TREATMENT FOR SEXUALLY TRANSMITTED INFECTION OTHER THAN HIV"
   4 "HIV TESTING"
   5 "ABORTION ADVICE OR COUNSELING"
   6 "OTHER";

 label define youfpsvc4
   1 "PHYSICAL EXAM"
   2 "BIRTH CONTROL COUNSELING OR METHODS, INCLUDING CONDOMS"
   3 "TESTING OR TREATMENT FOR SEXUALLY TRANSMITTED INFECTION OTHER THAN HIV"
   4 "HIV TESTING"
   5 "ABORTION ADVICE OR COUNSELING"
   6 "OTHER";

 label define youfpsvc5
   1 "PHYSICAL EXAM"
   2 "BIRTH CONTROL COUNSELING OR METHODS, INCLUDING CONDOMS"
   3 "TESTING OR TREATMENT FOR SEXUALLY TRANSMITTED INFECTION OTHER THAN HIV"
   4 "HIV TESTING"
   5 "ABORTION ADVICE OR COUNSELING"
   6 "OTHER";

 label define limited
   1 "YES"
   5 "NO";

 label define equipmnt
   1 "YES"
   5 "NO";

 label define physexam
   1 "YES"
   5 "NO";

 label define testichk
   1 "YES"
   5 "NO";

 label define bcadvice
   1 "YES"
   5 "NO";

 label define steradvi
   1 "YES"
   5 "NO";

 label define stdadvic
   1 "YES"
   5 "NO";

 label define hivadvic
   1 "YES"
   5 "NO";

 label define onevisit
   1 "AT A SINGLE VISIT"
   2 "MORE THAN 1 VISIT";

 label define numvisit
   2 "2 VISITS"
   3 "3 VISITS";

 label define placevis01
   1 "PRIVATE DOCTOR'S OFFICE"
   2 "HMO FACILITY"
   3 "COMMUNITY HEALTH CLINIC, COMMUNITY CLINIC, PUBLIC HEALTH CLINIC"
   4 "FAMILY PLANNING OR PLANNED PARENTHOOD CLINIC"
   5 "EMPLOYER OR COMPANY CLINIC"
   6 "SCHOOL OR SCHOOL-BASED CLINIC"
   7 "HOSPITAL OUTPATIENT CLINIC"
   8 "HOSPITAL EMERGENCY ROOM"
   9 "HOSPITAL REGULAR ROOM"
  10 "URGENT CARE CENTER, URGI-CARE, OR WALK-IN FACILITY"
  20 "SOME OTHER PLACE";

 label define placevis02
   1 "PRIVATE DOCTOR'S OFFICE"
   2 "HMO FACILITY"
   3 "COMMUNITY HEALTH CLINIC, COMMUNITY CLINIC, PUBLIC HEALTH CLINIC"
   4 "FAMILY PLANNING OR PLANNED PARENTHOOD CLINIC"
   5 "EMPLOYER OR COMPANY CLINIC"
   6 "SCHOOL OR SCHOOL-BASED CLINIC"
   7 "HOSPITAL OUTPATIENT CLINIC"
   8 "HOSPITAL EMERGENCY ROOM"
   9 "HOSPITAL REGULAR ROOM"
  10 "URGENT CARE CENTER, URGI-CARE, OR WALK-IN FACILITY"
  20 "SOME OTHER PLACE";

 label define placevis03
   1 "PRIVATE DOCTOR'S OFFICE"
   2 "HMO FACILITY"
   3 "COMMUNITY HEALTH CLINIC, COMMUNITY CLINIC, PUBLIC HEALTH CLINIC"
   4 "FAMILY PLANNING OR PLANNED PARENTHOOD CLINIC"
   5 "EMPLOYER OR COMPANY CLINIC"
   6 "SCHOOL OR SCHOOL-BASED CLINIC"
   7 "HOSPITAL OUTPATIENT CLINIC"
   8 "HOSPITAL EMERGENCY ROOM"
   9 "HOSPITAL REGULAR ROOM"
  10 "URGENT CARE CENTER, URGI-CARE, OR WALK-IN FACILITY"
  20 "SOME OTHER PLACE";

 label define placevis04
   1 "PRIVATE DOCTOR'S OFFICE"
   2 "HMO FACILITY"
   3 "COMMUNITY HEALTH CLINIC, COMMUNITY CLINIC, PUBLIC HEALTH CLINIC"
   4 "FAMILY PLANNING OR PLANNED PARENTHOOD CLINIC"
   5 "EMPLOYER OR COMPANY CLINIC"
   6 "SCHOOL OR SCHOOL-BASED CLINIC"
   7 "HOSPITAL OUTPATIENT CLINIC"
   8 "HOSPITAL EMERGENCY ROOM"
   9 "HOSPITAL REGULAR ROOM"
  10 "URGENT CARE CENTER, URGI-CARE, OR WALK-IN FACILITY"
  20 "SOME OTHER PLACE";

 label define svcpay1
   1 "INSURANCE"
   2 "CO-PAYMENT OR OUT-OF-POCKET PAYMENT"
   3 "MEDICAID"
   4 "NO PAYMENT REQUIRED"
   5 "SOME OTHER WAY";

 label define svcpay2
   1 "INSURANCE"
   2 "CO-PAYMENT OR OUT-OF-POCKET PAYMENT"
   3 "MEDICAID"
   4 "NO PAYMENT REQUIRED"
   5 "SOME OTHER WAY";

 label define svcpay3
   1 "INSURANCE"
   2 "CO-PAYMENT OR OUT-OF-POCKET PAYMENT"
   3 "MEDICAID"
   4 "NO PAYMENT REQUIRED"
   5 "SOME OTHER WAY";

 label define infhelp
   1 "YES"
   5 "NO";

 label define infsvcs1
   1 "ADVICE"
   2 "INFERTILITY TESTING"
   3 "DRUGS TO IMPROVE OVULATION"
   4 "SURGERY TO CORRECT BLOCKED TUBES"
   5 "ARTIFICIAL INSEMINATION"
   6 "TREATMENT FOR VARICOCELE"
   7 "OTHER TYPES OF MEDICAL HELP";

 label define infsvcs2
   1 "ADVICE"
   2 "INFERTILITY TESTING"
   3 "DRUGS TO IMPROVE OVULATION"
   4 "SURGERY TO CORRECT BLOCKED TUBES"
   5 "ARTIFICIAL INSEMINATION"
   6 "TREATMENT FOR VARICOCELE"
   7 "OTHER TYPES OF MEDICAL HELP";

 label define infsvcs3
   1 "ADVICE"
   2 "INFERTILITY TESTING"
   3 "DRUGS TO IMPROVE OVULATION"
   4 "SURGERY TO CORRECT BLOCKED TUBES"
   5 "ARTIFICIAL INSEMINATION"
   6 "TREATMENT FOR VARICOCELE"
   7 "OTHER TYPES OF MEDICAL HELP";

 label define infsvcs4
   1 "ADVICE"
   2 "INFERTILITY TESTING"
   3 "DRUGS TO IMPROVE OVULATION"
   4 "SURGERY TO CORRECT BLOCKED TUBES"
   5 "ARTIFICIAL INSEMINATION"
   6 "TREATMENT FOR VARICOCELE"
   7 "OTHER TYPES OF MEDICAL HELP";

 label define infsvcs5
   1 "ADVICE"
   2 "INFERTILITY TESTING"
   3 "DRUGS TO IMPROVE OVULATION"
   4 "SURGERY TO CORRECT BLOCKED TUBES"
   5 "ARTIFICIAL INSEMINATION"
   6 "TREATMENT FOR VARICOCELE"
   7 "OTHER TYPES OF MEDICAL HELP";

 label define infsvcs6
   1 "ADVICE"
   2 "INFERTILITY TESTING"
   3 "DRUGS TO IMPROVE OVULATION"
   4 "SURGERY TO CORRECT BLOCKED TUBES"
   5 "ARTIFICIAL INSEMINATION"
   6 "TREATMENT FOR VARICOCELE"
   7 "OTHER TYPES OF MEDICAL HELP";

 label define inftest
   1 "YOU"
   2 "HER"
   3 "OR BOTH OF YOU";

 label define whoinsem
   1 "YOU ONLY"
   2 "SOME OTHER DONOR ONLY"
   3 "BOTH";

 label define infhlpnw
   1 "YES"
   5 "NO";

 label define infrthis1
   1 "SPERM OR SEMEN PROBLEMS"
   2 "VARICOCELE"
   3 "OTHER"
   4 "NONE OF THE ABOVE";

 label define infrthis2
   1 "SPERM OR SEMEN PROBLEMS"
   2 "VARICOCELE"
   3 "OTHER"
   4 "NONE OF THE ABOVE";

 label define donbld85
   1 "YES"
   5 "NO";

 label define hivtest
   1 "YES"
   5 "NO";

 label define plchiv
   1 "PRIVATE DOCTOR'S OFFICE"
   2 "HMO FACILITY"
   3 "COMMUNITY HEALTH CLINIC, COMMUNITY CLINIC, PUBLIC HEALTH CLINIC"
   4 "FAMILY PLANNING OR PLANNED PARENTHOOD CLINIC"
   5 "EMPLOYER OR COMPANY CLINIC"
   6 "SCHOOL OR SCHOOL-BASED CLINIC"
   7 "HOSPITAL OUTPATIENT CLINIC"
   8 "HOSPITAL EMERGENCY ROOM"
   9 "HOSPITAL REGULAR ROOM"
  10 "URGENT CARE CENTER, URGI-CARE, OR WALK-IN FACILITY"
  11 "YOUR WORKSITE"
  12 "YOUR HOME"
  20 "SOME OTHER PLACE";

 label define hivtst1
   1 "FOR A HOSPITALIZATION OR SURGICAL PROCEDURE"
   2 "TO APPLY FOR HEALTH OR LIFE INSURANCE"
   3 "JUST TO FIND OUT IF YOU WERE INFECTED"
   4 "BECAUSE OF A REFERRAL BY A DOCTOR"
   5 "TO APPLY FOR A MARRIAGE LICENSE"
   6 "OR FOR SOME OTHER REASON";

 label define hivtst2
   1 "FOR A HOSPITALIZATION OR SURGICAL PROCEDURE"
   2 "TO APPLY FOR HEALTH OR LIFE INSURANCE"
   3 "JUST TO FIND OUT IF YOU WERE INFECTED"
   4 "BECAUSE OF A REFERRAL BY A DOCTOR"
   5 "TO APPLY FOR A MARRIAGE LICENSE"
   6 "OR FOR SOME OTHER REASON";

 label define hivtst3
   1 "FOR A HOSPITALIZATION OR SURGICAL PROCEDURE"
   2 "TO APPLY FOR HEALTH OR LIFE INSURANCE"
   3 "JUST TO FIND OUT IF YOU WERE INFECTED"
   4 "BECAUSE OF A REFERRAL BY A DOCTOR"
   5 "TO APPLY FOR A MARRIAGE LICENSE"
   6 "OR FOR SOME OTHER REASON";

 label define hivtst4
   1 "FOR A HOSPITALIZATION OR SURGICAL PROCEDURE"
   2 "TO APPLY FOR HEALTH OR LIFE INSURANCE"
   3 "JUST TO FIND OUT IF YOU WERE INFECTED"
   4 "BECAUSE OF A REFERRAL BY A DOCTOR"
   5 "TO APPLY FOR A MARRIAGE LICENSE"
   6 "OR FOR SOME OTHER REASON";

 label define talkdoct
   1 "YES"
   5 "NO";

 label define aidstalk01
   1 "HOW HIV/AIDS IS TRANSMITTED"
   2 "HOW TO PREVENT TRANSMISSION OF HIV/AIDS"
   3 "OTHER SEXUALLY TRANSMITTED DISEASES LIKE GONORRHEA, SYPHILIS, OR HERPES"
   4 "THE CORRECT USE OF CONDOMS"
   5 "NEEDLE CLEANING/USING CLEAN NEEDLES"
   6 "DANGERS OF NEEDLE SHARING"
   7 "ABSTINENCE FROM SEX (NOT HAVING SEX)"
   8 "BIRTH CONTROL METHODS"
   9 "SAFE SEX PRACTICES"
  10 "OTHER";

 label define aidstalk02
   1 "HOW HIV/AIDS IS TRANSMITTED"
   2 "HOW TO PREVENT TRANSMISSION OF HIV/AIDS"
   3 "OTHER SEXUALLY TRANSMITTED DISEASES LIKE GONORRHEA, SYPHILIS, OR HERPES"
   4 "THE CORRECT USE OF CONDOMS"
   5 "NEEDLE CLEANING/USING CLEAN NEEDLES"
   6 "DANGERS OF NEEDLE SHARING"
   7 "ABSTINENCE FROM SEX (NOT HAVING SEX)"
   8 "BIRTH CONTROL METHODS"
   9 "SAFE SEX PRACTICES"
  10 "OTHER";

 label define aidstalk03
   1 "HOW HIV/AIDS IS TRANSMITTED"
   2 "HOW TO PREVENT TRANSMISSION OF HIV/AIDS"
   3 "OTHER SEXUALLY TRANSMITTED DISEASES LIKE GONORRHEA, SYPHILIS, OR HERPES"
   4 "THE CORRECT USE OF CONDOMS"
   5 "NEEDLE CLEANING/USING CLEAN NEEDLES"
   6 "DANGERS OF NEEDLE SHARING"
   7 "ABSTINENCE FROM SEX (NOT HAVING SEX)"
   8 "BIRTH CONTROL METHODS"
   9 "SAFE SEX PRACTICES"
  10 "OTHER";

 label define aidstalk04
   1 "HOW HIV/AIDS IS TRANSMITTED"
   2 "HOW TO PREVENT TRANSMISSION OF HIV/AIDS"
   3 "OTHER SEXUALLY TRANSMITTED DISEASES LIKE GONORRHEA, SYPHILIS, OR HERPES"
   4 "THE CORRECT USE OF CONDOMS"
   5 "NEEDLE CLEANING/USING CLEAN NEEDLES"
   6 "DANGERS OF NEEDLE SHARING"
   7 "ABSTINENCE FROM SEX (NOT HAVING SEX)"
   8 "BIRTH CONTROL METHODS"
   9 "SAFE SEX PRACTICES"
  10 "OTHER";

 label define aidstalk05
   1 "HOW HIV/AIDS IS TRANSMITTED"
   2 "HOW TO PREVENT TRANSMISSION OF HIV/AIDS"
   3 "OTHER SEXUALLY TRANSMITTED DISEASES LIKE GONORRHEA, SYPHILIS, OR HERPES"
   4 "THE CORRECT USE OF CONDOMS"
   5 "NEEDLE CLEANING/USING CLEAN NEEDLES"
   6 "DANGERS OF NEEDLE SHARING"
   7 "ABSTINENCE FROM SEX (NOT HAVING SEX)"
   8 "BIRTH CONTROL METHODS"
   9 "SAFE SEX PRACTICES"
  10 "OTHER";

 label define aidstalk06
   1 "HOW HIV/AIDS IS TRANSMITTED"
   2 "HOW TO PREVENT TRANSMISSION OF HIV/AIDS"
   3 "OTHER SEXUALLY TRANSMITTED DISEASES LIKE GONORRHEA, SYPHILIS, OR HERPES"
   4 "THE CORRECT USE OF CONDOMS"
   5 "NEEDLE CLEANING/USING CLEAN NEEDLES"
   6 "DANGERS OF NEEDLE SHARING"
   7 "ABSTINENCE FROM SEX (NOT HAVING SEX)"
   8 "BIRTH CONTROL METHODS"
   9 "SAFE SEX PRACTICES"
  10 "OTHER";

 label define aidstalk07
   1 "HOW HIV/AIDS IS TRANSMITTED"
   2 "HOW TO PREVENT TRANSMISSION OF HIV/AIDS"
   3 "OTHER SEXUALLY TRANSMITTED DISEASES LIKE GONORRHEA, SYPHILIS, OR HERPES"
   4 "THE CORRECT USE OF CONDOMS"
   5 "NEEDLE CLEANING/USING CLEAN NEEDLES"
   6 "DANGERS OF NEEDLE SHARING"
   7 "ABSTINENCE FROM SEX (NOT HAVING SEX)"
   8 "BIRTH CONTROL METHODS"
   9 "SAFE SEX PRACTICES"
  10 "OTHER";

 label define aidstalk08
   1 "HOW HIV/AIDS IS TRANSMITTED"
   2 "HOW TO PREVENT TRANSMISSION OF HIV/AIDS"
   3 "OTHER SEXUALLY TRANSMITTED DISEASES LIKE GONORRHEA, SYPHILIS, OR HERPES"
   4 "THE CORRECT USE OF CONDOMS"
   5 "NEEDLE CLEANING/USING CLEAN NEEDLES"
   6 "DANGERS OF NEEDLE SHARING"
   7 "ABSTINENCE FROM SEX (NOT HAVING SEX)"
   8 "BIRTH CONTROL METHODS"
   9 "SAFE SEX PRACTICES"
  10 "OTHER";

 label define aidstalk09
   1 "HOW HIV/AIDS IS TRANSMITTED"
   2 "HOW TO PREVENT TRANSMISSION OF HIV/AIDS"
   3 "OTHER SEXUALLY TRANSMITTED DISEASES LIKE GONORRHEA, SYPHILIS, OR HERPES"
   4 "THE CORRECT USE OF CONDOMS"
   5 "NEEDLE CLEANING/USING CLEAN NEEDLES"
   6 "DANGERS OF NEEDLE SHARING"
   7 "ABSTINENCE FROM SEX (NOT HAVING SEX)"
   8 "BIRTH CONTROL METHODS"
   9 "SAFE SEX PRACTICES"
  10 "OTHER";

 label define aidstalk10
   1 "HOW HIV/AIDS IS TRANSMITTED"
   2 "HOW TO PREVENT TRANSMISSION OF HIV/AIDS"
   3 "OTHER SEXUALLY TRANSMITTED DISEASES LIKE GONORRHEA, SYPHILIS, OR HERPES"
   4 "THE CORRECT USE OF CONDOMS"
   5 "NEEDLE CLEANING/USING CLEAN NEEDLES"
   6 "DANGERS OF NEEDLE SHARING"
   7 "ABSTINENCE FROM SEX (NOT HAVING SEX)"
   8 "BIRTH CONTROL METHODS"
   9 "SAFE SEX PRACTICES"
  10 "OTHER";

 label define retrovir
   1 "DEFINITELY TRUE"
   2 "PROBABLY TRUE"
   3 "PROBABLY FALSE"
   4 "DEFINITELY FALSE"
   5 "DON T KNOW IF TRUE OR FALSE";

 label define sameadd
   1 "YES"
   5 "NO";

 label define cntry00
   1 "YES"
   5 "NO";

 label define brnout
   1 "YES"
   5 "NO";

 label define paydu
   1 "OWNED OR BEING BOUGHT BY YOU OR SOMEONE IN YOUR HOUSEHOLD"
   2 "RENTED";

 label define relraisd
   1 "NO RELIGION"
   2 "CATHOLIC"
   3 "BAPTIST/SOUTHERN BAPTIST"
   4 "METHODIST, LUTHERAN, PRESBYTERIAN, EPISCOPAL, CHURCH OF CHRIST"
   5 "FUNDAMENTALIST PROTESTANT"
   6 "OTHER PROTESTANT DENOMINATION"
   7 "PROTESTANT-NO SPECIFIC DENOMINATION"
   8 "OTHER NON-CHRISTIAN RELIGION";

 label define attnd14
   1 "MORE THAN ONCE A WEEK"
   2 "ONCE A WEEK"
   3 "1-3 TIMES PER MONTH"
   4 "LESS THAN ONCE A MONTH"
   5 "NEVER";

 label define relcurr
   1 "NO RELIGION"
   2 "CATHOLIC"
   3 "BAPTIST/SOUTHERN BAPTIST"
   4 "METHODIST, LUTHERAN, PRESBYTERIAN, EPISCOPAL, CHURCH OF CHRIST"
   5 "FUNDAMENTALIST PROTESTANT"
   6 "OTHER PROTESTANT DENOMINATION"
   7 "PROTESTANT-NO SPECIFIC DENOMINATION"
   8 "OTHER NON-CHRISTIAN RELIGION";

 label define fundam
   1 "A BORN AGAIN CHRISTIAN"
   2 "A CHARISMATIC"
   3 "AN EVANGELICAL"
   4 "A FUNDAMENTALIST"
   5 "NONE OF THE ABOVE";

 label define reldlife
   1 "VERY IMPORTANT"
   2 "SOMEWHAT IMPORTANT"
   3 "NOT IMPORTANT";

 label define attndnow
   1 "MORE THAN ONCE A WEEK"
   2 "ONCE A WEEK"
   3 "1-3 TIMES PER MONTH"
   4 "LESS THAN ONCE A MONTH"
   5 "NEVER";

 label define milsvc
   1 "YES"
   5 "NO";

 label define startmil
   1 "1985 OR EARLIER"
   2 "1986-1990"
   3 "1991-1995"
   4 "1996 OR LATER";

 label define endmil
   1 "1985 OR EARLIER"
   2 "1986-1990"
   3 "1991-1995"
   4 "1996 OR LATER";

 label define evwrk6mo
   1 "YES"
   5 "NO";

 label define evrntwrk
   1 "YES"
   5 "NO";

 label define wrk12mos
   0 "NO MONTHS"
   1 "1 MONTH"
   2 "2 MONTHS"
   3 "3 MONTHS"
   4 "4 MONTHS"
   5 "5 MONTHS"
   6 "6 MONTHS"
   7 "7 MONTHS"
   8 "8 MONTHS"
   9 "9 MONTHS"
  10 "10 MONTHS"
  11 "11 MONTHS"
  12 "12 MONTHS";

 label define ftpt12mos
   1 "FULL-TIME"
   2 "PART-TIME"
   3 "SOME OF EACH";

 label define dolastwk1
   1 "WORKING"
   2 "NOT WORKING AT JOB DUE TO TEMPORARY ILLNESS, VACATION, STRIKE, ETC./PATERNITY OR FAMILY LEAVE"
   3 "UNEMPLOYED, LAID OFF, OR LOOKING FOR WORK"
   4 "KEEPING HOUSE/TAKING CARE OF FAMILY"
   5 "GOING TO SCHOOL"
   6 "ON PERMANENT DISABILITY/SOMETHING ELSE";

 label define dolastwk2
   1 "WORKING"
   2 "NOT WORKING AT JOB DUE TO TEMPORARY ILLNESS, VACATION, STRIKE, ETC./PATERNITY OR FAMILY LEAVE"
   3 "UNEMPLOYED, LAID OFF, OR LOOKING FOR WORK"
   4 "KEEPING HOUSE/TAKING CARE OF FAMILY"
   5 "GOING TO SCHOOL"
   6 "ON PERMANENT DISABILITY/SOMETHING ELSE";

 label define dolastwk3
   1 "WORKING"
   2 "NOT WORKING AT JOB DUE TO TEMPORARY ILLNESS, VACATION, STRIKE, ETC./PATERNITY OR FAMILY LEAVE"
   3 "UNEMPLOYED, LAID OFF, OR LOOKING FOR WORK"
   4 "KEEPING HOUSE/TAKING CARE OF FAMILY"
   5 "GOING TO SCHOOL"
   6 "ON PERMANENT DISABILITY/SOMETHING ELSE";

 label define dolastwk4
   1 "WORKING"
   2 "NOT WORKING AT JOB DUE TO TEMPORARY ILLNESS, VACATION, STRIKE, ETC./PATERNITY OR FAMILY LEAVE"
   3 "UNEMPLOYED, LAID OFF, OR LOOKING FOR WORK"
   4 "KEEPING HOUSE/TAKING CARE OF FAMILY"
   5 "GOING TO SCHOOL"
   6 "ON PERMANENT DISABILITY/SOMETHING ELSE";

 label define dolastwk5
   1 "WORKING"
   2 "NOT WORKING AT JOB DUE TO TEMPORARY ILLNESS, VACATION, STRIKE, ETC./PATERNITY OR FAMILY LEAVE"
   3 "UNEMPLOYED, LAID OFF, OR LOOKING FOR WORK"
   4 "KEEPING HOUSE/TAKING CARE OF FAMILY"
   5 "GOING TO SCHOOL"
   6 "ON PERMANENT DISABILITY/SOMETHING ELSE";

 label define dolastwk6
   1 "WORKING"
   2 "NOT WORKING AT JOB DUE TO TEMPORARY ILLNESS, VACATION, STRIKE, ETC./PATERNITY OR FAMILY LEAVE"
   3 "UNEMPLOYED, LAID OFF, OR LOOKING FOR WORK"
   4 "KEEPING HOUSE/TAKING CARE OF FAMILY"
   5 "GOING TO SCHOOL"
   6 "ON PERMANENT DISABILITY/SOMETHING ELSE";

 label define rwrkst
   1 "YES"
   5 "NO";

 label define everwork
   1 "YES"
   5 "NO";

 label define rpayjob
   1 "YES"
   5 "NO";

 label define rnumjob
   0 "NO JOBS"
   1 "1 JOB"
   2 "2 JOBS";

 label define rftptx
   1 "FULL-TIME"
   2 "PART-TIME"
   3 "SOME OF EACH";

 label define rearnty
   1 "YES"
   5 "NO";

 label define splstwk1
   1 "WORKING"
   2 "NOT WORKING AT JOB DUE TO TEMPORARY ILLNESS, VACATION, STRIKE, PATERNITY/FAMILY LEAVE, ETC."
   3 "UNEMPLOYED, LAID OFF, OR LOOKING FOR WORK"
   4 "KEEPING HOUSE OR TAKING CARE OF FAMILY"
   5 "OTHER";

 label define splstwk2
   1 "WORKING"
   2 "NOT WORKING AT JOB DUE TO TEMPORARY ILLNESS, VACATION, STRIKE, PATERNITY/FAMILY LEAVE, ETC."
   3 "UNEMPLOYED, LAID OFF, OR LOOKING FOR WORK"
   4 "KEEPING HOUSE OR TAKING CARE OF FAMILY"
   5 "OTHER";

 label define splstwk3
   1 "WORKING"
   2 "NOT WORKING AT JOB DUE TO TEMPORARY ILLNESS, VACATION, STRIKE, PATERNITY/FAMILY LEAVE, ETC."
   3 "UNEMPLOYED, LAID OFF, OR LOOKING FOR WORK"
   4 "KEEPING HOUSE OR TAKING CARE OF FAMILY"
   5 "OTHER";

 label define splstwk4
   1 "WORKING"
   2 "NOT WORKING AT JOB DUE TO TEMPORARY ILLNESS, VACATION, STRIKE, PATERNITY/FAMILY LEAVE, ETC."
   3 "UNEMPLOYED, LAID OFF, OR LOOKING FOR WORK"
   4 "KEEPING HOUSE OR TAKING CARE OF FAMILY"
   5 "OTHER";

 label define splstwk5
   1 "WORKING"
   2 "NOT WORKING AT JOB DUE TO TEMPORARY ILLNESS, VACATION, STRIKE, PATERNITY/FAMILY LEAVE, ETC."
   3 "UNEMPLOYED, LAID OFF, OR LOOKING FOR WORK"
   4 "KEEPING HOUSE OR TAKING CARE OF FAMILY"
   5 "OTHER";

 label define spwrkst
   1 "YES"
   5 "NO";

 label define sppayjob
   1 "YES"
   5 "NO";

 label define spnumjob
   0 "NO JOBS"
   1 "1 JOB"
   2 "2 JOBS";

 label define spftptx
   1 "FULL-TIME"
   2 "PART-TIME"
   3 "SOME OF EACH";

 label define spearnty
   1 "YES"
   5 "NO";

 label define better
   1 "STRONGLY AGREE"
   2 "AGREE"
   3 "DISAGREE"
   4 "STRONGLY DISAGREE"
   5 "IF R INSISTS: NEITHER AGREE NOR DISAGREE";

 label define staytog
   1 "STRONGLY AGREE"
   2 "AGREE"
   3 "DISAGREE"
   4 "STRONGLY DISAGREE"
   5 "IF R INSISTS: NEITHER AGREE NOR DISAGREE";

 label define samesex
   1 "STRONGLY AGREE"
   2 "AGREE"
   3 "DISAGREE"
   4 "STRONGLY DISAGREE"
   5 "IF R INSISTS: NEITHER AGREE NOR DISAGREE";

 label define anyact
   1 "STRONGLY AGREE"
   2 "AGREE"
   3 "DISAGREE"
   4 "STRONGLY DISAGREE"
   5 "IF R INSISTS: NEITHER AGREE NOR DISAGREE";

 label define sxok18
   1 "STRONGLY AGREE"
   2 "AGREE"
   3 "DISAGREE"
   4 "STRONGLY DISAGREE"
   5 "IF R INSISTS: NEITHER AGREE NOR DISAGREE";

 label define sxok16
   1 "STRONGLY AGREE"
   2 "AGREE"
   3 "DISAGREE"
   4 "STRONGLY DISAGREE"
   5 "IF R INSISTS: NEITHER AGREE NOR DISAGREE";

 label define chreward
   1 "STRONGLY AGREE"
   2 "AGREE"
   3 "DISAGREE"
   4 "STRONGLY DISAGREE"
   5 "IF R INSISTS: NEITHER AGREE NOR DISAGREE";

 label define chsuppor
   1 "STRONGLY AGREE"
   2 "AGREE"
   3 "DISAGREE"
   4 "STRONGLY DISAGREE"
   5 "IF R INSISTS: NEITHER AGREE NOR DISAGREE";

 label define gayadopt
   1 "STRONGLY AGREE"
   2 "AGREE"
   3 "DISAGREE"
   4 "STRONGLY DISAGREE"
   5 "IF R INSISTS: NEITHER AGREE NOR DISAGREE";

 label define okcohab
   1 "STRONGLY AGREE"
   2 "AGREE"
   3 "DISAGREE"
   4 "STRONGLY DISAGREE"
   5 "IF R INSISTS: NEITHER AGREE NOR DISAGREE";

 label define warm
   1 "STRONGLY AGREE"
   2 "AGREE"
   3 "DISAGREE"
   4 "STRONGLY DISAGREE"
   5 "IF R INSISTS: NEITHER AGREE NOR DISAGREE";

 label define achieve
   1 "STRONGLY AGREE"
   2 "AGREE"
   3 "DISAGREE"
   4 "STRONGLY DISAGREE"
   5 "IF R INSISTS: NEITHER AGREE NOR DISAGREE";

 label define family
   1 "STRONGLY AGREE"
   2 "AGREE"
   3 "DISAGREE"
   4 "STRONGLY DISAGREE"
   5 "IF R INSISTS: NEITHER AGREE NOR DISAGREE";

 label define reactslf
   1 "VERY UPSET"
   2 "A LITTLE UPSET"
   3 "A LITTLE PLEASED"
   4 "VERY PLEASED"
   5 "IF R INSISTS: HE WOULDN T CARE";

 label define chbother
   1 "A GREAT DEAL"
   2 "SOME"
   3 "A LITTLE"
   4 "NOT AT ALL";

 label define lessplsr
   1 "NO CHANCE"
   2 "A LITTLE CHANCE"
   3 "50-50 CHANCE"
   4 "A PRETTY GOOD CHANCE"
   5 "AN ALMOST CERTAIN CHANCE";

 label define embarras
   1 "NO CHANCE"
   2 "A LITTLE CHANCE"
   3 "50-50 CHANCE"
   4 "A PRETTY GOOD CHANCE"
   5 "AN ALMOST CERTAIN CHANCE";

 label define apprec1
   1 "NO CHANCE"
   2 "A LITTLE CHANCE"
   3 "50-50 CHANCE"
   4 "A PRETTY GOOD CHANCE"
   5 "AN ALMOST CERTAIN CHANCE";

 label define acasilang
   1 "ENGLISH"
   2 "SPANISH";

 label define wage
   1 "YES"
   5 "NO";

 label define selfinc
   1 "YES"
   5 "NO";

 label define socsec
   1 "YES"
   5 "NO";

 label define disabil
   1 "YES"
   5 "NO";

 label define retire
   1 "YES"
   5 "NO";

 label define ssi
   1 "YES"
   5 "NO";

 label define unemp
   1 "YES"
   5 "NO";

 label define chldsupp
   1 "YES"
   5 "NO";

 label define interest
   1 "YES"
   5 "NO";

 label define dividend
   1 "YES"
   5 "NO";

 label define othinc
   1 "YES"
   5 "NO";

 label define toincwmy
   1 "WEEKLY"
   2 "MONTHLY"
   3 "YEARLY";

 label define totinc
   1 "UNDER $96 (WEEKLY)/UNDER $417 (MONTHLY)/UNDER $5,000 (YEARLY)"
   2 "$96-$143 (WEEKLY)/$417-624 (MONTHLY)/$5,000-7,499 (YEARLY)"
   3 "$144-191 (WEEKLY)/$625-832 (MONTHLY)/$7,500-9,999 (YEARLY)"
   4 "$192-239 (WEEKLY)/$833-1,041 (MONTHLY)/$10,000-12,499 (YEARLY)"
   5 "$240-288 (WEEKLY)/$1,042-1,249 (MONTHLY)/$12,500-14,999 (YEARLY)"
   6 "$289-384 (WEEKLY)/$1,250-1,666 (MONTHLY)/$15,000-19,999 (YEARLY)"
   7 "$385-480 (WEEKLY)/$1,667-2,082 (MONTHLY)/$20,000-24,999 (YEARLY)"
   8 "$481-576 (WEEKLY)/$2,083-2,499 (MONTHLY)/$25,000-29,999 (YEARLY)"
   9 "$577-672 (WEEKLY)/$2,500-2,916 (MONTHLY)/$30,000-34,999 (YEARLY)"
  10 "$673-768 (WEEKLY)/$2,917-3,332 (MONTHLY)/$35,000-39,999 (YEARLY)"
  11 "$769-961 (WEEKLY)/$3,333-4,166 (MONTHLY)/$40,000-49,999 (YEARLY)"
  12 "$962-1,153 (WEEKLY)/$4,167-4,999 (MONTHLY)/$50,000-59,999 (YEARLY)"
  13 "$1,154-1,441 (WEEKLY)/$5,000-6,249 (MONTHLY)/$60,000-74,999 (YEARLY)"
  14 "$1,442 OR MORE (WEEKLY)/$6,250 OR MORE (MONTHLY)/$75,000 OR MORE (YEARLY)";

 label define pubasst
   1 "YES"
   5 "NO";

 label define pubastyp1
   1 "YOUR STATE'S PUBLIC ASSISTANCE PROGRAM"
   2 "GENERAL ASSISTANCE/EMERGENCY ASSISTANCE/OTHER ASSISTANCE";

 label define foodstmp
   1 "YES"
   5 "NO";

 label define wic
   1 "YES"
   5 "NO";

 label define hlptrans
   1 "YES"
   5 "NO";

 label define hlpchldc
   1 "YES"
   5 "NO";

 label define hlpjob
   1 "YES"
   5 "NO";

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
  44 "44 YEARS"
  45 "45 YEARS";

 label define fmarital
   1 "MARRIED"
   2 "WIDOWED"
   3 "DIVORCED"
   4 "SEPARATED"
   5 "NEVER MARRIED";

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

 label define hispanic
   1 "HISPANIC"
   2 "NON-HISPANIC";

 label define race
   1 "BLACK"
   2 "WHITE"
   3 "OTHER";

 label define hisprace
   1 "HISPANIC"
   2 "NON-HISPANIC WHITE"
   3 "NON-HISPANIC BLACK"
   4 "NON-HISPANIC OTHER";

 label define numkdhh
   0 "NO CHILDREN"
   1 "1 CHILD"
   2 "2 CHILDREN"
   3 "3 CHILDREN"
   4 "4 CHILDREN"
   5 "5 OR MORE CHILDREN";

 label define numfmhh
   0 "NO FAMILY MEMBERS"
   1 "1 FAMILY MEMBER"
   2 "2 FAMILY MEMBERS"
   3 "3 FAMILY MEMBERS"
   4 "4 FAMILY MEMBERS"
   5 "5 FAMILY MEMBERS"
   6 "6 FAMILY MEMBERS"
   7 "7 OR MORE FAMILY MEMBERS";

 label define intctfam
   1 "TWO BIOLOGICAL OR ADOPTIVE PARENTS FROM BIRTH"
   2 "ANYTHING OTHER THAN 2 BIOLOGICAL OR ADOPTIVE PARENTS FROM BIRTH";

 label define parage14
   1 "R LIVED WITH BOTH BIOLOGICAL OR ADOPTIVE PARENTS AT AGE 14"
   2 "R LIVED WITH 1 BIOLOGICAL PARENT AND 1 ADOPTIVE OR STEP PARENT AT AGE 14"
   3 "R LIVED IN ANY OTHER PARENTAL SITUATION OR A NONPARENTAL SITUATION AT AGE 14";

 label define educmom
   1 "LESS THAN HIGH SCHOOL"
   2 "HIGH SCHOOL GRAD OR GED"
   3 "SOME COLLEGE"
   4 "BACHELOR'S DEGREE OR HIGHER"
  95 "NO MOTHER-FIGURE";

 label define agemomb1
   1 "LESS THAN 18 YEARS"
   2 "18-19 YEARS"
   3 "20-24 YEARS"
   4 "25-29 YEARS"
   5 "30 OR OLDER"
  96 "MOTHER-FIGURE HAD NO CHILDREN";

 label define fmarno
   0 "NEVER BEEN MARRIED"
   1 "1 TIME"
   2 "2 TIMES"
   3 "3 TIMES"
   4 "4 TIMES";

 label define rmarital
   1 "CURRENTLY MARRIED"
   2 "NOT MARRIED BUT LIVING WITH OPP SEX PARTNER"
   3 "WIDOWED"
   4 "DIVORCED"
   5 "SEPARATED FOR REASONS OF MARITAL DISCORD"
   6 "NEVER BEEN MARRIED";

 label define ager_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define fmarital_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define educat_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define hieduc_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define hispanic_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define race_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define hisprace_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define numkdhh_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define numfmhh_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define intctfam_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define parage14_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define educmom_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define agemomb1_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define fmarno_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define rmarital_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define hadsex
   1 "YES, R EVER HAD INTERCOURSE"
   2 "NO, R NEVER HAD INTERCOURSE";

 label define sexonce
   1 "YES (R HAS HAD SEX ONLY ONCE)"
   2 "NO (R HAS HAD SEX MORE THAN ONCE)";

 label define firstpflag
   0 "NEVER HAD SEXUAL INTERCOURSE (RHADSEX = 2) OR IT IS NOT ASCERTAINED (SEXSTAT = .)"
   1 "CMFSTSEX - CM OF FIRST SEX EVER, BASED ON DL SERIES"
   2 "MIN (OF CMLSXP CMLSXP2 CMLSXP3)"
   3 "MIN (OF CMFSXP CMFSXP2 CMFSXP3)"
   4 "MIN (OF CMLSXP CMLSXP2 CMLSXP3 CMFSXP CMFSXP2 CMFSXP3)"
   5 "CMLSXP - CM WHEN R LAST HAD SEX WITH MOST RECENT PARTNER"
   6 "CMLSXP2 - CM WHEN R LAST HAD SEX WITH 2ND-TO-LAST PARTNER"
   7 "CMLSXP3 - CM WHEN R LAST HAD SEX WITH 3RD-TO-LAST PARTNER"
   8 "CMFSXP - CM WHEN R FIRST HAD SEX WITH MOST RECENT PARTNER"
   9 "CMFSXP2 - CM WHEN R FIRST HAD SEX WITH 2ND-TO-LAST PARTNER"
  10 "CMFSXP3 - CM WHEN R FIRST HAD SEX WITH 3RD-TO-LAST PARTNER"
  11 "CMFSXCWP - CM WHEN R LAST HAD SEX WITH CWP (SECTION C)";

 label define fsexrltn
   1 "MARRIED TO HER"
   2 "ENGAGED TO HER"
   3 "LIVING TOGETHER IN A SEXUAL RELATIONSHIP, BUT NOT ENGAGED"
   4 "GOING OUT WITH HER OR GOING STEADY"
   5 "GOING OUT WITH HER ONCE IN A WHILE"
   6 "JUST FRIENDS"
   7 "HAD JUST MET HER"
   8 "SOMETHING ELSE";

 label define sex1mthd1
   1 "CONDOM"
   2 "WITHDRAWAL"
   3 "VASECTOMY"
   4 "PILL"
   5 "FEMALE STERILIZATION"
   6 "INJECTION -- DEPO-PROVERA/LUNELLE"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT -- NORPLANT"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE"
  96 "DID NOT USE A METHOD AT 1ST INTERCOURSE";

 label define sex1mthd2
   1 "CONDOM"
   2 "WITHDRAWAL"
   3 "VASECTOMY"
   4 "PILL"
   5 "FEMALE STERILIZATION"
   6 "INJECTION -- DEPO-PROVERA/LUNELLE"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT -- NORPLANT"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE"
  96 "DID NOT USE A METHOD AT 1ST INTERCOURSE";

 label define sex1mthd3
   1 "CONDOM"
   2 "WITHDRAWAL"
   3 "VASECTOMY"
   4 "PILL"
   5 "FEMALE STERILIZATION"
   6 "INJECTION -- DEPO-PROVERA/LUNELLE"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT -- NORPLANT"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE"
  96 "DID NOT USE A METHOD AT 1ST INTERCOURSE";

 label define sex1mthd4
   1 "CONDOM"
   2 "WITHDRAWAL"
   3 "VASECTOMY"
   4 "PILL"
   5 "FEMALE STERILIZATION"
   6 "INJECTION -- DEPO-PROVERA/LUNELLE"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT -- NORPLANT"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE"
  96 "DID NOT USE A METHOD AT 1ST INTERCOURSE";

 label define orderflag
   1 "SECTION D PARTNER DATES (NONMISSING) ARE IN PROPER CHRONOLOGICAL ORDER, OR ONLY ONE VALID DATE REPORTED"
   2 "SECTION D PARTNERS REPORTED OUT OF ORDER: AFFECTS LAST PARTNER AND POSSIBLY OTHERS"
   3 "SECTION D PARTNERS REPORTED OUT OF ORDER: AFFECTS 2ND-TO-LAST AND 3RD-TO-LAST PARTNERS ONLY";

 label define sex3mo
   1 "YES, HAD INTERCOURSE"
   2 "NO, DID NOT HAVE INTERCOURSE";

 label define sex12mo
   1 "YES, HAD INTERCOURSE"
   2 "NO, DID NOT HAVE INTERCOURSE";

 label define lsexrltn
   1 "MARRIED TO HER"
   3 "LIVING TOGETHER IN A SEXUAL RELATIONSHIP"
   4 "GOING OUT WITH HER OR GOING STEADY"
   5 "GOING OUT WITH HER ONCE IN A WHILE"
   6 "JUST FRIENDS"
   7 "HAD JUST MET HER"
   8 "SOMETHING ELSE"
   9 "ENGAGED TO HER: ONLY ASKED OF A SUBSET OF RS";

 label define lsexuse1
   1 "CONDOM"
   2 "WITHDRAWAL"
   3 "VASECTOMY"
   4 "PILL"
   5 "FEMALE STERILIZATION"
   6 "INJECTION -- DEPO-PROVERA/LUNELLE"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT -- NORPLANT"
   9 "RYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE"
  95 "R USED NO METHOD    ; R DOES NOT KNOW IF PARTNER USED A METHOD"
  96 "NO METHOD USED LAST SEX";

 label define lsexuse2
   1 "CONDOM"
   2 "WITHDRAWAL"
   3 "VASECTOMY"
   4 "PILL"
   5 "FEMALE STERILIZATION"
   6 "INJECTION -- DEPO-PROVERA/LUNELLE"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT -- NORPLANT"
   9 "RYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE"
  95 "R USED NO METHOD    ; R DOES NOT KNOW IF PARTNER USED A METHOD"
  96 "NO METHOD USED LAST SEX";

 label define lsexuse3
   1 "CONDOM"
   2 "WITHDRAWAL"
   3 "VASECTOMY"
   4 "PILL"
   5 "FEMALE STERILIZATION"
   6 "INJECTION -- DEPO-PROVERA/LUNELLE"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT -- NORPLANT"
   9 "RYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE"
  95 "R USED NO METHOD    ; R DOES NOT KNOW IF PARTNER USED A METHOD"
  96 "NO METHOD USED LAST SEX";

 label define lsexuse4
   1 "CONDOM"
   2 "WITHDRAWAL"
   3 "VASECTOMY"
   4 "PILL"
   5 "FEMALE STERILIZATION"
   6 "INJECTION -- DEPO-PROVERA/LUNELLE"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT -- NORPLANT"
   9 "RYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE"
  95 "R USED NO METHOD    ; R DOES NOT KNOW IF PARTNER USED A METHOD"
  96 "NO METHOD USED LAST SEX";

 label define meth12m1
   1 "CONDOM"
   2 "WITHDRAWAL"
   3 "VASECTOMY"
   4 "PILL"
   5 "FEMALE STERILIZATION"
   6 "INJECTION -- DEPO-PROVERA/LUNELLE"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT -- NORPLANT"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE"
  95 "R DID NOT USE A METHOD - R DOES NOT KNOW IF PARTNER USED A METHOD"
  96 "NO METHOD USED AT LAST SEX IN PAST 12 MONTHS";

 label define meth12m2
   1 "CONDOM"
   2 "WITHDRAWAL"
   3 "VASECTOMY"
   4 "PILL"
   5 "FEMALE STERILIZATION"
   6 "INJECTION -- DEPO-PROVERA/LUNELLE"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT -- NORPLANT"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE"
  95 "R DID NOT USE A METHOD - R DOES NOT KNOW IF PARTNER USED A METHOD"
  96 "NO METHOD USED AT LAST SEX IN PAST 12 MONTHS";

 label define meth12m3
   1 "CONDOM"
   2 "WITHDRAWAL"
   3 "VASECTOMY"
   4 "PILL"
   5 "FEMALE STERILIZATION"
   6 "INJECTION -- DEPO-PROVERA/LUNELLE"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT -- NORPLANT"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE"
  95 "R DID NOT USE A METHOD - R DOES NOT KNOW IF PARTNER USED A METHOD"
  96 "NO METHOD USED AT LAST SEX IN PAST 12 MONTHS";

 label define meth12m4
   1 "CONDOM"
   2 "WITHDRAWAL"
   3 "VASECTOMY"
   4 "PILL"
   5 "FEMALE STERILIZATION"
   6 "INJECTION -- DEPO-PROVERA/LUNELLE"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT -- NORPLANT"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE"
  95 "R DID NOT USE A METHOD - R DOES NOT KNOW IF PARTNER USED A METHOD"
  96 "NO METHOD USED AT LAST SEX IN PAST 12 MONTHS";

 label define meth3m1
   1 "CONDOM"
   2 "WITHDRAWAL"
   3 "VASECTOMY"
   4 "PILL"
   5 "FEMALE STERILIZATION"
   6 "INJECTION -- DEPO-PROVERA/LUNELLE"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT -- NORPLANT"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE"
  95 "R DID NOT USE A METHOD - R DOES NOT KNOW IF PARTNER USED A METHOD"
  96 "NO METHOD USED AT LAST SEX IN PAST 3 MONTHS";

 label define meth3m2
   1 "CONDOM"
   2 "WITHDRAWAL"
   3 "VASECTOMY"
   4 "PILL"
   5 "FEMALE STERILIZATION"
   6 "INJECTION -- DEPO-PROVERA/LUNELLE"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT -- NORPLANT"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE"
  95 "R DID NOT USE A METHOD - R DOES NOT KNOW IF PARTNER USED A METHOD"
  96 "NO METHOD USED AT LAST SEX IN PAST 3 MONTHS";

 label define meth3m3
   1 "CONDOM"
   2 "WITHDRAWAL"
   3 "VASECTOMY"
   4 "PILL"
   5 "FEMALE STERILIZATION"
   6 "INJECTION -- DEPO-PROVERA/LUNELLE"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT -- NORPLANT"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE"
  95 "R DID NOT USE A METHOD - R DOES NOT KNOW IF PARTNER USED A METHOD"
  96 "NO METHOD USED AT LAST SEX IN PAST 3 MONTHS";

 label define meth3m4
   1 "CONDOM"
   2 "WITHDRAWAL"
   3 "VASECTOMY"
   4 "PILL"
   5 "FEMALE STERILIZATION"
   6 "INJECTION -- DEPO-PROVERA/LUNELLE"
   7 "SPERMICIDAL FOAM/JELLY/CREAM/FILM/SUPPOSITORY"
   8 "HORMONAL IMPLANT -- NORPLANT"
   9 "RHYTHM OR SAFE PERIOD"
  10 "SOMETHING ELSE"
  95 "R DID NOT USE A METHOD - R DOES NOT KNOW IF PARTNER USED A METHOD"
  96 "NO METHOD USED AT LAST SEX IN PAST 3 MONTHS";

 label define nump3mos
   0 "0 PARTNERS"
   1 "1 PARTNER"
   2 "2 PARTNERS"
   3 "3 PARTNERS EXACTLY"
   4 "3, POSSIBLY MORE PARTNERS";

 label define lifprtnr
   0 "NONE"
   1 "1 PARTNER"
   2 "2 PARTNERS"
   3 "3 PARTNERS"
   4 "4 PARTNERS"
   5 "5 PARTNERS"
   6 "6 PARTNERS"
   7 "7 PARTNERS"
   8 "8 PARTNERS"
   9 "9 PARTNERS"
  50 "50 OR MORE PARTNERS";

 label define parts1yr
   0 "NONE"
   1 "1 PARTNER"
   2 "2 PARTNERS"
   3 "3 PARTNERS"
   4 "4 PARTNERS"
   5 "5 PARTNERS"
   6 "6 PARTNERS"
   7 "7 OR MORE PARTNERS";

 label define cohever
   1 "YES, EVER COHABITED (LIVED WITH A WOMAN OUTSIDE OF MARRIAGE)"
   2 "NO, NEVER COHABITED (LIVED WITH A WOMAN OUTSIDE OF MARRIAGE)";

 label define evmarcoh
   1 "YES, EVER MARRIED OR COHABITED"
   2 "NO, NEVER MARRIED OR COHABITED";

 label define marend1
   1 "DIVORCED OR ANNULLED"
   2 "SEPARATED"
   3 "WIDOWED";

 label define premarw1
   1 "YES"
   2 "NO";

 label define cohstat
   1 "NEVER COHABITED OUTSIDE OF MARRIAGE"
   2 "FIRST COHABITED BEFORE FIRST MARRIAGE"
   3 "FIRST COHABITED AFTER FIRST MARRIAGE";

 label define cohout
   1 "INTACT COHABITATION"
   2 "INTACT MARRIAGE"
   3 "DISSOLVED MARRIAGE"
   4 "DISSOLVED COHABITATION";

 label define b1premar
   1 "YES"
   2 "NO";

 label define marbaby1
   1 "YES"
   2 "NO";

 label define cebow
   0 "NONE"
   1 "1 CHILD";

 label define cebowc
   0 "NONE"
   1 "1 CHILD";

 label define cebowp
   0 "NONE"
   1 "1 CHILD";

 label define evrnopat
   1 "YES, 1 OR MORE CHILDREN OUT OF WEDLOCK, BUT NO ESTABLISHED PATERNITY"
   2 "NO, 1 OR MORE CHILDREN OUT OF WEDLOCK, BUT ESTABLISHED PATERNITY";

 label define nonliveb
   0 "NONE"
   1 "1 PREGNANCY"
   2 "2 PREGNANCIES";

 label define compreg
   0 "NONE"
   1 "1 PREGNANCY"
   2 "2 PREGNANCIES"
   3 "3 PREGNANCIES"
   4 "4 PREGNANCIES";

 label define abortion
   0 "NONE"
   1 "1 PREGNANCY";

 label define lossnum
   0 "NONE"
   1 "1 PREGNANCY";

 label define wantb01
   1 "LATER, OVERDUE"
   2 "RIGHT TIME"
   3 "TOO SOON, MISTIMED"
   4 "DIDN'T CARE, INDIFFERENT"
   5 "UNWANTED"
   6 "DON'T KNOW, NOT SURE"
   7 "R DID NOT KNOW ABOUT THE PREGNANCY LEADING TO THE BIRTH";

 label define wantb02
   1 "LATER, OVERDUE"
   2 "RIGHT TIME"
   3 "TOO SOON, MISTIMED"
   4 "DIDN'T CARE, INDIFFERENT"
   5 "UNWANTED"
   6 "DON'T KNOW, NOT SURE"
   7 "R DID NOT KNOW ABOUT THE PREGNANCY LEADING TO THE BIRTH";

 label define wantb03
   1 "LATER, OVERDUE"
   2 "RIGHT TIME"
   3 "TOO SOON, MISTIMED"
   4 "DIDN'T CARE, INDIFFERENT"
   5 "UNWANTED"
   6 "DON'T KNOW, NOT SURE"
   7 "R DID NOT KNOW ABOUT THE PREGNANCY LEADING TO THE BIRTH";

 label define wantb04
   1 "LATER, OVERDUE"
   2 "RIGHT TIME"
   3 "TOO SOON, MISTIMED"
   4 "DIDN'T CARE, INDIFFERENT"
   5 "UNWANTED"
   6 "DON'T KNOW, NOT SURE"
   7 "R DID NOT KNOW ABOUT THE PREGNANCY LEADING TO THE BIRTH";

 label define wantb05
   1 "LATER, OVERDUE"
   2 "RIGHT TIME"
   3 "TOO SOON, MISTIMED"
   4 "DIDN'T CARE, INDIFFERENT"
   5 "UNWANTED"
   6 "DON'T KNOW, NOT SURE"
   7 "R DID NOT KNOW ABOUT THE PREGNANCY LEADING TO THE BIRTH";

 label define wantb06
   1 "LATER, OVERDUE"
   2 "RIGHT TIME"
   3 "TOO SOON, MISTIMED"
   4 "DIDN'T CARE, INDIFFERENT"
   5 "UNWANTED"
   6 "DON'T KNOW, NOT SURE"
   7 "R DID NOT KNOW ABOUT THE PREGNANCY LEADING TO THE BIRTH";

 label define wantb07
   1 "LATER, OVERDUE"
   2 "RIGHT TIME"
   3 "TOO SOON, MISTIMED"
   4 "DIDN'T CARE, INDIFFERENT"
   5 "UNWANTED"
   6 "DON'T KNOW, NOT SURE"
   7 "R DID NOT KNOW ABOUT THE PREGNANCY LEADING TO THE BIRTH";

 label define wantb08
   1 "LATER, OVERDUE"
   2 "RIGHT TIME"
   3 "TOO SOON, MISTIMED"
   4 "DIDN'T CARE, INDIFFERENT"
   5 "UNWANTED"
   6 "DON'T KNOW, NOT SURE"
   7 "R DID NOT KNOW ABOUT THE PREGNANCY LEADING TO THE BIRTH";

 label define wantb09
   1 "LATER, OVERDUE"
   2 "RIGHT TIME"
   3 "TOO SOON, MISTIMED"
   4 "DIDN'T CARE, INDIFFERENT"
   5 "UNWANTED"
   6 "DON'T KNOW, NOT SURE"
   7 "R DID NOT KNOW ABOUT THE PREGNANCY LEADING TO THE BIRTH";

 label define wantb10
   1 "LATER, OVERDUE"
   2 "RIGHT TIME"
   3 "TOO SOON, MISTIMED"
   4 "DIDN'T CARE, INDIFFERENT"
   5 "UNWANTED"
   6 "DON'T KNOW, NOT SURE"
   7 "R DID NOT KNOW ABOUT THE PREGNANCY LEADING TO THE BIRTH";

 label define unintb5
   1 "YES"
   2 "NO"
   3 "R DID NOT KNOW ABOUT PREGNANCY(IES) LEADING TO BIRTH(S) IN THE PAST 5 YEARS";

 label define hadsex_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define sexonce_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define vry1stsx_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define vry1stag_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define fsexpage_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define fsexrltn_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define sex1mthd1_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define sex1mthd2_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define sex1mthd3_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define sex1mthd4_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define lsexdate_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define sex3mo_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define sex12mo_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define lsexrage_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define lsexpage_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define lsexrltn_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define lsexuse1_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define lsexuse2_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define lsexuse3_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define lsexuse4_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define meth12m1_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define meth12m2_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define meth12m3_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define meth12m4_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define meth3m1_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define meth3m2_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define meth3m3_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define meth3m4_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define nump3mos_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define lifprtnr_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define parts1yr_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define cohever_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define evmarcoh_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define mardat01_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define marend1_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define mardis01_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define mar1diss_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define premarw1_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define cohab1_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define cohstat_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define cohout_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define coh1dur_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define datbaby1_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define agebaby1_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define b1premar_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define marbaby1_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define cebow_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define cebowc_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define cebowp_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define evrnopat_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define nonliveb_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define compreg_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define abortion_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define lossnum_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define wantb01_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define wantb02_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define wantb03_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define wantb04_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define wantb05_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define wantb06_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define wantb07_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define wantb08_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define wantb09_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define wantb10_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define unintb5_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define dadtype
   1 "ONLY CORESIDENTIAL CHILDREN"
   2 "ONLY NON-CORESIDENTIAL CHILDREN"
   3 "BOTH CORESIDENTIAL AND NON-CORESIDENTIAL CHILDREN"
   4 "NO CHILDREN 18 OR YOUNGER, OR NO CHILDREN AT ALL";

 label define dadtypu5
   1 "ONLY CORESIDENTIAL CHILDREN UNDER 5"
   2 "ONLY NON-CORESIDENTIAL CHILDREN UNDER 5"
   3 "BOTH CORESIDENTIAL AND NONCORESIDENTIAL CHILDREN UNDER 5"
   4 "NEITHER CORESIDENTIAL OR NONCORESIDENTIAL CHILDREN UNDER 5, OR NO CHILDREN";

 label define dadtyp518
   1 "ONLY CORESIDENTIAL CHILDREN 5 TO 18"
   2 "ONLY NON-CORESIDENTIAL CHILDREN 5 TO 18"
   3 "BOTH CORESIDENTIAL AND NONCORESIDENTIAL CHILDREN 5 TO 18"
   4 "NEITHER CORESIDENTIAL OR NONCORESIDENTIAL CHILDREN 5 TO 18, OR NO CHILDREN";

 label define numcru18
   0 "NONE"
   1 "1 CHILD"
   2 "2 CHILDREN"
   3 "3 CHILDREN";

 label define numncu18
   0 "NONE"
   1 "1 CHILD"
   2 "2 CHILDREN"
   3 "3 CHILDREN";

 label define supp12mo
   1 "CONTRIBUTED CHILD SUPPORT ON A REGULAR BASIS IN LAST 12 MONTHS"
   2 "CONTRIBUTED CHILD SUPPORT ONCE IN A WHILE IN LAST 12 MONTHS"
   3 "DID NOT CONTRIBUTE CHILD SUPPORT IN LAST 12 MONTHS";

 label define dadtype_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define dadtypu5_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define dadtyp518_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define numcru18_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define numncu18_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define supp12mo_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define intent
   1 "R INTENDS TO HAVE (MORE) CHILDREN"
   2 "R DOES NOT INTEND TO HAVE (MORE) CHILDREN"
   3 "R DOES NOT KNOW HER INTENT";

 label define addexp
   0 "NO ADDITIONAL BIRTHS"
   5 ".5 ADDITIONAL BIRTHS"
  10 "1 ADDITIONAL BIRTH"
  15 "1.5 ADDITIONAL BIRTHS"
  20 "2 ADDITIONAL BIRTHS"
  25 "2.5 ADDITIONAL BIRTHS"
  30 "3 ADDITIONAL BIRTHS"
  35 "3.5 ADDITIONAL BIRTHS"
  40 "4 ADDITIONAL BIRTHS"
  50 "5 ADDITIONAL BIRTHS"
  60 "6 ADDITIONAL BIRTHS"
  70 "7 ADDITIONAL BIRTHS"
  80 "8 ADDITIONAL BIRTHS"
  90 "9 ADDITIONAL BIRTHS"
  100 "10 ADDITIONAL BIRTHS" 
  110 "11 ADDITIONAL BIRTHS" 
  120 "12 ADDITIONAL BIRTHS"      
  180 "18 ADDITIONAL BIRTHS";

 label define intent_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define addexp_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define insuranc
   1 "NOT COVERED BY ANY HEALTH INSURANCE"
   2 "COVERED BY A PRIVATE HEALTH INSURANCE PLAN ONLY"
   3 "COVERED BY MEDICAID (MENTIONED AT ALL)"
   4 "COVERED BY PUBLIC/GOVERNMENT/STATE/MILITARY HEALTH CARE (MENTIONED AT ALL)";

 label define infever
   1 "YES, SOUGHT MEDICAL HELP TO HAVE A BABY"
   2 "NO, NEVER SOUGHT MEDICAL HELP TO HAVE A BABY";

 label define evhivtst
   0 "NO HIV TEST REPORTED"
   1 "YES, ONLY AS PART OF BLOOD DONATION"
   2 "YES, ONLY OUTSIDE OF BLOOD DONATION"
   3 "YES, IN BOTH CONTEXTS";

 label define insuranc_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define infever_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define evhivtst_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define metro
   1 "MSA, CENTRAL CITY"
   2 "MSA, OTHER"
   3 "NOT MSA";

 label define religion
   1 "NO RELIGION"
   2 "CATHOLIC"
   3 "PROTESTANT"
   4 "OTHER RELIGIONS";

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

 label define metro_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define religion_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define laborfor_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define poverty
 500 "500 PERCENT OF POVERTY LEVEL OR GREATER";

 label define totincr
   1 "UNDER $5000"
   2 "$5000-$7499"
   3 "$7500-$9999"
   4 "$10,000-$12,499"
   5 "$12,500-$14,999"
   6 "$15,000-$19,999"
   7 "$20,000-$24,999"
   8 "$25,000-$29,999"
   9 "$30,000-$34,999"
  10 "$35,000-$39,999"
  11 "$40,000-$49,999"
  12 "$50,000-$59,000"
  13 "$60,000-$74,999"
  14 "$75,000 OR MORE";

 label define pubassis
   1 "YES (R RECEIVED PUBLIC ASSISTANCE IN 2001)"
   2 "NO (R DID NOT RECEIVE PUBLIC ASSISTANCE IN 2001)";

 label define poverty_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define totincr_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

 label define pubassis_i
   0 "QUESTIONNAIRE DATA (NOT IMPUTED)"
   1 "MODEL-BASED IMPUTATION"
   2 "LOGICAL IMPUTATION";

#delimit cr

 label values rscrinf rscrinf
 label values rdormres rdormres
 label values rostscrn rostscrn
 label values rscreenhisp rscreenhisp
 label values rscreenrace rscreenrace
 label values age_a age_a
 label values age_r age_r
 label values marstat marstat
 label values fmarstat fmarstat
 label values hisp hisp
 label values hispgrp hispgrp
 label values numrace numrace
 label values wplocale wplocale
 label values womrel womrel
 label values fl_rage fl_rage
 label values fl_rrace fl_rrace
 label values fl_rhisp fl_rhisp
 label values goschol goschol
 label values vaca vaca
 label values higrade higrade
 label values compgrd compgrd
 label values havedip havedip
 label values dipged dipged
 label values havedeg havedeg
 label values degrees degrees
 label values wthparnw wthparnw
 label values onown onown
 label values intact intact
 label values parmarr parmarr
 label values lvsit14f lvsit14f
 label values lvsit14m lvsit14m
 label values womrasdu womrasdu
 label values momdegre momdegre
 label values momworkd momworkd
 label values momchild momchild
 label values momfstch momfstch
 label values mom18 mom18
 label values manrasdu manrasdu
 label values daddegre daddegre
 label values bothbiol bothbiol
 label values intact18 intact18
 label values onown18 onown18
 label values timesmar timesmar
 label values evcohab1 evcohab1
 label values numcoh1 numcoh1
 label values evcohab2 evcohab2
 label values numcoh2 numcoh2
 label values agescrn agescrn
 label values fmarit fmarit
 label values evrmarry evrmarry
 label values roscnt roscnt
 label values evrcohab evrcohab
 label values numwife numwife
 label values numcohab numcohab
 label values talkpar1 talkpar1
 label values talkpar2 talkpar2
 label values talkpar3 talkpar3
 label values talkpar4 talkpar4
 label values talkpar5 talkpar5
 label values sedno sedno
 label values sednog sednog
 label values sedbc sedbc
 label values sedbcg sedbcg
 label values pledge pledge
 label values everoper everoper
 label values typeoper typeoper
 label values steroper steroper
 label values plcstrop plcstrop
 label values rvrsvas rvrsvas
 label values rsurgstr rsurgstr
 label values fathposs fathposs
 label values fathdiff fathdiff
 label values rstrstat rstrstat
 label values eversex eversex
 label values rhadsex rhadsex
 label values sxmtonce sxmtonce
 label values ynosex ynosex
 label values evrchil evrchil
 label values evrchiln evrchiln
 label values father father
 label values lifeprt lifeprt
 label values lifeprts lifeprts
 label values sxmon12 sxmon12
 label values mon12prt mon12prt
 label values mon12prts mon12prts
 label values sexstat sexstat
 label values biokids biokids
 label values adopkids adopkids
 label values currpreg currpreg
 label values currprts currprts
 label values pregsnow pregsnow
 label values sexfreq sexfreq
 label values confreq confreq
 label values p1rltn1 p1rltn1
 label values p1currwife p1currwife
 label values p1currsep p1currsep
 label values p1rltn2 p1rltn2
 label values p1cohabit p1cohabit
 label values p2rltn1 p2rltn1
 label values p2currwife p2currwife
 label values p2currsep p2currsep
 label values p2rltn2 p2rltn2
 label values p2cohabit p2cohabit
 label values p3rltn1 p3rltn1
 label values p3currwife p3currwife
 label values p3currsep p3currsep
 label values p3rltn2 p3rltn2
 label values p3cohabit p3cohabit
 label values p1relation p1relation
 label values p2relation p2relation
 label values p3relation p3relation
 label values first first
 label values livtogwf livtogwf
 label values engathen engathen
 label values willmarr willmarr
 label values cwphisp cwphisp
 label values cwprace1 cwprace1
 label values cwprace2 cwprace2
 label values cwprace3 cwprace3
 label values cwpraceb cwpraceb
 label values cwpeducn cwpeducn
 label values cwpborn cwpborn
 label values cwpmarbf cwpmarbf
 label values cwpsx1rl cwpsx1rl
 label values cwpfuse cwpfuse
 label values cwpfmet01 cwpfmet01
 label values cwpfmet02 cwpfmet02
 label values cwpfmet03 cwpfmet03
 label values cwpfmet04 cwpfmet04
 label values cwpopstr cwpopstr
 label values cwptypop1 cwptypop1
 label values cwptypop2 cwptypop2
 label values cwptotst cwptotst
 label values cwprevst cwprevst
 label values psurgstr psurgstr
 label values cwpposs cwpposs
 label values cwpdiff cwpdiff
 label values pstrstat pstrstat
 label values cwplstsx cwplstsx
 label values cwpluse cwpluse
 label values cwplmet01 cwplmet01
 label values cwplmet02 cwplmet02
 label values cwplmet03 cwplmet03
 label values cwplmet04 cwplmet04
 label values cwpluse1 cwpluse1
 label values cwplmet11 cwplmet11
 label values cwplmet12 cwplmet12
 label values cwplmet13 cwplmet13
 label values cwplmet14 cwplmet14
 label values cwpluse2 cwpluse2
 label values cwplmet21 cwplmet21
 label values cwplmet22 cwplmet22
 label values cwplmet23 cwplmet23
 label values cwplmet24 cwplmet24
 label values cwprecbc cwprecbc
 label values cwpallbc01 cwpallbc01
 label values cwpallbc02 cwpallbc02
 label values cwpallbc03 cwpallbc03
 label values cwpallbc04 cwpallbc04
 label values cwpallbc05 cwpallbc05
 label values cwpallbc06 cwpallbc06
 label values cwplsxuse cwplsxuse
 label values cwpbcmst cwpbcmst
 label values cwpnofrq cwpnofrq
 label values cwpbiokd cwpbiokd
 label values partfath partfath
 label values bkidagegp21 bkidagegp21
 label values bkidhh21 bkidhh21
 label values bkidmar21 bkidmar21
 label values cwpchsex cwpchsex
 label values cwpchmar cwpchmar
 label values cwpchres cwpchres
 label values cwpchlrn cwpchlrn
 label values cwpchliv1 cwpchliv1
 label values cwpchliv2 cwpchliv2
 label values cwpchage cwpchage
 label values cwpchleg cwpchleg
 label values cwpchhop cwpchhop
 label values cwpchevr cwpchevr
 label values cwpchwnt cwpchwnt
 label values cwpchson cwpchson
 label values bkidagegp22 bkidagegp22
 label values bkidhh22 bkidhh22
 label values bkidmar22 bkidmar22
 label values cwpchsex2 cwpchsex2
 label values multbirt2 multbirt2
 label values cwpchmar2 cwpchmar2
 label values cwpchres2 cwpchres2
 label values cwpchlrn2 cwpchlrn2
 label values cwpchliv10 cwpchliv10
 label values cwpchliv11 cwpchliv11
 label values cwpchage2 cwpchage2
 label values cwpchleg2 cwpchleg2
 label values cwpchhop2 cwpchhop2
 label values cwpchevr2 cwpchevr2
 label values cwpchwnt2 cwpchwnt2
 label values cwpchson2 cwpchson2
 label values bkidagegp23 bkidagegp23
 label values bkidhh23 bkidhh23
 label values bkidmar23 bkidmar23
 label values cwpchsex3 cwpchsex3
 label values multbirt3 multbirt3
 label values cwpchmar3 cwpchmar3
 label values cwpchres3 cwpchres3
 label values cwpchlrn3 cwpchlrn3
 label values cwpchliv19 cwpchliv19
 label values cwpchage3 cwpchage3
 label values cwpchleg3 cwpchleg3
 label values cwpchhop3 cwpchhop3
 label values cwpchevr3 cwpchevr3
 label values cwpchwnt3 cwpchwnt3
 label values cwpchson3 cwpchson3
 label values bkidagegp24 bkidagegp24
 label values bkidhh24 bkidhh24
 label values bkidmar24 bkidmar24
 label values cwpchsex4 cwpchsex4
 label values multbirt4 multbirt4
 label values cwpchres4 cwpchres4
 label values cwpchlrn4 cwpchlrn4
 label values cwpchliv28 cwpchliv28
 label values cwpchleg4 cwpchleg4
 label values cwpchhop4 cwpchhop4
 label values cwpchevr4 cwpchevr4
 label values cwpchwnt4 cwpchwnt4
 label values cwpchson4 cwpchson4
 label values bkidagegp25 bkidagegp25
 label values bkidhh25 bkidhh25
 label values bkidmar25 bkidmar25
 label values cwpchsex5 cwpchsex5
 label values multbirt5 multbirt5
 label values cwpchres5 cwpchres5
 label values cwpchlrn5 cwpchlrn5
 label values cwpchliv37 cwpchliv37
 label values cwpchleg5 cwpchleg5
 label values cwpchhop5 cwpchhop5
 label values cwpchevr5 cwpchevr5
 label values cwpchwnt5 cwpchwnt5
 label values cwpchson5 cwpchson5
 label values bkidagegp26 bkidagegp26
 label values bkidhh26 bkidhh26
 label values bkidmar26 bkidmar26
 label values cwpchsex6 cwpchsex6
 label values multbirt6 multbirt6
 label values cwpchres6 cwpchres6
 label values cwpchliv46 cwpchliv46
 label values bkidagegp27 bkidagegp27
 label values bkidhh27 bkidhh27
 label values bkidmar27 bkidmar27
 label values cwpchsex7 cwpchsex7
 label values multbirt7 multbirt7
 label values cwpchliv55 cwpchliv55
 label values cwpprgnw cwpprgnw
 label values cwptrypg cwptrypg
 label values cwpcpwnt cwpcpwnt
 label values cwpcpson cwpcpson
 label values cwpotkid cwpotkid
 label values cwpokad cwpokad
 label values akidagegp21 akidagegp21
 label values akidhh21 akidhh21
 label values cwpoksex cwpoksex
 label values cwpokliv1 cwpokliv1
 label values akidagegp22 akidagegp22
 label values akidhh22 akidhh22
 label values cwpoksex2 cwpoksex2
 label values cwpokliv8 cwpokliv8
 label values akidagegp23 akidagegp23
 label values akidhh23 akidhh23
 label values cwpoksex3 cwpoksex3
 label values cwpokliv15 cwpokliv15
 label values cwpnbevr cwpnbevr
 label values cwpnbrel cwpnbrel
 label values cwpnbfos cwpnbfos
 label values cwpnbad cwpnbad
 label values akidhh31 akidhh31
 label values cwpnbsex cwpnbsex
 label values cwpnbliv1 cwpnbliv1
 label values akidagegp31 akidagegp31
 label values akidhh32 akidhh32
 label values cwpnbsex2 cwpnbsex2
 label values cwpnbliv8 cwpnbliv8
 label values akidagegp32 akidagegp32
 label values c_nbakids c_nbakids
 label values thiswom thiswom
 label values pxrelat pxrelat
 label values pxrelat2 pxrelat2
 label values livtogn livtogn
 label values engagthn engagthn
 label values marrend marrend
 label values pxcurr pxcurr
 label values p1currprt p1currprt
 label values pxmarry pxmarry
 label values pxlast pxlast
 label values pxluse pxluse
 label values pxlmeth01 pxlmeth01
 label values pxlmeth02 pxlmeth02
 label values pxlmeth03 pxlmeth03
 label values pxlmeth04 pxlmeth04
 label values pxlruse pxlruse
 label values pxlrmeth1 pxlrmeth1
 label values pxlrmeth2 pxlrmeth2
 label values pxlrmeth3 pxlrmeth3
 label values pxlrmeth4 pxlrmeth4
 label values pxlpuse pxlpuse
 label values pxlpmeth1 pxlpmeth1
 label values pxlpmeth2 pxlpmeth2
 label values pxlpmeth3 pxlpmeth3
 label values pxlpmeth4 pxlpmeth4
 label values lsxusep lsxusep
 label values pxlsxprb pxlsxprb
 label values pxmtonce pxmtonce
 label values mtoncep mtoncep
 label values pxrelage pxrelage
 label values pxrelyrs pxrelyrs
 label values pxfrltn1 pxfrltn1
 label values pxhisp pxhisp
 label values pxrace1 pxrace1
 label values pxrace2 pxrace2
 label values pxrace3 pxrace3
 label values pxbest pxbest
 label values pxdob_m pxdob_m
 label values pxeduc pxeduc
 label values pxmarbf pxmarbf
 label values pxanych pxanych
 label values pxanychn pxanychn
 label values pxablech pxablech
 label values pxfrltn2 pxfrltn2
 label values pxfuse pxfuse
 label values pxfmeth01 pxfmeth01
 label values pxfmeth02 pxfmeth02
 label values pxfmeth03 pxfmeth03
 label values pxfmeth04 pxfmeth04
 label values pxfmeth05 pxfmeth05
 label values pxanyuse pxanyuse
 label values pxmethod01 pxmethod01
 label values pxmethod02 pxmethod02
 label values pxmethod03 pxmethod03
 label values pxmethod04 pxmethod04
 label values pxmethod05 pxmethod05
 label values pxmethod06 pxmethod06
 label values pxmstuse pxmstuse
 label values pxnofreq pxnofreq
 label values pxchild pxchild
 label values pxcxsex pxcxsex
 label values kidmar kidmar
 label values kidagegp kidagegp
 label values kidliv kidliv
 label values kidhh kidhh
 label values pxcxmarb pxcxmarb
 label values pxcxres pxcxres
 label values pxcxknow pxcxknow
 label values pxcxliv01 pxcxliv01
 label values pxcxliv02 pxcxliv02
 label values pxcxage pxcxage
 label values pxcxlaw pxcxlaw
 label values pxcxhop pxcxhop
 label values pxcxever pxcxever
 label values pxwant pxwant
 label values pxsoon pxsoon
 label values pxcxsex2 pxcxsex2
 label values kidmar2 kidmar2
 label values kidagegp2 kidagegp2
 label values kidliv2 kidliv2
 label values kidhh2 kidhh2
 label values multbirt12 multbirt12
 label values pxcxres2 pxcxres2
 label values pxcxknow2 pxcxknow2
 label values pxcxliv11 pxcxliv11
 label values pxcxliv12 pxcxliv12
 label values pxcxlaw2 pxcxlaw2
 label values pxcxhop2 pxcxhop2
 label values pxcxever2 pxcxever2
 label values pxwant2 pxwant2
 label values pxsoon2 pxsoon2
 label values pxcxsex3 pxcxsex3
 label values kidmar3 kidmar3
 label values kidagegp3 kidagegp3
 label values kidliv3 kidliv3
 label values kidhh3 kidhh3
 label values multbirt13 multbirt13
 label values pxcxres3 pxcxres3
 label values pxcxknow3 pxcxknow3
 label values pxcxliv21 pxcxliv21
 label values pxcxliv22 pxcxliv22
 label values pxcxlaw3 pxcxlaw3
 label values pxcxhop3 pxcxhop3
 label values pxcxever3 pxcxever3
 label values pxwant3 pxwant3
 label values pxsoon3 pxsoon3
 label values pxcxsex4 pxcxsex4
 label values kidmar4 kidmar4
 label values kidagegp4 kidagegp4
 label values kidliv4 kidliv4
 label values kidhh4 kidhh4
 label values pxcxknow4 pxcxknow4
 label values pxcxliv31 pxcxliv31
 label values pxwant4 pxwant4
 label values pxsoon4 pxsoon4
 label values pxcpreg pxcpreg
 label values pxtrying pxtrying
 label values pxrwant pxrwant
 label values pxrsoon pxrsoon
 label values pxotkid pxotkid
 label values pxokad pxokad
 label values akidhh41 akidhh41
 label values akidagegp41 akidagegp41
 label values pxoksex pxoksex
 label values pxokliv1 pxokliv1
 label values pxokliv2 pxokliv2
 label values pxnbevr pxnbevr
 label values pxnbrel pxnbrel
 label values pxnbfos pxnbfos
 label values pxnbad pxnbad
 label values pxnbxsex pxnbxsex
 label values pxnbliv1 pxnbliv1
 label values akidhh51 akidhh51
 label values akidagegp51 akidagegp51
 label values pxnbxsex2 pxnbxsex2
 label values pxnbliv9 pxnbliv9
 label values akidhh52 akidhh52
 label values akidagegp52 akidagegp52
 label values d_nbakids d_nbakids
 label values thiswom2 thiswom2
 label values pxrelat3 pxrelat3
 label values pxrelat4 pxrelat4
 label values livtogn2 livtogn2
 label values engagthn2 engagthn2
 label values marrend2 marrend2
 label values pxcurr2 pxcurr2
 label values p2currprt p2currprt
 label values pxmarry2 pxmarry2
 label values pxlast2 pxlast2
 label values pxluse2 pxluse2
 label values pxlmeth11 pxlmeth11
 label values pxlmeth12 pxlmeth12
 label values pxlmeth13 pxlmeth13
 label values pxlmeth14 pxlmeth14
 label values pxlruse2 pxlruse2
 label values pxlrmeth5 pxlrmeth5
 label values pxlrmeth6 pxlrmeth6
 label values pxlrmeth7 pxlrmeth7
 label values pxlrmeth8 pxlrmeth8
 label values pxlpuse2 pxlpuse2
 label values pxlpmeth8 pxlpmeth8
 label values pxlpmeth9 pxlpmeth9
 label values pxlpmeth10 pxlpmeth10
 label values pxlpmeth11 pxlpmeth11
 label values lsxusep2 lsxusep2
 label values pxlsxprb2 pxlsxprb2
 label values pxmtonce2 pxmtonce2
 label values mtoncep2 mtoncep2
 label values pxrelage2 pxrelage2
 label values pxrelyrs2 pxrelyrs2
 label values pxfrltn3 pxfrltn3
 label values pxhisp2 pxhisp2
 label values pxrace6 pxrace6
 label values pxrace7 pxrace7
 label values pxbest2 pxbest2
 label values pxdob_m2 pxdob_m2
 label values pxeduc2 pxeduc2
 label values pxmarbf2 pxmarbf2
 label values pxanych2 pxanych2
 label values pxanychn2 pxanychn2
 label values pxablech2 pxablech2
 label values pxfrltn4 pxfrltn4
 label values pxfuse2 pxfuse2
 label values pxfmeth11 pxfmeth11
 label values pxfmeth12 pxfmeth12
 label values pxfmeth13 pxfmeth13
 label values pxfmeth14 pxfmeth14
 label values pxfmeth15 pxfmeth15
 label values pxanyuse2 pxanyuse2
 label values pxmethod11 pxmethod11
 label values pxmethod12 pxmethod12
 label values pxmethod13 pxmethod13
 label values pxmethod14 pxmethod14
 label values pxmethod15 pxmethod15
 label values pxmethod16 pxmethod16
 label values pxmstuse2 pxmstuse2
 label values pxnofreq2 pxnofreq2
 label values pxchild2 pxchild2
 label values pxcxsex11 pxcxsex11
 label values kidmar11 kidmar11
 label values kidagegp11 kidagegp11
 label values kidliv11 kidliv11
 label values kidhh11 kidhh11
 label values pxcxres11 pxcxres11
 label values pxcxknow11 pxcxknow11
 label values pxcxliv101 pxcxliv101
 label values pxcxliv102 pxcxliv102
 label values pxcxage11 pxcxage11
 label values pxcxlaw11 pxcxlaw11
 label values pxcxhop11 pxcxhop11
 label values pxcxever11 pxcxever11
 label values pxwant11 pxwant11
 label values pxsoon11 pxsoon11
 label values pxcxsex12 pxcxsex12
 label values kidmar12 kidmar12
 label values kidagegp12 kidagegp12
 label values kidliv12 kidliv12
 label values kidhh12 kidhh12
 label values multbirt22 multbirt22
 label values pxcxres12 pxcxres12
 label values pxcxknow12 pxcxknow12
 label values pxcxliv111 pxcxliv111
 label values pxcxage12 pxcxage12
 label values pxcxlaw12 pxcxlaw12
 label values pxcxhop12 pxcxhop12
 label values pxcxever12 pxcxever12
 label values pxwant12 pxwant12
 label values pxsoon12 pxsoon12
 label values pxcxsex13 pxcxsex13
 label values kidmar13 kidmar13
 label values kidagegp13 kidagegp13
 label values kidliv13 kidliv13
 label values kidhh13 kidhh13
 label values pxcxres13 pxcxres13
 label values pxcxknow13 pxcxknow13
 label values pxcxliv121 pxcxliv121
 label values pxcxlaw13 pxcxlaw13
 label values pxcxhop13 pxcxhop13
 label values pxwant13 pxwant13
 label values pxsoon13 pxsoon13
 label values pxcxsex14 pxcxsex14
 label values kidmar14 kidmar14
 label values kidagegp14 kidagegp14
 label values kidliv14 kidliv14
 label values kidhh14 kidhh14
 label values pxcxres14 pxcxres14
 label values pxcxknow14 pxcxknow14
 label values pxcxliv131 pxcxliv131
 label values pxcxlaw14 pxcxlaw14
 label values pxcxhop14 pxcxhop14
 label values pxwant14 pxwant14
 label values pxsoon14 pxsoon14
 label values pxcpreg2 pxcpreg2
 label values pxtrying2 pxtrying2
 label values pxrwant2 pxrwant2
 label values pxrsoon2 pxrsoon2
 label values pxotkid2 pxotkid2
 label values pxokad2 pxokad2
 label values pxnbevr2 pxnbevr2
 label values pxnbrel2 pxnbrel2
 label values pxnbfos2 pxnbfos2
 label values pxnbad2 pxnbad2
 label values d_nbakids2 d_nbakids2
 label values thiswom3 thiswom3
 label values pxrelat5 pxrelat5
 label values pxrelat6 pxrelat6
 label values livtogn3 livtogn3
 label values engagthn3 engagthn3
 label values marrend3 marrend3
 label values pxcurr3 pxcurr3
 label values p3currprt p3currprt
 label values pxmarry3 pxmarry3
 label values pxlast3 pxlast3
 label values pxluse3 pxluse3
 label values pxlmeth21 pxlmeth21
 label values pxlmeth22 pxlmeth22
 label values pxlmeth23 pxlmeth23
 label values pxlmeth24 pxlmeth24
 label values pxlruse3 pxlruse3
 label values pxlrmeth9 pxlrmeth9
 label values pxlrmeth10 pxlrmeth10
 label values pxlrmeth11 pxlrmeth11
 label values pxlrmeth12 pxlrmeth12
 label values pxlpuse3 pxlpuse3
 label values pxlpmeth15 pxlpmeth15
 label values pxlpmeth16 pxlpmeth16
 label values pxlpmeth17 pxlpmeth17
 label values pxlpmeth18 pxlpmeth18
 label values lsxusep3 lsxusep3
 label values pxlsxprb3 pxlsxprb3
 label values pxmtonce3 pxmtonce3
 label values mtoncep3 mtoncep3
 label values pxrelage3 pxrelage3
 label values pxrelyrs3 pxrelyrs3
 label values pxfrltn5 pxfrltn5
 label values pxhisp3 pxhisp3
 label values pxrace11 pxrace11
 label values pxrace12 pxrace12
 label values pxbest3 pxbest3
 label values pxdob_m3 pxdob_m3
 label values pxeduc3 pxeduc3
 label values pxmarbf3 pxmarbf3
 label values pxanych3 pxanych3
 label values pxanychn3 pxanychn3
 label values pxablech3 pxablech3
 label values pxfrltn6 pxfrltn6
 label values pxfuse3 pxfuse3
 label values pxfmeth21 pxfmeth21
 label values pxfmeth22 pxfmeth22
 label values pxfmeth23 pxfmeth23
 label values pxfmeth24 pxfmeth24
 label values pxfmeth25 pxfmeth25
 label values pxanyuse3 pxanyuse3
 label values pxmethod21 pxmethod21
 label values pxmethod22 pxmethod22
 label values pxmethod23 pxmethod23
 label values pxmethod24 pxmethod24
 label values pxmethod25 pxmethod25
 label values pxmethod26 pxmethod26
 label values pxmstuse3 pxmstuse3
 label values pxnofreq3 pxnofreq3
 label values pxchild3 pxchild3
 label values pxcxsex21 pxcxsex21
 label values kidmar21 kidmar21
 label values kidagegp21 kidagegp21
 label values kidliv21 kidliv21
 label values kidhh21 kidhh21
 label values pxcxmarb21 pxcxmarb21
 label values pxcxres21 pxcxres21
 label values pxcxknow21 pxcxknow21
 label values pxcxliv201 pxcxliv201
 label values pxcxliv202 pxcxliv202
 label values pxcxage21 pxcxage21
 label values pxcxlaw21 pxcxlaw21
 label values pxcxhop21 pxcxhop21
 label values pxcxever21 pxcxever21
 label values pxwant21 pxwant21
 label values pxsoon21 pxsoon21
 label values pxcxsex22 pxcxsex22
 label values kidmar22 kidmar22
 label values kidagegp22 kidagegp22
 label values kidliv22 kidliv22
 label values kidhh22 kidhh22
 label values pxcxres22 pxcxres22
 label values pxcxknow22 pxcxknow22
 label values pxcxliv211 pxcxliv211
 label values pxcxlaw22 pxcxlaw22
 label values pxcxhop22 pxcxhop22
 label values pxwant22 pxwant22
 label values pxcpreg3 pxcpreg3
 label values pxtrying3 pxtrying3
 label values pxrwant3 pxrwant3
 label values pxrsoon3 pxrsoon3
 label values pxotkid3 pxotkid3
 label values pxokad3 pxokad3
 label values pxnbevr3 pxnbevr3
 label values pxnbrel3 pxnbrel3
 label values pxnbfos3 pxnbfos3
 label values pxnbad3 pxnbad3
 label values d_nbakids3 d_nbakids3
 label values fpage18 fpage18
 label values fpage15 fpage15
 label values fpage20 fpage20
 label values fprelage fprelage
 label values fprelyrs fprelyrs
 label values fprltn fprltn
 label values fpuse fpuse
 label values fpmeth01 fpmeth01
 label values fpmeth02 fpmeth02
 label values fpmeth03 fpmeth03
 label values fpmeth04 fpmeth04
 label values fpprobe fpprobe
 label values fwverify fwverify
 label values fwver fwver
 label values fwverify2 fwverify2
 label values fwver2 fwver2
 label values fwverify3 fwverify3
 label values fwver3 fwver3
 label values fcverify fcverify
 label values fcver fcver
 label values exrelation exrelation
 label values livtogn4 livtogn4
 label values engagthn4 engagthn4
 label values marrend4 marrend4
 label values fwpdob_m fwpdob_m
 label values fwphisp fwphisp
 label values fwprace1 fwprace1
 label values fwprace2 fwprace2
 label values fwpraceb fwpraceb
 label values fwpmarbf fwpmarbf
 label values fwpbiokd fwpbiokd
 label values kidliv31 kidliv31
 label values kidagegp31 kidagegp31
 label values kidhh31 kidhh31
 label values kidmar31 kidmar31
 label values fwpchsex fwpchsex
 label values fwchmarb fwchmarb
 label values fwpchres fwpchres
 label values fwpchlrn fwpchlrn
 label values fwpchliv01 fwpchliv01
 label values fwpchliv02 fwpchliv02
 label values fwpchage fwpchage
 label values fwpchleg fwpchleg
 label values fwpchhop fwpchhop
 label values fwpchevr fwpchevr
 label values fwprwant fwprwant
 label values fwpsoon fwpsoon
 label values kidliv32 kidliv32
 label values kidagegp32 kidagegp32
 label values kidhh32 kidhh32
 label values kidmar32 kidmar32
 label values fwpchsex2 fwpchsex2
 label values fwchmarb2 fwchmarb2
 label values fwpchres2 fwpchres2
 label values fwpchlrn2 fwpchlrn2
 label values fwpchliv11 fwpchliv11
 label values fwpchliv12 fwpchliv12
 label values fwpchage2 fwpchage2
 label values fwpchleg2 fwpchleg2
 label values fwpchhop2 fwpchhop2
 label values fwpchevr2 fwpchevr2
 label values fwprwant2 fwprwant2
 label values fwpsoon2 fwpsoon2
 label values kidliv33 kidliv33
 label values kidagegp33 kidagegp33
 label values kidhh33 kidhh33
 label values kidmar33 kidmar33
 label values fwpchsex3 fwpchsex3
 label values fwpchres3 fwpchres3
 label values fwpchlrn3 fwpchlrn3
 label values fwpchliv21 fwpchliv21
 label values fwpchliv22 fwpchliv22
 label values fwpchage3 fwpchage3
 label values fwpchleg3 fwpchleg3
 label values fwpchhop3 fwpchhop3
 label values fwpchevr3 fwpchevr3
 label values fwprwant3 fwprwant3
 label values fwpsoon3 fwpsoon3
 label values kidmar34 kidmar34
 label values kidagegp34 kidagegp34
 label values kidhh34 kidhh34
 label values kidliv34 kidliv34
 label values fwpchsex4 fwpchsex4
 label values multbirt44 multbirt44
 label values fwpchres4 fwpchres4
 label values fwpchliv31 fwpchliv31
 label values fwpchage4 fwpchage4
 label values fwpchleg4 fwpchleg4
 label values fwpchhop4 fwpchhop4
 label values fwpchevr4 fwpchevr4
 label values fwprwant4 fwprwant4
 label values kidmar35 kidmar35
 label values kidagegp35 kidagegp35
 label values kidhh35 kidhh35
 label values kidliv35 kidliv35
 label values fwpchsex5 fwpchsex5
 label values fwpchliv41 fwpchliv41
 label values fwpchage5 fwpchage5
 label values fwpchleg5 fwpchleg5
 label values fwpchhop5 fwpchhop5
 label values fwpchevr5 fwpchevr5
 label values fwpotkid fwpotkid
 label values fwpokad fwpokad
 label values akidhh101 akidhh101
 label values fwpoksex fwpoksex
 label values fwpokliv1 fwpokliv1
 label values fwpokliv2 fwpokliv2
 label values akidagegp101 akidagegp101
 label values akidagegp102 akidagegp102
 label values akidhh102 akidhh102
 label values fwpoksex2 fwpoksex2
 label values fwpokliv9 fwpokliv9
 label values akidagegp103 akidagegp103
 label values akidhh103 akidhh103
 label values fwpoksex3 fwpoksex3
 label values fwpokliv17 fwpokliv17
 label values fwpnbevr fwpnbevr
 label values fwpnbrel fwpnbrel
 label values fwpnbfos fwpnbfos
 label values fwpnbad fwpnbad
 label values akidagegp111 akidagegp111
 label values akidhh111 akidhh111
 label values fwpnbsex fwpnbsex
 label values akidagegp112 akidagegp112
 label values akidhh112 akidhh112
 label values fwpnbsex2 fwpnbsex2
 label values fwpnbliv9 fwpnbliv9
 label values e_okakids e_okakids
 label values exrelation2 exrelation2
 label values livtogn5 livtogn5
 label values engagthn5 engagthn5
 label values marrend5 marrend5
 label values fwpdob_m2 fwpdob_m2
 label values fwpmarbf2 fwpmarbf2
 label values fwpbiokd2 fwpbiokd2
 label values kidmar41 kidmar41
 label values kidagegp41 kidagegp41
 label values kidhh41 kidhh41
 label values kidliv41 kidliv41
 label values fwpchsex11 fwpchsex11
 label values fwpchres11 fwpchres11
 label values fwpchlrn11 fwpchlrn11
 label values fwpchliv101 fwpchliv101
 label values fwpchliv102 fwpchliv102
 label values fwpchage11 fwpchage11
 label values fwpchleg11 fwpchleg11
 label values fwpchhop11 fwpchhop11
 label values fwpchevr11 fwpchevr11
 label values fwprwant11 fwprwant11
 label values fwpsoon11 fwpsoon11
 label values kidmar42 kidmar42
 label values kidagegp42 kidagegp42
 label values kidhh42 kidhh42
 label values kidliv42 kidliv42
 label values fwpchsex12 fwpchsex12
 label values fwpchres12 fwpchres12
 label values fwpchliv111 fwpchliv111
 label values fwpchage12 fwpchage12
 label values fwpchleg12 fwpchleg12
 label values fwpchhop12 fwpchhop12
 label values kidmar43 kidmar43
 label values kidagegp43 kidagegp43
 label values kidhh43 kidhh43
 label values kidliv43 kidliv43
 label values fwpchsex13 fwpchsex13
 label values fwpchliv121 fwpchliv121
 label values kidmar44 kidmar44
 label values kidagegp44 kidagegp44
 label values kidhh44 kidhh44
 label values kidliv44 kidliv44
 label values fwpchsex14 fwpchsex14
 label values fwpchliv131 fwpchliv131
 label values fwpotkid2 fwpotkid2
 label values fwpokad2 fwpokad2
 label values akidagegp121 akidagegp121
 label values akidhh121 akidhh121
 label values fwpoksex11 fwpoksex11
 label values fwpokliv81 fwpokliv81
 label values fwpnbevr2 fwpnbevr2
 label values fwpnbrel2 fwpnbrel2
 label values fwpnbfos2 fwpnbfos2
 label values fwpnbad2 fwpnbad2
 label values akidagegp131 akidagegp131
 label values akidhh131 akidhh131
 label values fwpnbsex11 fwpnbsex11
 label values fwpnbliv81 fwpnbliv81
 label values e_okakids2 e_okakids2
 label values exrelation3 exrelation3
 label values livtogn6 livtogn6
 label values engagthn6 engagthn6
 label values marrend6 marrend6
 label values fwpdob_m3 fwpdob_m3
 label values fwpmarbf3 fwpmarbf3
 label values fwpbiokd3 fwpbiokd3
 label values kidmar51 kidmar51
 label values kidagegp51 kidagegp51
 label values kidhh51 kidhh51
 label values kidliv51 kidliv51
 label values fwpchsex21 fwpchsex21
 label values fwpchres21 fwpchres21
 label values fwpchlrn21 fwpchlrn21
 label values fwpchliv201 fwpchliv201
 label values fwpchage21 fwpchage21
 label values fwpchleg21 fwpchleg21
 label values fwpchhop21 fwpchhop21
 label values fwpchevr21 fwpchevr21
 label values fwprwant21 fwprwant21
 label values fwpotkid3 fwpotkid3
 label values fwpokad3 fwpokad3
 label values fwpnbevr3 fwpnbevr3
 label values fwpnbrel3 fwpnbrel3
 label values fwpnbfos3 fwpnbfos3
 label values fwpnbad3 fwpnbad3
 label values e_okakids3 e_okakids3
 label values exrelation11 exrelation11
 label values fstunion fstunion
 label values engagthn14 engagthn14
 label values fwphisp11 fwphisp11
 label values fwprace51 fwprace51
 label values fwprace52 fwprace52
 label values fwprace53 fwprace53
 label values fwprace54 fwprace54
 label values fwpraceb11 fwpraceb11
 label values fwpmarbf11 fwpmarbf11
 label values fwpbiokd11 fwpbiokd11
 label values kidagegp131 kidagegp131
 label values kidhh131 kidhh131
 label values kidliv131 kidliv131
 label values fwpchsex101 fwpchsex101
 label values fwpchres101 fwpchres101
 label values fwpchlrn101 fwpchlrn101
 label values fwpchliv1001 fwpchliv1001
 label values fwpchliv1002 fwpchliv1002
 label values fwpchage101 fwpchage101
 label values fwpchleg101 fwpchleg101
 label values fwpchhop101 fwpchhop101
 label values fwpchevr101 fwpchevr101
 label values fwprwant101 fwprwant101
 label values fwpsoon101 fwpsoon101
 label values kidagegp132 kidagegp132
 label values kidhh132 kidhh132
 label values kidliv132 kidliv132
 label values fwpchsex102 fwpchsex102
 label values fwpchres102 fwpchres102
 label values fwpchlrn102 fwpchlrn102
 label values fwpchliv1011 fwpchliv1011
 label values fwpchliv1012 fwpchliv1012
 label values fwpchage102 fwpchage102
 label values fwpchleg102 fwpchleg102
 label values fwpchhop102 fwpchhop102
 label values fwpchevr102 fwpchevr102
 label values fwprwant102 fwprwant102
 label values fwpsoon102 fwpsoon102
 label values kidagegp133 kidagegp133
 label values kidhh133 kidhh133
 label values kidliv133 kidliv133
 label values fwpchsex103 fwpchsex103
 label values multbirt143 multbirt143
 label values fwpchres103 fwpchres103
 label values fwpchlrn103 fwpchlrn103
 label values fwpchliv1021 fwpchliv1021
 label values fwpchage103 fwpchage103
 label values fwpchleg103 fwpchleg103
 label values fwpchhop103 fwpchhop103
 label values fwprwant103 fwprwant103
 label values kidagegp134 kidagegp134
 label values kidhh134 kidhh134
 label values kidliv134 kidliv134
 label values fwpchsex104 fwpchsex104
 label values fwpchres104 fwpchres104
 label values fwpchliv1031 fwpchliv1031
 label values fwpchleg104 fwpchleg104
 label values fwpchhop104 fwpchhop104
 label values kidagegp135 kidagegp135
 label values kidhh135 kidhh135
 label values kidliv135 kidliv135
 label values fwpchsex105 fwpchsex105
 label values fwpchres105 fwpchres105
 label values fwpchliv1041 fwpchliv1041
 label values fwpchleg105 fwpchleg105
 label values fwpchhop105 fwpchhop105
 label values fwpotkid11 fwpotkid11
 label values fwpokad11 fwpokad11
 label values akidagegp301 akidagegp301
 label values akidhh301 akidhh301
 label values fwpoksex101 fwpoksex101
 label values fwpokliv801 fwpokliv801
 label values fwpnbevr11 fwpnbevr11
 label values fwpnbrel11 fwpnbrel11
 label values fwpnbfos11 fwpnbfos11
 label values fwpnbad11 fwpnbad11
 label values e_okakids11 e_okakids11
 label values otbchil otbchil
 label values otbprobe otbprobe
 label values otbchiln otbchiln
 label values otbsame otbsame
 label values obcsexx obcsexx
 label values obcmliv obcmliv
 label values obcknowx obcknowx
 label values obclivex01 obclivex01
 label values obclivex02 obclivex02
 label values obclivex03 obclivex03
 label values obcage obcage
 label values kidagegp141 kidagegp141
 label values kidliv141 kidliv141
 label values kidhh141 kidhh141
 label values obclawx obclawx
 label values obchopx obchopx
 label values obceverx obceverx
 label values obcrwanx obcrwanx
 label values obcsoonx obcsoonx
 label values obcsexx2 obcsexx2
 label values multbirt152 multbirt152
 label values obcmliv2 obcmliv2
 label values obcknowx2 obcknowx2
 label values obclivex11 obclivex11
 label values obcage2 obcage2
 label values kidagegp142 kidagegp142
 label values kidliv142 kidliv142
 label values kidhh142 kidhh142
 label values obclawx2 obclawx2
 label values obchopx2 obchopx2
 label values obceverx2 obceverx2
 label values obcrwanx2 obcrwanx2
 label values obcsoonx2 obcsoonx2
 label values obcsexx3 obcsexx3
 label values multbirt153 multbirt153
 label values obcmliv3 obcmliv3
 label values obcknowx3 obcknowx3
 label values obclivex21 obclivex21
 label values obcage3 obcage3
 label values kidagegp143 kidagegp143
 label values kidliv143 kidliv143
 label values kidhh143 kidhh143
 label values obclawx3 obclawx3
 label values obchopx3 obchopx3
 label values obceverx3 obceverx3
 label values obcrwanx3 obcrwanx3
 label values obcsoonx3 obcsoonx3
 label values obcsexx4 obcsexx4
 label values multbirt154 multbirt154
 label values obcmliv4 obcmliv4
 label values obcknowx4 obcknowx4
 label values obclivex31 obclivex31
 label values obcage4 obcage4
 label values kidagegp144 kidagegp144
 label values kidliv144 kidliv144
 label values kidhh144 kidhh144
 label values obclawx4 obclawx4
 label values obchopx4 obchopx4
 label values obceverx4 obceverx4
 label values obcrwanx4 obcrwanx4
 label values obcsoonx4 obcsoonx4
 label values obcsexx5 obcsexx5
 label values obcmliv5 obcmliv5
 label values obcknowx5 obcknowx5
 label values obclivex41 obclivex41
 label values obcage5 obcage5
 label values kidagegp145 kidagegp145
 label values kidliv145 kidliv145
 label values kidhh145 kidhh145
 label values obclawx5 obclawx5
 label values obchopx5 obchopx5
 label values obceverx5 obceverx5
 label values obcrwanx5 obcrwanx5
 label values obcsoonx5 obcsoonx5
 label values obcsexx6 obcsexx6
 label values obcmliv6 obcmliv6
 label values obcknowx6 obcknowx6
 label values obclivex51 obclivex51
 label values kidagegp146 kidagegp146
 label values kidliv146 kidliv146
 label values kidhh146 kidhh146
 label values obclawx6 obclawx6
 label values obchopx6 obchopx6
 label values obceverx6 obceverx6
 label values obcrwanx6 obcrwanx6
 label values obcsoonx6 obcsoonx6
 label values otachil otachil
 label values otachiln otachiln
 label values otnbrel otnbrel
 label values otnbfos otnbfos
 label values otnbad otnbad
 label values f_akids f_akids
 label values otnbsex otnbsex
 label values otnbliv1 otnbliv1
 label values akidhh321 akidhh321
 label values akidagegp321 akidagegp321
 label values otnbsex2 otnbsex2
 label values otnbliv9 otnbliv9
 label values akidhh322 akidhh322
 label values akidagegp322 akidagegp322
 label values otpreg otpreg
 label values otprgprb otprgprb
 label values otprgn otprgn
 label values otprgend otprgend
 label values otmsn otmsn
 label values otstn otstn
 label values otabn otabn
 label values totprg totprg
 label values numlife numlife
 label values otpregs otpregs
 label values totpregs_c totpregs_c
 label values totpregs_r totpregs_r
 label values anykids anykids
 label values bkidliv bkidliv
 label values bkidliv2 bkidliv2
 label values bkidliv3 bkidliv3
 label values bkidliv4 bkidliv4
 label values bkidliv5 bkidliv5
 label values bkidliv6 bkidliv6
 label values bkidliv7 bkidliv7
 label values bkidliv8 bkidliv8
 label values bkidliv9 bkidliv9
 label values bkidliv10 bkidliv10
 label values biosex1 biosex1
 label values biosex2 biosex2
 label values biosex3 biosex3
 label values biosex4 biosex4
 label values biosex5 biosex5
 label values biosex6 biosex6
 label values biosex7 biosex7
 label values biosex8 biosex8
 label values biosex9 biosex9
 label values biosex10 biosex10
 label values biohh1 biohh1
 label values biohh2 biohh2
 label values biohh3 biohh3
 label values biohh4 biohh4
 label values biohh5 biohh5
 label values biohh6 biohh6
 label values biohh7 biohh7
 label values biohh8 biohh8
 label values biohh9 biohh9
 label values biohh10 biohh10
 label values biomar1 biomar1
 label values biomar2 biomar2
 label values biomar3 biomar3
 label values biomar4 biomar4
 label values biomar5 biomar5
 label values biomar6 biomar6
 label values biomar7 biomar7
 label values biomar8 biomar8
 label values biomar9 biomar9
 label values biomar10 biomar10
 label values biocohb1 biocohb1
 label values biocohb2 biocohb2
 label values biocohb3 biocohb3
 label values biocohb4 biocohb4
 label values biocohb5 biocohb5
 label values biocohb6 biocohb6
 label values biocohb7 biocohb7
 label values biocohb8 biocohb8
 label values biocohb9 biocohb9
 label values biocohb10 biocohb10
 label values biolrnpg1 biolrnpg1
 label values biolrnpg2 biolrnpg2
 label values biolrnpg3 biolrnpg3
 label values biolrnpg4 biolrnpg4
 label values biolrnpg5 biolrnpg5
 label values biolrnpg6 biolrnpg6
 label values biolrnpg7 biolrnpg7
 label values biolrnpg8 biolrnpg8
 label values biolrnpg9 biolrnpg9
 label values biolrnpg10 biolrnpg10
 label values biolgpat1 biolgpat1
 label values biolgpat2 biolgpat2
 label values biolgpat3 biolgpat3
 label values biolgpat4 biolgpat4
 label values biolgpat5 biolgpat5
 label values biolgpat6 biolgpat6
 label values biolgpat7 biolgpat7
 label values biolgpat8 biolgpat8
 label values biolgpat9 biolgpat9
 label values biolgpat10 biolgpat10
 label values biohspat1 biohspat1
 label values biohspat2 biohspat2
 label values biohspat3 biohspat3
 label values biohspat4 biohspat4
 label values biohspat5 biohspat5
 label values biohspat6 biohspat6
 label values biohspat7 biohspat7
 label values biohspat8 biohspat8
 label values biohspat9 biohspat9
 label values biohspat10 biohspat10
 label values biolvevr1 biolvevr1
 label values biolvevr2 biolvevr2
 label values biolvevr3 biolvevr3
 label values biolvevr4 biolvevr4
 label values biolvevr5 biolvevr5
 label values biolvevr6 biolvevr6
 label values biolvevr7 biolvevr7
 label values biolvevr8 biolvevr8
 label values biolvevr9 biolvevr9
 label values biolvevr10 biolvevr10
 label values biowant1 biowant1
 label values biowant2 biowant2
 label values biowant3 biowant3
 label values biowant4 biowant4
 label values biowant5 biowant5
 label values biowant6 biowant6
 label values biowant7 biowant7
 label values biowant8 biowant8
 label values biowant9 biowant9
 label values biowant10 biowant10
 label values biohsoon1 biohsoon1
 label values biohsoon2 biohsoon2
 label values biohsoon3 biohsoon3
 label values biohsoon4 biohsoon4
 label values biohsoon5 biohsoon5
 label values biohsoon6 biohsoon6
 label values biohsoon7 biohsoon7
 label values biohsoon8 biohsoon8
 label values biohsoon9 biohsoon9
 label values biohsoon10 biohsoon10
 label values crall crall
 label values crallu5 crallu5
 label values crall518 crall518
 label values crmalu5 crmalu5
 label values crmal518 crmal518
 label values crfemu5 crfemu5
 label values crfem518 crfem518
 label values ncall ncall
 label values ncallu5 ncallu5
 label values ncall518 ncall518
 label values ncmalu5 ncmalu5
 label values ncmal518 ncmal518
 label values ncfemu5 ncfemu5
 label values ncfem518 ncfem518
 label values croutg croutg
 label values crrelg crrelg
 label values crpta crpta
 label values introga4 introga4
 label values crhelp crhelp
 label values crtalk crtalk
 label values crtake crtake
 label values crmeal crmeal
 label values introga9 introga9
 label values crfeed crfeed
 label values crbath crbath
 label values crplay crplay
 label values crread crread
 label values crgood crgood
 label values ncvisit ncvisit
 label values ncsatvis ncsatvis
 label values ncoutg ncoutg
 label values ncrelg ncrelg
 label values ncpta ncpta
 label values introgb6 introgb6
 label values nchelp nchelp
 label values nctalk nctalk
 label values nctake nctake
 label values ncmeal ncmeal
 label values introgb11 introgb11
 label values ncfeed ncfeed
 label values ncbath ncbath
 label values ncplay ncplay
 label values ncread ncread
 label values ncgood ncgood
 label values ncmoney ncmoney
 label values ncreg ncreg
 label values chsuppyr chsuppyr
 label values ncagree ncagree
 label values ncagreen ncagreen
 label values rwant rwant
 label values probwant probwant
 label values jintend jintend
 label values jsureint jsureint
 label values jintendn jintendn
 label values jexpectl jexpectl
 label values jexpects jexpects
 label values intend intend
 label values intendn intendn
 label values expectl expectl
 label values expects expects
 label values usualcar usualcar
 label values uslplace uslplace
 label values cover12 cover12
 label values numnocov numnocov
 label values coverhow01 coverhow01
 label values coverhow02 coverhow02
 label values coverhow03 coverhow03
 label values coverhow04 coverhow04
 label values nowcover01 nowcover01
 label values nowcover02 nowcover02
 label values nowcover03 nowcover03
 label values gofpcwgf gofpcwgf
 label values whengogf whengogf
 label values yougofpc yougofpc
 label values whengofp whengofp
 label values youfpsvc1 youfpsvc1
 label values youfpsvc2 youfpsvc2
 label values youfpsvc3 youfpsvc3
 label values youfpsvc4 youfpsvc4
 label values youfpsvc5 youfpsvc5
 label values limited limited
 label values equipmnt equipmnt
 label values physexam physexam
 label values testichk testichk
 label values bcadvice bcadvice
 label values steradvi steradvi
 label values stdadvic stdadvic
 label values hivadvic hivadvic
 label values onevisit onevisit
 label values numvisit numvisit
 label values placevis01 placevis01
 label values placevis02 placevis02
 label values placevis03 placevis03
 label values placevis04 placevis04
 label values svcpay1 svcpay1
 label values svcpay2 svcpay2
 label values svcpay3 svcpay3
 label values infhelp infhelp
 label values infsvcs1 infsvcs1
 label values infsvcs2 infsvcs2
 label values infsvcs3 infsvcs3
 label values infsvcs4 infsvcs4
 label values infsvcs5 infsvcs5
 label values infsvcs6 infsvcs6
 label values inftest inftest
 label values whoinsem whoinsem
 label values infhlpnw infhlpnw
 label values infrthis1 infrthis1
 label values infrthis2 infrthis2
 label values donbld85 donbld85
 label values hivtest hivtest
 label values plchiv plchiv
 label values hivtst1 hivtst1
 label values hivtst2 hivtst2
 label values hivtst3 hivtst3
 label values hivtst4 hivtst4
 label values talkdoct talkdoct
 label values aidstalk01 aidstalk01
 label values aidstalk02 aidstalk02
 label values aidstalk03 aidstalk03
 label values aidstalk04 aidstalk04
 label values aidstalk05 aidstalk05
 label values aidstalk06 aidstalk06
 label values aidstalk07 aidstalk07
 label values aidstalk08 aidstalk08
 label values aidstalk09 aidstalk09
 label values aidstalk10 aidstalk10
 label values retrovir retrovir
 label values sameadd sameadd
 label values cntry00 cntry00
 label values brnout brnout
 label values paydu paydu
 label values relraisd relraisd
 label values attnd14 attnd14
 label values relcurr relcurr
 label values fundam fundam
 label values reldlife reldlife
 label values attndnow attndnow
 label values milsvc milsvc
 label values startmil startmil
 label values endmil endmil
 label values evwrk6mo evwrk6mo
 label values evrntwrk evrntwrk
 label values wrk12mos wrk12mos
 label values ftpt12mos ftpt12mos
 label values dolastwk1 dolastwk1
 label values dolastwk2 dolastwk2
 label values dolastwk3 dolastwk3
 label values dolastwk4 dolastwk4
 label values dolastwk5 dolastwk5
 label values dolastwk6 dolastwk6
 label values rwrkst rwrkst
 label values everwork everwork
 label values rpayjob rpayjob
 label values rnumjob rnumjob
 label values rftptx rftptx
 label values rearnty rearnty
 label values splstwk1 splstwk1
 label values splstwk2 splstwk2
 label values splstwk3 splstwk3
 label values splstwk4 splstwk4
 label values splstwk5 splstwk5
 label values spwrkst spwrkst
 label values sppayjob sppayjob
 label values spnumjob spnumjob
 label values spftptx spftptx
 label values spearnty spearnty
 label values better better
 label values staytog staytog
 label values samesex samesex
 label values anyact anyact
 label values sxok18 sxok18
 label values sxok16 sxok16
 label values chreward chreward
 label values chsuppor chsuppor
 label values gayadopt gayadopt
 label values okcohab okcohab
 label values warm warm
 label values achieve achieve
 label values family family
 label values reactslf reactslf
 label values chbother chbother
 label values lessplsr lessplsr
 label values embarras embarras
 label values apprec1 apprec1
 label values acasilang acasilang
 label values wage wage
 label values selfinc selfinc
 label values socsec socsec
 label values disabil disabil
 label values retire retire
 label values ssi ssi
 label values unemp unemp
 label values chldsupp chldsupp
 label values interest interest
 label values dividend dividend
 label values othinc othinc
 label values toincwmy toincwmy
 label values totinc totinc
 label values pubasst pubasst
 label values pubastyp1 pubastyp1
 label values foodstmp foodstmp
 label values wic wic
 label values hlptrans hlptrans
 label values hlpchldc hlpchldc
 label values hlpjob hlpjob
 label values ager ager
 label values fmarital fmarital
 label values educat educat
 label values hieduc hieduc
 label values hispanic hispanic
 label values race race
 label values hisprace hisprace
 label values numkdhh numkdhh
 label values numfmhh numfmhh
 label values intctfam intctfam
 label values parage14 parage14
 label values educmom educmom
 label values agemomb1 agemomb1
 label values fmarno fmarno
 label values rmarital rmarital
 label values ager_i ager_i
 label values fmarital_i fmarital_i
 label values educat_i educat_i
 label values hieduc_i hieduc_i
 label values hispanic_i hispanic_i
 label values race_i race_i
 label values hisprace_i hisprace_i
 label values numkdhh_i numkdhh_i
 label values numfmhh_i numfmhh_i
 label values intctfam_i intctfam_i
 label values parage14_i parage14_i
 label values educmom_i educmom_i
 label values agemomb1_i agemomb1_i
 label values fmarno_i fmarno_i
 label values rmarital_i rmarital_i
 label values hadsex hadsex
 label values sexonce sexonce
 label values firstpflag firstpflag
 label values fsexrltn fsexrltn
 label values sex1mthd1 sex1mthd1
 label values sex1mthd2 sex1mthd2
 label values sex1mthd3 sex1mthd3
 label values sex1mthd4 sex1mthd4
 label values orderflag orderflag
 label values sex3mo sex3mo
 label values sex12mo sex12mo
 label values lsexrltn lsexrltn
 label values lsexuse1 lsexuse1
 label values lsexuse2 lsexuse2
 label values lsexuse3 lsexuse3
 label values lsexuse4 lsexuse4
 label values meth12m1 meth12m1
 label values meth12m2 meth12m2
 label values meth12m3 meth12m3
 label values meth12m4 meth12m4
 label values meth3m1 meth3m1
 label values meth3m2 meth3m2
 label values meth3m3 meth3m3
 label values meth3m4 meth3m4
 label values nump3mos nump3mos
 label values lifprtnr lifprtnr
 label values parts1yr parts1yr
 label values cohever cohever
 label values evmarcoh evmarcoh
 label values marend1 marend1
 label values premarw1 premarw1
 label values cohstat cohstat
 label values cohout cohout
 label values b1premar b1premar
 label values marbaby1 marbaby1
 label values cebow cebow
 label values cebowc cebowc
 label values cebowp cebowp
 label values evrnopat evrnopat
 label values nonliveb nonliveb
 label values compreg compreg
 label values abortion abortion
 label values lossnum lossnum
 label values wantb01 wantb01
 label values wantb02 wantb02
 label values wantb03 wantb03
 label values wantb04 wantb04
 label values wantb05 wantb05
 label values wantb06 wantb06
 label values wantb07 wantb07
 label values wantb08 wantb08
 label values wantb09 wantb09
 label values wantb10 wantb10
 label values unintb5 unintb5
 label values hadsex_i hadsex_i
 label values sexonce_i sexonce_i
 label values vry1stsx_i vry1stsx_i
 label values vry1stag_i vry1stag_i
 label values fsexpage_i fsexpage_i
 label values fsexrltn_i fsexrltn_i
 label values sex1mthd1_i sex1mthd1_i
 label values sex1mthd2_i sex1mthd2_i
 label values sex1mthd3_i sex1mthd3_i
 label values sex1mthd4_i sex1mthd4_i
 label values lsexdate_i lsexdate_i
 label values sex3mo_i sex3mo_i
 label values sex12mo_i sex12mo_i
 label values lsexrage_i lsexrage_i
 label values lsexpage_i lsexpage_i
 label values lsexrltn_i lsexrltn_i
 label values lsexuse1_i lsexuse1_i
 label values lsexuse2_i lsexuse2_i
 label values lsexuse3_i lsexuse3_i
 label values lsexuse4_i lsexuse4_i
 label values meth12m1_i meth12m1_i
 label values meth12m2_i meth12m2_i
 label values meth12m3_i meth12m3_i
 label values meth12m4_i meth12m4_i
 label values meth3m1_i meth3m1_i
 label values meth3m2_i meth3m2_i
 label values meth3m3_i meth3m3_i
 label values meth3m4_i meth3m4_i
 label values nump3mos_i nump3mos_i
 label values lifprtnr_i lifprtnr_i
 label values parts1yr_i parts1yr_i
 label values cohever_i cohever_i
 label values evmarcoh_i evmarcoh_i
 label values mardat01_i mardat01_i
 label values marend1_i marend1_i
 label values mardis01_i mardis01_i
 label values mar1diss_i mar1diss_i
 label values premarw1_i premarw1_i
 label values cohab1_i cohab1_i
 label values cohstat_i cohstat_i
 label values cohout_i cohout_i
 label values coh1dur_i coh1dur_i
 label values datbaby1_i datbaby1_i
 label values agebaby1_i agebaby1_i
 label values b1premar_i b1premar_i
 label values marbaby1_i marbaby1_i
 label values cebow_i cebow_i
 label values cebowc_i cebowc_i
 label values cebowp_i cebowp_i
 label values evrnopat_i evrnopat_i
 label values nonliveb_i nonliveb_i
 label values compreg_i compreg_i
 label values abortion_i abortion_i
 label values lossnum_i lossnum_i
 label values wantb01_i wantb01_i
 label values wantb02_i wantb02_i
 label values wantb03_i wantb03_i
 label values wantb04_i wantb04_i
 label values wantb05_i wantb05_i
 label values wantb06_i wantb06_i
 label values wantb07_i wantb07_i
 label values wantb08_i wantb08_i
 label values wantb09_i wantb09_i
 label values wantb10_i wantb10_i
 label values unintb5_i unintb5_i
 label values dadtype dadtype
 label values dadtypu5 dadtypu5
 label values dadtyp518 dadtyp518
 label values numcru18 numcru18
 label values numncu18 numncu18
 label values supp12mo supp12mo
 label values dadtype_i dadtype_i
 label values dadtypu5_i dadtypu5_i
 label values dadtyp518_i dadtyp518_i
 label values numcru18_i numcru18_i
 label values numncu18_i numncu18_i
 label values supp12mo_i supp12mo_i
 label values intent intent
 label values addexp addexp
 label values intent_i intent_i
 label values addexp_i addexp_i
 label values insuranc insuranc
 label values infever infever
 label values evhivtst evhivtst
 label values insuranc_i insuranc_i
 label values infever_i infever_i
 label values evhivtst_i evhivtst_i
 label values metro metro
 label values religion religion
 label values laborfor laborfor
 label values metro_i metro_i
 label values religion_i religion_i
 label values laborfor_i laborfor_i
 label values poverty poverty
 label values totincr totincr
 label values pubassis pubassis
 label values poverty_i poverty_i
 label values totincr_i totincr_i
 label values pubassis_i pubassis_i
 

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

