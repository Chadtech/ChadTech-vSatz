import os
import pygame
import PIL
from PIL import Image
import Tkinter, tkFileDialog
brunk = Tkinter.Tk()
brunk.withdraw()

screenWidth=1366
screenHeight=724

screen = pygame.display.set_mode((1366,724),pygame.RESIZABLE)

os.chdir(os.path.abspath('chars12x16'))

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
os.chdir(os.path.abspath('Punctuation'))

#Punctuation
L_pQuestion = pygame.image.load('char0.PNG').convert()
L_pExclaimation = pygame.image.load('char1.PNG').convert()
L_pPeriod = pygame.image.load('char2.PNG').convert()
L_pComma = pygame.image.load('char3.PNG').convert()
L_pColon = pygame.image.load('char4.PNG').convert()
L_pSemicolon = pygame.image.load('char5.PNG').convert()
L_pSinglequote = pygame.image.load('char6.PNG').convert()

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
L_mEq = pygame.image.load('char0.PNG').convert()
L_mGt = pygame.image.load('char1.PNG').convert()
L_mGe = pygame.image.load('char2.PNG').convert()
L_mLt = pygame.image.load('char3.PNG').convert()
L_mLe = pygame.image.load('char4.PNG').convert()
L_mDi = pygame.image.load('char5.PNG').convert()
L_mAp = pygame.image.load('char6.PNG').convert()
L_mPl = pygame.image.load('char7.PNG').convert()
L_mSb = pygame.image.load('char8.PNG').convert()
L_mMu = pygame.image.load('char9.PNG').convert()
L_mFs = pygame.image.load('char10.PNG').convert()
L_mBs = pygame.image.load('char11.PNG').convert()
L_mQe = pygame.image.load('char12.PNG').convert()
L_mSr = pygame.image.load('char13.PNG').convert()
L_mAs = pygame.image.load('char14.PNG').convert()
L_mAd = pygame.image.load('char15.PNG').convert()
L_mNe = pygame.image.load('char16.PNG').convert()
L_mAn = pygame.image.load('char17.PNG').convert()
L_mDe = pygame.image.load('char18.PNG').convert()
L_mGr = pygame.image.load('char19.PNG').convert()
L_mIn = pygame.image.load('char20.PNG').convert()
L_mDv = pygame.image.load('char21.PNG').convert()

os.chdir(os.path.dirname(os.getcwd()))
os.chdir(os.path.abspath('FirstOrderLogic'))

#First Order Logic
L_fE = pygame.image.load('char0.PNG').convert()
L_fA = pygame.image.load('char1.PNG').convert()
L_fN = pygame.image.load('char2.PNG').convert()
L_fI = pygame.image.load('char3.PNG').convert()
L_fF = pygame.image.load('char4.PNG').convert()
L_fD = pygame.image.load('char5.PNG').convert()

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
L_blp = pygame.image.load('char0.PNG').convert()
L_brp = pygame.image.load('char1.PNG').convert()
L_blc = pygame.image.load('char2.PNG').convert()
L_brc = pygame.image.load('char3.PNG').convert()
L_blb = pygame.image.load('char4.PNG').convert()
L_brb = pygame.image.load('char5.PNG').convert()
L_blh = pygame.image.load('char6.PNG').convert()
L_brh = pygame.image.load('char7.PNG').convert()

os.chdir(os.path.dirname(os.getcwd()))
os.chdir(os.path.abspath('setTheory'))

#set Theory
L_sEo = pygame.image.load('char0.PNG').convert()
L_sDc = pygame.image.load('char1.PNG').convert()
L_sNs = pygame.image.load('char2.PNG').convert()
L_sIn = pygame.image.load('char3.PNG').convert()
L_sUn = pygame.image.load('char4.PNG').convert()
L_sBs = pygame.image.load('char5.PNG').convert()
L_sSs = pygame.image.load('char6.PNG').convert()
L_sNp = pygame.image.load('char7.PNG').convert()
L_sNb = pygame.image.load('char8.PNG').convert()

os.chdir(os.path.dirname(os.getcwd()))
os.chdir(os.path.abspath('ProofTheory'))

#Proof Theory
L_pSt = pygame.image.load('char0.PNG').convert()
L_pNs = pygame.image.load('char1.PNG').convert()
L_pDt = pygame.image.load('char2.PNG').convert()
L_pNd = pygame.image.load('char3.PNG').convert()
L_pLc = pygame.image.load('char4.PNG').convert()

os.chdir(os.path.dirname(os.getcwd()))
os.chdir(os.path.abspath('Cursor'))

#Under Cursor
L_C = pygame.image.load('char0.PNG').convert()

os.chdir(os.path.dirname(os.getcwd()))
os.chdir(os.path.abspath('Cursor Lowercase'))
#lower case letters
C_la = pygame.image.load('char0.PNG').convert()
C_lb = pygame.image.load('char1.PNG').convert()
C_lc = pygame.image.load('char2.PNG').convert()
C_ld = pygame.image.load('char3.PNG').convert()
C_le = pygame.image.load('char4.PNG').convert()
C_lf = pygame.image.load('char5.PNG').convert()
C_lg = pygame.image.load('char6.PNG').convert()
C_lh = pygame.image.load('char7.PNG').convert()
C_li = pygame.image.load('char8.PNG').convert()
C_lj = pygame.image.load('char9.PNG').convert()
C_lk = pygame.image.load('char10.PNG').convert()
C_ll = pygame.image.load('char11.PNG').convert()
C_lm = pygame.image.load('char12.PNG').convert()
C_ln = pygame.image.load('char13.PNG').convert()
C_lo = pygame.image.load('char14.PNG').convert()
C_lp = pygame.image.load('char15.PNG').convert()
C_lq = pygame.image.load('char16.PNG').convert()
C_lr = pygame.image.load('char17.PNG').convert()
C_ls = pygame.image.load('char18.PNG').convert()
C_lt = pygame.image.load('char19.PNG').convert()
C_lu = pygame.image.load('char20.PNG').convert()
C_lv = pygame.image.load('char21.PNG').convert()
C_lw = pygame.image.load('char22.PNG').convert()
C_lx = pygame.image.load('char23.PNG').convert()
C_ly = pygame.image.load('char24.PNG').convert()
C_lz = pygame.image.load('char25.PNG').convert()


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
l_fS = pygame.image.load('char1.PNG').convert()

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
os.chdir(os.path.dirname(os.getcwd()))



#ChadTechv0.
class cursor(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([2,16])
		self.image.fill((192,192,192))
		self.rect = self.image.get_rect()

pygame.init()

group = pygame.sprite.Group()

pygame.display.set_caption("ChadTech vSatz")
quit = False
clock = pygame.time.Clock()

charWidth=12
charHeight=16 #With the buffer the height ought to be 35, but it would be misleading to say the height is 35, instead of saying we need to shift 35 per line.
lilcharHeight=6
lineGap=4

xMarg = 96 - charWidth
yMarg = 48

lineLen=(screenWidth-(2*xMarg))/charWidth
lineNum=(screenHeight-(2*yMarg))/(charHeight+lineGap)

curLin=0
curVort=0
curChar=0

whicScript = 'normal'

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
	'NUMERA:9':57,

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
	'LEFTCONTROL':306

}

class Char:
	def __init__(self,image,keys,keyDig):
		self.image=image
		self.keys=keys #The keys variable, refers to a tuple, who elements are sets, containing valid key combinations to produce that character. The elements of the set are elements of the dictionary
		self.keyDig=keyDig
		self.superscript=[]
		self.subscript=[]

class Vort:
	def __init__(self):
		self.charen=[]
	def vortLen(self):
		vortLen = 0
		for yit in range(len(charen)):
			vortLen+=charen[yit].width
		return vortLen

#Invisible Chars

empty=Char(l_fS,(set([ letCor['l'], letCor['w'] ]) ),255)
enter=Char(l_fS,( set([ letCor['ENTER'] ]) ),255)
wordwrap=Char(l_fS,(set([ letCor['l'], letCor['w'] ]) ),255)
backspace=Char(l_fS,(set ([ letCor['BACKSPACE'] ]) ),255)

rightarrow=Char(l_fS,(set ([ letCor['RIGHTARROW'] ]) ),255)
leftarrow=Char(l_fS,(set ([ letCor['LEFTARROW'] ]) ),255,)
uparrow=Char(l_fS,(set ([ letCor['UPARROW'] ]) ),255)
downarrow=Char(l_fS,(set ([ letCor['DOWNARROW'] ]) ),255)

save=Char(l_fS,(set ([ letCor['LEFTCONTROL'],letCor['s'] ]),set ([ letCor['RIGHTCONTROL'],letCor['s'] ])),255)
oPen=Char(l_fS,(set ([ letCor['LEFTCONTROL'],letCor['o'] ]),set ([ letCor['RIGHTCONTROL'],letCor['o'] ])),255)

superSet=Char(l_fS,(set([ letCor['LEFTSHIFT'],letCor['EQUALS'] ]),set([ letCor['RIGHTSHIFT'],letCor['EQUALS'] ])),255)
subSet==Char(l_fS,(set([ letCor['LEFTSHIFT'],letCor['HYPHEN'] ]),set([ letCor['RIGHTSHIFT'],letCor['HYPHEN'] ])),255)

#Nothing
nothing=Char(l_fS,set([ letCor['a'], letCor['q'], letCor['l'] ]),255)

############Visible Chars

#Space
space=Char(L_S,( set([ letCor['SPACE'] ]) ),53)

#Lower Case Chars 
lowercase__a=Char(L_la,( set([ letCor['a'] ]) ),1)
lowercase__b=Char(L_lb,( set([ letCor['b'] ]) ),2)
lowercase__c=Char(L_lc,( set([ letCor['c'] ]) ),3)
lowercase__d=Char(L_ld,( set([ letCor['d'] ]) ),4)
lowercase__e=Char(L_le,( set([ letCor['e'] ]) ),5)
lowercase__f=Char(L_lf,( set([ letCor['f'] ]) ),6)
lowercase__g=Char(L_lg,( set([ letCor['g'] ]) ),7)
lowercase__h=Char(L_lh,( set([ letCor['h'] ]) ),8)
lowercase__i=Char(L_li,( set([ letCor['i'] ]) ),9)
lowercase__j=Char(L_lj,( set([ letCor['j'] ]) ),10)
lowercase__k=Char(L_lk,( set([ letCor['k'] ]) ),11)
lowercase__l=Char(L_ll,( set([ letCor['l'] ]) ),12)
lowercase__m=Char(L_lm,( set([ letCor['m'] ]) ),13)
lowercase__n=Char(L_ln,( set([ letCor['n'] ]) ),14)
lowercase__o=Char(L_lo,( set([ letCor['o'] ]) ),15)
lowercase__p=Char(L_lp,( set([ letCor['p'] ]) ),16)
lowercase__q=Char(L_lq,( set([ letCor['q'] ]) ),17)
lowercase__r=Char(L_lr,( set([ letCor['r'] ]) ),18)
lowercase__s=Char(L_ls,( set([ letCor['s'] ]) ),19)
lowercase__t=Char(L_lt,( set([ letCor['t'] ]) ),20)
lowercase__u=Char(L_lu,( set([ letCor['u'] ]) ),21)
lowercase__v=Char(L_lv,( set([ letCor['v'] ]) ),22)
lowercase__w=Char(L_lw,( set([ letCor['w'] ]) ),23)
lowercase__x=Char(L_lx,( set([ letCor['x'] ]) ),24)
lowercase__y=Char(L_ly,( set([ letCor['y'] ]) ),25)
lowercase__z=Char(L_lz,( set([ letCor['z'] ]) ),26)

#Upper Case Chars
uppercase__A=Char(L_lA,( set([ letCor['a'], letCor['LEFTSHIFT'] ]), set([ letCor['a'], letCor['RIGHTSHIFT'] ]) ),27)
uppercase__B=Char(L_lB,( set([ letCor['b'], letCor['LEFTSHIFT'] ]), set([ letCor['b'], letCor['RIGHTSHIFT'] ]) ),28)
uppercase__C=Char(L_lC,( set([ letCor['c'], letCor['LEFTSHIFT'] ]), set([ letCor['c'], letCor['RIGHTSHIFT'] ]) ),29)
uppercase__D=Char(L_lD,( set([ letCor['d'], letCor['LEFTSHIFT'] ]), set([ letCor['d'], letCor['RIGHTSHIFT'] ]) ),30)
uppercase__E=Char(L_lE,( set([ letCor['e'], letCor['LEFTSHIFT'] ]), set([ letCor['e'], letCor['RIGHTSHIFT'] ]) ),31)
uppercase__F=Char(L_lF,( set([ letCor['f'], letCor['LEFTSHIFT'] ]), set([ letCor['f'], letCor['RIGHTSHIFT'] ]) ),32)
uppercase__G=Char(L_lG,( set([ letCor['g'], letCor['LEFTSHIFT'] ]), set([ letCor['g'], letCor['RIGHTSHIFT'] ]) ),33)
uppercase__H=Char(L_lH,( set([ letCor['h'], letCor['LEFTSHIFT'] ]), set([ letCor['h'], letCor['RIGHTSHIFT'] ]) ),34)
uppercase__I=Char(L_lI,( set([ letCor['i'], letCor['LEFTSHIFT'] ]), set([ letCor['i'], letCor['RIGHTSHIFT'] ]) ),35)
uppercase__J=Char(L_lJ,( set([ letCor['j'], letCor['LEFTSHIFT'] ]), set([ letCor['j'], letCor['RIGHTSHIFT'] ]) ),36)
uppercase__K=Char(L_lK,( set([ letCor['k'], letCor['LEFTSHIFT'] ]), set([ letCor['k'], letCor['RIGHTSHIFT'] ]) ),37)
uppercase__L=Char(L_lL,( set([ letCor['l'], letCor['LEFTSHIFT'] ]), set([ letCor['l'], letCor['RIGHTSHIFT'] ]) ),38)
uppercase__M=Char(L_lM,( set([ letCor['m'], letCor['LEFTSHIFT'] ]), set([ letCor['m'], letCor['RIGHTSHIFT'] ]) ),39)
uppercase__N=Char(L_lN,( set([ letCor['n'], letCor['LEFTSHIFT'] ]), set([ letCor['n'], letCor['RIGHTSHIFT'] ]) ),40)
uppercase__O=Char(L_lO,( set([ letCor['o'], letCor['LEFTSHIFT'] ]), set([ letCor['o'], letCor['RIGHTSHIFT'] ]) ),41)
uppercase__P=Char(L_lP,( set([ letCor['p'], letCor['LEFTSHIFT'] ]), set([ letCor['p'], letCor['RIGHTSHIFT'] ]) ),42)
uppercase__Q=Char(L_lQ,( set([ letCor['q'], letCor['LEFTSHIFT'] ]), set([ letCor['q'], letCor['RIGHTSHIFT'] ]) ),43)
uppercase__R=Char(L_lR,( set([ letCor['r'], letCor['LEFTSHIFT'] ]), set([ letCor['r'], letCor['RIGHTSHIFT'] ]) ),44)
uppercase__S=Char(L_lS,( set([ letCor['s'], letCor['LEFTSHIFT'] ]), set([ letCor['s'], letCor['RIGHTSHIFT'] ]) ),45)
uppercase__T=Char(L_lT,( set([ letCor['t'], letCor['LEFTSHIFT'] ]), set([ letCor['t'], letCor['RIGHTSHIFT'] ]) ),46)
uppercase__U=Char(L_lU,( set([ letCor['u'], letCor['LEFTSHIFT'] ]), set([ letCor['u'], letCor['RIGHTSHIFT'] ]) ),47)
uppercase__V=Char(L_lV,( set([ letCor['v'], letCor['LEFTSHIFT'] ]), set([ letCor['v'], letCor['RIGHTSHIFT'] ]) ),48)
uppercase__W=Char(L_lW,( set([ letCor['w'], letCor['LEFTSHIFT'] ]), set([ letCor['w'], letCor['RIGHTSHIFT'] ]) ),49)
uppercase__X=Char(L_lX,( set([ letCor['x'], letCor['LEFTSHIFT'] ]), set([ letCor['x'], letCor['RIGHTSHIFT'] ]) ),50)
uppercase__Y=Char(L_lY,( set([ letCor['y'], letCor['LEFTSHIFT'] ]), set([ letCor['y'], letCor['RIGHTSHIFT'] ]) ),51)
uppercase__Z=Char(L_lZ,( set([ letCor['z'], letCor['LEFTSHIFT'] ]), set([ letCor['z'], letCor['RIGHTSHIFT'] ]) ),52)

#Punctuation

punctuation__period=Char(L_pPeriod,( set([ letCor['PERIOD'] ]) ),54)
punctuation__comma=Char(L_pComma,( set([ letCor['COMMA'] ]) ),55)
punctuation__question=Char(L_pQuestion,( set([ letCor['FORWARDSLASH'],letCor['LEFTSHIFT'] ]),set([ letCor['FORWARDSLASH'],letCor['RIGHTSHIFT'] ]) ),56)
punctuation__semicolon=Char(L_pSemicolon,( set([ letCor['SEMICOLON'] ]) ),57)
punctuation__colon=Char(L_pColon,( set([ letCor['SEMICOLON'],letCor['LEFTSHIFT'] ]),set([ letCor['SEMICOLON'],letCor['RIGHTSHIFT'] ]) ),58)
punctuation__exclaimation=Char(L_pExclaimation,( set([ letCor['NUMERAL1'],letCor['LEFTSHIFT'] ]),set([ letCor['NUMERAL1'],letCor['RIGHTSHIFT'] ]) ),59)
punctuation__singlequote=Char(L_pSinglequote,( set([ letCor['SINGLEQUOTE'] ]) ),60)

modallogic_possible=Char(L_mP,( set([ letCor['NUMERAL2'],letCor['p'] ]) ),61)
modallogic_necessary=Char(L_mN,( set([ letCor['NUMERAL2'],letCor['n'] ]) ),62)

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
}

class Doc:
	def __init__(self):
		self.vorten=[]

ourDoc= Doc()
ourDoc.vorten.append(Vort())
cursor= Doc()
cursor.vorten.append(Vort())

keys = set([])
quit=False
while quit==False:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			howManyChars=0
			keys.add(event.key)
			print 'CURVOT', curVort, 'CURCHAR', curChar

			whichChar=superSet
			for yit in range(len(whichChar.keys)):
				if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
					superSet=True

			whichChar=subSet
			for yit in range(len(whichChar.keys)):
				if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
					subSet=True

			######################## Check if this is a super script or sub script

			if whichScript == 'normal':

				######################## Lower case letters

				whichChar=lowercase__a
				if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
					ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
					curChar+=1

				whichChar=lowercase__b
				if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
					ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
					curChar+=1

				whichChar=lowercase__c
				if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
					ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
					curChar+=1

				whichChar=lowercase__d
				if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
					ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
					curChar+=1

				whichChar=lowercase__e
				if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
					ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
					curChar+=1

				whichChar=lowercase__f
				if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
					ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
					curChar+=1

				whichChar=lowercase__g
				if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
					ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
					curChar+=1

				whichChar=lowercase__h
				if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
					ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
					curChar+=1

				whichChar=lowercase__i
				if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
					ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
					curChar+=1

				whichChar=lowercase__j
				if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
					ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
					curChar+=1

				whichChar=lowercase__k
				if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
					ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
					curChar+=1

				whichChar=lowercase__l
				if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
					ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
					curChar+=1

				whichChar=lowercase__m
				if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
					ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
					curChar+=1

				whichChar=lowercase__n
				if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
					ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
					curChar+=1

				whichChar=lowercase__o
				if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
					ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
					curChar+=1

				whichChar=lowercase__p
				if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
					ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
					curChar+=1

				whichChar=lowercase__q
				if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
					ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
					curChar+=1

				whichChar=lowercase__r
				if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
					ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
					curChar+=1

				whichChar=lowercase__s
				if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
					ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
					curChar+=1

				whichChar=lowercase__t
				if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
					ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
					curChar+=1

				whichChar=lowercase__u
				if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
					ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
					curChar+=1

				whichChar=lowercase__v
				if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
					ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
					curChar+=1

				whichChar=lowercase__w
				if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
					ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
					curChar+=1

				whichChar=lowercase__x
				if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
					ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
					curChar+=1

				whichChar=lowercase__y
				if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
					ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
					curChar+=1

				whichChar=lowercase__z
				if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
					ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
					curChar+=1

				######################### Upper case Letters

				whichChar=uppercase__A
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
						curChar+=1

				whichChar=uppercase__B
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
						curChar+=1

				whichChar=uppercase__C
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
						curChar+=1

				whichChar=uppercase__D
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
						curChar+=1

				whichChar=uppercase__E
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
						curChar+=1

				whichChar=uppercase__F
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
						curChar+=1

				whichChar=uppercase__G
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
						curChar+=1

				whichChar=uppercase__H
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
						curChar+=1

				whichChar=uppercase__I
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
						curChar+=1

				whichChar=uppercase__J
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
						curChar+=1

				whichChar=uppercase__K
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
						curChar+=1

				whichChar=uppercase__L
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
						curChar+=1

				whichChar=uppercase__M
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
						curChar+=1

				whichChar=uppercase__N
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
						curChar+=1

				whichChar=uppercase__O
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
						curChar+=1

				whichChar=uppercase__P
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
						curChar+=1

				whichChar=uppercase__Q
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
						curChar+=1

				whichChar=uppercase__R
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
						curChar+=1

				whichChar=uppercase__S
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
						curChar+=1

				whichChar=uppercase__T
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
						curChar+=1

				whichChar=uppercase__U
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
						curChar+=1

				whichChar=uppercase__V
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
						curChar+=1

				whichChar=uppercase__W
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
						curChar+=1

				whichChar=uppercase__X
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
						curChar+=1

				whichChar=uppercase__Y
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
						curChar+=1

				whichChar=uppercase__Z
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
						curChar+=1

				#########################Punctuation

				whichChar=punctuation__period
				if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
					ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
					curChar+=1

				whichChar=punctuation__comma
				if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
					ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
					curChar+=1

				whichChar=punctuation__question
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
						curChar+=1

				whichChar=punctuation__exclaimation
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
						curChar+=1

				whichChar=punctuation__semicolon
				if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
					ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
					curChar+=1

				whichChar=punctuation__colon
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
						curChar+=1

				whichChar=punctuation__singlequote
				if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
					ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
					curChar+=1

				######################### Modal Logic Characters

				whichChar=modallogic_possible
				if event.key in whichChar.keys and whichChar.keys.issubset(keys):
					ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
					curChar+=1

				whichChar=modallogic_necessary
				if event.key in whichChar.keys and whichChar.keys.issubset(keys):
					ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
					curChar+=1

				######################### Commandy keys

				if event.key in space.keys:
					ourDoc.vorten[curVort].charen.insert(curChar,space)
					curVort+=1
					ourDoc.vorten.insert(curVort,Vort())
					curChar=0

	 			if event.key in enter.keys:
					ourDoc.vorten.insert(curVort+1,Vort())
					curVort+=1
					curChar=0
					ourDoc.vorten[curVort].charen.insert(curChar,enter)
					ourDoc.vorten.insert(curVort+1,Vort())
					curVort+=1

				if event.key in backspace.keys:
					if curChar!=0 or curVort!=0:
						while len(ourDoc.vorten[curVort].charen)==0:
							ourDoc.vorten.pop(curVort)
							curVort-=1
							curChar=len(ourDoc.vorten[curVort].charen)
						ourDoc.vorten[curVort].charen.pop(curChar-1)
						curChar-=1

				if event.key in leftarrow.keys:
					if curChar!=0:
						curChar-=1
					else:
						if curVort!=0:
							curVort-=1
							curChar=len(ourDoc.vorten[curVort].charen)

				if event.key in rightarrow.keys:
					if curChar==len(ourDoc.vorten[curVort].charen):
						if curVort!=(len(ourDoc.vorten)-1):
							curVort+=1
							curChar=0
					else:
						curChar+=1

				if event.key in uparrow.keys:
					for yit in lineLen*[0]:
						if curChar!=0:
							curChar-=1
						else:
							if curVort!=0:
								curVort-=1
								curChar=len(ourDoc.vorten[curVort].charen)

			else: #Else, as in superChek or subChek is true

				if superChek and not subChek:

				if subChek and not 

			########################################## Saving DOcuments

				whichChar=save
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						saveName = tkFileDialog.asksaveasfilename()
						saveName = str(saveName)
						pygame.image.save(screen,"curpag.PNG")
						saveIm = Image.open('curpag.PNG')
						saveImSize = saveIm.size
						Xboun, Yboun = 0,0
						Xboun, Yboun = saveIm.size
						for yit in range(len(ourDoc.vorten)):
							for vapp in range(len(ourDoc.vorten[yit].charen)):
								if vapp%3==0:
									vortON,vortTW,vortTH = 0,0,0
									vortON = ourDoc.vorten[yit].charen[vapp].keyDig
									if vapp+1 < len(ourDoc.vorten[yit].charen):
										vortTW = ourDoc.vorten[yit].charen[vapp+1].keyDig
									if vapp+2 < len(ourDoc.vorten[yit].charen):
										vortTH = ourDoc.vorten[yit].charen[vapp+2].keyDig
									saveIm.putpixel((vapp/3,yit),(vortON,vortTW,vortTH))
						saveIm.save(saveName,"png")

			########################################### Opening Documents

				whichChar=oPen
				for yit in range(len(whichChar.keys)):
					if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
						openName = tkFileDialog.askopenfilename()
						openName = str(openName)
						openIm =  Image.open(openName)
						ourDoc= Doc()
						ourDoc.vorten.append(Vort())
						cursor= Doc()
						cursor.vorten.append(Vort())
						xBou,yBou=0,0
						r,g,b = openIm.getpixel((xBou,yBou))
						print 'PRE OPEN RGB', r,g,b
						while r!=0:
							print 'GOT HERE'
							ourDoc.vorten.append(Vort())
							while r!=0:
								print 'AND HERE'
								r,g,b = openIm.getpixel((xBou,yBou))
								print r,g,b
								if r!=0:
									ourDoc.vorten[yBou].charen.append(charLets[r])
								if g!=0:
									ourDoc.vorten[yBou].charen.append(charLets[g])
								if b!=0:
									ourDoc.vorten[yBou].charen.append(charLets[b])
								xBou+=1
							yBou+=1
							xBou=0
							r,g,b = openIm.getpixel((xBou,yBou))
						curVort=len(ourDoc.vorten)-1
						print curVort, len(ourDoc.vorten[curVort].charen)
						curChar=len(ourDoc.vorten[curVort].charen)


		###############################This section breaks the list of words, into a list of lines containing the words

		blitScreen = []
		thisLin = 0
		blitScreen.append( [0,[]] )
		cursorChar = 0
		cursorVort = 0
		cursorLine = 0
		for yit in range(len(ourDoc.vorten)):
			if ourDoc.vorten[yit].charen==[enter]:
				blitScreen.append( [0,[]] )
				thisLin+=1
			else:
				if blitScreen[thisLin][0]+len(ourDoc.vorten[yit].charen)<=lineLen:
					blitScreen[thisLin][1].append(ourDoc.vorten[yit])
					blitScreen[thisLin][0]+=len(ourDoc.vorten[yit].charen)
				else:
					blitScreen.append( [0,[]] )
					thisLin+=1
					blitScreen[thisLin][0]=len(ourDoc.vorten[yit].charen)
					blitScreen[thisLin][1].append(ourDoc.vorten[yit])
			if yit==curVort:
				cursorVort=yit
				cursorLine=thisLin
				for vapp in range(len(blitScreen[len(blitScreen)-1][1])):
					cursorChar+= len(blitScreen[len(blitScreen)-1][1][vapp].charen)
				cursorChar-=len(ourDoc.vorten[curVort].charen)-curChar

	 	############################This section takes the words in each line, and breaks them down into a list of characters to paste onto the screen

		blitChars=[]
		for yit in range(len(blitScreen)):
			blitChars.append([])
			for vapp in range(len(blitScreen[yit][1])):
				for gno in range(len(blitScreen[yit][1][vapp].charen)):
					blitChars[yit].append(blitScreen[yit][1][vapp].charen[gno])
			for vapp in range(lineLen):
				if vapp<len(blitChars[yit]):
					screen.blit(blitChars[yit][vapp].image,[(vapp*charWidth)+xMarg,(yit*(charHeight+lineGap))+yMarg])
				else:
					screen.blit(L_S,[(vapp*charWidth)+xMarg,(yit*(charHeight+lineGap))+yMarg])
		screen.blit(L_C,[xMarg+(cursorChar*charWidth),yMarg+(cursorLine*(charHeight+lineGap))])

		######################################
		
		if event.type == pygame.KEYUP:
			keys.remove(event.key)
		if event.type == pygame.QUIT:
			quit = True

	pygame.display.flip()
	clock.tick(60)

pygame.quit()