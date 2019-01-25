#delimit ;

   infix
      year     1 - 20
      id_      21 - 40
      agewed   41 - 60
      divorce  61 - 80
      sibs     81 - 100
      childs   101 - 120
      age      121 - 140
      educ     141 - 160
      paeduc   161 - 180
      maeduc   181 - 200
      speduc   201 - 220
      degree   221 - 240
      padeg    241 - 260
      madeg    261 - 280
      spdeg    281 - 300
      sex      301 - 320
      race     321 - 340
      res16    341 - 360
      reg16    361 - 380
      srcbelt  381 - 400
      partyid  401 - 420
      pres04   421 - 440
      pres08   441 - 460
      pres12   461 - 480
      polviews 481 - 500
      natspac  501 - 520
      natenvir 521 - 540
      natheal  541 - 560
      natcity  561 - 580
      natcrime 581 - 600
      natdrug  601 - 620
      nateduc  621 - 640
      natrace  641 - 660
      natarms  661 - 680
      nataid   681 - 700
      natfare  701 - 720
      spkath   721 - 740
      colath   741 - 760
      libath   761 - 780
      spkhomo  781 - 800
      colhomo  801 - 820
      libhomo  821 - 840
      cappun   841 - 860
      gunlaw   861 - 880
      grass    881 - 900
      relig    901 - 920
      fund     921 - 940
      attend   941 - 960
      reliten  961 - 980
      postlife 981 - 1000
      pray     1001 - 1020
      relig16  1021 - 1040
      fund16   1041 - 1060
      sprel16  1061 - 1080
      prayer   1081 - 1100
      bible    1101 - 1120
      racmar   1121 - 1140
      racpres  1141 - 1160
      affrmact 1161 - 1180
      happy    1181 - 1200
      hapmar   1201 - 1220
      health   1221 - 1240
      life     1241 - 1260
      helpful  1261 - 1280
      fair     1281 - 1300
      trust    1301 - 1320
      conclerg 1321 - 1340
      coneduc  1341 - 1360
      confed   1361 - 1380
      conpress 1381 - 1400
      conjudge 1401 - 1420
      conlegis 1421 - 1440
      conarmy  1441 - 1460
      satjob   1461 - 1480
      class_   1481 - 1500
      satfin   1501 - 1520
      finrela  1521 - 1540
      union_   1541 - 1560
      fepol    1561 - 1580
      abany    1581 - 1600
      chldidel 1601 - 1620
      sexeduc  1621 - 1640
      premarsx 1641 - 1660
      xmarsex  1661 - 1680
      homosex  1681 - 1700
      spanking 1701 - 1720
      fear     1721 - 1740
      owngun   1741 - 1760
      pistol   1761 - 1780
      hunt     1781 - 1800
      phone    1801 - 1820
      memchurh 1821 - 1840
      realinc  1841 - 1860
      cohort   1861 - 1880
      marcohrt 1881 - 1900
      ballot   1901 - 1920
      wtssall  1921 - 1940
      adults   1941 - 1960
      compuse  1961 - 1980
      databank 1981 - 2000
      wtssnr   2001 - 2020
using GSS.dat;

label variable year     "Gss year for this respondent                       ";
label variable id_      "Respondent id number";
label variable agewed   "Age when first married";
label variable divorce  "Ever been divorced or separated";
label variable sibs     "Number of brothers and sisters";
label variable childs   "Number of children";
label variable age      "Age of respondent";
label variable educ     "Highest year of school completed";
label variable paeduc   "Highest year school completed, father";
label variable maeduc   "Highest year school completed, mother";
label variable speduc   "Highest year school completed, spouse";
label variable degree   "Rs highest degree";
label variable padeg    "Fathers highest degree";
label variable madeg    "Mothers highest degree";
label variable spdeg    "Spouses highest degree";
label variable sex      "Respondents sex";
label variable race     "Race of respondent";
label variable res16    "Type of place lived in when 16 yrs old";
label variable reg16    "Region of residence, age 16";
label variable srcbelt  "Src beltcode";
label variable partyid  "Political party affiliation";
label variable pres04   "Vote for kerry, bush, nader";
label variable pres08   "Vote obama or mccain";
label variable pres12   "Vote obama or romney";
label variable polviews "Think of self as liberal or conservative";
label variable natspac  "Space exploration program";
label variable natenvir "Improving & protecting environment";
label variable natheal  "Improving & protecting nations health";
label variable natcity  "Solving problems of big cities";
label variable natcrime "Halting rising crime rate";
label variable natdrug  "Dealing with drug addiction";
label variable nateduc  "Improving nations education system";
label variable natrace  "Improving the conditions of blacks";
label variable natarms  "Military, armaments, and defense";
label variable nataid   "Foreign aid";
label variable natfare  "Welfare";
label variable spkath   "Allow anti-religionist to speak";
label variable colath   "Allow anti-religionist to teach";
label variable libath   "Allow anti-religious book in library";
label variable spkhomo  "Allow homosexual to speak";
label variable colhomo  "Allow homosexual to teach";
label variable libhomo  "Allow homosexuals book in library";
label variable cappun   "Favor or oppose death penalty for murder";
label variable gunlaw   "Favor or oppose gun permits";
label variable grass    "Should marijuana be made legal";
label variable relig    "Rs religious preference";
label variable fund     "How fundamentalist is r currently";
label variable attend   "How often r attends religious services";
label variable reliten  "Strength of affiliation";
label variable postlife "Belief in life after death";
label variable pray     "How often does r pray";
label variable relig16  "Religion in which raised";
label variable fund16   "How fundamentalist was r at age 16";
label variable sprel16  "Religion in which spouse raised";
label variable prayer   "Bible prayer in public schools";
label variable bible    "Feelings about the bible";
label variable racmar   "Favor law against racial intermarriage";
label variable racpres  "Would vote for black president";
label variable affrmact "Favor preference in hiring blacks";
label variable happy    "General happiness";
label variable hapmar   "Happiness of marriage";
label variable health   "Condition of health";
label variable life     "Is life exciting or dull";
label variable helpful  "People helpful or looking out for selves";
label variable fair     "People fair or try to take advantage";
label variable trust    "Can people be trusted";
label variable conclerg "Confidence in organized religion";
label variable coneduc  "Confidence in education";
label variable confed   "Confid. in exec branch of fed govt";
label variable conpress "Confidence in press";
label variable conjudge "Confid. in united states supreme court";
label variable conlegis "Confidence in congress";
label variable conarmy  "Confidence in military";
label variable satjob   "Job or housework";
label variable class_   "Subjective class identification";
label variable satfin   "Satisfaction with financial situation";
label variable finrela  "Opinion of family income";
label variable union_   "Does r or spouse belong to union";
label variable fepol    "Women not suited for politics";
label variable abany    "Abortion if woman wants for any reason";
label variable chldidel "Ideal number of children";
label variable sexeduc  "Sex education in public schools";
label variable premarsx "Sex before marriage";
label variable xmarsex  "Sex with person other than spouse";
label variable homosex  "Homosexual sex relations";
label variable spanking "Favor spanking to discipline child";
label variable fear     "Afraid to walk at night in neighborhood";
label variable owngun   "Have gun in home";
label variable pistol   "Pistol or revolver in home";
label variable hunt     "Does r or spouse hunt";
label variable phone    "Does r have telephone";
label variable memchurh "Membership in church group";
label variable realinc  "Family income in constant $";
label variable cohort   "Year of birth";
label variable marcohrt "Year of first marriage";
label variable ballot   "Ballot used for interview";
label variable wtssall  "Weight variable";
label variable adults   "Household members 18 yrs and older";
label variable compuse  "R use computer";
label variable databank "Computer data threat to individual privacy";
label variable wtssnr   "Weight variable";


label define gsp001x
   99       "No answer"
   98       "Don't know"
   0        "Not applicable"
;
label define gsp002x
   9        "No answer"
   8        "Don't know"
   2        "No"
   1        "Yes"
   0        "Not applicable"
;
label define gsp003x
   99       "No answer"
   98       "Don't know"
   -1       "Not applicable"
;
label define gsp004x
   9        "Dk na"
   8        "Eight or more"
;
label define gsp005x
   99       "No answer"
   98       "Don't know"
   89       "89 or older"
;
label define gsp006x
   99       "No answer"
   98       "Don't know"
   97       "Not applicable"
;
label define gsp007x
   99       "No answer"
   98       "Don't know"
   97       "Not applicable"
;
label define gsp008x
   99       "No answer"
   98       "Don't know"
   97       "Not applicable"
;
label define gsp009x
   99       "No answer"
   98       "Don't know"
   97       "Not applicable"
;
label define gsp010x
   9        "No answer"
   8        "Don't know"
   7        "Not applicable"
   4        "Graduate"
   3        "Bachelor"
   2        "Junior college"
   1        "High school"
   0        "Lt high school"
;
label define gsp011x
   9        "No answer"
   8        "Don't know"
   7        "Not applicable"
   4        "Graduate"
   3        "Bachelor"
   2        "Junior college"
   1        "High school"
   0        "Lt high school"
;
label define gsp012x
   9        "No answer"
   8        "Don't know"
   7        "Not applicable"
   4        "Graduate"
   3        "Bachelor"
   2        "Junior college"
   1        "High school"
   0        "Lt high school"
;
label define gsp013x
   9        "No answer"
   8        "Don't know"
   7        "Not applicable"
   4        "Graduate"
   3        "Bachelor"
   2        "Junior college"
   1        "High school"
   0        "Lt high school"
;
label define gsp014x
   2        "Female"
   1        "Male"
;
label define gsp015x
   3        "Other"
   2        "Black"
   1        "White"
   0        "Not applicable"
;
label define gsp016x
   9        "No answer"
   8        "Don't know"
   6        "City gt 250000"
   5        "Big-city suburb"
   4        "50000 to 250000"
   3        "Town lt 50000"
   2        "Farm"
   1        "Country,nonfarm"
   0        "Not applicable"
;
label define gsp017x
   9        "Pacific"
   8        "Mountain"
   7        "W. sou. central"
   6        "E. sou. central"
   5        "South atlantic"
   4        "W. nor. central"
   3        "E. nor. central"
   2        "Middle atlantic"
   1        "New england"
   0        "Foreign"
;
label define gsp018x
   6        "Other rural"
   5        "Other urban"
   4        "Suburb, 13-100"
   3        "Suburb, 12 lrgst"
   2        "Smsa's 13-100"
   1        "12 lrgst smsa's"
   0        "Not assigned"
;
label define gsp019x
   9        "No answer"
   8        "Don't know"
   7        "Other party"
   6        "Strong republican"
   5        "Not str republican"
   4        "Ind,near rep"
   3        "Independent"
   2        "Ind,near dem"
   1        "Not str democrat"
   0        "Strong democrat"
;
label define gsp020x
   9        "No answer"
   8        "Dont know"
   6        "Didnt vote"
   4        "Other (specify)"
   3        "Nader"
   2        "Bush"
   1        "Kerry"
   0        "Not applicable"
;
label define gsp021x
   9        "No answer"
   8        "Don't know"
   4        "Didn't vote"
   3        "Other candidate (specify)"
   2        "Mccain"
   1        "Obama"
   0        "Not applicable"
;
label define gsp022x
   9        "No answer"
   8        "Don't know"
   4        "Didn't vote for president"
   3        "Other candidate (specify)"
   2        "Romney"
   1        "Obama"
   0        "Not applicable"
;
label define gsp023x
   9        "No answer"
   8        "Don't know"
   7        "Extrmly conservative"
   6        "Conservative"
   5        "Slghtly conservative"
   4        "Moderate"
   3        "Slightly liberal"
   2        "Liberal"
   1        "Extremely liberal"
   0        "Not applicable"
;
label define gsp024x
   9        "No answer"
   8        "Don't know"
   3        "Too much"
   2        "About right"
   1        "Too little"
   0        "Not applicable"
;
label define gsp025x
   9        "No answer"
   8        "Don't know"
   3        "Too much"
   2        "About right"
   1        "Too little"
   0        "Not applicable"
;
label define gsp026x
   9        "No answer"
   8        "Don't know"
   3        "Too much"
   2        "About right"
   1        "Too little"
   0        "Not applicable"
;
label define gsp027x
   9        "No answer"
   8        "Don't know"
   3        "Too much"
   2        "About right"
   1        "Too little"
   0        "Not applicable"
;
label define gsp028x
   9        "No answer"
   8        "Don't know"
   3        "Too much"
   2        "About right"
   1        "Too little"
   0        "Not applicable"
;
label define gsp029x
   9        "No answer"
   8        "Don't know"
   3        "Too much"
   2        "About right"
   1        "Too little"
   0        "Not applicable"
;
label define gsp030x
   9        "No answer"
   8        "Don't know"
   3        "Too much"
   2        "About right"
   1        "Too little"
   0        "Not applicable"
;
label define gsp031x
   9        "No answer"
   8        "Don't know"
   3        "Too much"
   2        "About right"
   1        "Too little"
   0        "Not applicable"
;
label define gsp032x
   9        "No answer"
   8        "Don't know"
   3        "Too much"
   2        "About right"
   1        "Too little"
   0        "Not applicable"
;
label define gsp033x
   9        "No answer"
   8        "Don't know"
   3        "Too much"
   2        "About right"
   1        "Too little"
   0        "Not applicable"
;
label define gsp034x
   9        "No answer"
   8        "Don't know"
   3        "Too much"
   2        "About right"
   1        "Too little"
   0        "Not applicable"
;
label define gsp035x
   9        "No answer"
   8        "Don't know"
   2        "Not allowed"
   1        "Allowed"
   0        "Not applicable"
;
label define gsp036x
   9        "No answer"
   8        "Don't know"
   5        "Not allowed"
   4        "Allowed"
   0        "Not applicable"
;
label define gsp037x
   9        "No answer"
   8        "Don't know"
   2        "Not remove"
   1        "Remove"
   0        "Not applicable"
;
label define gsp038x
   9        "No answer"
   8        "Don't know"
   2        "Not allowed"
   1        "Allowed"
   0        "Not applicable"
;
label define gsp039x
   9        "No answer"
   8        "Don't know"
   5        "Not allowed"
   4        "Allowed"
   0        "Not applicable"
;
label define gsp040x
   9        "No answer"
   8        "Don't know"
   2        "Not remove"
   1        "Remove"
   0        "Not applicable"
;
label define gsp041x
   9        "No answer"
   8        "Don't know"
   2        "Oppose"
   1        "Favor"
   0        "Not applicable"
;
label define gsp042x
   9        "No answer"
   8        "Don't know"
   2        "Oppose"
   1        "Favor"
   0        "Not applicable"
;
label define gsp043x
   9        "No answer"
   8        "Don't know"
   2        "Not legal"
   1        "Legal"
   0        "Not applicable"
;
label define gsp044x
   99       "No answer"
   98       "Don't know"
   13       "Inter-nondenominational"
   12       "Native american"
   11       "Christian"
   10       "Orthodox-christian"
   9        "Moslem/islam"
   8        "Other eastern"
   7        "Hinduism"
   6        "Buddhism"
   5        "Other"
   4        "None"
   3        "Jewish"
   2        "Catholic"
   1        "Protestant"
   0        "Not applicable"
;
label define gsp045x
   9        "Na-excluded"
   8        "Don't know"
   3        "Liberal"
   2        "Moderate"
   1        "Fundamentalist"
   0        "Not applicable"
;
label define gsp046x
   9        "Dk,na"
   8        "More thn once wk"
   7        "Every week"
   6        "Nrly every week"
   5        "2-3x a month"
   4        "Once a month"
   3        "Sevrl times a yr"
   2        "Once a year"
   1        "Lt once a year"
   0        "Never"
;
label define gsp047x
   9        "No answer"
   8        "Don't know"
   4        "No religion"
   3        "Somewhat strong"
   2        "Not very strong"
   1        "Strong"
   0        "Not applicable"
;
label define gsp048x
   9        "No answer"
   8        "Don't know"
   2        "No"
   1        "Yes"
   0        "Not applicable"
;
label define gsp049x
   9        "No answer"
   8        "Don't know"
   6        "Never"
   5        "Lt once a week"
   4        "Once a week"
   3        "Several times a week"
   2        "Once a day"
   1        "Several times a day"
   0        "Not applicable"
;
label define gsp050x
   99       "No answer"
   98       "Don't know"
   13       "Inter-nondenominational"
   12       "Native american"
   11       "Christian"
   10       "Orthodox-christian"
   9        "Moslem/islam"
   8        "Other eastern"
   7        "Hinduism"
   6        "Buddhism"
   5        "Other"
   4        "None"
   3        "Jewish"
   2        "Catholic"
   1        "Protestant"
   0        "Not applicable"
;
label define gsp051x
   9        "Na-excluded"
   8        "Don't know"
   3        "Liberal"
   2        "Moderate"
   1        "Fundamentalist"
   0        "Not applicable"
;
label define gsp052x
   9        "No answer"
   8        "Dont know"
   5        "Other"
   4        "None"
   3        "Jewish"
   2        "Catholic"
   1        "Protestant"
   0        "Not applicable"
;
label define gsp053x
   9        "No answer"
   8        "Don't know"
   2        "Disapprove"
   1        "Approve"
   0        "Not applicable"
;
label define gsp054x
   9        "No answer"
   8        "Don't know"
   4        "Other"
   3        "Book of fables"
   2        "Inspired word"
   1        "Word of god"
   0        "Not applicable"
;
label define gsp055x
   9        "No answer"
   8        "Don't know"
   2        "No"
   1        "Yes"
   0        "Not applicable"
;
label define gsp056x
   9        "No answer"
   8        "Don't know"
   2        "No"
   1        "Yes"
   0        "Not applicable"
;
label define gsp057x
   9        "No answer"
   8        "Don't know"
   4        "Strongly oppose pref"
   3        "Oppose pref"
   2        "Support pref"
   1        "Strongly support pref"
   0        "Not applicable"
;
label define gsp058x
   9        "No answer"
   8        "Don't know"
   3        "Not too happy"
   2        "Pretty happy"
   1        "Very happy"
   0        "Not applicable"
;
label define gsp059x
   9        "No answer"
   8        "Don't know"
   3        "Not too happy"
   2        "Pretty happy"
   1        "Very happy"
   0        "Not applicable"
;
label define gsp060x
   9        "No answer"
   8        "Don't know"
   4        "Poor"
   3        "Fair"
   2        "Good"
   1        "Excellent"
   0        "Not applicable"
;
label define gsp061x
   9        "No answer"
   8        "Don't know"
   3        "Dull"
   2        "Routine"
   1        "Exciting"
   0        "Not applicable"
;
label define gsp062x
   9        "No answer"
   8        "Don't know"
   3        "Depends"
   2        "Lookout for self"
   1        "Helpful"
   0        "Not applicable"
;
label define gsp063x
   9        "No answer"
   8        "Don't know"
   3        "Depends"
   2        "Fair"
   1        "Take advantage"
   0        "Not applicable"
;
label define gsp064x
   9        "No answer"
   8        "Don't know"
   3        "Depends"
   2        "Cannot trust"
   1        "Can trust"
   0        "Not applicable"
;
label define gsp065x
   9        "No answer"
   8        "Don't know"
   3        "Hardly any"
   2        "Only some"
   1        "A great deal"
   0        "Not applicable"
;
label define gsp066x
   9        "No answer"
   8        "Don't know"
   3        "Hardly any"
   2        "Only some"
   1        "A great deal"
   0        "Not applicable"
;
label define gsp067x
   9        "No answer"
   8        "Don't know"
   3        "Hardly any"
   2        "Only some"
   1        "A great deal"
   0        "Not applicable"
;
label define gsp068x
   9        "No answer"
   8        "Don't know"
   3        "Hardly any"
   2        "Only some"
   1        "A great deal"
   0        "Not applicable"
;
label define gsp069x
   9        "No answer"
   8        "Don't know"
   3        "Hardly any"
   2        "Only some"
   1        "A great deal"
   0        "Not applicable"
;
label define gsp070x
   9        "No answer"
   8        "Don't know"
   3        "Hardly any"
   2        "Only some"
   1        "A great deal"
   0        "Not applicable"
;
label define gsp071x
   9        "No answer"
   8        "Don't know"
   3        "Hardly any"
   2        "Only some"
   1        "A great deal"
   0        "Not applicable"
;
label define gsp072x
   9        "No answer"
   8        "Don't know"
   4        "Very dissatisfied"
   3        "A little dissat"
   2        "Mod. satisfied"
   1        "Very satisfied"
   0        "Not applicable"
;
label define gsp073x
   9        "No answer"
   8        "Don't know"
   5        "No class"
   4        "Upper class"
   3        "Middle class"
   2        "Working class"
   1        "Lower class"
   0        "Not applicable"
;
label define gsp074x
   9        "No answer"
   8        "Don't know"
   3        "Not at all sat"
   2        "More or less"
   1        "Satisfied"
   0        "Not applicable"
;
label define gsp075x
   9        "No answer"
   8        "Don't know"
   5        "Far above average"
   4        "Above average"
   3        "Average"
   2        "Below average"
   1        "Far below average"
   0        "Not applicable"
;
label define gsp076x
   9        "No answer"
   8        "Don't know"
   4        "Neither belongs"
   3        "R and spouse belong"
   2        "Spouse belongs"
   1        "R belongs"
   0        "Not applicable"
;
label define gsp077x
   9        "No answer"
   8        "Not sure"
   2        "Disagree"
   1        "Agree"
   0        "Not applicable"
;
label define gsp078x
   9        "No answer"
   8        "Don't know"
   2        "No"
   1        "Yes"
   0        "Not applicable"
;
label define gsp079x
   9        "Dk,na"
   8        "As many as want"
   7        "Seven+"
   -1       "Not applicable"
;
label define gsp080x
   9        "No answer"
   8        "Don't know"
   3        "Depends"
   2        "Oppose"
   1        "Favor"
   0        "Not applicable"
;
label define gsp081x
   9        "No answer"
   8        "Don't know"
   5        "Other"
   4        "Not wrong at all"
   3        "Sometimes wrong"
   2        "Almst always wrg"
   1        "Always wrong"
   0        "Not applicable"
;
label define gsp082x
   9        "No answer"
   8        "Don't know"
   5        "Other"
   4        "Not wrong at all"
   3        "Sometimes wrong"
   2        "Almst always wrg"
   1        "Always wrong"
   0        "Not applicable"
;
label define gsp083x
   9        "No answer"
   8        "Don't know"
   5        "Other"
   4        "Not wrong at all"
   3        "Sometimes wrong"
   2        "Almst always wrg"
   1        "Always wrong"
   0        "Not applicable"
;
label define gsp084x
   9        "No answer"
   8        "Don't know"
   4        "Strongly disagree"
   3        "Disagree"
   2        "Agree"
   1        "Strongly agree"
   0        "Not applicable"
;
label define gsp085x
   9        "No answer"
   8        "Don't know"
   2        "No"
   1        "Yes"
   0        "Not applicable"
;
label define gsp086x
   9        "No answer"
   8        "Don't know"
   3        "Refused"
   2        "No"
   1        "Yes"
   0        "Not applicable"
;
label define gsp087x
   9        "No answer"
   8        "Don't know"
   3        "Refused"
   2        "No"
   1        "Yes"
   0        "Not applicable"
;
label define gsp088x
   9        "No answer"
   8        "Don't know"
   4        "Neither"
   3        "Both"
   2        "Spouse"
   1        "Resp"
   0        "Not applicable"
;
label define gsp089x
   9        "No answer"
   6        "Cellphone"
   5        "Phone,dk where"
   4        "Phone elsewhere"
   3        "Phone in home"
   2        "Refused"
   1        "No phone"
   0        "Not applicable"
;
label define gsp090x
   9        "No answer"
   8        "Don't know"
   2        "No"
   1        "Yes"
   0        "Not applicable"
;
label define gsp091x
   999999   "No answer"
   999998   "Dont know"
   0        "Not applicable"
;
label define gsp092x
   9999     "No answer"
   0        "Not applicable"
;
label define gsp093x
   9999     "No answer"
   0        "Not applicable"
;
label define gsp094x
   4        "Ballot d"
   3        "Ballot c"
   2        "Ballot b"
   1        "Ballot a"
   0        "Not applicable"
;
label define gsp095x
   9        "No answer"
   8        "8 or more"
;
label define gsp096x
   9        "No answer"
   8        "Don't know"
   2        "No"
   1        "Yes"
   0        "Not applicable"
;
label define gsp097x
   9        "No answer"
   8        "Cant choose"
   4        "Not a threat at all"
   3        "Not serious"
   2        "Fairly serious"
   1        "Very serious threat"
   0        "Not applicable"
;


label values agewed   gsp001x;
label values divorce  gsp002x;
label values sibs     gsp003x;
label values childs   gsp004x;
label values age      gsp005x;
label values educ     gsp006x;
label values paeduc   gsp007x;
label values maeduc   gsp008x;
label values speduc   gsp009x;
label values degree   gsp010x;
label values padeg    gsp011x;
label values madeg    gsp012x;
label values spdeg    gsp013x;
label values sex      gsp014x;
label values race     gsp015x;
label values res16    gsp016x;
label values reg16    gsp017x;
label values srcbelt  gsp018x;
label values partyid  gsp019x;
label values pres04   gsp020x;
label values pres08   gsp021x;
label values pres12   gsp022x;
label values polviews gsp023x;
label values natspac  gsp024x;
label values natenvir gsp025x;
label values natheal  gsp026x;
label values natcity  gsp027x;
label values natcrime gsp028x;
label values natdrug  gsp029x;
label values nateduc  gsp030x;
label values natrace  gsp031x;
label values natarms  gsp032x;
label values nataid   gsp033x;
label values natfare  gsp034x;
label values spkath   gsp035x;
label values colath   gsp036x;
label values libath   gsp037x;
label values spkhomo  gsp038x;
label values colhomo  gsp039x;
label values libhomo  gsp040x;
label values cappun   gsp041x;
label values gunlaw   gsp042x;
label values grass    gsp043x;
label values relig    gsp044x;
label values fund     gsp045x;
label values attend   gsp046x;
label values reliten  gsp047x;
label values postlife gsp048x;
label values pray     gsp049x;
label values relig16  gsp050x;
label values fund16   gsp051x;
label values sprel16  gsp052x;
label values prayer   gsp053x;
label values bible    gsp054x;
label values racmar   gsp055x;
label values racpres  gsp056x;
label values affrmact gsp057x;
label values happy    gsp058x;
label values hapmar   gsp059x;
label values health   gsp060x;
label values life     gsp061x;
label values helpful  gsp062x;
label values fair     gsp063x;
label values trust    gsp064x;
label values conclerg gsp065x;
label values coneduc  gsp066x;
label values confed   gsp067x;
label values conpress gsp068x;
label values conjudge gsp069x;
label values conlegis gsp070x;
label values conarmy  gsp071x;
label values satjob   gsp072x;
label values class_   gsp073x;
label values satfin   gsp074x;
label values finrela  gsp075x;
label values union_   gsp076x;
label values fepol    gsp077x;
label values abany    gsp078x;
label values chldidel gsp079x;
label values sexeduc  gsp080x;
label values premarsx gsp081x;
label values xmarsex  gsp082x;
label values homosex  gsp083x;
label values spanking gsp084x;
label values fear     gsp085x;
label values owngun   gsp086x;
label values pistol   gsp087x;
label values hunt     gsp088x;
label values phone    gsp089x;
label values memchurh gsp090x;
label values realinc  gsp091x;
label values cohort   gsp092x;
label values marcohrt gsp093x;
label values ballot   gsp094x;
label values adults   gsp095x;
label values compuse  gsp096x;
label values databank gsp097x;


