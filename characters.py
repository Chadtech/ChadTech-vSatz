
#### In this file all the character varieties are defined
#### THere can be up to 4096 different kinds of characters.
#### The 4096 cap is a consequnce of how documents are saved
#### (as a number stored in color values of 1 and a half pixels
#### (16 ^ 3)

#############################################################
#############################################################

#### Enumerate below are descriptions of each of the
#### Char object's properties

#### 0. 'lilimage' is a small image that is blitted (pasted)
#### if the character is a subscript or superscript

#### 1. 'image' is the image blitted when the character
#### is a plain ol' normal sized character item

#### 2. 'keys', keys is (usually) a tuple, whos elements
#### are sets of numbers. The numbers in the sets correpond
#### to keys that must be pressed to add that Char to 
#### Charray (prnounced 'Sherry', the Doc objects used)
#### The sets correspond to different key combinations
#### that an trigger the same Char. For example, a capital
#### 'A' can be triggered by a set of a, and left shift, or
#### a and right shift.

#### 3. 'keyDig' standing for 'Key Digits', is the unique
#### number corresponding to that Char. When the Char is
#### saved into an image, its the keyDig value that is
#### stored. The keyDigs are crucially linked to the
#### Charlets dictionary, who's keys are Char objects,
#### and whos values are numbers which MUST be the
#### Char's keyDig

#############################################################
#############################################################

#### Invisible Chars
#### These are characters they do not visibly appear in the text.
#### They usually dont even need to be stored in the document itself
#### The one notably exception is the enter key
#### For those that dont need to be saved their keydig is arbitrarily
#### stored as '255'

enter=Char(l_Frown,L_Frown,( set([ letCor['ENTER'] ]) ),113)
backspace=Char(l_Frown,L_Frown,(set ([ letCor['BACKSPACE'] ]) ),255)
rightarrow=Char(l_Frown,L_Frown,(set ([ letCor['RIGHTARROW'] ]) ),255)
leftarrow=Char(l_Frown,L_Frown,(set ([ letCor['LEFTARROW'] ]) ),255,)
uparrow=Char(l_Frown,L_Frown,(set ([ letCor['UPARROW'] ]) ),255)
downarrow=Char(l_Frown,L_Frown,(set ([ letCor['DOWNARROW'] ]) ),255)
save=Char(l_Frown,L_Frown,(set ([ letCor['LEFTCONTROL'],letCor['s'] ]),set ([ letCor['RIGHTCONTROL'],letCor['s'] ])),255)
oPen=Char(l_Frown,L_Frown,(set ([ letCor['LEFTCONTROL'],letCor['o'] ]),set ([ letCor['RIGHTCONTROL'],letCor['o'] ])),255)
superSet=Char(l_Frown,L_Frown,(set([ letCor['LEFTSHIFT'],letCor['EQUALS'] ]),set([ letCor['RIGHTSHIFT'],letCor['EQUALS'] ])),255)
subSet=Char(l_Frown,L_Frown,(set([ letCor['LEFTSHIFT'],letCor['HYPHEN'] ]),set([ letCor['RIGHTSHIFT'],letCor['HYPHEN'] ])),255)
greekSet = Char(l_Frown,L_Frown,(set([ letCor['TAB'], letCor['g'], ]), ), 255)
slantySet=Char(l_Frown,L_Frown,( set([ letCor['LEFTALT'],letCor['s'] ]), set([ letCor['RIGHTALT'],letCor['s'] ]) ), 255)
nothing=Char(l_Frown,L_Frown,set([ letCor['NOKEYS'] ]),255)
error=Char(l_Error,L_Error,set([ letCor['NOKEYS'] ]), 255)

############Visible Chars
#### These are the visible Chars in the text
#### They largely go in order of the keyDig, 
#### which in turn is just the order that I 
#### added them to the code.
#### 
#### Exceptions to the ordering are
#### noted in a comment
####
#### Exceptions have come about when
#### I find mistakes, or want to add
#### a Char to a category buried 
#### deep in the key dig sequence

#Space
space=Char(l_S,L_S,( set([ letCor['SPACE'] ]) ),53)

#Lower Case Chars 
lowercase__a=Char(l_la,L_la,( set([ letCor['a'] ]) ),1)
lowercase__b=Char(l_lb,L_lb,( set([ letCor['b'] ]) ),2)
lowercase__c=Char(l_lc,L_lc,( set([ letCor['c'] ]) ),3)
lowercase__d=Char(l_ld,L_ld,( set([ letCor['d'] ]) ),4)
lowercase__e=Char(l_le,L_le,( set([ letCor['e'] ]) ),5)
lowercase__f=Char(l_lf,L_lf,( set([ letCor['f'] ]) ),6)
lowercase__g=Char(l_lg,L_lg,( set([ letCor['g'] ]) ),7)
lowercase__h=Char(l_lh,L_lh,( set([ letCor['h'] ]) ),8)
lowercase__i=Char(l_li,L_li,( set([ letCor['i'] ]) ),9)
lowercase__j=Char(l_lj,L_lj,( set([ letCor['j'] ]) ),10)
lowercase__k=Char(l_lk,L_lk,( set([ letCor['k'] ]) ),11)
lowercase__l=Char(l_ll,L_ll,( set([ letCor['l'] ]) ),12)
lowercase__m=Char(l_lm,L_lm,( set([ letCor['m'] ]) ),13)
lowercase__n=Char(l_ln,L_ln,( set([ letCor['n'] ]) ),14)
lowercase__o=Char(l_lo,L_lo,( set([ letCor['o'] ]) ),15)
lowercase__p=Char(l_lp,L_lp,( set([ letCor['p'] ]) ),16)
lowercase__q=Char(l_lq,L_lq,( set([ letCor['q'] ]) ),17)
lowercase__r=Char(l_lr,L_lr,( set([ letCor['r'] ]) ),18)
lowercase__s=Char(l_ls,L_ls,( set([ letCor['s'] ]) ),19)
lowercase__t=Char(l_lt,L_lt,( set([ letCor['t'] ]) ),20)
lowercase__u=Char(l_lu,L_lu,( set([ letCor['u'] ]) ),21)
lowercase__v=Char(l_lv,L_lv,( set([ letCor['v'] ]) ),22)
lowercase__w=Char(l_lw,L_lw,( set([ letCor['w'] ]) ),23)
lowercase__x=Char(l_lx,L_lx,( set([ letCor['x'] ]) ),24)
lowercase__y=Char(l_ly,L_ly,( set([ letCor['y'] ]) ),25)
lowercase__z=Char(l_lz,L_lz,( set([ letCor['z'] ]) ),26)

#Upper Case Chars
uppercase__A=Char(l_lA,L_lA,( set([ letCor['a'], letCor['LEFTSHIFT'] ]), set([ letCor['a'], letCor['RIGHTSHIFT'] ]) ),27)
uppercase__B=Char(l_lB,L_lB,( set([ letCor['b'], letCor['LEFTSHIFT'] ]), set([ letCor['b'], letCor['RIGHTSHIFT'] ]) ),28)
uppercase__C=Char(l_lC,L_lC,( set([ letCor['c'], letCor['LEFTSHIFT'] ]), set([ letCor['c'], letCor['RIGHTSHIFT'] ]) ),29)
uppercase__D=Char(l_lD,L_lD,( set([ letCor['d'], letCor['LEFTSHIFT'] ]), set([ letCor['d'], letCor['RIGHTSHIFT'] ]) ),30)
uppercase__E=Char(l_lE,L_lE,( set([ letCor['e'], letCor['LEFTSHIFT'] ]), set([ letCor['e'], letCor['RIGHTSHIFT'] ]) ),31)
uppercase__F=Char(l_lF,L_lF,( set([ letCor['f'], letCor['LEFTSHIFT'] ]), set([ letCor['f'], letCor['RIGHTSHIFT'] ]) ),32)
uppercase__G=Char(l_lG,L_lG,( set([ letCor['g'], letCor['LEFTSHIFT'] ]), set([ letCor['g'], letCor['RIGHTSHIFT'] ]) ),33)
uppercase__H=Char(l_lH,L_lH,( set([ letCor['h'], letCor['LEFTSHIFT'] ]), set([ letCor['h'], letCor['RIGHTSHIFT'] ]) ),34)
uppercase__I=Char(l_lI,L_lI,( set([ letCor['i'], letCor['LEFTSHIFT'] ]), set([ letCor['i'], letCor['RIGHTSHIFT'] ]) ),35)
uppercase__J=Char(l_lJ,L_lJ,( set([ letCor['j'], letCor['LEFTSHIFT'] ]), set([ letCor['j'], letCor['RIGHTSHIFT'] ]) ),36)
uppercase__K=Char(l_lK,L_lK,( set([ letCor['k'], letCor['LEFTSHIFT'] ]), set([ letCor['k'], letCor['RIGHTSHIFT'] ]) ),37)
uppercase__L=Char(l_lL,L_lL,( set([ letCor['l'], letCor['LEFTSHIFT'] ]), set([ letCor['l'], letCor['RIGHTSHIFT'] ]) ),38)
uppercase__M=Char(l_lM,L_lM,( set([ letCor['m'], letCor['LEFTSHIFT'] ]), set([ letCor['m'], letCor['RIGHTSHIFT'] ]) ),39)
uppercase__N=Char(l_lN,L_lN,( set([ letCor['n'], letCor['LEFTSHIFT'] ]), set([ letCor['n'], letCor['RIGHTSHIFT'] ]) ),40)
uppercase__O=Char(l_lO,L_lO,( set([ letCor['o'], letCor['LEFTSHIFT'] ]), set([ letCor['o'], letCor['RIGHTSHIFT'] ]) ),41)
uppercase__P=Char(l_lP,L_lP,( set([ letCor['p'], letCor['LEFTSHIFT'] ]), set([ letCor['p'], letCor['RIGHTSHIFT'] ]) ),42)
uppercase__Q=Char(l_lQ,L_lQ,( set([ letCor['q'], letCor['LEFTSHIFT'] ]), set([ letCor['q'], letCor['RIGHTSHIFT'] ]) ),43)
uppercase__R=Char(l_lR,L_lR,( set([ letCor['r'], letCor['LEFTSHIFT'] ]), set([ letCor['r'], letCor['RIGHTSHIFT'] ]) ),44)
uppercase__S=Char(l_lS,L_lS,( set([ letCor['s'], letCor['LEFTSHIFT'] ]), set([ letCor['s'], letCor['RIGHTSHIFT'] ]) ),45)
uppercase__T=Char(l_lT,L_lT,( set([ letCor['t'], letCor['LEFTSHIFT'] ]), set([ letCor['t'], letCor['RIGHTSHIFT'] ]) ),46)
uppercase__U=Char(l_lU,L_lU,( set([ letCor['u'], letCor['LEFTSHIFT'] ]), set([ letCor['u'], letCor['RIGHTSHIFT'] ]) ),47)
uppercase__V=Char(l_lV,L_lV,( set([ letCor['v'], letCor['LEFTSHIFT'] ]), set([ letCor['v'], letCor['RIGHTSHIFT'] ]) ),48)
uppercase__W=Char(l_lW,L_lW,( set([ letCor['w'], letCor['LEFTSHIFT'] ]), set([ letCor['w'], letCor['RIGHTSHIFT'] ]) ),49)
uppercase__X=Char(l_lX,L_lX,( set([ letCor['x'], letCor['LEFTSHIFT'] ]), set([ letCor['x'], letCor['RIGHTSHIFT'] ]) ),50)
uppercase__Y=Char(l_lY,L_lY,( set([ letCor['y'], letCor['LEFTSHIFT'] ]), set([ letCor['y'], letCor['RIGHTSHIFT'] ]) ),51)
uppercase__Z=Char(l_lZ,L_lZ,( set([ letCor['z'], letCor['LEFTSHIFT'] ]), set([ letCor['z'], letCor['RIGHTSHIFT'] ]) ),52)


#################
#####Space is 53
#################

#Punctuation

punctuation__period=Char(l_punctuationPeriod,L_pPeriod,( set([ letCor['PERIOD'] ]) ),54)
punctuation__comma=Char(l_punctuationComma,L_pComma,( set([ letCor['COMMA'] ]) ),55)
punctuation__question=Char(l_punctuationQuestion,L_pQuestion,( set([ letCor['FORWARDSLASH'],letCor['LEFTSHIFT'] ]),set([ letCor['FORWARDSLASH'],letCor['RIGHTSHIFT'] ]) ),56)
punctuation__semicolon=Char(l_punctuationSemicolon,L_pSemicolon,( set([ letCor['SEMICOLON'] ]) ),57)
punctuation__colon=Char(l_punctuationColon,L_pColon,( set([ letCor['SEMICOLON'],letCor['LEFTSHIFT'] ]),set([ letCor['SEMICOLON'],letCor['RIGHTSHIFT'] ]) ),58)
punctuation__exclaimation=Char(l_punctuationExclaimation,L_pExclaimation,( set([ letCor['NUMERAL1'],letCor['LEFTSHIFT'] ]),set([ letCor['NUMERAL1'],letCor['RIGHTSHIFT'] ]) ),59)
punctuation__singlequote=Char(l_punctuationSinglequote,L_pSinglequote,( set([ letCor['SINGLEQUOTE'] ]) ),60)
punctuation__doublequote=Char(l_punctuationDoublequote,L_pDoublequote,( set([ letCor['LEFTSHIFT'], letCor['SINGLEQUOTE'] ]),set([ letCor['RIGHTSHIFT'], letCor['SINGLEQUOTE'] ]) ),61)

#Numerals

numeral__ze=Char(l_Nze,L_Nze,( set([ letCor['NUMERAL0'] ]) ),62)
numeral__on=Char(l_Non,L_Non,( set([ letCor['NUMERAL1'] ]) ),63)
numeral__tw=Char(l_Ntw,L_Ntw,( set([ letCor['NUMERAL2'] ]) ),64)
numeral__th=Char(l_Nth,L_Nth,( set([ letCor['NUMERAL3'] ]) ),65)
numeral__fo=Char(l_Nfo,L_Nfo,( set([ letCor['NUMERAL4'] ]) ),66)
numeral__fi=Char(l_Nfi,L_Nfi,( set([ letCor['NUMERAL5'] ]) ),67)
numeral__si=Char(l_Nsi,L_Nsi,( set([ letCor['NUMERAL6'] ]) ),68)
numeral__se=Char(l_Nse,L_Nse,( set([ letCor['NUMERAL7'] ]) ),69)
numeral__ei=Char(l_Nei,L_Nei,( set([ letCor['NUMERAL8'] ]) ),70)
numeral__ni=Char(l_Nni,L_Nni,( set([ letCor['NUMERAL9'] ]) ),71)

#Modal Logic

modallogic__possible=Char(l_modalPossible,L_mP,( set([ letCor['NUMERAL2'],letCor['p'] ]) ),72)
modallogic__necessary=Char(l_modalNecessary,L_mN,( set([ letCor['NUMERAL2'],letCor['n'] ]) ),73)

#First Order Logic

firstorderlogic__existential=Char(l_firstorderExistential,L_firstorderExistential,( set([ letCor['NUMERAL1'],letCor['e'] ]) ),74)
firstorderlogic__forall=Char(l_firstorderForall,L_firstorderForall,( set([ letCor['NUMERAL1'],letCor['a'] ]) ),75)
firstorderlogic__negation=Char(l_firstorderNegation,L_firstorderNegation,( set([ letCor['NUMERAL1'],letCor['n'] ]) ),76)
firstorderlogic__implication=Char(l_firstorderImplication,L_firstorderImplication,( set([ letCor['NUMERAL1'],letCor['i'] ]) ),77)
firstorderlogic__iff=Char(l_firstorderIff,L_firstorderIff,( set([ letCor['NUMERAL1'],letCor['f'] ]) ),78)
firstorderlogic__xor=Char(l_firstorderXor,L_firstorderXor,( set([ letCor['NUMERAL1'],letCor['x'] ]) ),79)
firstorderlogic__nand=Char(l_firstorderNand,L_firstorderNand,( set([ letCor['NUMERAL1'],letCor['d'] ]) ),80)
firstorderlogic__and=Char(l_firstorderAnd,L_firstorderAnd, ( set([ letCor['NUMERAL1'],letCor['PERIOD'] ]) ),81)

# Math

math__equals=Char(l_mEquals,L_mEquals,( set([ letCor['EQUALS'] ]) ),82)
math__greaterthan=Char(l_mGreaterThan,L_mGreaterThan,( set([ letCor['PERIOD'],letCor['RIGHTSHIFT'] ]), set([ letCor['PERIOD'],letCor['LEFTSHIFT'] ]), ), 83)
math__greaterthanorequal=Char(l_mGreaterThanOrEqual,L_mGreaterThanOrEqual, ( set([ letCor['EQUALS'],letCor['PERIOD'] ]), ), 84)
math__lessthan=Char(l_mLessThan,L_mLessThan,( set([ letCor['COMMA'],letCor['RIGHTSHIFT']]),set([ letCor['COMMA'],letCor['LEFTSHIFT'] ]), ), 85)
math__lessthanorequal=Char(l_mLessThanOrEqual,L_mLessThanOrEqual,( set([ letCor['EQUALS'],letCor['COMMA'] ]), ), 86)
math__division=Char(l_mDivision,L_mDivision,( set([ letCor['EQUALS'],letCor['d']]), ), 87)
math__approximately=Char(l_mApproximately,L_mApproximately,( set([ letCor['EQUALS'],letCor['a'],]), ),88)
math__plus=Char(l_mPlus,L_mPlus,( set([ letCor['EQUALS'],letCor['p'] ]), ),89)
math__minus=Char(l_mMinus,L_mMinus,( set([ letCor['HYPHEN'] ]), ),90)
math__multiply=Char(l_mMultiply,L_mMultiply,( set([ letCor['EQUALS'],letCor['m']]), ),91)
math__forwardslash=Char(l_mForwardSlash,L_mForwardSlash,( set([ letCor['FORWARDSLASH'] ]), ),92)
math__backslash=Char(l_mBackSlash,L_mBackSlash,( set([ letCor['BACKSLASH'] ]), ),93)
math__QED=Char(l_mQED,L_mQED,( set([ letCor['EQUALS'],letCor['q'] ]), ),94)
math__squareroot=Char(l_mSquareRoot,L_mSquareRoot,( set([ letCor['EQUALS'],letCor['s'] ]), ),95)
math__plusminus=Char(l_mPlusMinus,L_mPlusMinus,( set([ letCor['EQUALS'],letCor['l'] ]), ),96)
math__integral=Char(l_mIntegral,L_mIntegral,( set([ letCor['EQUALS'],letCor['f']]), ),97)
math__notequal=Char(l_mNotEqual,L_mNotEqual,( set([ letCor['EQUALS'],letCor['n']]), ),98)
math__angle=Char(l_mAngle,L_mAngle,( set([ letCor['EQUALS'], letCor['g'] ]), ),99)
math__triangle=Char(l_mTriangle,L_mTriangle,( set([ letCor['EQUALS'],letCor['t'] ]), ),100)
math__gradient=Char(l_mUpsideDownTriangle,L_mUpsideDownTriangle,( set([ letCor['EQUALS'], letCor['r'] ]), ),101)
math__divides=Char(l_mDivides,L_mDivides,(  set([ letCor['LEFTSHIFT'],letCor['BACKSLASH']]),set([ letCor['RIGHTSHIFT'],letCor['BACKSLASH']]) ),102)
math__doesntdivide=Char(l_mDoesntDivide,L_mDoesntDivide,( set([ letCor['EQUALS'],letCor['c'] ]), ), 103)
math__infinity=Char(l_mInfinity,L_mInfinity,( set([ letCor['EQUALS'],letCor['i'] ]), ), 104)

#Brackets

brackets__leftparentheses=Char(l_bLeftParenthesis,L_bLeftParenthesis,( set([ letCor['NUMERAL9'], letCor['LEFTSHIFT'] ]), set([ letCor['NUMERAL9'],letCor['RIGHTSHIFT'] ]), ), 105)
brackets__rightparentheses=Char(l_bRightParenthesis,L_bRightParenthesis,( set([ letCor['NUMERAL0'], letCor['LEFTSHIFT'] ]), set([ letCor['NUMERAL0'], letCor['RIGHTSHIFT'] ]), ), 106)
brackets__leftbracket=Char(l_bLeftBracket,L_bLeftBracket,( set([ letCor['LEFTBRACKET'] ]), ), 107)
brackets__rightbracket=Char(l_bRightBracket,L_bRightBracket,( set([ letCor['RIGHTBRACKET'] ]), ), 108)
brackets__leftcurly=Char(l_bLeftCurly,L_bLeftCurly,( set([ letCor['LEFTBRACKET'],letCor['LEFTSHIFT'] ]),set([ letCor['LEFTBRACKET'],letCor['RIGHTSHIFT'] ]) ), 109)
brackets__rightcurly=Char(l_bRightCurly,L_bRightCurly,( set([ letCor['RIGHTBRACKET'],letCor['LEFTSHIFT'] ]),set([ letCor['RIGHTBRACKET'],letCor['RIGHTSHIFT'] ]) ), 110)
brackets__leftchevron=Char(l_bLeftChevron,L_bLeftChevron,( set([ letCor['c'], letCor['LEFTBRACKET'] ]), ), 111)
brackets__rightchevron=Char(l_bRightChevron,L_bRightChevron,( set([ letCor['c'], letCor['RIGHTBRACKET'] ]), ), 112)

#################
#113 is enter
#################

#Misc

misc__numbersign=Char(l_miscNumbersign,L_miscNumbersign,( set([ letCor['NUMERAL3'], letCor['LEFTSHIFT'] ]), set([ letCor['NUMERAL3'],letCor['RIGHTSHIFT'] ]) ),114 )
misc__dollarsign=Char(l_miscDollarsign,L_miscDollarsign,( set([ letCor['NUMERAL4'], letCor['LEFTSHIFT'] ]), set([ letCor['NUMERAL4'],letCor['RIGHTSHIFT'] ]) ),115 )
misc__percentsign=Char(l_miscPercentsign,L_miscPercentsign,( set([ letCor['NUMERAL5'], letCor['LEFTSHIFT'] ]), set([ letCor['NUMERAL5'],letCor['RIGHTSHIFT'] ]) ),116 )
misc__ambersand=Char(l_miscAmbersand,L_miscAmbersand,( set([ letCor['NUMERAL7'], letCor['LEFTSHIFT'] ]), set([ letCor['NUMERAL7'],letCor['RIGHTSHIFT'] ]) ), 117)
misc__atsign=Char(l_miscAtsign,L_miscAtsign,( set([ letCor['NUMERAL2'],letCor['LEFTSHIFT'] ]), set([ letCor['NUMERAL2'],letCor['RIGHTSHIFT'] ]) ), 118)
misc__carrot=Char(l_miscCarrot,L_miscCarrot,( set([ letCor['NUMERAL6'],letCor['LEFTSHIFT'] ]), set([ letCor['NUMERAL6'],letCor['RIGHTSHIFT'] ]) ), 119)

#proof theory

prooftheory__singleturnstile=Char(l_pSingleturnstile,L_pSingleturnstile,( set([ letCor['NUMERAL0'],letCor['s'] ]), ), 120)
prooftheory__notsingleturnstile=Char(l_pNotsingleturnstile,L_pNotsingleturnstile,( set([ letCor['NUMERAL0'],letCor['x'] ]), ), 121)
prooftheory__doubleturnstile=Char(l_pDoubleturnstile,L_pDoubleturnstile,( set([ letCor['NUMERAL0'],letCor['d'] ]), ), 122)
prooftheory__notdoubleturnstile=Char(l_pNotdoubleturnstile,L_pNotdoubleturnstile,( set([ letCor['NUMERAL0'],letCor['c'] ]), ), 123)
prooftheory__logicalconstant=Char(l_pLogicalconstant,L_pLogicalconstant,( set([ letCor['NUMERAL0'],letCor['l'] ]), ), 124)

#set theory

settheory__elementof=Char(l_settheoryElementof,L_settheoryElementof,( set([ letCor['NUMERAL9'],letCor['e'] ]), ), 125)
settheory__notelementof=Char(l_settheoryNotelementof,L_settheoryNotelementof, ( set([ letCor['NUMERAL9'],letCor['d'] ]), ), 126 )
settheory__nullset=Char(l_settheoryNullset, L_settheoryNullset, ( set([ letCor['NUMERAL9'],letCor['n'] ]), ), 127)
settheory__intersection=Char(l_settheoryIntersection, L_settheoryIntersection, ( set([ letCor['NUMERAL9'],letCor['i'] ]), ), 128)
settheory__union=Char(l_settheoryUnion, L_settheoryUnion, ( set([ letCor['NUMERAL9'],letCor['u'] ]),), 129)
settheory__superset=Char(l_settheorySuperset, L_settheorySuperset, ( set([ letCor['NUMERAL9'], letCor['a'] ]), ), 130)
settheory__subset=Char(l_settheorySubset, L_settheorySubset, ( set([ letCor['NUMERAL9'],letCor['s'] ]), ), 131)
settheory__notsuperset=Char(l_settheoryNotsuperset,L_settheoryNotsuperset, ( set([ letCor['NUMERAL9'],letCor['z'] ]),), 132)
settheory__notsubset=Char(l_settheoryNotsubset,L_settheoryNotsubset, ( set([ letCor['NUMERAL9'], letCor['x'] ]), ), 133)

#################
#134 is error
#################

#Slanty

slanty__a=Char(l_Error,L_sa,( set ([ letCor[ 'a' ] ]), ), 135)
slanty__b=Char(l_Error,L_sb,( set ([ letCor[ 'b' ] ]), ), 136)
slanty__c=Char(l_Error,L_sc,( set ([ letCor[ 'c' ] ]), ), 137)
slanty__d=Char(l_Error,L_sd,( set ([ letCor[ 'd' ] ]), ), 138)
slanty__e=Char(l_Error,L_se,( set ([ letCor[ 'e' ] ]), ), 139)
slanty__f=Char(l_Error,L_sf,( set ([ letCor[ 'f' ] ]), ), 140)
slanty__g=Char(l_Error,L_sg,( set ([ letCor[ 'g' ] ]), ), 141)
slanty__h=Char(l_Error,L_sh,( set ([ letCor[ 'h' ] ]), ), 142)
slanty__i=Char(l_Error,L_si,( set ([ letCor[ 'i' ] ]), ), 143)
slanty__j=Char(l_Error,L_sj,( set ([ letCor[ 'j' ] ]), ), 144)
slanty__k=Char(l_Error,L_sk,( set ([ letCor[ 'k' ] ]), ), 145)
slanty__l=Char(l_Error,L_sl,( set ([ letCor[ 'l' ] ]), ), 146)
slanty__m=Char(l_Error,L_sm,( set ([ letCor[ 'm' ] ]), ), 147)
slanty__n=Char(l_Error,L_sn,( set ([ letCor[ 'n' ] ]), ), 148)
slanty__o=Char(l_Error,L_so,( set ([ letCor[ 'o' ] ]), ), 149)
slanty__p=Char(l_Error,L_sp,( set ([ letCor[ 'p' ] ]), ), 150)
slanty__q=Char(l_Error,L_sq,( set ([ letCor[ 'q' ] ]), ), 151)
slanty__r=Char(l_Error,L_sr,( set ([ letCor[ 'r' ] ]), ), 152)
slanty__s=Char(l_Error,L_ss,( set ([ letCor[ 's' ] ]), ), 153)
slanty__t=Char(l_Error,L_st,( set ([ letCor[ 't' ] ]), ), 154)
slanty__u=Char(l_Error,L_su,( set ([ letCor[ 'u' ] ]), ), 155)
slanty__v=Char(l_Error,L_sv,( set ([ letCor[ 'v' ] ]), ), 156)
slanty__w=Char(l_Error,L_sw,( set ([ letCor[ 'w' ] ]), ), 157)
slanty__x=Char(l_Error,L_sx,( set ([ letCor[ 'x' ] ]), ), 158)
slanty__y=Char(l_Error,L_sy,( set ([ letCor[ 'y' ] ]), ), 159)
slanty__z=Char(l_Error,L_sz,( set ([ letCor[ 'z' ] ]), ), 160)

#################
# 161 is a super script code
# 162 is a sub script code
#################

#### This is a first order character, categoried above. 
#### placed here to preserve the keyDig order

firstorderlogic__altnegation = Char(l_firstorderAltnegation,L_firstorderAltnegation,( set([ letCor['NUMERAL1'],letCor['b'] ]) ), 163)

#Alexander Hamilton
hamilton__On = Char(l_Error, L_hOn, ( set([ letCor['NUMERAL4'],letCor['a'] ]), ), 164)
hamilton__Tw = Char(l_Error, L_hTw, ( set([ letCor['NUMERAL4'],letCor['l'] ]), ), 165)
hamilton__Th = Char(l_Error, L_hTh, ( set([ letCor['NUMERAL4'],letCor['e'] ]), ), 166)
hamilton__Fo = Char(l_Error, L_hFo, ( set([ letCor['NUMERAL4'],letCor['x'] ]), ), 167)


#### Greek Symbols
#### Lowercase
greek_lowercasealpha = Char(l_lAlpha,L_lAlpha, ( set([ letCor['a'] ]) ), 168)
greek_lowercasebeta = Char(l_lBeta,L_lBeta, ( set([ letCor['b'] ]) ), 169 )
greek_lowercasegamma = Char(l_lGamma,L_lGamma, ( set([  letCor['g'] ]) ), 170)
greek_lowercasedelta = Char(l_lDelta,L_lDelta, ( set([ letCor['d'] ]) ), 171)
greek_lowercaseepsilon = Char(l_lEpsilon, L_lEpsilon, ( set([ letCor['e'] ]) ), 172)
greek_lowercasezeta = Char(l_lZeta, L_lZeta, (set([letCor['z'] ]) ), 173)
greek_lowercaseeta = Char(l_lEta, L_lEta, (set([ letCor['i'] ]) ), 174)
greek_lowercasetheta = Char(l_lTheta, L_lTheta, (set([ letCor['h'] ]) ), 175)
greek_lowercaseiota = Char(l_lIota, L_lIota, (set([letCor['j'] ]) ), 176)
greek_lowercasekappa = Char(l_lKappa, L_lKappa, (set([  letCor['k'] ]) ), 177)
greek_lowercaselambda = Char(l_lLambda, L_lLambda, (set([ letCor['l'] ]) ), 178)
greek_lowercasemu = Char(l_lMu, L_lMu, (set([letCor['m']]) ), 179)
greek_lowercasenu = Char(l_lNu, L_lNu, (set([letCor['n']]) ), 180)
greek_lowercasexi = Char(l_lXi, L_lXi, (set([letCor['x'] ]) ), 181)
greek_lowercaseomicron = Char(l_lOmicron, L_lOmicron, (set([letCor['o'] ]) ), 182)
greek_lowercasepi = Char(l_lPi, L_lPi, (set([letCor['p'] ]) ), 183)
greek_lowercaserho = Char(l_lRho, L_lRho, (set([letCor['r'], ]) ), 184)
greek_lowercasesigma = Char(l_lSigma, L_lSigma, (set([letCor['s'] ]) ), 185)
greek_lowercasetau = Char(l_lTau, L_lTau, (set([ letCor['t'] ])), 186)
greek_lowercaseupsilon = Char(l_lUpsilon, L_lUpsilon, (set([ letCor['y'] ]) ), 187)
greek_lowercasephi = Char(l_lPhi, L_lPhi, (set([ letCor['f'] ]) ), 188)
greek_lowercasechi = Char(l_lChi, L_lChi, (set([ letCor['c'] ]) ), 189)
greek_lowercasepsi = Char(l_lPsi, L_lPsi, (set([ letCor['q'] ]) ), 190)
greek_lowercaseomega = Char(l_lOmega, L_lOmega, (set([ letCor['w'] ]) ), 191)

#### Upper case Greek
greek_uppercasealpha = Char(l_LAlpha,L_LAlpha, ( set([ letCor['a'], letCor['LEFTSHIFT'] ]), set([ letCor['a'], letCor['RIGHTSHIFT'] ]) ), 192)
greek_uppercasebeta = Char(l_LBeta,L_LBeta, ( set([ letCor['b'], letCor['LEFTSHIFT'] ]), set([ letCor['b'], letCor['RIGHTSHIFT'] ])), 193 )
greek_uppercasegamma = Char(l_LGamma,L_LGamma, ( set([  letCor['g'], letCor['LEFTSHIFT'] ]),set([  letCor['g'], letCor['RIGHTSHIFT'] ]) ), 194)
greek_uppercasedelta = Char(l_LDelta,L_LDelta, ( set([ letCor['d'], letCor['LEFTSHIFT'] ]),set([ letCor['d'], letCor['RIGHTSHIFT'] ]) ), 195)
greek_uppercaseepsilon = Char(l_LEpsilon, L_LEpsilon, ( set([ letCor['e'], letCor['LEFTSHIFT'] ]) ,set([ letCor['e'], letCor['RIGHTSHIFT'] ]) ), 196)
greek_uppercasezeta = Char(l_LZeta, L_LZeta, (set([letCor['z'], letCor['LEFTSHIFT'] ]), set([letCor['z'], letCor['RIGHTSHIFT'] ])), 197)
greek_uppercaseeta = Char(l_LEta, L_LEta, (set([ letCor['i'], letCor['LEFTSHIFT'] ]), set([letCor['i'], letCor['RIGHTSHIFT'] ]) ), 198)
greek_uppercasetheta = Char(l_LTheta, L_LTheta, (set([ letCor['h'], letCor['LEFTSHIFT'] ]),set([letCor['h'], letCor['RIGHTSHIFT'] ]) ), 199)
greek_uppercaseiota = Char(l_LIota, L_LIota, (set([letCor['j'], letCor['LEFTSHIFT'] ]), set([letCor['j'], letCor['RIGHTSHIFT'] ])), 200)
greek_uppercasekappa = Char(l_LKappa, L_LKappa, (set([  letCor['k'], letCor['LEFTSHIFT'] ]), set([letCor['k'], letCor['RIGHTSHIFT'] ])), 201)
greek_uppercaselambda = Char(l_LLambda, L_LLambda, (set([ letCor['l'], letCor['LEFTSHIFT'] ]), set([letCor['l'], letCor['RIGHTSHIFT'] ])), 202)
greek_uppercasemu = Char(l_LMu, L_LMu, (set([letCor['m'], letCor['LEFTSHIFT'] ]),set([letCor['m'], letCor['RIGHTSHIFT'] ])), 203)
greek_uppercasenu = Char(l_LNu, L_LNu, (set([letCor['n'], letCor['LEFTSHIFT'] ]),set([letCor['n'], letCor['RIGHTSHIFT'] ]) ), 204)
greek_uppercasexi = Char(l_LXi, L_LXi, (set([letCor['x'] , letCor['LEFTSHIFT'] ]), set([letCor['x'], letCor['RIGHTSHIFT'] ])), 205)
greek_uppercaseomicron = Char(l_LOmicron, L_LOmicron, (set([letCor['o'] , letCor['LEFTSHIFT'] ]), set([letCor['o'], letCor['RIGHTSHIFT'] ])), 206)
greek_uppercasepi = Char(l_LPi, L_LPi, (set([letCor['p'] , letCor['LEFTSHIFT'] ]),set([letCor['p'], letCor['RIGHTSHIFT'] ]) ), 207)
greek_uppercaserho = Char(l_LRho, L_LRho, (set([letCor['r'], letCor['LEFTSHIFT'] ]), set([letCor['r'], letCor['RIGHTSHIFT'] ]) ), 208)
greek_uppercasesigma = Char(l_LSigma, L_LSigma, (set([letCor['s'], letCor['LEFTSHIFT'] ]), set([letCor['s'], letCor['RIGHTSHIFT'] ])), 209)
greek_uppercasetau = Char(l_LTau, L_LTau, (set([ letCor['t'], letCor['LEFTSHIFT'] ]), set([letCor['t'], letCor['RIGHTSHIFT'] ])), 210)
greek_uppercaseupsilon = Char(l_LUpsilon, L_LUpsilon, (set([ letCor['y'], letCor['LEFTSHIFT'] ]),set([letCor['y'], letCor['RIGHTSHIFT'] ])), 211)
greek_uppercasephi = Char(l_LPhi, L_LPhi, (set([ letCor['f'], letCor['LEFTSHIFT'] ]),set([letCor['f'], letCor['RIGHTSHIFT'] ])), 212)
greek_uppercasechi = Char(l_LChi, L_LChi, (set([ letCor['c'], letCor['LEFTSHIFT'] ]), set([letCor['c'], letCor['RIGHTSHIFT'] ])), 213)
greek_uppercasepsi = Char(l_LPsi, L_LPsi, (set([ letCor['q'], letCor['LEFTSHIFT'] ]), set([letCor['q'], letCor['RIGHTSHIFT'] ]) ), 214)
greek_uppercaseomega = Char(l_LOmega, L_LOmega, (set([ letCor['w'], letCor['LEFTSHIFT'] ]), set([letCor['w'], letCor['RIGHTSHIFT'] ])  ), 215)
