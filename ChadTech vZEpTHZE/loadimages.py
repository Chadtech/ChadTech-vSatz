introscreen = pygame.image.load('introscreen.PNG').convert()
selected = pygame.image.load('selected.PNG').convert()

os.chdir(os.path.abspath('chars12x16'))



#Load Images

os.chdir(os.path.abspath('Uppercase'))

######Capital Letters
#####################
L_lA = pygame.image.load('char0.PNG').convert()
L_lB = pygame.image.load('char1.PNG').convert()
L_lC = pygame.image.load('char2.PNG').convert()
L_lD = pygame.image.load('char3.PNG').convert()
L_lE = pygame.image.load('char4.PNG').convert()
L_lF = pygame.image.load('char5.PNG').convert()
L_lG = pygame.image.load('char6.PNG').convert()
L_lH = pygame.image.load('char7.PNG').convert()
L_lI = pygame.image.load('char8.PNG').convert()
L_lJ = pygame.image.load('char9.PNG').convert()
L_lK = pygame.image.load('char10.PNG').convert()
L_lL = pygame.image.load('char11.PNG').convert()
L_lM = pygame.image.load('char12.PNG').convert()
L_lN = pygame.image.load('char13.PNG').convert()
L_lO = pygame.image.load('char14.PNG').convert()
L_lP = pygame.image.load('char15.PNG').convert()
L_lQ = pygame.image.load('char16.PNG').convert()
L_lR = pygame.image.load('char17.PNG').convert()
L_lS = pygame.image.load('char18.PNG').convert()
L_lT = pygame.image.load('char19.PNG').convert()
L_lU = pygame.image.load('char20.PNG').convert()
L_lV = pygame.image.load('char21.PNG').convert()
L_lW = pygame.image.load('char22.PNG').convert()
L_lX = pygame.image.load('char23.PNG').convert()
L_lY = pygame.image.load('char24.PNG').convert()
L_lZ = pygame.image.load('char25.PNG').convert()

os.chdir(os.path.dirname(os.getcwd()))
os.chdir(os.path.abspath('Lowercase'))

#lower case letters
#####################
L_la = pygame.image.load('char0.PNG').convert()
L_lb = pygame.image.load('char1.PNG').convert()
L_lc = pygame.image.load('char2.PNG').convert()
L_ld = pygame.image.load('char3.PNG').convert()
L_le = pygame.image.load('char4.PNG').convert()
L_lf = pygame.image.load('char5.PNG').convert()
L_lg = pygame.image.load('char6.PNG').convert()
L_lh = pygame.image.load('char7.PNG').convert()
L_li = pygame.image.load('char8.PNG').convert()
L_lj = pygame.image.load('char9.PNG').convert()
L_lk = pygame.image.load('char10.PNG').convert()
L_ll = pygame.image.load('char11.PNG').convert()
L_lm = pygame.image.load('char12.PNG').convert()
L_ln = pygame.image.load('char13.PNG').convert()
L_lo = pygame.image.load('char14.PNG').convert()
L_lp = pygame.image.load('char15.PNG').convert()
L_lq = pygame.image.load('char16.PNG').convert()
L_lr = pygame.image.load('char17.PNG').convert()
L_ls = pygame.image.load('char18.PNG').convert()
L_lt = pygame.image.load('char19.PNG').convert()
L_lu = pygame.image.load('char20.PNG').convert()
L_lv = pygame.image.load('char21.PNG').convert()
L_lw = pygame.image.load('char22.PNG').convert()
L_lx = pygame.image.load('char23.PNG').convert()
L_ly = pygame.image.load('char24.PNG').convert()
L_lz = pygame.image.load('char25.PNG').convert()

os.chdir(os.path.dirname(os.getcwd()))
os.chdir(os.path.abspath('slantyfont'))

#slanty font
#####################

L_sa = pygame.image.load('char0.PNG').convert()
L_sb = pygame.image.load('char1.PNG').convert()
L_sc = pygame.image.load('char2.PNG').convert()
L_sd = pygame.image.load('char3.PNG').convert()
L_se = pygame.image.load('char4.PNG').convert()
L_sf = pygame.image.load('char5.PNG').convert()
L_sg = pygame.image.load('char6.PNG').convert()
L_sh = pygame.image.load('char7.PNG').convert()
L_si = pygame.image.load('char8.PNG').convert()
L_sj = pygame.image.load('char9.PNG').convert()
L_sk = pygame.image.load('char10.PNG').convert()
L_sl = pygame.image.load('char11.PNG').convert()
L_sm = pygame.image.load('char12.PNG').convert()
L_sn = pygame.image.load('char13.PNG').convert()
L_so = pygame.image.load('char14.PNG').convert()
L_sp = pygame.image.load('char15.PNG').convert()
L_sq = pygame.image.load('char16.PNG').convert()
L_sr = pygame.image.load('char17.PNG').convert()
L_ss = pygame.image.load('char18.PNG').convert()
L_st = pygame.image.load('char19.PNG').convert()
L_su = pygame.image.load('char20.PNG').convert()
L_sv = pygame.image.load('char21.PNG').convert()
L_sw = pygame.image.load('char22.PNG').convert()
L_sx = pygame.image.load('char23.PNG').convert()
L_sy = pygame.image.load('char24.PNG').convert()
L_sz = pygame.image.load('char25.PNG').convert()

os.chdir(os.path.dirname(os.getcwd()))
os.chdir(os.path.abspath('Punctuation'))

#Punctuation
#####################

L_pQuestion = pygame.image.load('char0.PNG').convert()
L_pExclaimation = pygame.image.load('char1.PNG').convert()
L_pPeriod = pygame.image.load('char2.PNG').convert()
L_pComma = pygame.image.load('char3.PNG').convert()
L_pColon = pygame.image.load('char4.PNG').convert()
L_pSemicolon = pygame.image.load('char5.PNG').convert()
L_pSinglequote = pygame.image.load('char6.PNG').convert()
L_pDoublequote = pygame.image.load('char7.PNG').convert()

os.chdir(os.path.dirname(os.getcwd()))
os.chdir(os.path.abspath('Space'))

#space
#####################
L_S = pygame.image.load('char0.PNG').convert()


#Modal Logic
#####################
os.chdir(os.path.dirname(os.getcwd()))
os.chdir(os.path.abspath('ModalLogic'))


L_mP = pygame.image.load('char0.PNG').convert()
L_mN = pygame.image.load('char1.PNG').convert()

os.chdir(os.path.dirname(os.getcwd()))
os.chdir(os.path.abspath('Math'))

#Math
#####################

L_mEquals = pygame.image.load('char0.PNG').convert()
L_mGreaterThan = pygame.image.load('char1.PNG').convert()
L_mGreaterThanOrEqual = pygame.image.load('char2.PNG').convert()
L_mLessThan = pygame.image.load('char3.PNG').convert()
L_mLessThanOrEqual = pygame.image.load('char4.PNG').convert()
L_mDivision = pygame.image.load('char5.PNG').convert()
L_mApproximately = pygame.image.load('char6.PNG').convert()
L_mPlus = pygame.image.load('char7.PNG').convert()
L_mMinus = pygame.image.load('char8.PNG').convert()
L_mMultiply = pygame.image.load('char9.PNG').convert()
L_mForwardSlash = pygame.image.load('char10.PNG').convert()
L_mBackSlash = pygame.image.load('char11.PNG').convert()
L_mQED = pygame.image.load('char12.PNG').convert()
L_mSquareRoot = pygame.image.load('char13.PNG').convert()
L_mPlusMinus = pygame.image.load('char14.PNG').convert()
L_mIntegral = pygame.image.load('char15.PNG').convert()
L_mNotEqual = pygame.image.load('char16.PNG').convert()
L_mAngle = pygame.image.load('char17.PNG').convert()
L_mTriangle = pygame.image.load('char18.PNG').convert()
L_mUpsideDownTriangle = pygame.image.load('char19.PNG').convert()
L_mInfinity = pygame.image.load('char20.PNG').convert()
L_mDivides = pygame.image.load('char21.PNG').convert()
L_mDoesntDivide = pygame.image.load('char22.PNG').convert()
L_mArrowON = pygame.image.load('char23.PNG').convert()
L_mArrowTW = pygame.image.load('char24.PNG').convert()

os.chdir(os.path.dirname(os.getcwd()))
os.chdir(os.path.abspath('FirstOrderLogic'))

#First Order Logic
#####################

L_firstorderExistential = pygame.image.load('char0.PNG').convert()
L_firstorderForall = pygame.image.load('char1.PNG').convert()
L_firstorderNegation = pygame.image.load('char2.PNG').convert()
L_firstorderImplication = pygame.image.load('char3.PNG').convert()
L_firstorderIff = pygame.image.load('char4.PNG').convert()
L_firstorderAnd = pygame.image.load('char5.PNG').convert()
L_firstorderXor = pygame.image.load('char6.PNG').convert()
L_firstorderNand = pygame.image.load('char7.PNG').convert()
L_firstorderAltnegation = pygame.image.load('char8.PNG').convert()

#Numerals
#####################

os.chdir(os.path.dirname(os.getcwd()))
os.chdir(os.path.abspath('Numerals'))


L_Nze = pygame.image.load('char0.PNG').convert()
L_Non = pygame.image.load('char1.PNG').convert()
L_Ntw = pygame.image.load('char2.PNG').convert()
L_Nth = pygame.image.load('char3.PNG').convert()
L_Nfo = pygame.image.load('char4.PNG').convert()
L_Nfi = pygame.image.load('char5.PNG').convert()
L_Nsi = pygame.image.load('char6.PNG').convert()
L_Nse = pygame.image.load('char7.PNG').convert()
L_Nei = pygame.image.load('char8.PNG').convert()
L_Nni = pygame.image.load('char9.PNG').convert()

#Brackets
#####################

os.chdir(os.path.dirname(os.getcwd()))
os.chdir(os.path.abspath('Brackets'))

L_bLeftParenthesis = pygame.image.load('char0.PNG').convert()
L_bRightParenthesis = pygame.image.load('char1.PNG').convert()
L_bLeftCurly = pygame.image.load('char2.PNG').convert()
L_bRightCurly = pygame.image.load('char3.PNG').convert()
L_bLeftBracket = pygame.image.load('char4.PNG').convert()
L_bRightBracket = pygame.image.load('char5.PNG').convert()
L_bLeftChevron = pygame.image.load('char6.PNG').convert()
L_bRightChevron = pygame.image.load('char7.PNG').convert()

#Misc
#####################

os.chdir(os.path.dirname(os.getcwd()))
os.chdir(os.path.abspath('Misc'))

L_miscNumbersign = pygame.image.load('char0.PNG').convert()
L_miscDollarsign = pygame.image.load('char1.PNG').convert()
L_miscPercentsign = pygame.image.load('char2.PNG').convert()
L_miscAmbersand = pygame.image.load('char3.PNG').convert()
L_miscAtsign = pygame.image.load('char4.PNG').convert()
L_miscCarrot = pygame.image.load('char5.PNG').convert()
L_miscAsterisk = pygame.image.load('char6.PNG').convert()

#Set Theory
#####################

os.chdir(os.path.dirname(os.getcwd()))
os.chdir(os.path.abspath('setTheory'))

L_settheoryElementof = pygame.image.load('char0.PNG').convert()
L_settheoryNotelementof = pygame.image.load('char1.PNG').convert()
L_settheoryNullset = pygame.image.load('char2.PNG').convert()
L_settheoryIntersection = pygame.image.load('char3.PNG').convert()
L_settheoryUnion = pygame.image.load('char4.PNG').convert()
L_settheorySuperset = pygame.image.load('char5.PNG').convert()
L_settheorySubset = pygame.image.load('char6.PNG').convert()
L_settheoryNotsuperset = pygame.image.load('char7.PNG').convert()
L_settheoryNotsubset = pygame.image.load('char8.PNG').convert()

#Proof Theory
#####################

os.chdir(os.path.dirname(os.getcwd()))
os.chdir(os.path.abspath('ProofTheory'))

L_pSingleturnstile = pygame.image.load('char0.PNG').convert()
L_pNotsingleturnstile = pygame.image.load('char1.PNG').convert()
L_pDoubleturnstile = pygame.image.load('char2.PNG').convert()
L_pNotdoubleturnstile = pygame.image.load('char3.PNG').convert()
L_pLogicalconstant = pygame.image.load('char4.PNG').convert()

#Lower Case Greek
#####################

os.chdir(os.path.dirname(os.getcwd()))
os.chdir(os.path.abspath('LowercaseGreek'))

L_lAlpha=pygame.image.load('char0.PNG').convert()
L_lBeta=pygame.image.load('char1.PNG').convert()
L_lGamma=pygame.image.load('char2.PNG').convert()
L_lDelta=pygame.image.load('char3.PNG').convert()
L_lEpsilon=pygame.image.load('char4.PNG').convert()
L_lZeta=pygame.image.load('char5.PNG').convert()
L_lEta=pygame.image.load('char6.PNG').convert()
L_lTheta=pygame.image.load('char7.PNG').convert()
L_lIota=pygame.image.load('char8.PNG').convert()
L_lKappa=pygame.image.load('char9.PNG').convert()
L_lLambda=pygame.image.load('char10.PNG').convert()
L_lMu=pygame.image.load('char11.PNG').convert()
L_lNu=pygame.image.load('char12.PNG').convert()
L_lXi=pygame.image.load('char13.PNG').convert()
L_lOmicron=pygame.image.load('char14.PNG').convert()
L_lPi=pygame.image.load('char15.PNG').convert()
L_lRho=pygame.image.load('char16.PNG').convert()
L_lSigma=pygame.image.load('char17.PNG').convert()
L_lTau=pygame.image.load('char18.PNG').convert()
L_lUpsilon=pygame.image.load('char19.PNG').convert()
L_lPhi=pygame.image.load('char20.PNG').convert()
L_lChi=pygame.image.load('char21.PNG').convert()
L_lPsi=pygame.image.load('char22.PNG').convert()
L_lOmega=pygame.image.load('char23.PNG').convert()

#Uppercase Greek
#####################

os.chdir(os.path.dirname(os.getcwd()))
os.chdir(os.path.abspath('UppercaseGreek'))

L_LAlpha=pygame.image.load('char0.PNG').convert()
L_LBeta=pygame.image.load('char1.PNG').convert()
L_LGamma=pygame.image.load('char2.PNG').convert()
L_LDelta=pygame.image.load('char3.PNG').convert()
L_LEpsilon=pygame.image.load('char4.PNG').convert()
L_LZeta=pygame.image.load('char5.PNG').convert()
L_LEta=pygame.image.load('char6.PNG').convert()
L_LTheta=pygame.image.load('char7.PNG').convert()
L_LIota=pygame.image.load('char8.PNG').convert()
L_LKappa=pygame.image.load('char9.PNG').convert()
L_LLambda=pygame.image.load('char10.PNG').convert()
L_LMu=pygame.image.load('char11.PNG').convert()
L_LNu=pygame.image.load('char12.PNG').convert()
L_LXi=pygame.image.load('char13.PNG').convert()
L_LOmicron=pygame.image.load('char14.PNG').convert()
L_LPi=pygame.image.load('char15.PNG').convert()
L_LRho=pygame.image.load('char16.PNG').convert()
L_LSigma=pygame.image.load('char17.PNG').convert()
L_LTau=pygame.image.load('char18.PNG').convert()
L_LUpsilon=pygame.image.load('char19.PNG').convert()
L_LPhi=pygame.image.load('char20.PNG').convert()
L_LChi=pygame.image.load('char21.PNG').convert()
L_LPsi=pygame.image.load('char22.PNG').convert()
L_LOmega=pygame.image.load('char23.PNG').convert()

#Cursor
#####################

os.chdir(os.path.dirname(os.getcwd()))
os.chdir(os.path.abspath('Cursor'))

L_C = pygame.image.load('char0.PNG').convert()

#Errors
#####################

os.chdir(os.path.dirname(os.getcwd()))
os.chdir(os.path.abspath('Error'))

L_Error = pygame.image.load('char0.PNG').convert()
L_Frown = pygame.image.load('char1.PNG').convert()

#Small portrait of Alexander Hamilton
#####################

os.chdir(os.path.dirname(os.getcwd()))
os.chdir(os.path.abspath('smallPortraitOfAlexanderHamilton'))

L_hOn = pygame.image.load('char0.PNG').convert()
L_hTw = pygame.image.load('char1.PNG').convert()
L_hTh = pygame.image.load('char2.PNG').convert()
L_hFo = pygame.image.load('char3.PNG').convert()

os.chdir(os.path.dirname(os.getcwd()))
os.chdir(os.path.dirname(os.getcwd()))
os.chdir(os.path.abspath('chars6x8'))
os.chdir(os.path.abspath('Uppercase'))

#Capital Letters
#####################

l_lA = pygame.image.load('char0.PNG').convert()
l_lB = pygame.image.load('char1.PNG').convert()
l_lC = pygame.image.load('char2.PNG').convert()
l_lD = pygame.image.load('char3.PNG').convert()
l_lE = pygame.image.load('char4.PNG').convert()
l_lF = pygame.image.load('char5.PNG').convert()
l_lG = pygame.image.load('char6.PNG').convert()
l_lH = pygame.image.load('char7.PNG').convert()
l_lI = pygame.image.load('char8.PNG').convert()
l_lJ = pygame.image.load('char9.PNG').convert()
l_lK = pygame.image.load('char10.PNG').convert()
l_lL = pygame.image.load('char11.PNG').convert()
l_lM = pygame.image.load('char12.PNG').convert()
l_lN = pygame.image.load('char13.PNG').convert()
l_lO = pygame.image.load('char14.PNG').convert()
l_lP = pygame.image.load('char15.PNG').convert()
l_lQ = pygame.image.load('char16.PNG').convert()
l_lR = pygame.image.load('char17.PNG').convert()
l_lS = pygame.image.load('char18.PNG').convert()
l_lT = pygame.image.load('char19.PNG').convert()
l_lU = pygame.image.load('char20.PNG').convert()
l_lV = pygame.image.load('char21.PNG').convert()
l_lW = pygame.image.load('char22.PNG').convert()
l_lX = pygame.image.load('char23.PNG').convert()
l_lY = pygame.image.load('char24.PNG').convert()
l_lZ = pygame.image.load('char25.PNG').convert()

os.chdir(os.path.dirname(os.getcwd()))
os.chdir(os.path.abspath('Lowercase'))

#Lowercase
#####################

l_la = pygame.image.load('char0.PNG').convert()
l_lb = pygame.image.load('char1.PNG').convert()
l_lc = pygame.image.load('char2.PNG').convert()
l_ld = pygame.image.load('char3.PNG').convert()
l_le = pygame.image.load('char4.PNG').convert()
l_lf = pygame.image.load('char5.PNG').convert()
l_lg = pygame.image.load('char6.PNG').convert()
l_lh = pygame.image.load('char7.PNG').convert()
l_li = pygame.image.load('char8.PNG').convert()
l_lj = pygame.image.load('char9.PNG').convert()
l_lk = pygame.image.load('char10.PNG').convert()
l_ll = pygame.image.load('char11.PNG').convert()
l_lm = pygame.image.load('char12.PNG').convert()
l_ln = pygame.image.load('char13.PNG').convert()
l_lo = pygame.image.load('char14.PNG').convert()
l_lp = pygame.image.load('char15.PNG').convert()
l_lq = pygame.image.load('char16.PNG').convert()
l_lr = pygame.image.load('char17.PNG').convert()
l_ls = pygame.image.load('char18.PNG').convert()
l_lt = pygame.image.load('char19.PNG').convert()
l_lu = pygame.image.load('char20.PNG').convert()
l_lv = pygame.image.load('char21.PNG').convert()
l_lw = pygame.image.load('char22.PNG').convert()
l_lx = pygame.image.load('char23.PNG').convert()
l_ly = pygame.image.load('char24.PNG').convert()
l_lz = pygame.image.load('char25.PNG').convert()

#Space
#####################

os.chdir(os.path.dirname(os.getcwd()))
os.chdir(os.path.abspath('Space'))

l_S = pygame.image.load('char0.PNG').convert()

#Numerals 
#####################

os.chdir(os.path.dirname(os.getcwd()))
os.chdir(os.path.abspath('Numerals'))

l_Nze = pygame.image.load('char0.PNG').convert()
l_Non = pygame.image.load('char1.PNG').convert()
l_Ntw = pygame.image.load('char2.PNG').convert()
l_Nth = pygame.image.load('char3.PNG').convert()
l_Nfo = pygame.image.load('char4.PNG').convert()
l_Nfi = pygame.image.load('char5.PNG').convert()
l_Nsi = pygame.image.load('char6.PNG').convert()
l_Nse = pygame.image.load('char7.PNG').convert()
l_Nei = pygame.image.load('char8.PNG').convert()
l_Nni = pygame.image.load('char9.PNG').convert()

#Punctuation
#####################

os.chdir(os.path.dirname(os.getcwd()))
os.chdir(os.path.abspath('Punctuation'))

l_punctuationQuestion = pygame.image.load('char0.PNG').convert()
l_punctuationExclaimation = pygame.image.load('char1.PNG').convert()
l_punctuationPeriod = pygame.image.load('char2.PNG').convert()
l_punctuationComma = pygame.image.load('char3.PNG').convert()
l_punctuationColon = pygame.image.load('char4.PNG').convert()
l_punctuationSemicolon = pygame.image.load('char5.PNG').convert()
l_punctuationSinglequote = pygame.image.load('char6.PNG').convert()
l_punctuationDoublequote = pygame.image.load('char7.PNG').convert()

#Modal Logic
#####################

os.chdir(os.path.dirname(os.getcwd()))
os.chdir(os.path.abspath('Modallogic'))

l_modalPossible = pygame.image.load('char0.PNG').convert()
l_modalNecessary = pygame.image.load('char1.PNG').convert()

os.chdir(os.path.dirname(os.getcwd()))
os.chdir(os.path.abspath('FirstOrderLogic'))

#First Order Logic
#####################

l_firstorderExistential = pygame.image.load('char0.PNG').convert()
l_firstorderForall = pygame.image.load('char1.PNG').convert()
l_firstorderNegation = pygame.image.load('char2.PNG').convert()
l_firstorderImplication = pygame.image.load('char3.PNG').convert()
l_firstorderIff = pygame.image.load('char4.PNG').convert()
l_firstorderAnd = pygame.image.load('char5.PNG').convert()
l_firstorderXor = pygame.image.load('char6.PNG').convert()
l_firstorderNand = pygame.image.load('char7.PNG').convert()
l_firstorderAltnegation = pygame.image.load('char8.PNG').convert()

#Brackets
#####################

os.chdir(os.path.dirname(os.getcwd()))
os.chdir(os.path.abspath('Brackets'))

l_bLeftParenthesis = pygame.image.load('char0.PNG').convert()
l_bRightParenthesis = pygame.image.load('char1.PNG').convert()
l_bLeftBracket = pygame.image.load('char2.PNG').convert()
l_bRightBracket = pygame.image.load('char3.PNG').convert()
l_bLeftCurly = pygame.image.load('char4.PNG').convert()
l_bRightCurly = pygame.image.load('char5.PNG').convert()
l_bLeftChevron = pygame.image.load('char6.PNG').convert()
l_bRightChevron = pygame.image.load('char7.PNG').convert()

#Misc
#####################

os.chdir(os.path.dirname(os.getcwd()))
os.chdir(os.path.abspath('Misc'))

l_miscNumbersign = pygame.image.load('char0.PNG').convert()
l_miscDollarsign = pygame.image.load('char1.PNG').convert()
l_miscPercentsign = pygame.image.load('char2.PNG').convert()
l_miscAmbersand = pygame.image.load('char3.PNG').convert()
l_miscAtsign = pygame.image.load('char4.PNG').convert()
l_miscCarrot = pygame.image.load('char5.PNG').convert()
l_miscAsterisk = pygame.image.load('char6.PNG').convert()

#Set Theory
#####################

os.chdir(os.path.dirname(os.getcwd()))
os.chdir(os.path.abspath('setTheory'))

l_settheoryElementof = pygame.image.load('char0.PNG').convert()
l_settheoryNotelementof = pygame.image.load('char1.PNG').convert()
l_settheoryNullset = pygame.image.load('char2.PNG').convert()
l_settheoryIntersection = pygame.image.load('char3.PNG').convert()
l_settheoryUnion = pygame.image.load('char4.PNG').convert()
l_settheorySuperset = pygame.image.load('char5.PNG').convert()
l_settheorySubset = pygame.image.load('char6.PNG').convert()
l_settheoryNotsuperset = pygame.image.load('char7.PNG').convert()
l_settheoryNotsubset = pygame.image.load('char8.PNG').convert()

#Proof Theory
#####################

os.chdir(os.path.dirname(os.getcwd()))
os.chdir(os.path.abspath('ProofTheory'))

l_pSingleturnstile = pygame.image.load('char0.PNG').convert()
l_pNotsingleturnstile = pygame.image.load('char1.PNG').convert()
l_pDoubleturnstile = pygame.image.load('char2.PNG').convert()
l_pNotdoubleturnstile = pygame.image.load('char3.PNG').convert()
l_pLogicalconstant = pygame.image.load('char4.PNG').convert()

#Math
#####################

os.chdir(os.path.dirname(os.getcwd()))
os.chdir(os.path.abspath('Math'))

l_mEquals = pygame.image.load('char0.PNG').convert()
l_mGreaterThan = pygame.image.load('char1.PNG').convert()
l_mGreaterThanOrEqual = pygame.image.load('char2.PNG').convert()
l_mLessThan = pygame.image.load('char3.PNG').convert()
l_mLessThanOrEqual = pygame.image.load('char4.PNG').convert()
l_mDivision = pygame.image.load('char5.PNG').convert()
l_mApproximately = pygame.image.load('char6.PNG').convert()
l_mPlus = pygame.image.load('char7.PNG').convert()
l_mMinus = pygame.image.load('char8.PNG').convert()
l_mMultiply = pygame.image.load('char9.PNG').convert()
l_mForwardSlash = pygame.image.load('char10.PNG').convert()
l_mBackSlash = pygame.image.load('char11.PNG').convert()
l_mQED = pygame.image.load('char12.PNG').convert()
l_mSquareRoot = pygame.image.load('char13.PNG').convert()
l_mPlusMinus = pygame.image.load('char14.PNG').convert()
l_mIntegral = pygame.image.load('char15.PNG').convert()
l_mNotEqual = pygame.image.load('char16.PNG').convert()
l_mAngle = pygame.image.load('char17.PNG').convert()
l_mTriangle = pygame.image.load('char18.PNG').convert()
l_mUpsideDownTriangle = pygame.image.load('char19.PNG').convert()
l_mInfinity = pygame.image.load('char20.PNG').convert()
l_mDivides = pygame.image.load('char21.PNG').convert()
l_mDoesntDivide = pygame.image.load('char22.PNG').convert()
l_mArrowON = pygame.image.load('char23.PNG').convert()
l_mArrowTW = pygame.image.load('char24.PNG').convert()

#Error
#####################

os.chdir(os.path.dirname(os.getcwd()))
os.chdir(os.path.abspath('Error'))

l_Error = pygame.image.load('char0.PNG').convert()
l_Frown = pygame.image.load('char1.PNG').convert()

#Lower case Greek
#####################

os.chdir(os.path.dirname(os.getcwd()))
os.chdir(os.path.abspath('LowercaseGreek'))

l_lAlpha=pygame.image.load('char0.PNG').convert()
l_lBeta=pygame.image.load('char1.PNG').convert()
l_lGamma=pygame.image.load('char2.PNG').convert()
l_lDelta=pygame.image.load('char3.PNG').convert()
l_lEpsilon=pygame.image.load('char4.PNG').convert()
l_lZeta=pygame.image.load('char5.PNG').convert()
l_lEta=pygame.image.load('char6.PNG').convert()
l_lTheta=pygame.image.load('char7.PNG').convert()
l_lIota=pygame.image.load('char8.PNG').convert()
l_lKappa=pygame.image.load('char9.PNG').convert()
l_lLambda=pygame.image.load('char10.PNG').convert()
l_lMu=pygame.image.load('char11.PNG').convert()
l_lNu=pygame.image.load('char12.PNG').convert()
l_lXi=pygame.image.load('char13.PNG').convert()
l_lOmicron=pygame.image.load('char14.PNG').convert()
l_lPi=pygame.image.load('char15.PNG').convert()
l_lRho=pygame.image.load('char16.PNG').convert()
l_lSigma=pygame.image.load('char17.PNG').convert()
l_lTau=pygame.image.load('char18.PNG').convert()
l_lUpsilon=pygame.image.load('char19.PNG').convert()
l_lPhi=pygame.image.load('char20.PNG').convert()
l_lChi=pygame.image.load('char21.PNG').convert()
l_lPsi=pygame.image.load('char22.PNG').convert()
l_lOmega=pygame.image.load('char23.PNG').convert()

#Uppercase Greek
#####################

os.chdir(os.path.dirname(os.getcwd()))
os.chdir(os.path.abspath('UppercaseGreek'))

l_LAlpha=pygame.image.load('char0.PNG').convert()
l_LBeta=pygame.image.load('char1.PNG').convert()
l_LGamma=pygame.image.load('char2.PNG').convert()
l_LDelta=pygame.image.load('char3.PNG').convert()
l_LEpsilon=pygame.image.load('char4.PNG').convert()
l_LZeta=pygame.image.load('char5.PNG').convert()
l_LEta=pygame.image.load('char6.PNG').convert()
l_LTheta=pygame.image.load('char7.PNG').convert()
l_LIota=pygame.image.load('char8.PNG').convert()
l_LKappa=pygame.image.load('char9.PNG').convert()
l_LLambda=pygame.image.load('char10.PNG').convert()
l_LMu=pygame.image.load('char11.PNG').convert()
l_LNu=pygame.image.load('char12.PNG').convert()
l_LXi=pygame.image.load('char13.PNG').convert()
l_LOmicron=pygame.image.load('char14.PNG').convert()
l_LPi=pygame.image.load('char15.PNG').convert()
l_LRho=pygame.image.load('char16.PNG').convert()
l_LSigma=pygame.image.load('char17.PNG').convert()
l_LTau=pygame.image.load('char18.PNG').convert()
l_LUpsilon=pygame.image.load('char19.PNG').convert()
l_LPhi=pygame.image.load('char20.PNG').convert()
l_LChi=pygame.image.load('char21.PNG').convert()
l_LPsi=pygame.image.load('char22.PNG').convert()
l_LOmega=pygame.image.load('char23.PNG').convert()

os.chdir(os.path.dirname(os.getcwd()))
os.chdir(os.path.dirname(os.getcwd()))