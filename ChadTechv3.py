import os
import pygame
import PIL
from PIL import Image
import Tkinter, tkFileDialog
brunk = Tkinter.Tk()
brunk.withdraw()

screenWidth=1366
screenHeight=724

screen = pygame.display.set_mode((1000,500),pygame.RESIZABLE)

pygame.display.set_caption("ChadTech vSatz",)
pygame.display.set_icon(pygame.image.load("icon.PNG").convert())

introscreen = pygame.image.load('introscreen.PNG').convert()
selected = pygame.image.load('selected.PNG').convert()

os.chdir(os.path.abspath('chars12x16'))

lineGap =1

#Load Images

os.chdir(os.path.abspath('Uppercase'))

#Capital Letters
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
L_S = pygame.image.load('char0.PNG').convert()

os.chdir(os.path.dirname(os.getcwd()))
os.chdir(os.path.abspath('ModalLogic'))

#Modal Logic
L_mP = pygame.image.load('char0.PNG').convert()
L_mN = pygame.image.load('char1.PNG').convert()

os.chdir(os.path.dirname(os.getcwd()))
os.chdir(os.path.abspath('Math'))

#Math
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

os.chdir(os.path.dirname(os.getcwd()))
os.chdir(os.path.abspath('FirstOrderLogic'))

#First Order Logic
L_firstorderExistential = pygame.image.load('char0.PNG').convert()
L_firstorderForall = pygame.image.load('char1.PNG').convert()
L_firstorderNegation = pygame.image.load('char2.PNG').convert()
L_firstorderImplication = pygame.image.load('char3.PNG').convert()
L_firstorderIff = pygame.image.load('char4.PNG').convert()
L_firstorderAnd = pygame.image.load('char5.PNG').convert()
L_firstorderXor = pygame.image.load('char6.PNG').convert()
L_firstorderNand = pygame.image.load('char7.PNG').convert()
L_firstorderAltnegation = pygame.image.load('char8.PNG').convert()

os.chdir(os.path.dirname(os.getcwd()))
os.chdir(os.path.abspath('Numerals'))

#Numerals
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

os.chdir(os.path.dirname(os.getcwd()))
os.chdir(os.path.abspath('Brackets'))

#Brackets
L_bLeftParenthesis = pygame.image.load('char0.PNG').convert()
L_bRightParenthesis = pygame.image.load('char1.PNG').convert()
L_bLeftCurly = pygame.image.load('char2.PNG').convert()
L_bRightCurly = pygame.image.load('char3.PNG').convert()
L_bLeftBracket = pygame.image.load('char4.PNG').convert()
L_bRightBracket = pygame.image.load('char5.PNG').convert()
L_bLeftChevron = pygame.image.load('char6.PNG').convert()
L_bRightChevron = pygame.image.load('char7.PNG').convert()

os.chdir(os.path.dirname(os.getcwd()))
os.chdir(os.path.abspath('Misc'))

#Misc
L_miscNumbersign = pygame.image.load('char0.PNG').convert()
L_miscDollarsign = pygame.image.load('char1.PNG').convert()
L_miscPercentsign = pygame.image.load('char2.PNG').convert()
L_miscAmbersand = pygame.image.load('char3.PNG').convert()
L_miscAtsign = pygame.image.load('char4.PNG').convert()
L_miscCarrot = pygame.image.load('char5.PNG').convert()

os.chdir(os.path.dirname(os.getcwd()))
os.chdir(os.path.abspath('setTheory'))

#set Theory
L_settheoryElementof = pygame.image.load('char0.PNG').convert()
L_settheoryNotelementof = pygame.image.load('char1.PNG').convert()
L_settheoryNullset = pygame.image.load('char2.PNG').convert()
L_settheoryIntersection = pygame.image.load('char3.PNG').convert()
L_settheoryUnion = pygame.image.load('char4.PNG').convert()
L_settheorySuperset = pygame.image.load('char5.PNG').convert()
L_settheorySubset = pygame.image.load('char6.PNG').convert()
L_settheoryNotsuperset = pygame.image.load('char7.PNG').convert()
L_settheoryNotsubset = pygame.image.load('char8.PNG').convert()

os.chdir(os.path.dirname(os.getcwd()))
os.chdir(os.path.abspath('ProofTheory'))

#Proof Theory
L_pSingleturnstile = pygame.image.load('char0.PNG').convert()
L_pNotsingleturnstile = pygame.image.load('char1.PNG').convert()
L_pDoubleturnstile = pygame.image.load('char2.PNG').convert()
L_pNotdoubleturnstile = pygame.image.load('char3.PNG').convert()
L_pLogicalconstant = pygame.image.load('char4.PNG').convert()

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

os.chdir(os.path.dirname(os.getcwd()))
os.chdir(os.path.abspath('Cursor'))

L_C = pygame.image.load('char0.PNG').convert()

os.chdir(os.path.dirname(os.getcwd()))
os.chdir(os.path.abspath('Error'))

L_Error = pygame.image.load('char0.PNG').convert()
L_Frown = pygame.image.load('char1.PNG').convert()

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

#Capital Letters
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

os.chdir(os.path.dirname(os.getcwd()))
os.chdir(os.path.abspath('Space'))

#space
l_S = pygame.image.load('char0.PNG').convert()

os.chdir(os.path.dirname(os.getcwd()))
os.chdir(os.path.abspath('Numerals'))

#Numerals
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

os.chdir(os.path.dirname(os.getcwd()))
os.chdir(os.path.abspath('Punctuation'))

#Punctuation
l_punctuationQuestion = pygame.image.load('char0.PNG').convert()
l_punctuationExclaimation = pygame.image.load('char1.PNG').convert()
l_punctuationPeriod = pygame.image.load('char2.PNG').convert()
l_punctuationComma = pygame.image.load('char3.PNG').convert()
l_punctuationColon = pygame.image.load('char4.PNG').convert()
l_punctuationSemicolon = pygame.image.load('char5.PNG').convert()
l_punctuationSinglequote = pygame.image.load('char6.PNG').convert()
l_punctuationDoublequote = pygame.image.load('char7.PNG').convert()

os.chdir(os.path.dirname(os.getcwd()))
os.chdir(os.path.abspath('Modallogic'))

l_modalPossible = pygame.image.load('char0.PNG').convert()
l_modalNecessary = pygame.image.load('char1.PNG').convert()

os.chdir(os.path.dirname(os.getcwd()))
os.chdir(os.path.abspath('FirstOrderLogic'))

#First Order Logic
l_firstorderExistential = pygame.image.load('char0.PNG').convert()
l_firstorderForall = pygame.image.load('char1.PNG').convert()
l_firstorderNegation = pygame.image.load('char2.PNG').convert()
l_firstorderImplication = pygame.image.load('char3.PNG').convert()
l_firstorderIff = pygame.image.load('char4.PNG').convert()
l_firstorderAnd = pygame.image.load('char5.PNG').convert()
l_firstorderXor = pygame.image.load('char6.PNG').convert()
l_firstorderNand = pygame.image.load('char7.PNG').convert()
l_firstorderAltnegation = pygame.image.load('char8.PNG').convert()

os.chdir(os.path.dirname(os.getcwd()))
os.chdir(os.path.abspath('Brackets'))

#Brackets
l_bLeftParenthesis = pygame.image.load('char0.PNG').convert()
l_bRightParenthesis = pygame.image.load('char1.PNG').convert()
l_bLeftCurly = pygame.image.load('char2.PNG').convert()
l_bRightCurly = pygame.image.load('char3.PNG').convert()
l_bLeftBracket = pygame.image.load('char4.PNG').convert()
l_bRightBracket = pygame.image.load('char5.PNG').convert()
l_bLeftChevron = pygame.image.load('char6.PNG').convert()
l_bRightChevron = pygame.image.load('char7.PNG').convert()

os.chdir(os.path.dirname(os.getcwd()))
os.chdir(os.path.abspath('Misc'))

#Misc
l_miscNumbersign = pygame.image.load('char0.PNG').convert()
l_miscDollarsign = pygame.image.load('char1.PNG').convert()
l_miscPercentsign = pygame.image.load('char2.PNG').convert()
l_miscAmbersand = pygame.image.load('char3.PNG').convert()
l_miscAtsign = pygame.image.load('char4.PNG').convert()
l_miscCarrot = pygame.image.load('char5.PNG').convert()

os.chdir(os.path.dirname(os.getcwd()))
os.chdir(os.path.abspath('setTheory'))

#set Theory
l_settheoryElementof = pygame.image.load('char0.PNG').convert()
l_settheoryNotelementof = pygame.image.load('char1.PNG').convert()
l_settheoryNullset = pygame.image.load('char2.PNG').convert()
l_settheoryIntersection = pygame.image.load('char3.PNG').convert()
l_settheoryUnion = pygame.image.load('char4.PNG').convert()
l_settheorySuperset = pygame.image.load('char5.PNG').convert()
l_settheorySubset = pygame.image.load('char6.PNG').convert()
l_settheoryNotsuperset = pygame.image.load('char7.PNG').convert()
l_settheoryNotsubset = pygame.image.load('char8.PNG').convert()

os.chdir(os.path.dirname(os.getcwd()))
os.chdir(os.path.abspath('ProofTheory'))

#Proof Theory
l_pSingleturnstile = pygame.image.load('char0.PNG').convert()
l_pNotsingleturnstile = pygame.image.load('char1.PNG').convert()
l_pDoubleturnstile = pygame.image.load('char2.PNG').convert()
l_pNotdoubleturnstile = pygame.image.load('char3.PNG').convert()
l_pLogicalconstant = pygame.image.load('char4.PNG').convert()


os.chdir(os.path.dirname(os.getcwd()))
os.chdir(os.path.abspath('Math'))

#Math
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

os.chdir(os.path.dirname(os.getcwd()))
os.chdir(os.path.abspath('Error'))

l_Error = pygame.image.load('char0.PNG').convert()
l_Frown = pygame.image.load('char1.PNG').convert()

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

pygame.init()



#group = pygame.sprite.Group()

pygame.display.set_caption("ChadTech vSatz",)
pygame.display.set_icon(pygame.image.load("icon.PNG").convert())
quit = False
clock = pygame.time.Clock()

charWidth=12
charHeight=16 #With the buffer the height ought to be 35, but it would be misleading to say the height is 35, instead of saying we need to shift 35 per line.
lilcharWidth=6
lilcharHeight=8


lilCharOffsetX = 9
lilCharOffsetSuperSetY = -8
lilCharOffsetSubSetY=16

xMarg = (8*charWidth)-charWidth
yMarg = (2*charHeight)

curLin=0
curVort=0
curChar=0

shiftCou = 1
shiftMag = 8

slantyChek = False

whichScript = 'normal'
greekOn = 'Yes'


def addChar(input):
	return [input,[],[]]

letCor = {
	
	'BACKSPACE':8,
	'TAB':9,
	'ENTER':13,

	'SPACE':32,

	'SINGLEQUOTE':39,

	'COMMA':44,
	'HYPHEN':45,
	'PERIOD':46,

	'FORWARDSLASH':47,
	'NUMERAL0':48,
	'NUMERAL1':49,
	'NUMERAL2':50,
	'NUMERAL3':51,
	'NUMERAL4':52,
	'NUMERAL5':53,
	'NUMERAL6':54,
	'NUMERAL7':55,
	'NUMERAL8':56,
	'NUMERAL9':57,

	'SEMICOLON':59,

	'EQUALS':61,

	'LEFTBRACKET':91,
	'RIGHTBRACKET':93,

	'BACKSLASH':92,

	'TILDE':96,

	'a':97,
	'b':98,
	'c':99,
	'd':100,
	'e':101,
	'f':102,
	'g':103,
	'h':104,
	'i':105,
	'j':106,
	'k':107,
	'l':108,
	'm':109,
	'n':110,
	'o':111,
	'p':112,
	'q':113,
	'r':114,
	's':115,
	't':116,
	'u':117,
	'v':118,
	'w':119,
	'x':120,
	'y':121,
	'z':122,

	'UPARROW':273,
	'DOWNARROW':274,
	'RIGHTARROW':275,
	'LEFTARROW':276,

	'RIGHTSHIFT':303,
	'LEFTSHIFT':304,
	'RIGHTCONTROL':305,
	'LEFTCONTROL':306,
	'RIGHTALT':307,
	'LEFTALT':308,

	'NOKEYS':14000

}

class Char:
	def __init__(self,lilimage,image,keys,keyDig):
		self.lilimage=lilimage
		self.image=image
		self.keys=keys #The keys variable, refers to a tuple, who elements are sets, containing valid key combinations to produce that character. The elements of the set are elements of the dictionary
		self.keyDig=keyDig

class Vort:
	def __init__(self):
		self.charen=[]

#Invisible Chars

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

#Nothing
nothing=Char(l_Frown,L_Frown,set([ letCor['NOKEYS'] ]),255)

#Error
error=Char(l_Error,L_Error,set([ letCor['NOKEYS'] ]), 255)

############Visible Chars

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

#Space is 53

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

#113 is enter

#Misc

misc__numbersign=Char(l_miscNumbersign,L_miscNumbersign,( set([ letCor['NUMERAL3'], letCor['LEFTSHIFT'] ]), set([ letCor['NUMERAL4'],letCor['RIGHTSHIFT'] ]) ),114 )
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

#134 is error

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

# 161 is a super script code
# 162 is a sub script code

#### Forgot this symbol
firstorderLogic__altnegation = (l_firstorderAltnegation,L_firstorderAltnegation,( set([ letCor['NUMERAL1'],letCor['b'] ]), ), 163)

hamilton__On = Char(l_Error, L_hOn, ( set([ letCor['NUMERAL4'],letCor['a'] ]), ), 164)
hamilton__Tw = Char(l_Error, L_hTw, ( set([ letCor['NUMERAL4'],letCor['l'] ]), ), 165)
hamilton__Th = Char(l_Error, L_hTh, ( set([ letCor['NUMERAL4'],letCor['e'] ]), ), 166)
hamilton__Fo = Char(l_Error, L_hFo, ( set([ letCor['NUMERAL4'],letCor['x'] ]), ), 167)


#### Greek Symbols

greek_lowercasealpha = Char(l_lAlpha,L_lAlpha, ( set([ letCor['a'] ]), ), 168)
greek_lowercasebeta = Char(l_lBeta,L_lBeta, ( set([ letCor['b'] ]), ), 169 )
greek_lowercasegamma = Char(l_lGamma,L_lGamma, ( set([  letCor['g'] ]), ), 170)
greek_lowercasedelta = Char(l_lDelta,L_lDelta, ( set([ letCor['d'] ]), ), 171)
greek_lowercaseepsilon = Char(l_lEpsilon, L_lEpsilon, ( set([ letCor['e'] ]), ), 172)
greek_lowercasezeta = Char(l_lZeta, L_lZeta, (set([letCor['z'] ]), ), 173)
greek_lowercaseeta = Char(l_lEta, L_lEta, (set([ letCor['i'] ]), ), 174)
greek_lowercasetheta = Char(l_lTheta, L_lTheta, (set([ letCor['h'] ]), ), 175)
greek_lowercaseiota = Char(l_lIota, L_lIota, (set([letCor['j'] ]), ), 176)
greek_lowercasekappa = Char(l_lKappa, L_lKappa, (set([  letCor['k'] ]), ), 177)
greek_lowercaselambda = Char(l_lLambda, L_lLambda, (set([ letCor['l'] ]), ), 178)
greek_lowercasemu = Char(l_lMu, L_lMu, (set([letCor['m']]), ), 179)
greek_lowercasenu = Char(l_lMu, L_lMu, (set([letCor['n']]), ), 180)
greek_lowercasexi = Char(l_lXi, L_lXi, (set([letCor['x'] ]), ), 181)
greek_lowercaseomicron = Char(l_lOmicron, L_lOmicron, (set([letCor['o'] ]), ), 182)
greek_lowercasepi = Char(l_lPi, L_lPi, (set([letCor['p'] ]), ), 183)
greek_lowercaserho = Char(l_lRho, L_lRho, (set([letCor['r'], ]), ), 184)
greek_lowercasesigma = Char(l_lSigma, L_lSigma, (set([letCor['s'] ]), ), 185)
greek_lowercasetau = Char(l_lTau, L_lTau, (set([ letCor['t'] ]), ), 186)
greek_lowercaseupsilon = Char(l_lUpsilon, L_lUpsilon, (set([ letCor['y'] ]), ), 187)
greek_lowercasephi = Char(l_lPhi, L_lPhi, (set([ letCor['f'] ]), ), 188)
greek_lowercasechi = Char(l_lChi, L_lChi, (set([ letCor['c'] ]), ), 189)
greek_lowercasepsi = Char(l_lPsi, L_lPsi, (set([ letCor['q'] ]), ), 190)
greek_lowercaseomega = Char(l_lOmega, L_lOmega, (set([ letCor['w'] ]), ), 191)

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

charLets={
	
	1:lowercase__a,
	2:lowercase__b,
	3:lowercase__c,
	4:lowercase__d,
	5:lowercase__e,
	6:lowercase__f,
	7:lowercase__g,
	8:lowercase__h,
	9:lowercase__i,
	10:lowercase__j,
	11:lowercase__k,
	12:lowercase__l,
	13:lowercase__m,
	14:lowercase__n,
	15:lowercase__o,
	16:lowercase__p,
	17:lowercase__q,
	18:lowercase__r,
	19:lowercase__s,
	20:lowercase__t,
	21:lowercase__u,
	22:lowercase__v,
	23:lowercase__w,
	24:lowercase__x,
	25:lowercase__y,
	26:lowercase__z,
	27:uppercase__A,
	28:uppercase__B,
	29:uppercase__C,
	30:uppercase__D,
	31:uppercase__E,
	32:uppercase__F,
	33:uppercase__G,
	34:uppercase__H,
	35:uppercase__I,
	36:uppercase__J,
	37:uppercase__K,
	38:uppercase__L,
	39:uppercase__M,
	40:uppercase__N,
	41:uppercase__O,
	42:uppercase__P,
	43:uppercase__Q,
	44:uppercase__R,
	45:uppercase__S,
	46:uppercase__T,
	47:uppercase__U,
	48:uppercase__V,
	49:uppercase__W,
	50:uppercase__X,
	51:uppercase__Y,
	52:uppercase__Z,
	53:space,
	54:punctuation__period,
	55:punctuation__comma,
	56:punctuation__question,
	57:punctuation__semicolon,
	58:punctuation__colon,
	59:punctuation__exclaimation,
	60:punctuation__singlequote,
	61:punctuation__doublequote,
	62:numeral__ze,
	63:numeral__on,
	64:numeral__tw,
	65:numeral__th,
	66:numeral__fo,
	67:numeral__fi,
	68:numeral__si,
	69:numeral__se,
	70:numeral__ei,
	71:numeral__ni,
	72:modallogic__possible,
	73:modallogic__necessary,
	74:firstorderlogic__existential,
	75:firstorderlogic__forall,
	76:firstorderlogic__negation,
	77:firstorderlogic__implication,
	78:firstorderlogic__iff,
	79:firstorderlogic__xor,
	80:firstorderlogic__nand,
	81:firstorderlogic__and,
	82:math__equals,
	83:math__greaterthan,
	84:math__greaterthanorequal,
	85:math__lessthan,
	86:math__lessthanorequal,
	87:math__division,
	88:math__approximately,
	89:math__plus,
	90:math__minus,
	91:math__multiply,
	92:math__forwardslash,
	93:math__backslash,
	94:math__QED,
	95:math__squareroot,
	96:math__plusminus,
	97:math__integral,
	98:math__notequal,
	99:math__angle,
	100:math__triangle,
	101:math__gradient,
	102:math__divides,
	103:math__doesntdivide,
	104:math__infinity,
	105:brackets__leftparentheses,
	106:brackets__rightparentheses,
	107:brackets__leftbracket,
	108:brackets__rightbracket,
	109:brackets__leftcurly,
	110:brackets__rightcurly,
	111:brackets__leftchevron,
	112:brackets__rightchevron,
	113:enter,
	114:misc__numbersign,
	115:misc__dollarsign,
	116:misc__percentsign,
	117:misc__ambersand,
	118:misc__atsign,
	119:misc__carrot,
	120:prooftheory__singleturnstile,
	121:prooftheory__notsingleturnstile,
	122:prooftheory__doubleturnstile,
	123:prooftheory__notdoubleturnstile,
	124:prooftheory__logicalconstant,
	125:settheory__elementof,
	126:settheory__notelementof,
	127:settheory__nullset,
	128:settheory__intersection,
	129:settheory__union,
	130:settheory__superset,
	131:settheory__subset,
	132:settheory__notsuperset,
	133:settheory__notsubset,
	134:error,
	135:slanty__a,
	136:slanty__b,
	137:slanty__c,
	138:slanty__d,
	139:slanty__e,
	140:slanty__f,
	141:slanty__g,
	142:slanty__h,
	143:slanty__i,
	144:slanty__j,
	145:slanty__k,
	146:slanty__l,
	147:slanty__m,
	148:slanty__n,
	149:slanty__o,
	150:slanty__p,
	151:slanty__q,
	152:slanty__r,
	153:slanty__s,
	154:slanty__t,
	155:slanty__u,
	156:slanty__v,
	157:slanty__w,
	158:slanty__x,
	159:slanty__y,
	160:slanty__z,
	### 161 and 162 are codes for the super and sub scripts.
	161:error,
	162:error,
	163:firstorderLogic__altnegation,
	164:hamilton__On,
	165:hamilton__Tw,
	166:hamilton__Th,
	167:hamilton__Fo,



}

class Doc:
	def __init__(self):
		self.charen=[]

windX=0
windY=0

sizeFou = False
quit=False
while sizeFou == False:
	
	screen.blit(introscreen,[0,0])
	
	for event in pygame.event.get():

		if event.type == 5:
			mouX,mouY = event.pos

			##################################3
			########### Okay Check

			################################################3
			####################                  Row ZE 400

			if (mouX>307 and mouX<449) and (mouY>67 and mouY<92):
				windX=400
				windY=400

			if (mouX>465 and mouX<607) and (mouY>67 and mouY<92):
				windX=400
				windY=200

			if (mouX>619 and mouX<761) and (mouY>67 and mouY<92):
				windX=400
				windY=267

			if (mouX>775 and mouX<918) and (mouY>67 and mouY<92):
				windX=400
				windY=300

			################################################3
			####################                  Row TW 600

			if (mouX>307 and mouX<449) and (mouY>107 and mouY<132):
				windX=600
				windY=600

			if (mouX>465 and mouX<607) and (mouY>107 and mouY<132):
				windX=600
				windY=300

			if (mouX>619 and mouX<761) and (mouY>107 and mouY<132):
				windX=600
				windY=400

			if (mouX>775 and mouX<918) and (mouY>107 and mouY<132):
				windX=600
				windY=450

			################################################3
			####################                  Row TH 800

			if (mouX>307 and mouX<449) and (mouY>147 and mouY<172):
				windX=800
				windY=800

			if (mouX>465 and mouX<607) and (mouY>147 and mouY<172):
				windX=800
				windY=400

			if (mouX>619 and mouX<761) and (mouY>147 and mouY<172):
				windX=800
				windY=533

			if (mouX>775 and mouX<918) and (mouY>147 and mouY<172):
				windX=800
				windY=600

			################################################3
			####################                  Row FO 1000

			if (mouX>307 and mouX<449) and (mouY>187 and mouY<212):
				windX=1000
				windY=1000

			if (mouX>465 and mouX<607) and (mouY>187 and mouY<212):
				windX=1000
				windY=500

			if (mouX>619 and mouX<761) and (mouY>187 and mouY<212):
				windX=1000
				windY=667

			if (mouX>775 and mouX<918) and (mouY>187 and mouY<212):
				windX=1000
				windY=750

			################################################3
			####################                  Row FI 1200

			if (mouX>307 and mouX<449) and (mouY>227 and mouY<252):
				windX=1200
				windY=1200

			if (mouX>465 and mouX<607) and (mouY>227 and mouY<252):
				windX=1200
				windY=600

			if (mouX>619 and mouX<761) and (mouY>227 and mouY<252):
				windX=1200
				windY=800

			if (mouX>775 and mouX<918) and (mouY>227 and mouY<252):
				windX=1200
				windY=900

			################################################3
			####################                  Row SI 1400

			if (mouX>307 and mouX<449) and (mouY>267 and mouY<292):
				windX=1400
				windY=1400

			if (mouX>465 and mouX<607) and (mouY>267 and mouY<292):
				windX=1400
				windY=700

			if (mouX>619 and mouX<761) and (mouY>267 and mouY<292):
				windX=1400
				windY=933

			if (mouX>775 and mouX<918) and (mouY>267 and mouY<292):
				windX=1400
				windY=1050

			################################################3
			####################                  Row SE 1600

			if (mouX>307 and mouX<449) and (mouY>307 and mouY<332):
				windX=1600
				windY=1600

			if (mouX>465 and mouX<607) and (mouY>307 and mouY<332):
				windX=1600
				windY=800

			if (mouX>619 and mouX<761) and (mouY>307 and mouY<332):
				windX=1600
				windY=1067

			if (mouX>775 and mouX<918) and (mouY>307 and mouY<332):
				windX=1600
				windY=1200

			################################################3
			####################                  Row EI 1800

			if (mouX>307 and mouX<449) and (mouY>347 and mouY<372):
				windX=1800
				windY=1800

			if (mouX>465 and mouX<607) and (mouY>347 and mouY<372):
				windX=1800
				windY=900

			if (mouX>619 and mouX<761) and (mouY>347 and mouY<372):
				windX=1800
				windY=1200

			if (mouX>775 and mouX<918) and (mouY>347 and mouY<372):
				windX=1800
				windY=1350

			################################################3
			####################                  line Gap

			if (mouX>307 and mouX<449) and (mouY>407 and mouY<432):
				lineGap = 0

			if (mouX>465 and mouX<607) and (mouY>407 and mouY<432):
				lineGap = 4

			if (mouX>619 and mouX<761) and (mouY>407 and mouY<432):
				lineGap = 8

			if (mouX>775 and mouX<918) and (mouY>407 and mouY<432):
				lineGap = 16

			################################################3
			####################                  OKAY

			if (mouX>307 and mouX<449) and (mouY>447 and mouY<472):
				sizeFou = True

			####################################### 157, 40



		if event.type == pygame.QUIT:
			quit=True
			sizeFou=True

	if windX==400 and windY==400:
		screen.blit(selected,(308,67))

	if windX==400 and windY==200:
		screen.blit(selected,(464,67))

	if windX==400 and windY==267:
		screen.blit(selected,(620,67))

	if windX==400 and windY==300:
		screen.blit(selected,(776,67))

	###############################################

	if windX==600 and windY==600:
		screen.blit(selected,(308,107))

	if windX==600 and windY==300:
		screen.blit(selected,(464,107))

	if windX==600 and windY==400:
		screen.blit(selected,(620,107))

	if windX==600 and windY==450:
		screen.blit(selected,(776,107))

	###############################################

	if windX==800 and windY==800:
		screen.blit(selected,(308,147))

	if windX==800 and windY==400:
		screen.blit(selected,(464,147))

	if windX==800 and windY==533:
		screen.blit(selected,(620,147))

	if windX==800 and windY==600:
		screen.blit(selected,(776,147))

	###############################################

	if windX==1000 and windY==1000:
		screen.blit(selected,(308,187))

	if windX==1000 and windY==500:
		screen.blit(selected,(464,187))

	if windX==1000 and windY==667:
		screen.blit(selected,(620,187))

	if windX==1000 and windY==750:
		screen.blit(selected,(776,187))

	###############################################

	if windX==1200 and windY==1200:
		screen.blit(selected,(308,227))

	if windX==1200 and windY==600:
		screen.blit(selected,(464,227))

	if windX==1200 and windY==800:
		screen.blit(selected,(620,227))

	if windX==1200 and windY==900:
		screen.blit(selected,(776,227))

	###############################################

	if windX==1400 and windY==1400:
		screen.blit(selected,(308,267))

	if windX==1400 and windY==700:
		screen.blit(selected,(464,267))

	if windX==1400 and windY==933:
		screen.blit(selected,(620,267))

	if windX==1400 and windY==1050:
		screen.blit(selected,(776,267))

	###############################################

	if windX==1600 and windY==1600:
		screen.blit(selected,(308,307))

	if windX==1600 and windY==800:
		screen.blit(selected,(464,307))

	if windX==1600 and windY==1067:
		screen.blit(selected,(620,307))

	if windX==1600 and windY==1200:
		screen.blit(selected,(776,307))

	###############################################

	if windX==1800 and windY==1800:
		screen.blit(selected,(308,347))

	if windX==1800 and windY==900:
		screen.blit(selected,(464,347))

	if windX==1800 and windY==1200:
		screen.blit(selected,(620,347))

	if windX==1800 and windY==1350:
		screen.blit(selected,(776,347))

	###############################################

	if lineGap == 0:
		screen.blit(selected,(308,407))

	if lineGap == 4:
		screen.blit(selected,(464,407))

	if lineGap == 8:
		screen.blit(selected,(620,407))

	if lineGap == 16:
		screen.blit(selected,(776,407))

	pygame.display.flip()
	#clock.tick(60)

if lineGap==1:
		lineGap = 4

if windX ==0 and windY ==0:
	windX = 1000
	windY = 500

screen = pygame.display.set_mode((windX,windY),pygame.RESIZABLE)

lineLen=(windX-(2*xMarg))/charWidth
lineNum=(windY-(2*yMarg))/(charHeight+lineGap)

maxLineNum = (windY-(2*yMarg))/(charHeight+lineGap)

charray = Doc()

keys = set([])
while quit==False:
	for event in pygame.event.get():

		if not (letCor['LEFTSHIFT'] in keys) and not (letCor['RIGHTSHIFT'] in keys):
			shiftCou = 1

		if event.type == pygame.KEYDOWN:
			howManyChars=0
			keys.add(event.key)

			if whichScript == 'normal':

				whichChar=superSet
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						whichScript = 'superscript'

				whichChar=subSet
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						whichScript = 'subscript'

				whichChar=slantySet
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						if slantyChek == False:
							slantyChek=True
						else:
							slantyChek=False

				whichChar=greekSet
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						whichScript ='greek'
						greekKeyActivate=True

			if whichScript=='greek' and greekKeyActivate==False:
				whichChar=greekSet
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						whichScript ='normal'



			if whichScript == 'superscript':

				whichChar=subSet
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						whichScript = 'normal'

			if whichScript == 'subscript':

				whichChar=superSet
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						whichScript = 'normal'

			######################## Check if this is a super script or sub script

			if whichScript == 'normal' or whichScript=='greek':

				################Check if greek

				if whichScript=='normal':

					######################## Lower case letters

					whichChar=lowercase__a
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

					whichChar=lowercase__b
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

					whichChar=lowercase__c
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

					whichChar=lowercase__d
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

					whichChar=lowercase__e
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

					whichChar=lowercase__f
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

					whichChar=lowercase__g
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

					whichChar=lowercase__h
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

					whichChar=lowercase__i
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

					whichChar=lowercase__j
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

					whichChar=lowercase__k
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

					whichChar=lowercase__l
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

					whichChar=lowercase__m
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

					whichChar=lowercase__n
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

					whichChar=lowercase__o
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

					whichChar=lowercase__p
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

					whichChar=lowercase__q
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

					whichChar=lowercase__r
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

					whichChar=lowercase__s
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

					whichChar=lowercase__t
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

					whichChar=lowercase__u
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

					whichChar=lowercase__v
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

					whichChar=lowercase__w
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

					whichChar=lowercase__x
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

					whichChar=lowercase__y
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

					whichChar=lowercase__z
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

					######################### Upper case Letters

					whichChar=uppercase__A
					for yit in range(len(whichChar.keys)):
						if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
							charray.charen.insert(curChar,addChar(whichChar))
							curChar+=1

					whichChar=uppercase__B
					for yit in range(len(whichChar.keys)):
						if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
							charray.charen.insert(curChar,addChar(whichChar))
							curChar+=1

					whichChar=uppercase__C
					for yit in range(len(whichChar.keys)):
						if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
							charray.charen.insert(curChar,addChar(whichChar))
							curChar+=1

					whichChar=uppercase__D
					for yit in range(len(whichChar.keys)):
						if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
							charray.charen.insert(curChar,addChar(whichChar))
							curChar+=1

					whichChar=uppercase__E
					for yit in range(len(whichChar.keys)):
						if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
							charray.charen.insert(curChar,addChar(whichChar))
							curChar+=1

					whichChar=uppercase__F
					for yit in range(len(whichChar.keys)):
						if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
							charray.charen.insert(curChar,addChar(whichChar))
							curChar+=1

					whichChar=uppercase__G
					for yit in range(len(whichChar.keys)):
						if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
							charray.charen.insert(curChar,addChar(whichChar))
							curChar+=1

					whichChar=uppercase__H
					for yit in range(len(whichChar.keys)):
						if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
							charray.charen.insert(curChar,addChar(whichChar))
							curChar+=1

					whichChar=uppercase__I
					for yit in range(len(whichChar.keys)):
						if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
							charray.charen.insert(curChar,addChar(whichChar))
							curChar+=1

					whichChar=uppercase__J
					for yit in range(len(whichChar.keys)):
						if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
							charray.charen.insert(curChar,addChar(whichChar))
							curChar+=1

					whichChar=uppercase__K
					for yit in range(len(whichChar.keys)):
						if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
							charray.charen.insert(curChar,addChar(whichChar))
							curChar+=1

					whichChar=uppercase__L
					for yit in range(len(whichChar.keys)):
						if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
							charray.charen.insert(curChar,addChar(whichChar))
							curChar+=1

					whichChar=uppercase__M
					for yit in range(len(whichChar.keys)):
						if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
							charray.charen.insert(curChar,addChar(whichChar))
							curChar+=1

					whichChar=uppercase__N
					for yit in range(len(whichChar.keys)):
						if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
							charray.charen.insert(curChar,addChar(whichChar))
							curChar+=1

					whichChar=uppercase__O
					for yit in range(len(whichChar.keys)):
						if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
							charray.charen.insert(curChar,addChar(whichChar))
							curChar+=1

					whichChar=uppercase__P
					for yit in range(len(whichChar.keys)):
						if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
							charray.charen.insert(curChar,addChar(whichChar))
							curChar+=1

					whichChar=uppercase__Q
					for yit in range(len(whichChar.keys)):
						if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
							charray.charen.insert(curChar,addChar(whichChar))
							curChar+=1

					whichChar=uppercase__R
					for yit in range(len(whichChar.keys)):
						if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
							charray.charen.insert(curChar,addChar(whichChar))
							curChar+=1

					whichChar=uppercase__S
					for yit in range(len(whichChar.keys)):
						if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
							charray.charen.insert(curChar,addChar(whichChar))
							curChar+=1

					whichChar=uppercase__T
					for yit in range(len(whichChar.keys)):
						if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
							charray.charen.insert(curChar,addChar(whichChar))
							curChar+=1

					whichChar=uppercase__U
					for yit in range(len(whichChar.keys)):
						if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
							charray.charen.insert(curChar,addChar(whichChar))
							curChar+=1

					whichChar=uppercase__V
					for yit in range(len(whichChar.keys)):
						if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
							charray.charen.insert(curChar,addChar(whichChar))
							curChar+=1

					whichChar=uppercase__W
					for yit in range(len(whichChar.keys)):
						if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
							charray.charen.insert(curChar,addChar(whichChar))
							curChar+=1

					whichChar=uppercase__X
					for yit in range(len(whichChar.keys)):
						if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
							charray.charen.insert(curChar,addChar(whichChar))
							curChar+=1

					whichChar=uppercase__Y
					for yit in range(len(whichChar.keys)):
						if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
							charray.charen.insert(curChar,addChar(whichChar))
							curChar+=1

					whichChar=uppercase__Z
					for yit in range(len(whichChar.keys)):
						if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
							charray.charen.insert(curChar,addChar(whichChar))
							curChar+=1
				elif whichScript=='greek':


					whichChar=greekSet
					for yit in range(len(whichChar.keys)):
						if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
							whichScript=='normal'

					whichChar=greek_lowercasealpha
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

					whichChar=greek_lowercasebeta
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

					whichChar=greek_lowercasegamma
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

					whichChar=greek_lowercasedelta
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

					whichChar=greek_lowercasezeta
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

					whichChar=greek_lowercaseeta
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

					whichChar=greek_lowercasetheta
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

					whichChar=greek_lowercaseiota
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

					whichChar=greek_lowercasekappa
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

					whichChar=greek_lowercaselambda
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

					whichChar=greek_lowercasemu
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

					whichChar=greek_lowercasenu
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

					whichChar=greek_lowercasexi
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

					whichChar=greek_lowercaseomicron
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

					whichChar=greek_lowercasepi
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

					whichChar=greek_lowercaserho
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

					whichChar=greek_lowercasesigma
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

					whichChar=greek_lowercasetau
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

					whichChar=greek_lowercaseupsilon
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

					whichChar=greek_lowercasephi
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

					whichChar=greek_lowercasechi
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

					whichChar=greek_lowercasepsi
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

					whichChar=greek_lowercaseomega
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

					###### Upper case Greek

					whichChar=greek_uppercasealpha
					for yit in range(len(whichChar.keys)):
						if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
							charray.charen.insert(curChar,addChar(whichChar))
							curChar+=1

					whichChar=greek_uppercasebeta
					for yit in range(len(whichChar.keys)):
						if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
							charray.charen.insert(curChar,addChar(whichChar))
							curChar+=1

					whichChar=greek_uppercasegamma
					for yit in range(len(whichChar.keys)):
						if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
							charray.charen.insert(curChar,addChar(whichChar))
							curChar+=1

					whichChar=greek_uppercasedelta
					for yit in range(len(whichChar.keys)):
						if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
							charray.charen.insert(curChar,addChar(whichChar))
							curChar+=1

					whichChar=greek_uppercaseepsilon
					for yit in range(len(whichChar.keys)):
						if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
							charray.charen.insert(curChar,addChar(whichChar))
							curChar+=1

					whichChar=greek_uppercasezeta
					for yit in range(len(whichChar.keys)):
						if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
							charray.charen.insert(curChar,addChar(whichChar))
							curChar+=1

					whichChar=greek_uppercaseeta
					for yit in range(len(whichChar.keys)):
						if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
							charray.charen.insert(curChar,addChar(whichChar))
							curChar+=1

					whichChar=greek_uppercasetheta
					for yit in range(len(whichChar.keys)):
						if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
							charray.charen.insert(curChar,addChar(whichChar))
							curChar+=1

					whichChar=greek_uppercaseiota
					for yit in range(len(whichChar.keys)):
						if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
							charray.charen.insert(curChar,addChar(whichChar))
							curChar+=1

					whichChar=greek_uppercasekappa
					for yit in range(len(whichChar.keys)):
						if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
							charray.charen.insert(curChar,addChar(whichChar))
							curChar+=1

					whichChar=greek_uppercaselambda
					for yit in range(len(whichChar.keys)):
						if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
							charray.charen.insert(curChar,addChar(whichChar))
							curChar+=1

					whichChar=greek_uppercasemu
					for yit in range(len(whichChar.keys)):
						if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
							charray.charen.insert(curChar,addChar(whichChar))
							curChar+=1

					whichChar=greek_uppercasenu
					for yit in range(len(whichChar.keys)):
						if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
							charray.charen.insert(curChar,addChar(whichChar))
							curChar+=1

					whichChar=greek_uppercasexi
					for yit in range(len(whichChar.keys)):
						if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
							charray.charen.insert(curChar,addChar(whichChar))
							curChar+=1

					whichChar=greek_uppercaseomicron
					for yit in range(len(whichChar.keys)):
						if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
							charray.charen.insert(curChar,addChar(whichChar))
							curChar+=1

					whichChar=greek_uppercasepi
					for yit in range(len(whichChar.keys)):
						if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
							charray.charen.insert(curChar,addChar(whichChar))
							curChar+=1

					whichChar=greek_uppercaserho
					for yit in range(len(whichChar.keys)):
						if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
							charray.charen.insert(curChar,addChar(whichChar))
							curChar+=1

					whichChar=greek_uppercasesigma
					for yit in range(len(whichChar.keys)):
						if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
							charray.charen.insert(curChar,addChar(whichChar))
							curChar+=1

					whichChar=greek_uppercasetau
					for yit in range(len(whichChar.keys)):
						if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
							charray.charen.insert(curChar,addChar(whichChar))
							curChar+=1

					whichChar=greek_uppercaseupsilon
					for yit in range(len(whichChar.keys)):
						if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
							charray.charen.insert(curChar,addChar(whichChar))
							curChar+=1

					whichChar=greek_uppercasephi
					for yit in range(len(whichChar.keys)):
						if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
							charray.charen.insert(curChar,addChar(whichChar))
							curChar+=1

					whichChar=greek_uppercasechi
					for yit in range(len(whichChar.keys)):
						if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
							charray.charen.insert(curChar,addChar(whichChar))
							curChar+=1

					whichChar=greek_uppercasepsi
					for yit in range(len(whichChar.keys)):
						if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
							charray.charen.insert(curChar,addChar(whichChar))
							curChar+=1

					whichChar=greek_uppercaseomega
					for yit in range(len(whichChar.keys)):
						if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
							charray.charen.insert(curChar,addChar(whichChar))
							curChar+=1


				#########################Punctuation

				whichChar=punctuation__period
				if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
					charray.charen.insert(curChar,addChar(whichChar))
					curChar+=1

				whichChar=punctuation__comma
				if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
					charray.charen.insert(curChar,addChar(whichChar))
					curChar+=1

				whichChar=punctuation__question
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

				whichChar=punctuation__exclaimation
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

				whichChar=punctuation__semicolon
				if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
					charray.charen.insert(curChar,addChar(whichChar))
					curChar+=1

				whichChar=punctuation__colon
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

				whichChar=punctuation__singlequote
				if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
					charray.charen.insert(curChar,addChar(whichChar))
					curChar+=1

				whichChar=punctuation__doublequote
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

				######################### Numbers

				whichChar=numeral__ze
				if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
					charray.charen.insert(curChar,addChar(whichChar))
					curChar+=1

				whichChar=numeral__on
				if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
					charray.charen.insert(curChar,addChar(whichChar))
					curChar+=1

				whichChar=numeral__tw
				if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
					charray.charen.insert(curChar,addChar(whichChar))
					curChar+=1

				whichChar=numeral__th
				if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
					charray.charen.insert(curChar,addChar(whichChar))
					curChar+=1

				whichChar=numeral__fo
				if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
					charray.charen.insert(curChar,addChar(whichChar))
					curChar+=1

				whichChar=numeral__fi
				if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
					charray.charen.insert(curChar,addChar(whichChar))
					curChar+=1

				whichChar=numeral__si
				if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
					charray.charen.insert(curChar,addChar(whichChar))
					curChar+=1

				whichChar=numeral__se
				if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
					charray.charen.insert(curChar,addChar(whichChar))
					curChar+=1

				whichChar=numeral__ei
				if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
					charray.charen.insert(curChar,addChar(whichChar))
					curChar+=1

				whichChar=numeral__ni
				if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
					charray.charen.insert(curChar,addChar(whichChar))
					curChar+=1

				######################### Modal Logic Characters

				whichChar=modallogic__possible
				if event.key in whichChar.keys and whichChar.keys.issubset(keys):
					for yit in [0]*2:
						if curChar!=0:
							charray.charen.pop(curChar-1)
							curChar-=1
					charray.charen.insert(curChar,addChar(whichChar))
					curChar+=1

				whichChar=modallogic__necessary
				if event.key in whichChar.keys and whichChar.keys.issubset(keys):
					for yit in [0]*2:
						if curChar!=0:
							charray.charen.pop(curChar-1)
							curChar-=1
					charray.charen.insert(curChar,addChar(whichChar))
					curChar+=1

				######################## First order logic

				whichChar=firstorderlogic__existential
				if event.key in whichChar.keys and whichChar.keys.issubset(keys):
					for yit in [0]*2:
						if curChar!=0:
							charray.charen.pop(curChar-1)
							curChar-=1
					charray.charen.insert(curChar,addChar(whichChar))
					curChar+=1

				whichChar=firstorderlogic__forall
				if event.key in whichChar.keys and whichChar.keys.issubset(keys):
					for yit in [0]*2:
						if curChar!=0:
							charray.charen.pop(curChar-1)
							curChar-=1
					charray.charen.insert(curChar,addChar(whichChar))
					curChar+=1

				whichChar=firstorderlogic__negation
				if event.key in whichChar.keys and whichChar.keys.issubset(keys):
					for yit in [0]*2:
						if curChar!=0:
							charray.charen.pop(curChar-1)
							curChar-=1
					charray.charen.insert(curChar,addChar(whichChar))
					curChar+=1

				whichChar=firstorderlogic__implication
				if event.key in whichChar.keys and whichChar.keys.issubset(keys):
					for yit in [0]*2:
						if curChar!=0:
							charray.charen.pop(curChar-1)
							curChar-=1
					charray.charen.insert(curChar,addChar(whichChar))
					curChar+=1

				whichChar=firstorderlogic__iff
				if event.key in whichChar.keys and whichChar.keys.issubset(keys):
					for yit in [0]*2:
						if curChar!=0:
							charray.charen.pop(curChar-1)
							curChar-=1
					charray.charen.insert(curChar,addChar(whichChar))
					curChar+=1

				whichChar=firstorderlogic__and
				if event.key in whichChar.keys and whichChar.keys.issubset(keys):
					for yit in [0]*2:
						if curChar!=0:
							charray.charen.pop(curChar-1)
							curChar-=1
					charray.charen.insert(curChar,addChar(whichChar))
					curChar+=1

				whichChar=firstorderlogic__xor
				if event.key in whichChar.keys and whichChar.keys.issubset(keys):
					for yit in [0]*2:
						if curChar!=0:
							charray.charen.pop(curChar-1)
							curChar-=1
					charray.charen.insert(curChar,addChar(whichChar))
					curChar+=1

				whichChar=firstorderlogic__nand
				if event.key in whichChar.keys and whichChar.keys.issubset(keys):
					for yit in [0]*2:
						if curChar!=0:
							charray.charen.pop(curChar-1)
							curChar-=1
					charray.charen.insert(curChar,addChar(whichChar))
					curChar+=1

				######################### Math

				whichChar=math__equals
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys and whichChar.keys.issubset(keys):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

				whichChar=math__greaterthan
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

				whichChar=math__greaterthanorequal
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						for yit in [0]*2:
							if curChar!=0:
								charray.charen.pop(curChar-1)
								curChar-=1
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

				whichChar=math__lessthan
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

				whichChar=math__lessthanorequal
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						for yit in [0]*2:
							if curChar!=0:
								charray.charen.pop(curChar-1)
								curChar-=1
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

				whichChar=math__division
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						for yit in [0]*2:
							if curChar!=0:
								charray.charen.pop(curChar-1)
								curChar-=1
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

				whichChar=math__approximately
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						for yit in [0]*2:
							if curChar!=0:
								charray.charen.pop(curChar-1)
								curChar-=1
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

				whichChar=math__plus
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						for yit in [0]*2:
							if curChar!=0:
								charray.charen.pop(curChar-1)
								curChar-=1
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

				whichChar=math__minus
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

				whichChar=math__multiply
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						for yit in [0]*2:
							if curChar!=0:
								charray.charen.pop(curChar-1)
								curChar-=1
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

				whichChar=math__forwardslash
				for yit in range(len(whichChar.keys)):
					if (event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys)) and not (letCor['LEFTSHIFT'] in keys or letCor['RIGHTSHIFT'] in keys):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

				whichChar=math__backslash
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

				whichChar=math__QED
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						for yit in [0]*2:
							if curChar!=0:
								charray.charen.pop(curChar-1)
								curChar-=1
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

				whichChar=math__squareroot
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						for yit in [0]*2:
							if curChar!=0:
								charray.charen.pop(curChar-1)
								curChar-=1
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

				whichChar=math__plusminus
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						for yit in [0]*2:
							if curChar!=0:
								charray.charen.pop(curChar-1)
								curChar-=1
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

				whichChar=math__integral
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						for yit in [0]*2:
							if curChar!=0:
								charray.charen.pop(curChar-1)
								curChar-=1
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

				whichChar=math__notequal
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						for yit in [0]*2:
							if curChar!=0:
								charray.charen.pop(curChar-1)
								curChar-=1
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

				whichChar=math__angle
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						for yit in [0]*2:
							if curChar!=0:
								charray.charen.pop(curChar-1)
								curChar-=1
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

				whichChar=math__triangle
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						for yit in [0]*2:
							if curChar!=0:
								charray.charen.pop(curChar-1)
								curChar-=1
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

				whichChar=math__gradient
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						for yit in [0]*2:
							if curChar!=0:
								charray.charen.pop(curChar-1)
								curChar-=1
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

				whichChar=math__divides
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						for yit in [0]*2:
							if curChar!=0:
								charray.charen.pop(curChar-1)
								curChar-=1
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

				whichChar=math__doesntdivide
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						for yit in [0]*2:
							if curChar!=0:
								charray.charen.pop(curChar-1)
								curChar-=1
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

				########################### Brackets

				whichChar=brackets__leftparentheses
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

				whichChar=brackets__rightparentheses
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

				whichChar=brackets__leftbracket
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

				whichChar=brackets__rightbracket
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

				whichChar=brackets__leftcurly
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						for yit in [0]*1:
							if curChar!=0:
								charray.charen.pop(curChar-1)
								curChar-=1
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

				whichChar=brackets__rightcurly
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						for yit in [0]*1:
							if curChar!=0:
								charray.charen.pop(curChar-1)
								curChar-=1
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

				whichChar=brackets__leftchevron
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						for yit in [0]*2:
							if curChar!=0:
								charray.charen.pop(curChar-1)
								curChar-=1
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

				whichChar=brackets__rightchevron
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						for yit in [0]*2:
							if curChar!=0:
								charray.charen.pop(curChar-1)
								curChar-=1
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

				######################### Misc

				whichChar=misc__atsign
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

				whichChar=misc__numbersign
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

				whichChar=misc__dollarsign
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

				whichChar=misc__percentsign
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

				whichChar=misc__carrot
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

				whichChar=misc__ambersand
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

				######################### Proof Theory

				whichChar=prooftheory__singleturnstile
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						for yit in [0]*2:
							if curChar!=0:
								charray.charen.pop(curChar-1)
								curChar-=1
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

				whichChar=prooftheory__notsingleturnstile
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						for yit in [0]*2:
							if curChar!=0:
								charray.charen.pop(curChar-1)
								curChar-=1
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

				whichChar=prooftheory__doubleturnstile
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						for yit in [0]*2:
							if curChar!=0:
								charray.charen.pop(curChar-1)
								curChar-=1
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

				whichChar=prooftheory__notdoubleturnstile
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						for yit in [0]*2:
							if curChar!=0:
								charray.charen.pop(curChar-1)
								curChar-=1
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

				whichChar=prooftheory__logicalconstant
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						for yit in [0]*2:
							if curChar!=0:
								charray.charen.pop(curChar-1)
								curChar-=1
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

				######################### Set Theory

				whichChar=settheory__elementof
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						for yit in [0]*2:
							if curChar!=0:
								charray.charen.pop(curChar-1)
								curChar-=1
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

				whichChar=settheory__notelementof
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						for yit in [0]*2:
							if curChar!=0:
								charray.charen.pop(curChar-1)
								curChar-=1
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

				whichChar=settheory__nullset
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						for yit in [0]*2:
							if curChar!=0:
								charray.charen.pop(curChar-1)
								curChar-=1
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

				whichChar=settheory__intersection
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						for yit in [0]*2:
							if curChar!=0:
								charray.charen.pop(curChar-1)
								curChar-=1
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

				whichChar=settheory__union
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						for yit in [0]*2:
							if curChar!=0:
								charray.charen.pop(curChar-1)
								curChar-=1
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

				whichChar=settheory__superset
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						for yit in [0]*2:
							if curChar!=0:
								charray.charen.pop(curChar-1)
								curChar-=1
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

				whichChar=settheory__subset
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						for yit in [0]*2:
							if curChar!=0:
								charray.charen.pop(curChar-1)
								curChar-=1
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

				whichChar=settheory__notsuperset
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						for yit in [0]*2:
							if curChar!=0:
								charray.charen.pop(curChar-1)
								curChar-=1
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

				whichChar=settheory__notsubset
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						for yit in [0]*2:
							if curChar!=0:
								charray.charen.pop(curChar-1)
								curChar-=1
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

				######################### Alexander Hamilton

				whichChar=hamilton__On
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						for yit in [0]*2:
							if curChar!=0:
								charray.charen.pop(curChar-1)
								curChar-=1
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

				whichChar=hamilton__Tw
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						for yit in [0]*2:
							if curChar!=0:
								charray.charen.pop(curChar-1)
								curChar-=1
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

				whichChar=hamilton__Th
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						for yit in [0]*2:
							if curChar!=0:
								charray.charen.pop(curChar-1)
								curChar-=1
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

				whichChar=hamilton__Fo
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						for yit in [0]*2:
							if curChar!=0:
								charray.charen.pop(curChar-1)
								curChar-=1
						charray.charen.insert(curChar,addChar(whichChar))
						curChar+=1

				######################### Commandy keys

				if event.key in space.keys:
					charray.charen.insert(curChar,addChar(space))
					curChar+=1

	 			if event.key in enter.keys:
					charray.charen.insert(curChar,addChar(enter))
					curChar+=1

				if event.key in backspace.keys:
					if curChar!=0:
						charray.charen.pop(curChar-1)
						curChar-=1

				if event.key in backspace.keys and ((letCor['LEFTSHIFT'] in keys) or (letCor['RIGHTSHIFT'] in keys)):
					for yit in [0]*shiftCou:
						if curChar!=0:
							charray.charen.pop(curChar-1)
							curChar-=1
					shiftCou=shiftCou*shiftMag

				if event.key in backspace.keys and ((letCor['LEFTCONTROL'] in keys) or (letCor['RIGHTCONTROL'] in keys)):
					for yit in [0]*6:
						if curChar!=0:
							charray.charen.pop(curChar-1)
							curChar-=1

				if event.key in leftarrow.keys:
					if curChar>0:
						curChar-=1

				if event.key in leftarrow.keys and ((letCor['LEFTSHIFT'] in keys) or (letCor['RIGHTSHIFT'] in keys)):
					for yit in [0]*shiftCou:
						if curChar>0:
							curChar-=1
					shiftCou=shiftCou*shiftMag

				if event.key in leftarrow.keys and ((letCor['LEFTCONTROL'] in keys) or (letCor['RIGHTCONTROL'] in keys)):
					for yit in [0]*6:
						if curChar>0:
							curChar-=1

				if event.key in rightarrow.keys:
					if curChar<(len(charray.charen)):
						curChar+=1

				if event.key in rightarrow.keys and ((letCor['LEFTSHIFT'] in keys) or (letCor['RIGHTSHIFT'] in keys)):
					for yit in [0]*shiftCou:
						if event.key in rightarrow.keys:
							if curChar<(len(charray.charen)):
								curChar+=1

				if event.key in rightarrow.keys and ((letCor['LEFTCONTROL'] in keys) or (letCor['RIGHTCONTROL'] in keys)):
					for yit in [0]*6:
						if event.key in rightarrow.keys:
							if curChar<(len(charray.charen)):
								curChar+=1

				if event.key in uparrow.keys and cursorLine!=0:
					savX=curX
					savY=curY
					coucou = 0
					while (curY!=(savY-(charHeight+lineGap)) or curX>=savX) and coucou<lineLen:
						coucou+=1
						blitScreen = []
						thisLin = 0
						blitScreen.append( [0,[]] )
						cursorChar = 0
						cursorVort = 0
						cursorLine = 0

				if event.key in downarrow.keys and cursorLine!=(len(blitScreen)-1):
					savX=curX
					savY=curY
					coucou = 0
					while (curY<=(savY+(charHeight+lineGap)) or curX>savX) and coucou<lineLen:
						coucou+=1
						blitScreen = []
						thisLin = 0
						blitScreen.append( [0,[]] )
						cursorChar = 0
						cursorVort = 0
						cursorLine = 0

			########################################## Saving DOcuments

				whichChar=save
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):

						##### Backspace the 's' we just added to the document
						charray.charen.pop(curChar-1)
						curChar-=1

						##### Get the name of the file
						saveName=tkFileDialog.asksaveasfilename()
						saveName=str(saveName)

						###### Make sure the file gets a name. If the Users hits cancel the name is '', therefore we shouldnt save anything
						if saveName!='':
							
							##### Paste Each page onto the screen and take a picture of it naming it 'pag'+page Number+'.PNG'
							hsyCou=0

							screen.fill((0,0,0))
							#Pag (hsy) in pagen
							for hsy in pagen:
								blitCharen=[]
								yitCou=0
								#For the linen in pag (hsy)
								for yit in hsy:
									blitCharen.append([])
									#for the vorten in linen
									for vapp in yit[1]:
										#for the charen in vorten
										for gno in vapp:
											blitCharen[yitCou].append(gno)
									#Paste every char in line of pag		
									for vapp in range(lineLen):
										if vapp<len(blitCharen[yitCou]):
											screen.blit(blitCharen[yitCou][vapp][0].image,[(vapp*charWidth)+xMarg,yitCou*(charHeight+lineGap)+yMarg])
											for dukh in range(len(blitCharen[yitCou][vapp][1])):
												screen.blit(blitCharen[yitCou][vapp][1][dukh].lilimage,[(vapp*charWidth)+(dukh*lilcharWidth)+xMarg+lilCharOffsetX,(yitCou*(charHeight+lineGap))+lilCharOffsetSuperSetY+yMarg])
											for dukh in range(len(blitCharen[yitCou][vapp][2])):
												screen.blit(blitCharen[yitCou][vapp][2][dukh].lilimage,[(vapp*charWidth)+(dukh*lilcharWidth)+xMarg+lilCharOffsetX,(yitCou*(charHeight+lineGap))+lilCharOffsetSubSetY+yMarg])
										else:
											screen.blit(L_S,[(vapp*charWidth)+xMarg,yitCou*(charHeight+lineGap)+yMarg])
									yitCou+=1
								pygame.image.save(screen,'pag'+str(hsyCou)+'.PNG')
								screen.fill((0,0,0))
								hsyCou+=1

							###### Stitch pages together
							stXs,stYs = 0,0
							for hsy in range(len(pagen)):
								filName="pag"+str(hsy)+".PNG"
								thX, thY=Image.open(filName).size
								stXs=thX
								stYs+=thY
							stImage = Image.new('RGB',(stXs,stYs),'black')
							for hsy in range(len(pagen)):
								stImage.paste(Image.open('pag'+str(hsy)+'.PNG'),(0,hsy*windY,stXs,windY+(hsy*windY)))

							############## Put the character in the pixel
							#############################################

							####### Make an array of all the character digits
							charCodes=[]
							for yit in charray.charen:
								charCodes.append(yit[0].keyDig)
							pixelCharCodes=[]

							##### Make an array of all the superScript digits, where the even indexed elements are the character they belong to, and the odd indexed elements are the character digits
							superRay =[]
							for yit in range(len(charray.charen)):
								for vapp in range(len(charray.charen[yit][1])):
									superRay.append(yit)
									superRay.append(charray.charen[yit][1][vapp].keyDig)
							###### Add '161' to the CharCodes array so that we can end it with the signal that there are superscripts
							#if len(superRay):
							charCodes.append(161) 

							###### Store the charCodes as pixel values
							pixelCharCodes=[]
							# Make sure there is an event amount of CharCodes, 0s wont be read
							if len(charCodes)%2==1:
								charCodes.append(0)
							for yit in range(len(charCodes)/2):
								red, green, blue = 0,0,0

								# ((_,_),(_,_),(=,=)) -v
								blue=(charCodes[yit*2])%256 
								# ((_,_),(_,+),(_,_)) -v
								green+=((charCodes[yit*2])/256)%16 # This value should not exceed 16. Problems will occur if it does, the modulus is present to store the value incorrectly, where it would otherwise crash the whole program

								# ((=,=),(_,_),(_,_)) -v
								red=((charCodes[(yit*2)+1])/16)%256 # This value should not exceed 256. The justification is similar to the one given in the comment above
								# ((_,_),(+,_),(_,_)) -v
								green+=((charCodes[(yit*2)+1])%16)*16 

								#### What is going on here?
								#### I need to store the character digits in the pixels
								#### If I store the digit in a color value, I am constrained to 256 possible characters, which I consider too low
								#### If I store the digit in all three color values I have 16,777,216 possible characters, which is excessive
								#### Thus, I am left with the more difficult task of storing two character digits in 3 pixel values, leading me to a cozy 4096 possible characters
								#### The way I am doing this is re-allocating the three 16^2 color values, into two 16^3 chacacter digit values //// (16*16)*(16*16)*(16*16) = (16*16*16)*(16*16*16) .  Character Digit<(16*16*16)

								pixelCharCodes.append((red,green,blue))

							##### Make an array of all the subcript digits, where the even indexed elements are the character they belong to, and the odd indexed elements are the character digits
							subRay =[]
							for yit in range(len(charray.charen)):
								for vapp in range(len(charray.charen[yit][2])):
									subRay.append(yit)
									subRay.append(charray.charen[yit][2][vapp].keyDig)
							###### Add '162' to the superRay array so that we can end it with the signal that there are subScripts
							#if len(subRay):
							#	print 'Yep, subRay'
							

							##### Store the superScripts as pixel values
							for yit in range(len(superRay)/2):
								red, green, blue = 0,0,0

								##### The location of the superscript needs to be stored one higher than its actual value. 
								##### This is to avoid the unlikely circumstance that the superscript corresponds to the
								##### First letter (the zeroth letter).
								#####
								##### The first letter, stored as a zero, would be transparent to the open function

								blue = (superRay[yit*2]+1)%256
								green = ((superRay[yit*2]+1)/256)%256
								red = (superRay[yit*2]+1)/65536
								pixelCharCodes.append((red,green,blue))

								blue = superRay[(yit*2)+1]%256
								green = (superRay[(yit*2)+1]/256)%256
								red = superRay[(yit*2)+1]/65536
								pixelCharCodes.append((red,green,blue))

							pixelCharCodes.append((0,0,162))

							##### Store the subScripts as pixel values
							for yit in range(len(subRay)/2):
								red, green, blue = 0,0,0

								blue = (subRay[yit*2]+1)%256
								green = ((subRay[yit*2]+1)/256)%256
								red = (subRay[yit*2]+1)/65536
								pixelCharCodes.append((red,green,blue))

								blue = subRay[(yit*2)+1]%256
								green = (subRay[(yit*2)+1]/256)%256
								red = subRay[(yit*2)+1]/65536
								pixelCharCodes.append((red,green,blue))

							##### Put the pixels on the image
							for yit in range(len(pixelCharCodes)):
								print pixelCharCodes[yit]
								stImage.putpixel( (yit/stYs,yit%stYs), pixelCharCodes[yit] )

							##### Then save the image
							try:
								if '.PNG' in saveName:
									stImage.save(saveName,"png")
								else:
									stImage.save(saveName+'.PNG',"png")
							except:
								pass

				######################################## Opening Documents

				whichChar=oPen
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						openName=tkFileDialog.askopenfilename()
						openName = str(openName)
						openIm = Image.open(openName)
						xSize,ySize = openIm.size
						charray = Doc()
						red,green,blue = openIm.getpixel((0,0))

						whatsGoinOn='addingChars'
						for yit in range(ySize*xMarg):
							if whatsGoinOn=='addingChars':
								red,green,blue = openIm.getpixel((yit/(ySize),yit%(ySize)))

								onNum=0
								twNum=0

								onNum+=blue
								twNum+=(red*16)

								onNum+=(green%16)*16
								twNum+=(green/16)

								if onNum!=161 and onNum!=0:
									charray.charen.append(addChar(charLets[onNum]))
								if twNum!=161 and twNum!=0:
									charray.charen.append(addChar(charLets[twNum]))

								if onNum==161 or twNum==161:
									whatsGoinOn='addingSuperscripts'
									even=True

							elif whatsGoinOn=='addingSuperscripts':
								red,green,blue = openIm.getpixel((yit/(ySize),yit%(ySize)))
								if (red,green,blue)!=(0,0,162):
									if (red,green,blue)!=(0,0,0):
										if even==True:
											charSpot=0
											charSpot+=blue
											charSpot+=green*256
											charSpot+=red*65536
											charSpot-=1
											even=False
										elif even!=True:
											partSuper=0
											partSuper+=blue
											partSuper+=green*256
											partSuper+=red*65536
											print 'PARTSUPER',partSuper,'CHARSPOT',charSpot,'RGB',(red,green,blue)
											charray.charen[charSpot][1].append(charLets[partSuper])
											even=True
								else:
									whatsGoinOn='addingSubscripts'
									even=True

							elif whatsGoinOn=='addingSubscripts':
								red,green,blue = openIm.getpixel((yit/(ySize),yit%(ySize)))
								if (red,green,blue)!=(0,0,0):
									if even==True:
										charSpot=0
										charSpot+=blue
										charSpot+=green*256
										charSpot+=red*65536
										charSpot-=1
										even=False
									elif even!=True:
										partSub=0
										partSub+=blue
										partSub+=green*256
										partSub+=red*65536
										print 'PART SUB',partSub,'CHARSPOT',charSpot,'RGB',(red,green,blue)
										charray.charen[charSpot][2].append(charLets[partSub])
										even=True

						curChar=len(charray.charen)-1

			else: #Else, as in whichscript!='normal'

				if whichScript == 'superscript':

					whichChar=lowercase__a
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][1].append(whichChar)

					whichChar=lowercase__b
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][1].append(whichChar)

					whichChar=lowercase__c
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][1].append(whichChar)

					whichChar=lowercase__d
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][1].append(whichChar)

					whichChar=lowercase__e
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][1].append(whichChar)

					whichChar=lowercase__f
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][1].append(whichChar)

					whichChar=lowercase__g
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][1].append(whichChar)

					whichChar=lowercase__h
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][1].append(whichChar)

					whichChar=lowercase__i
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][1].append(whichChar)

					whichChar=lowercase__j
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][1].append(whichChar)

					whichChar=lowercase__k
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][1].append(whichChar)

					whichChar=lowercase__l
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][1].append(whichChar)	

					whichChar=lowercase__m
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][1].append(whichChar)

					whichChar=lowercase__n
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][1].append(whichChar)

					whichChar=lowercase__o
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][1].append(whichChar)

					whichChar=lowercase__p
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][1].append(whichChar)

					whichChar=lowercase__q
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][1].append(whichChar)

					whichChar=lowercase__r
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][1].append(whichChar)

					whichChar=lowercase__s
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][1].append(whichChar)

					whichChar=lowercase__t
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][1].append(whichChar)

					whichChar=lowercase__u
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][1].append(whichChar)

					whichChar=lowercase__v
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][1].append(whichChar)

					whichChar=lowercase__w
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][1].append(whichChar)

					whichChar=lowercase__x
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][1].append(whichChar)

					whichChar=lowercase__y
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][1].append(whichChar)

					whichChar=lowercase__z
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][1].append(whichChar)

					whichChar=numeral__on
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][1].append(whichChar)

					whichChar=numeral__tw
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][1].append(whichChar)

					whichChar=numeral__th
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][1].append(whichChar)

					whichChar=numeral__fo
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][1].append(whichChar)

					whichChar=numeral__fi
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][1].append(whichChar)

					whichChar=numeral__si
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][1].append(whichChar)

					whichChar=numeral__se
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][1].append(whichChar)

					whichChar=numeral__ei
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][1].append(whichChar)

					whichChar=numeral__ni
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][1].append(whichChar)

					whichChar=numeral__ze
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][1].append(whichChar)

				if whichScript == 'subscript':

					whichChar=lowercase__a
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][2].append(whichChar)

					whichChar=lowercase__b
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][2].append(whichChar)

					whichChar=lowercase__c
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][2].append(whichChar)

					whichChar=lowercase__d
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][2].append(whichChar)

					whichChar=lowercase__e
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][2].append(whichChar)

					whichChar=lowercase__f
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][2].append(whichChar)

					whichChar=lowercase__g
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][2].append(whichChar)

					whichChar=lowercase__h
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][2].append(whichChar)

					whichChar=lowercase__i
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][2].append(whichChar)

					whichChar=lowercase__j
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][2].append(whichChar)

					whichChar=lowercase__k
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][2].append(whichChar)

					whichChar=lowercase__l
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][2].append(whichChar)	

					whichChar=lowercase__m
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][2].append(whichChar)

					whichChar=lowercase__n
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][2].append(whichChar)

					whichChar=lowercase__o
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][2].append(whichChar)

					whichChar=lowercase__p
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][2].append(whichChar)

					whichChar=lowercase__q
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][2].append(whichChar)

					whichChar=lowercase__r
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][2].append(whichChar)

					whichChar=lowercase__s
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][2].append(whichChar)

					whichChar=lowercase__t
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][2].append(whichChar)

					whichChar=lowercase__u
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][2].append(whichChar)

					whichChar=lowercase__v
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][2].append(whichChar)

					whichChar=lowercase__w
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][2].append(whichChar)

					whichChar=lowercase__x
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][2].append(whichChar)

					whichChar=lowercase__y
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][2].append(whichChar)

					whichChar=lowercase__z
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][2].append(whichChar)

					whichChar=numeral__ze
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][2].append(whichChar)

					whichChar=numeral__on
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][2].append(whichChar)

					whichChar=numeral__tw
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][2].append(whichChar)

					whichChar=numeral__th
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][2].append(whichChar)

					whichChar=numeral__fo
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][2].append(whichChar)

					whichChar=numeral__fi
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][2].append(whichChar)

					whichChar=numeral__si
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][2].append(whichChar)

					whichChar=numeral__se
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][2].append(whichChar)

					whichChar=numeral__ei
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][2].append(whichChar)

					whichChar=numeral__ni
					if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
						charray.charen[curChar-1][2].append(whichChar)

		############################## Fill the screen with black

		screen.fill((0,0,0))

		############################ Turn charray into vorten

		vorten=[]
		forward=0
		vorten.append([])
		whichChar=0
		vortChar=0
		cursorVort=0


		for yit in charray.charen:
			whichChar+=1
			#Add this char to vorten
			if yit!=addChar(space) and yit!=addChar(enter):
				vorten[forward].append(yit)
			if yit==addChar(space):
				vorten[forward].append(yit)
				vorten.append([])
				forward+=1
			if yit==addChar(enter):
				if vorten[forward]==[]:
					vorten[forward].append(yit)
					vorten.append([])
					forward+=1
				else:
					vorten.append([])
					forward+=1
					vorten[forward].append(yit)
					vorten.append([])
					forward+=1
			#Check if its the current char
			if whichChar==curChar:
				cursorVort=forward
				vortChar=len(vorten[forward])

		############################### Turn vorten in Linen

		linen = []
		linen.append([0,[]])
		thisLin=0
		cursorLine=0
		whichVort=0
		vortInLin=0

		for yit in vorten:
			#Add vort to Linen
			if yit==[addChar(enter)]:
				linen.append([0,[]])
				thisLin+=1
			else:
				if (linen[thisLin][0]+len(yit))<=lineLen:
					linen[thisLin][1].append(yit)
					linen[thisLin][0]+=len(yit)
				else:
					linen.append([0,[]])
					thisLin+=1
					linen[thisLin][0]=len(yit)
					linen[thisLin][1].append(yit)
			#Check if its the current line
			if whichVort==cursorVort:
				cursorLine=thisLin
				vortInLin=len(linen[thisLin][1])
			whichVort+=1
		lineChar=0
		cursorChar=0
		for yit in range(vortInLin-1):
			lineChar+=len(linen[cursorLine][1][yit])
		cursorChar=lineChar+vortChar

		############################ Turn lines into pagen

		pagen=[]
		linCou=0

		for yit in linen:
			if linCou%maxLineNum==0:
				pagen.append([])
			pagen[len(pagen)-1].append(yit)
			linCou+=1

		whichPag=cursorLine/maxLineNum

		############################ Turn pagen back into charen, and blit

		blitCharen=[]
		yitCou=0

		#For the linen in pagen
		for yit in pagen[whichPag]:
			blitCharen.append([])
			#for the vorten in linen
			for vapp in yit[1]:
				#for the charen in vorten
				for gno in vapp:
					blitCharen[yitCou].append(gno)
			#Paste every char in line of pag		
			for vapp in range(lineLen):
				if vapp<len(blitCharen[yitCou]):
					screen.blit(blitCharen[yitCou][vapp][0].image,[(vapp*charWidth)+xMarg,yitCou*(charHeight+lineGap)+yMarg])
					for dukh in range(len(blitCharen[yitCou][vapp][1])):
						screen.blit(blitCharen[yitCou][vapp][1][dukh].lilimage,[(vapp*charWidth)+(dukh*lilcharWidth)+xMarg+lilCharOffsetX,(yitCou*(charHeight+lineGap))+lilCharOffsetSuperSetY+yMarg])
					for dukh in range(len(blitCharen[yitCou][vapp][2])):
						screen.blit(blitCharen[yitCou][vapp][2][dukh].lilimage,[(vapp*charWidth)+(dukh*lilcharWidth)+xMarg+lilCharOffsetX,(yitCou*(charHeight+lineGap))+lilCharOffsetSubSetY+yMarg])
				else:
					screen.blit(L_S,[(vapp*charWidth)+xMarg,yitCou*(charHeight+lineGap)+yMarg])
			yitCou+=1
		screen.blit(L_C,[xMarg+(cursorChar*charWidth),yMarg+(cursorLine%maxLineNum)*(charHeight+lineGap)])

		######################################
		
		if event.type == pygame.KEYUP:
			keys.remove(event.key)
			greekKeyActivate=False
		if event.type == pygame.QUIT:
			quit = True

	pygame.display.flip()
	clock.tick(60)

pygame.quit()
