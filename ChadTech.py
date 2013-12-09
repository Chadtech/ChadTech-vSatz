import os
import pygame
import PIL
from PIL import Image
import Tkinter, tkFileDialog
brunk = Tkinter.Tk()
brunk.withdraw()
#ChadTechv0.1
class cursor(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([2,16])
		self.image.fill((192,192,192))
		self.rect = self.image.get_rect()

pygame.init()

group = pygame.sprite.Group()

screen = pygame.display.set_mode((1152,768),pygame.RESIZABLE)

pygame.display.set_caption("ChadTech")
quit = False
clock = pygame.time.Clock()

whichLet = 0
tempSpot = whichLet

lineLen = 80

charWidth = 12
charHeight = 35

lilWhichLet = 0
basePlaceX = 0
basePlaceY = 0

lilCharWidth = 6
lilCharHeight = 8

lilCharXOffset = 9
lilCharYOffset = -8

lilCharSubBuf = 24

xMarg = 96
yMarg = 48

xMod= 0
xYit = 0
yYit = 0

supaSaveCou = 0
subSaveCou = 0

pag = []
pagLen = 0
pagLenDummy = 0

repor = ''

dummyCount = 0

supaChek = False
subDummy = 0

aChek = False
bChek = False
cChek = False
dChek = False
eChek = False
fChek = False
gChek = False
hChek = False
iChek = False
jChek = False
kChek = False
lChek = False
mChek = False
nChek = False
oChek = False
pChek = False
qChek = False
rChek = False
sChek = False
tChek = False
uChek = False
vChek = False
wChek = False
xChek = False
yChek = False
zChek = False
rSChek = False

#Lower case number codes
a = 0
b = 1
c = 2
d = 3
e = 4
f = 5
g = 6
h = 7
i = 8
j = 9
k = 10
l = 11
m = 12
n = 13
o = 14
p = 15
q = 16
r = 17
s = 18
t = 19
u = 20
v = 21
w = 22
x = 23
y = 24
z = 25

#upper case number codes
A = 26
B = 27
C = 28
D = 29
E = 30
F = 31
G = 32
H = 33
I = 34
J = 35
K = 36
L = 37
M = 38
N = 39
O = 40
P = 41
Q = 42
R = 43
S = 44
T = 45
U = 46
V = 47
W = 48
X = 49
Y = 50
Z = 51

#Space codes
rSp = 52
dSp = 53

#Numeral number codes
On = 54
Tw = 55
Th = 56
Fo = 57
Fi = 58
Si = 59
Se = 60
Ei = 61
Ni = 62
Ze = 63

#First Order Logic Number codes
Ex = 64
Fa = 65
Ne = 66
Im = 67
Ff = 68
Nd = 69

#modal
mP = 70
mN = 71

#Punctuation
pQ = 72
pE = 73
pP = 74
pC = 75
pO = 76
pS = 77
pU = 78

#Math
mEq = 79 
mGt = 80
mGe = 81
mLt = 82
mLe = 83
mDi = 84
mAp = 85
mPl = 86
mSb = 87
mMu = 88
mFs = 89
mBs = 90
mQe = 91 
mSr = 92
mAs = 93
mAd = 94
mNe = 95
mAn = 96
mDe = 97
mGr = 98
mIn = 99

#brackets
blp = 100
brp = 101
blc = 102
brc = 103
blb = 104
brb = 105
blh = 106
brh = 107

#Math Cont
mDv = 108

#Set Theory

sEo = 109
sDc = 110
sNs = 111
sIn = 112
sUn = 113
sBs = 114
sSs = 115
sNp = 116
sNb = 117

#Proof Theory

pSt = 118
pNs = 119
pDt = 120
pNd = 121
pLc = 122


def getLet(inp):
	if inp == a:
		return L_la
	if inp == b:
		return L_lb
	if inp == c:
		return L_lc
	if inp == d:
		return L_ld
	if inp == e:
		return L_le
	if inp == f:
		return L_lf
	if inp == g:
		return L_lg
	if inp == h:
		return L_lh
	if inp == i:
		return L_li
	if inp == j:
		return L_lj
	if inp == k:
		return L_lk
	if inp == l:
		return L_ll
	if inp == m:
		return L_lm
	if inp == n:
		return L_ln
	if inp == o:
		return L_lo
	if inp == p:
		return L_lp
	if inp == q:
		return L_lq
	if inp == r:
		return L_lr
	if inp == s:
		return L_ls
	if inp == t:
		return L_lt
	if inp == u:
		return L_lu
	if inp == v:
		return L_lv
	if inp == w:
		return L_lw
	if inp == x:
		return L_lx
	if inp == y:
		return L_ly
	if inp == z:
		return L_lz

	if inp == A:
		return L_lA
	if inp == B:
		return L_lB
	if inp == C:
		return L_lC
	if inp == D:
		return L_lD
	if inp == E:
		return L_lE
	if inp == F:
		return L_lF
	if inp == G:
		return L_lG
	if inp == H:
		return L_lH
	if inp == I:
		return L_lI
	if inp == J:
		return L_lJ
	if inp == K:
		return L_lK
	if inp == L:
		return L_lL
	if inp == M:
		return L_lM
	if inp == N:
		return L_lN
	if inp == O:
		return L_lO
	if inp == P:
		return L_lP
	if inp == Q:
		return L_lQ
	if inp == R:
		return L_lR
	if inp == S:
		return L_lS
	if inp == T:
		return L_lT
	if inp == U:
		return L_lU
	if inp == V:
		return L_lV
	if inp == W:
		return L_lW
	if inp == X:
		return L_lX
	if inp == Y:
		return L_lY
	if inp == Z:
		return L_lZ

	if inp == rSp:
		return L_S
	if inp == dSp:
		return L_S
#First Order Logic
	if inp == Ex:
		return L_fE
	if inp == Fa:
		return L_fA
	if inp == Ne:
		return L_fN
	if inp == Im:
		return L_fI
	if inp == Ff:
		return L_fF
	if inp == Nd:
		return L_fD
#Modal Logic
	if inp == mP:
		return L_mP
	if inp == mN:
		return L_mN
#Punctuation
	if inp == pQ:
		return L_pQ
	if inp == pE:
		return L_pE
	if inp == pP:
		return L_pP
	if inp == pC:
		return L_pC
	if inp == pO:
		return L_pO
	if inp == pS:
		return L_pS
	if inp == pU:
		return L_pU
#Math
	if inp == mEq:
		return L_mEq
	if inp == mGt:
		return L_mGt
	if inp == mGe:
		return L_mGe
	if inp == mLt:
		return L_mLt
	if inp == mLe:
		return L_mLe
	if inp == mDi:
		return L_mDi
	if inp == mAp:
		return L_mAp
	if inp == mPl:
		return L_mPl
	if inp == mAd:
		return L_mAd
	if inp == mSb:
		return L_mSb
	if inp == mMu:
		return L_mMu
	if inp == mFs:
		return L_mFs
	if inp == mBs:
		return L_mBs
	if inp == mSr:
		return L_mSr
	if inp == mAs:
		return L_mAs
	if inp == mAd:
		return L_mAd
	if inp == mNe:
		return L_mNe
	if inp == mAn:
		return L_mAn
	if inp == mDe:
		return L_mDe
	if inp == mGr:
		return L_mGr
	if inp == mIn:
		return L_mIn
	if inp == mQe:
		return L_mQe
	if inp == mDv:
		return L_mDv

#Numbers
	if inp == On:
		return L_Non
	if inp == Tw:
		return L_Ntw
	if inp == Th:
		return L_Nth
	if inp == Fo:
		return L_Nfo
	if inp == Fi:
		return L_Nfi
	if inp == Si:
		return L_Nsi
	if inp == Se:
		return L_Nse
	if inp == Ei:
		return L_Nei
	if inp == Ni:
		return L_Nni
	if inp == Ze:
		return L_Nze

#Brackets
	if inp == blp:
		return L_blp
	if inp == brp:
		return L_brp
	if inp == blc:
		return L_blc
	if inp == brc:
		return L_brc
	if inp == blb:
		return L_blb
	if inp == brb:
		return L_brb
	if inp == blh:
		return L_blh

# Set Theory

	if inp == sEo:
		return L_sEo
	if inp == sDc:
		return L_sDc
	if inp == sNs:
		return L_sNs
	if inp == sIn:
		return L_sIn
	if inp == sUn:
		return L_sUn
	if inp == sBs:
		return L_sBs
	if inp == sSs:
		return L_sSs
	if inp == sNp:
		return L_sNp
	if inp == sNb:
		return L_sNb

#proof theory

	if inp == pSt:
		return L_pSt
	if inp == pNs:
		return L_pNs
	if inp == pDt:
		return L_pDt
	if inp == pNd:
		return L_pNd
	if inp == pLc:
		return L_pLc

def getLetl(inp):
	if inp == a:
		return l_la
	if inp == b:
		return l_lb
	if inp == c:
		return l_lc
	if inp == d:
		return l_ld
	if inp == e:
		return l_le
	if inp == f:
		return l_lf
	if inp == g:
		return l_lg
	if inp == h:
		return l_lh
	if inp == i:
		return l_li
	if inp == j:
		return l_lj
	if inp == k:
		return l_lk
	if inp == l:
		return l_ll
	if inp == m:
		return l_lm
	if inp == n:
		return l_ln
	if inp == o:
		return l_lo
	if inp == p:
		return l_lP
	if inp == q:
		return l_lq
	if inp == r:
		return l_lr
	if inp == s:
		return l_ls
	if inp == t:
		return l_lt
	if inp == u:
		return l_lu
	if inp == v:
		return l_lv
	if inp == w:
		return l_lW
	if inp == x:
		return l_lx
	if inp == y:
		return l_ly
	if inp == z:
		return l_lZ

	if inp == A:
		return l_lA
	if inp == B:
		return l_lB
	if inp == C:
		return l_lC
	if inp == D:
		return l_lD
	if inp == E:
		return l_lE
	if inp == F:
		return l_lF
	if inp == G:
		return l_lG
	if inp == H:
		return l_lH
	if inp == I:
		return l_lI
	if inp == J:
		return l_lJ
	if inp == K:
		return l_lK
	if inp == L:
		return l_lL
	if inp == M:
		return l_lM
	if inp == O:
		return l_lO
	if inp == P:
		return l_lP
	if inp == Q:
		return l_lQ
	if inp == R:
		return l_lR
	if inp == S:
		return l_lS
	if inp == T:
		return l_lT
	if inp == U:
		return l_lU
	if inp == V:
		return l_lV
	if inp == W:
		return l_lW
	if inp == X:
		return l_lX
	if inp == Y:
		return l_lY
	if inp == Z:
		return l_lZ

	if inp == On:
		return l_Non
	if inp == Tw:
		return l_Ntw
	if inp == Th:
		return l_Nth
	if inp == Fo:
		return l_Nfo
	if inp == Fi:
		return l_Nfi
	if inp == Si:
		return l_Nsi
	if inp == Se:
		return l_Nse
	if inp == Ei:
		return l_Nei
	if inp == Ni:
		return l_Nni
	if inp == Ze:
		return l_Nze


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
L_pQ = pygame.image.load('char0.PNG').convert()
L_pE = pygame.image.load('char1.PNG').convert()
L_pP = pygame.image.load('char2.PNG').convert()
L_pC = pygame.image.load('char3.PNG').convert()
L_pO = pygame.image.load('char4.PNG').convert()
L_pS = pygame.image.load('char5.PNG').convert()
L_pU = pygame.image.load('char6.PNG').convert()

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
os.chdir(os.path.abspath('SetTheory'))

#Set Theory
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

#Set Theory
L_pSt = pygame.image.load('char0.PNG').convert()
L_pNs = pygame.image.load('char1.PNG').convert()
L_pDt = pygame.image.load('char2.PNG').convert()
L_pNd = pygame.image.load('char3.PNG').convert()
L_pLc = pygame.image.load('char4.PNG').convert()


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

screen.fill((0,0,0))

blinker = cursor()
blinker.rect.x = xMarg
blinker.rect.y = yMarg
group.add(blinker)

while quit == False:

	for event in pygame.event.get():

		pressed = pygame.key.get_pressed()

		if event.type == pygame.QUIT:
			quit = True

		if not supaChek and not subDummy:
			blinker.rect.x = ((whichLet%lineLen)*charWidth)+xMarg
			blinker.rect.y = ((whichLet/lineLen)*charHeight)+yMarg
			group.draw(screen)

		if event.type == pygame.KEYDOWN:
			if not supaChek and not subDummy:

	#-----------LETTERS, UPPER CASE AND LOWER CASE--------------

				#Lower a
				if pressed[pygame.K_a] and not pressed[pygame.K_LSHIFT] and not aChek:
					screen.blit(L_la,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([a,[],[]])
					else:
						pag.insert(whichLet,[a,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot

					whichLet += 1
					aChek = True

				#Upper A
				if pressed[pygame.K_a] and pressed[pygame.K_LSHIFT] and not aChek:
					screen.blit(L_lA,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([A,[],[]])
					else:
						pag.insert(whichLet,[A,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1
					aChek = True

				#Lower b
				if pressed[pygame.K_b] and not pressed[pygame.K_LSHIFT] and not bChek:
					screen.blit(L_lb,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([b,[],[]])
					else:
						pag.insert(whichLet,[b,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1
					bChek = True

				#Upper B
				if pressed[pygame.K_b] and pressed[pygame.K_LSHIFT] and not bChek:
					screen.blit(L_lB,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([B,[],[]])
					else:
						pag.insert(whichLet,[B,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1
					bChek = True

				#Lower C
				if pressed[pygame.K_c] and not pressed[pygame.K_LSHIFT] and not cChek:
					screen.blit(L_lc,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([c,[],[]])
					else:
						pag.insert(whichLet,[c,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1
					cChek = True

				#Upper C
				if pressed[pygame.K_c] and pressed[pygame.K_LSHIFT] and not cChek:
					screen.blit(L_lC,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([C,[],[]])
					else:
						pag.insert(whichLet,[C,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1
					cChek = True

				#Lower d
				if pressed[pygame.K_d] and not pressed[pygame.K_LSHIFT] and not dChek:
					screen.blit(L_ld,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([d,[],[]])
					else:
						pag.insert(whichLet,[d,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1
					dChek = True

				#Upper D
				if pressed[pygame.K_d] and pressed[pygame.K_LSHIFT] and not dChek:
					screen.blit(L_lD,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([D,[],[]])
					else:
						pag.insert(whichLet,[D,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1
					dChek = True

				#Lower e
				if pressed[pygame.K_e] and not pressed[pygame.K_LSHIFT] and not eChek:
					screen.blit(L_le,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([e,[],[]])
					else:
						pag.insert(whichLet,[e,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1
					eChek = True

				#Upper E
				if pressed[pygame.K_e] and pressed[pygame.K_LSHIFT] and not eChek:
					screen.blit(L_lE,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([E,[],[]])
					else:
						pag.insert(whichLet,[E,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1
					eChek = True

				#Lower f
				if pressed[pygame.K_f] and not pressed[pygame.K_LSHIFT] and not fChek:
					screen.blit(L_lf,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([f,[],[]])
					else:
						pag.insert(whichLet,[f,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1
					fChek = True

				#Upper F
				if pressed[pygame.K_f] and pressed[pygame.K_LSHIFT] and not fChek:
					screen.blit(L_lF,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([F,[],[]])
					else:
						pag.insert(whichLet,[F,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1
					fChek = True

				#Lower g
				if pressed[pygame.K_g] and not pressed[pygame.K_LSHIFT] and not gChek:
					screen.blit(L_lg,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([g,[],[]])
					else:
						pag.insert(whichLet,[g,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1
					gChek = True

				#Upper G
				if pressed[pygame.K_g] and pressed[pygame.K_LSHIFT] and not gChek:
					screen.blit(L_lG,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([G,[],[]])
					else:
						pag.insert(whichLet,[G,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1
					gChek = True

				#Lower h
				if pressed[pygame.K_h] and not pressed[pygame.K_LSHIFT] and not hChek:
					screen.blit(L_lh,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([h,[],[]])
					else:
						pag.insert(whichLet,[h,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1
					hChek = True

				#Upper H
				if pressed[pygame.K_h] and pressed[pygame.K_LSHIFT] and not hChek:
					screen.blit(L_lH,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([H,[],[]])
					else:
						pag.insert(whichLet,[H,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1
					hChek = True

				#Lower i
				if pressed[pygame.K_i] and not pressed[pygame.K_LSHIFT] and not iChek:
					screen.blit(L_li,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([i,[],[]])
					else:
						pag.insert(whichLet,[i,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1
					iChek = True

				#Upper I
				if pressed[pygame.K_i] and pressed[pygame.K_LSHIFT] and not iChek:
					screen.blit(L_lI,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([I,[],[]])
					else:
						pag.insert(whichLet,[I,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1
					iChek = True

				#Lower j
				if pressed[pygame.K_j] and not pressed[pygame.K_LSHIFT] and not jChek:
					screen.blit(L_lj,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([j,[],[]])
					else:
						pag.insert(whichLet,[j,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1
					jChek = True

				#Upper J
				if pressed[pygame.K_j] and pressed[pygame.K_LSHIFT] and not jChek:
					screen.blit(L_lJ,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([J,[],[]])
					else:
						pag.insert(whichLet,[J,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1
					jChek = True

				#Lower k
				if pressed[pygame.K_k] and not pressed[pygame.K_LSHIFT] and not kChek:
					screen.blit(L_lk,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([k,[],[]])
					else:
						pag.insert(whichLet,[k,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1
					kChek = True

				#Upper K
				if pressed[pygame.K_k] and pressed[pygame.K_LSHIFT] and not kChek:
					screen.blit(L_lK,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([K,[],[]])
					else:
						pag.insert(whichLet,[K,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1
					kChek = True

				#Lower l
				if pressed[pygame.K_l] and not pressed[pygame.K_LSHIFT] and not lChek:
					screen.blit(L_ll,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([l,[],[]])
					else:
						pag.insert(whichLet,[l,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1
					lChek = True

				#Upper L
				if pressed[pygame.K_l] and pressed[pygame.K_LSHIFT] and not lChek:
					screen.blit(L_lL,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([L,[],[]])
					else:
						pag.insert(whichLet,[L,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1
					lChek = True

				#Lower m
				if pressed[pygame.K_m] and not pressed[pygame.K_LSHIFT] and not mChek:
					screen.blit(L_lm,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([m,[],[]])
					else:
						pag.insert(whichLet,[m,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1
					mChek = True

				#Upper M
				if pressed[pygame.K_m] and pressed[pygame.K_LSHIFT] and not mChek:
					screen.blit(L_lM,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([M,[],[]])
					else:
						pag.insert(whichLet,[M,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1
					mChek = True

				#Lower n
				if pressed[pygame.K_n] and not pressed[pygame.K_LSHIFT] and not nChek:
					screen.blit(L_ln,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([n,[],[]])
					else:
						pag.insert(whichLet,[n,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1
					nChek = True

				#Upper N
				if pressed[pygame.K_n] and pressed[pygame.K_LSHIFT] and not nChek:
					screen.blit(L_lN,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([N,[],[]])
					else:
						pag.insert(whichLet,[N,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1
					nChek = True

				#Lower o
				if pressed[pygame.K_o] and not pressed[pygame.K_LSHIFT] and not oChek:
					screen.blit(L_lo,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([o,[],[]])
					else:
						pag.insert(whichLet,[o,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1
					oChek = True

				#Upper O
				if pressed[pygame.K_o] and pressed[pygame.K_LSHIFT] and not oChek:
					screen.blit(L_lO,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([O,[],[]])
					else:
						pag.insert(whichLet,[O,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1
					oChek = True

				#Lower p
				if pressed[pygame.K_p] and not pressed[pygame.K_LSHIFT] and not pChek:
					screen.blit(L_lp,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([p,[],[]])
					else:
						pag.insert(whichLet,[p,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1
					pChek = True

				#Upper P
				if pressed[pygame.K_p] and pressed[pygame.K_LSHIFT] and not pChek:
					screen.blit(L_lP,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([P,[],[]])
					else:
						pag.insert(whichLet,[P,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1
					pChek = True

				#Lower q
				if pressed[pygame.K_q] and not pressed[pygame.K_LSHIFT] and not qChek:
					screen.blit(L_lq,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([q,[],[]])
					else:
						pag.insert(whichLet,[q,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1
					qChek = True

				#Upper Q
				if pressed[pygame.K_q] and pressed[pygame.K_LSHIFT] and not qChek:
					screen.blit(L_lQ,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([Q,[],[]])
					else:
						pag.insert(whichLet,[Q,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1
					qChek = True

				#Lower r
				if pressed[pygame.K_r] and not pressed[pygame.K_LSHIFT] and not rChek:
					screen.blit(L_lr,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([r,[],[]])
					else:
						pag.insert(whichLet,[r,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1
					rChek = True

				#Upper R
				if pressed[pygame.K_r] and pressed[pygame.K_LSHIFT] and not rChek:
					screen.blit(L_lR,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([R,[],[]])
					else:
						pag.insert(whichLet,[R,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1
					rChek = True

				#Lower s
				if pressed[pygame.K_s] and not pressed[pygame.K_LSHIFT] and not sChek and not pressed[pygame.K_LCTRL]:
					screen.blit(L_ls,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([s,[],[]])
					else:
						pag.insert(whichLet,[s,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1
					sChek = True

				#Upper S
				if pressed[pygame.K_s] and pressed[pygame.K_LSHIFT] and not sChek:
					screen.blit(L_lS,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([S,[],[]])
					else:
						pag.insert(whichLet,[S,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1
					sChek = True

				#Lower t
				if pressed[pygame.K_t] and not pressed[pygame.K_LSHIFT] and not tChek:
					screen.blit(L_lt,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([t,[],[]])
					else:
						pag.insert(whichLet,[t,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1
					tChek = True

				#Upper T
				if pressed[pygame.K_t] and pressed[pygame.K_LSHIFT] and not tChek:
					screen.blit(L_lT,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([T,[],[]])
					else:
						pag.insert(whichLet,[T,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1
					tChek = True

				#Lower u
				if pressed[pygame.K_u] and not pressed[pygame.K_LSHIFT] and not uChek:
					screen.blit(L_lu,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([u,[],[]])
					else:
						pag.insert(whichLet,[u,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1
					uChek = True

				#Upper U
				if pressed[pygame.K_u] and pressed[pygame.K_LSHIFT] and not uChek:
					screen.blit(L_lU,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([U,[],[]])
					else:
						pag.insert(whichLet,[U,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1
					uChek = True

				#Lower v
				if pressed[pygame.K_v] and not pressed[pygame.K_LSHIFT] and not vChek:
					screen.blit(L_lv,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([v,[],[]])
					else:
						pag.insert(whichLet,[v,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1
					vChek = True

				#Upper V
				if pressed[pygame.K_v] and pressed[pygame.K_LSHIFT] and not vChek:
					screen.blit(L_lV,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([V,[],[]])
					else:
						pag.insert(whichLet,[V,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1
					vChek = True

				#Lower w
				if pressed[pygame.K_w] and not pressed[pygame.K_LSHIFT] and not wChek:
					screen.blit(L_lw,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([w,[],[]])
					else:
						pag.insert(whichLet,[w,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1
					wChek = True

				#Upper W
				if pressed[pygame.K_w] and pressed[pygame.K_LSHIFT] and not wChek:
					screen.blit(L_lW,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([W,[],[]])
					else:
						pag.insert(whichLet,[W,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1
					wChek = True

				#Lower x
				if pressed[pygame.K_x] and not pressed[pygame.K_LSHIFT] and not xChek:
					screen.blit(L_lx,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([x,[],[]])
					else:
						pag.insert(whichLet,[x,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1
					xChek = True

				#Upper X
				if pressed[pygame.K_x] and pressed[pygame.K_LSHIFT] and not xChek:
					screen.blit(L_lX,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([X,[],[]])
					else:
						pag.insert(whichLet,[X,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1
					xChek = True

				#Lower Y
				if pressed[pygame.K_y] and not pressed[pygame.K_LSHIFT] and not yChek:
					screen.blit(L_ly,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([y,[],[]])
					else:
						pag.insert(whichLet,[y,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1
					yChek = True

				#Upper Y
				if pressed[pygame.K_y] and pressed[pygame.K_LSHIFT] and not yChek:
					screen.blit(L_lY,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([Y,[],[]])
					else:
						pag.insert(whichLet,[Y,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1
					yChek = True

				#Lower z
				if pressed[pygame.K_z] and not pressed[pygame.K_LSHIFT] and not zChek:
					screen.blit(L_lz,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([z,[],[]])
					else:
						pag.insert(whichLet,[z,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1
					zChek = True

				#Upper Z
				if pressed[pygame.K_z] and pressed[pygame.K_LSHIFT] and not zChek:
					screen.blit(L_lZ,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([Z,[],[]])
					else:
						pag.insert(whichLet,[Z,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1
					zChek = True

#-------------------------- Punctuation -------------------------

				#Period
				if pressed[pygame.K_PERIOD] and not (pressed[pygame.K_LSHIFT] or pressed[pygame.K_RSHIFT]):
					screen.blit(L_pP,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([pP,[],[]])
					else:
						pag.insert(whichLet,[pP,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#Comma
				if pressed[pygame.K_COMMA] and not (pressed[pygame.K_LSHIFT] or pressed[pygame.K_RSHIFT]):
					screen.blit(L_pC,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([pC,[],[]])
					else:
						pag.insert(whichLet,[pC,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#Single Quote
				if pressed[pygame.K_QUOTE]:
					screen.blit(L_pU,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([pU,[],[]])
					else:
						pag.insert(whichLet,[pU,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#question mark
				if pressed[pygame.K_SLASH] and pressed[pygame.K_RSHIFT]:
					screen.blit(L_pQ,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([pQ,[],[]])
					else:
						pag.insert(whichLet,[pQ,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#Colon
				if pressed[pygame.K_SEMICOLON] and (pressed[pygame.K_LSHIFT] or pressed[pygame.K_RSHIFT]):
					screen.blit(L_pO,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([pO,[],[]])
					else:
						pag.insert(whichLet,[pO,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#Semi Colon
				if pressed[pygame.K_SEMICOLON] and not (pressed[pygame.K_RSHIFT] or pressed[pygame.K_LSHIFT]):
					screen.blit(L_pS,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([pS,[],[]])
					else:
						pag.insert(whichLet,[pS,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

#--------------------------------------------Brackets-------------------------------------------------

				#Left Paratheses
				if pressed[pygame.K_9] and (pressed[pygame.K_RSHIFT] or pressed[pygame.K_LSHIFT]):
					screen.blit(L_blp,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([blp,[],[]])
					else:
						pag.insert(whichLet,[blp,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1
					
				#Right Paratheses
				if pressed[pygame.K_0] and (pressed[pygame.K_RSHIFT] or pressed[pygame.K_LSHIFT]):
					screen.blit(L_brp,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([brp,[],[]])
					else:
						pag.insert(whichLet,[brp,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#Left curly Bracket
				if pressed[pygame.K_LEFTBRACKET] and (pressed[pygame.K_RSHIFT] or pressed[pygame.K_LSHIFT]):
					screen.blit(L_blc,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([blc,[],[]])
					else:
						pag.insert(whichLet,[blc,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#Right curly Bracket
				if pressed[pygame.K_RIGHTBRACKET] and (pressed[pygame.K_RSHIFT] or pressed[pygame.K_LSHIFT]):
					screen.blit(L_brc,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([brc,[],[]])
					else:
						pag.insert(whichLet,[brc,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#Left Bracket
				if pressed[pygame.K_LEFTBRACKET] and not (pressed[pygame.K_RSHIFT] or pressed[pygame.K_LSHIFT]):
					screen.blit(L_blb,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([blb,[],[]])
					else:
						pag.insert(whichLet,[blb,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#Right Bracket
				if pressed[pygame.K_RIGHTBRACKET] and not (pressed[pygame.K_RSHIFT] or pressed[pygame.K_LSHIFT]):
					screen.blit(L_brb,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([brb,[],[]])
					else:
						pag.insert(whichLet,[brb,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#Left Chevron
				if pressed[pygame.K_LEFTBRACKET] and pressed[pygame.K_EQUALS]:
					for vapp in range(2):
						if whichLet != 0: 
							if whichLet == len(pag):
								screen.blit(L_S,[charWidth*((whichLet-1)%lineLen)+xMarg,charHeight*((whichLet-1)/lineLen)+yMarg])
								pag.pop(whichLet-1)
								whichLet -= 1
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+(xMarg+charWidth),charHeight*(len(pag)/lineLen)+yMarg])
							else:
								pag.pop(whichLet-1)
								whichLet -= 1
								tempSpot = whichLet
								while whichLet < len(pag):
									screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
									whichLet += 1
								whichLet = tempSpot
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+xMarg,charHeight*(len(pag)/lineLen)+yMarg])
					screen.blit(L_blh,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([blh,[],[]])
					else:
						pag.insert(whichLet,[blh,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#Right Chevron
				if pressed[pygame.K_RIGHTBRACKET] and pressed[pygame.K_EQUALS]:
					for vapp in range(2):
						if whichLet != 0: 
							if whichLet == len(pag):
								screen.blit(L_S,[charWidth*((whichLet-1)%lineLen)+xMarg,charHeight*((whichLet-1)/lineLen)+yMarg])
								pag.pop(whichLet-1)
								whichLet -= 1
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+(xMarg+charWidth),charHeight*(len(pag)/lineLen)+yMarg])
							else:
								pag.pop(whichLet-1)
								whichLet -= 1
								tempSpot = whichLet
								while whichLet < len(pag):
									screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
									whichLet += 1
								whichLet = tempSpot
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+xMarg,charHeight*(len(pag)/lineLen)+yMarg])
					screen.blit(L_brh,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([brh,[],[]])
					else:
						pag.insert(whichLet,[brh,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

#----------------------Math----------------------------------

				#Equal sign
				if pressed[pygame.K_EQUALS] and not (pressed[pygame.K_LSHIFT] or pressed[pygame.K_LEFTBRACKET] or pressed[pygame.K_RIGHTBRACKET]):
					screen.blit(L_mEq,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([mEq,[],[]])
					else:
						pag.insert(whichLet,[mEq,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#Greater Than
				if pressed[pygame.K_PERIOD] and (pressed[pygame.K_LSHIFT] or pressed[pygame.K_RSHIFT]):
					screen.blit(L_mGt,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([mGt,[],[]])
					else:
						pag.insert(whichLet,[mGt,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#Greater Than or Equal to
				if pressed[pygame.K_EQUALS] and pressed[pygame.K_PERIOD]:
					for vapp in range(3):
						if whichLet != 0: 
							if whichLet == len(pag):
								screen.blit(L_S,[charWidth*((whichLet-1)%lineLen)+xMarg,charHeight*((whichLet-1)/lineLen)+yMarg])
								pag.pop(whichLet-1)
								whichLet -= 1
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+(xMarg+charWidth),charHeight*(len(pag)/lineLen)+yMarg])
							else:
								pag.pop(whichLet-1)
								whichLet -= 1
								tempSpot = whichLet
								while whichLet < len(pag):
									screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
									whichLet += 1
								whichLet = tempSpot
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+xMarg,charHeight*(len(pag)/lineLen)+yMarg])
					screen.blit(L_mGe,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([mGe,[],[]])
					else:
						pag.insert(whichLet,[mGe,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#Less Than
				if pressed[pygame.K_COMMA] and (pressed[pygame.K_LSHIFT] or pressed[pygame.K_RSHIFT]):
					screen.blit(L_mLt,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([mLt,[],[]])
					else:
						pag.insert(whichLet,[mLt,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#Less Than or Equal to
				if pressed[pygame.K_EQUALS] and pressed[pygame.K_COMMA]:
					for vapp in range(3):
						if whichLet != 0: 
							if whichLet == len(pag):
								screen.blit(L_S,[charWidth*((whichLet-1)%lineLen)+xMarg,charHeight*((whichLet-1)/lineLen)+yMarg])
								pag.pop(whichLet-1)
								whichLet -= 1
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+(xMarg+charWidth),charHeight*(len(pag)/lineLen)+yMarg])
							else:
								pag.pop(whichLet-1)
								whichLet -= 1
								tempSpot = whichLet
								while whichLet < len(pag):
									screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
									whichLet += 1
								whichLet = tempSpot
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+xMarg,charHeight*(len(pag)/lineLen)+yMarg])
					screen.blit(L_mLe,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([mLe,[],[]])
					else:
						pag.insert(whichLet,[mLe,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#Division Sign
				if pressed[pygame.K_EQUALS] and pressed[pygame.K_d]:
					for vapp in range(3):
						if whichLet != 0: 
							if whichLet == len(pag):
								screen.blit(L_S,[charWidth*((whichLet-1)%lineLen)+xMarg,charHeight*((whichLet-1)/lineLen)+yMarg])
								pag.pop(whichLet-1)
								whichLet -= 1
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+(xMarg+charWidth),charHeight*(len(pag)/lineLen)+yMarg])
							else:
								pag.pop(whichLet-1)
								whichLet -= 1
								tempSpot = whichLet
								while whichLet < len(pag):
									screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
									whichLet += 1
								whichLet = tempSpot
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+xMarg,charHeight*(len(pag)/lineLen)+yMarg])
					screen.blit(L_mDi,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([mDi,[],[]])
					else:
						pag.insert(whichLet,[mDi,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#Approximation sign
				if pressed[pygame.K_EQUALS] and pressed[pygame.K_a]:
					for vapp in range(3):
						if whichLet != 0: 
							if whichLet == len(pag):
								screen.blit(L_S,[charWidth*((whichLet-1)%lineLen)+xMarg,charHeight*((whichLet-1)/lineLen)+yMarg])
								pag.pop(whichLet-1)
								whichLet -= 1
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+(xMarg+charWidth),charHeight*(len(pag)/lineLen)+yMarg])
							else:
								pag.pop(whichLet-1)
								whichLet -= 1
								tempSpot = whichLet
								while whichLet < len(pag):
									screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
									whichLet += 1
								whichLet = tempSpot
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+xMarg,charHeight*(len(pag)/lineLen)+yMarg])
					screen.blit(L_mAp,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([mAp,[],[]])
					else:
						pag.insert(whichLet,[mAp,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#Plus sign
				if pressed[pygame.K_EQUALS] and pressed[pygame.K_p]:
					for vapp in range(3):
						if whichLet != 0: 
							if whichLet == len(pag):
								screen.blit(L_S,[charWidth*((whichLet-1)%lineLen)+xMarg,charHeight*((whichLet-1)/lineLen)+yMarg])
								pag.pop(whichLet-1)
								whichLet -= 1
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+(xMarg+charWidth),charHeight*(len(pag)/lineLen)+yMarg])
							else:
								pag.pop(whichLet-1)
								whichLet -= 1
								tempSpot = whichLet
								while whichLet < len(pag):
									screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
									whichLet += 1
								whichLet = tempSpot
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+xMarg,charHeight*(len(pag)/lineLen)+yMarg])
					screen.blit(L_mPl,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([mPl,[],[]])
					else:
						pag.insert(whichLet,[mPl,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#Minus sign
				if pressed[pygame.K_MINUS] and not (pressed[pygame.K_LSHIFT] or pressed[pygame.K_RSHIFT]):
					screen.blit(L_mSb,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([mSb,[],[]])
					else:
						pag.insert(whichLet,[mSb,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#Multiplication sign
				if pressed[pygame.K_EQUALS] and pressed[pygame.K_m]:
					for vapp in range(3):
						if whichLet != 0: 
							if whichLet == len(pag):
								screen.blit(L_S,[charWidth*((whichLet-1)%lineLen)+xMarg,charHeight*((whichLet-1)/lineLen)+yMarg])
								pag.pop(whichLet-1)
								whichLet -= 1
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+(xMarg+charWidth),charHeight*(len(pag)/lineLen)+yMarg])
							else:
								pag.pop(whichLet-1)
								whichLet -= 1
								tempSpot = whichLet
								while whichLet < len(pag):
									screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
									whichLet += 1
								whichLet = tempSpot
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+xMarg,charHeight*(len(pag)/lineLen)+yMarg])
					screen.blit(L_mMu,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([mMu,[],[]])
					else:
						pag.insert(whichLet,[mMu,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#QED
				if pressed[pygame.K_EQUALS] and pressed[pygame.K_q]:
					for vapp in range(3):
						if whichLet != 0: 
							if whichLet == len(pag):
								screen.blit(L_S,[charWidth*((whichLet-1)%lineLen)+xMarg,charHeight*((whichLet-1)/lineLen)+yMarg])
								pag.pop(whichLet-1)
								whichLet -= 1
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+(xMarg+charWidth),charHeight*(len(pag)/lineLen)+yMarg])
							else:
								pag.pop(whichLet-1)
								whichLet -= 1
								tempSpot = whichLet
								while whichLet < len(pag):
									screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
									whichLet += 1
								whichLet = tempSpot
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+xMarg,charHeight*(len(pag)/lineLen)+yMarg])
					screen.blit(L_mQe,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([mQe,[],[]])
					else:
						pag.insert(whichLet,[mQe,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#Forward Slash
				if pressed[pygame.K_SLASH] and not (pressed[pygame.K_LSHIFT] or pressed[pygame.K_RSHIFT]):
					screen.blit(L_mFs,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([mFs,[],[]])
					else:
						pag.insert(whichLet,[mFs,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#Backslash
				if pressed[pygame.K_BACKSLASH] and not (pressed[pygame.K_LSHIFT] or pressed[pygame.K_RSHIFT]):
					screen.blit(L_mBs,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([mBs,[],[]])
					else:
						pag.insert(whichLet,[mBs,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#Square root
				if pressed[pygame.K_s] and pressed[pygame.K_EQUALS]:
					for vapp in range(3):
						if whichLet != 0: 
							if whichLet == len(pag):
								screen.blit(L_S,[charWidth*((whichLet-1)%lineLen)+xMarg,charHeight*((whichLet-1)/lineLen)+yMarg])
								pag.pop(whichLet-1)
								whichLet -= 1
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+(xMarg+charWidth),charHeight*(len(pag)/lineLen)+yMarg])
							else:
								pag.pop(whichLet-1)
								whichLet -= 1
								tempSpot = whichLet
								while whichLet < len(pag):
									screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
									whichLet += 1
								whichLet = tempSpot
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+xMarg,charHeight*(len(pag)/lineLen)+yMarg])
					screen.blit(L_mSr,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([mSr,[],[]])
					else:
						pag.insert(whichLet,[mSr,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#Plus/Minus
				if pressed[pygame.K_l] and pressed[pygame.K_EQUALS]:
					for vapp in range(3):
						if whichLet != 0: 
							if whichLet == len(pag):
								screen.blit(L_S,[charWidth*((whichLet-1)%lineLen)+xMarg,charHeight*((whichLet-1)/lineLen)+yMarg])
								pag.pop(whichLet-1)
								whichLet -= 1
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+(xMarg+charWidth),charHeight*(len(pag)/lineLen)+yMarg])
							else:
								pag.pop(whichLet-1)
								whichLet -= 1
								tempSpot = whichLet
								while whichLet < len(pag):
									screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
									whichLet += 1
								whichLet = tempSpot
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+xMarg,charHeight*(len(pag)/lineLen)+yMarg])
					screen.blit(L_mAs,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([mAs,[],[]])
					else:
						pag.insert(whichLet,[mAs,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#Integral
				if pressed[pygame.K_f] and pressed[pygame.K_EQUALS]:
					for vapp in range(3):
						if whichLet != 0: 
							if whichLet == len(pag):
								screen.blit(L_S,[charWidth*((whichLet-1)%lineLen)+xMarg,charHeight*((whichLet-1)/lineLen)+yMarg])
								pag.pop(whichLet-1)
								whichLet -= 1
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+(xMarg+charWidth),charHeight*(len(pag)/lineLen)+yMarg])
							else:
								pag.pop(whichLet-1)
								whichLet -= 1
								tempSpot = whichLet
								while whichLet < len(pag):
									screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
									whichLet += 1
								whichLet = tempSpot
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+xMarg,charHeight*(len(pag)/lineLen)+yMarg])
					screen.blit(L_mAd,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([mAd,[],[]])
					else:
						pag.insert(whichLet,[mAd,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#Divides 
				if pressed[pygame.K_BACKSLASH] and (pressed[pygame.K_LSHIFT] or pressed[pygame.K_RSHIFT]):
					screen.blit(L_mDv,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([mDv,[],[]])
					else:
						pag.insert(whichLet,[mDv,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#Doesnt equal
				if pressed[pygame.K_n] and pressed[pygame.K_EQUALS]:
					for vapp in range(3):
						if whichLet != 0: 
							if whichLet == len(pag):
								screen.blit(L_S,[charWidth*((whichLet-1)%lineLen)+xMarg,charHeight*((whichLet-1)/lineLen)+yMarg])
								pag.pop(whichLet-1)
								whichLet -= 1
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+(xMarg+charWidth),charHeight*(len(pag)/lineLen)+yMarg])
							else:
								pag.pop(whichLet-1)
								whichLet -= 1
								tempSpot = whichLet
								while whichLet < len(pag):
									screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
									whichLet += 1
								whichLet = tempSpot
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+xMarg,charHeight*(len(pag)/lineLen)+yMarg])
					screen.blit(L_mNe,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([mNe,[],[]])
					else:
						pag.insert(whichLet,[mNe,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#Angle
				if pressed[pygame.K_g] and pressed[pygame.K_EQUALS]:
					for vapp in range(3):
						if whichLet != 0: 
							if whichLet == len(pag):
								screen.blit(L_S,[charWidth*((whichLet-1)%lineLen)+xMarg,charHeight*((whichLet-1)/lineLen)+yMarg])
								pag.pop(whichLet-1)
								whichLet -= 1
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+(xMarg+charWidth),charHeight*(len(pag)/lineLen)+yMarg])
							else:
								pag.pop(whichLet-1)
								whichLet -= 1
								tempSpot = whichLet
								while whichLet < len(pag):
									screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
									whichLet += 1
								whichLet = tempSpot
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+xMarg,charHeight*(len(pag)/lineLen)+yMarg])
					screen.blit(L_mAn,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([mAn,[],[]])
					else:
						pag.insert(whichLet,[mAn,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#Delta (Triangle??)
				if pressed[pygame.K_t] and pressed[pygame.K_EQUALS]:
					for vapp in range(3):
						if whichLet != 0: 
							if whichLet == len(pag):
								screen.blit(L_S,[charWidth*((whichLet-1)%lineLen)+xMarg,charHeight*((whichLet-1)/lineLen)+yMarg])
								pag.pop(whichLet-1)
								whichLet -= 1
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+(xMarg+charWidth),charHeight*(len(pag)/lineLen)+yMarg])
							else:
								pag.pop(whichLet-1)
								whichLet -= 1
								tempSpot = whichLet
								while whichLet < len(pag):
									screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
									whichLet += 1
								whichLet = tempSpot
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+xMarg,charHeight*(len(pag)/lineLen)+yMarg])
					screen.blit(L_mDe,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([mDe,[],[]])
					else:
						pag.insert(whichLet,[mDe,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#Gradient
				if pressed[pygame.K_r] and pressed[pygame.K_EQUALS]:
					for vapp in range(3):
						if whichLet != 0: 
							if whichLet == len(pag):
								screen.blit(L_S,[charWidth*((whichLet-1)%lineLen)+xMarg,charHeight*((whichLet-1)/lineLen)+yMarg])
								pag.pop(whichLet-1)
								whichLet -= 1
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+(xMarg+charWidth),charHeight*(len(pag)/lineLen)+yMarg])
							else:
								pag.pop(whichLet-1)
								whichLet -= 1
								tempSpot = whichLet
								while whichLet < len(pag):
									screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
									whichLet += 1
								whichLet = tempSpot
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+xMarg,charHeight*(len(pag)/lineLen)+yMarg])
					screen.blit(L_mGr,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([mGr,[],[]])
					else:
						pag.insert(whichLet,[mGr,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#Infinity
				if pressed[pygame.K_i] and pressed[pygame.K_EQUALS]:
					for vapp in range(3):
						if whichLet != 0: 
							if whichLet == len(pag):
								screen.blit(L_S,[charWidth*((whichLet-1)%lineLen)+xMarg,charHeight*((whichLet-1)/lineLen)+yMarg])
								pag.pop(whichLet-1)
								whichLet -= 1
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+(xMarg+charWidth),charHeight*(len(pag)/lineLen)+yMarg])
							else:
								pag.pop(whichLet-1)
								whichLet -= 1
								tempSpot = whichLet
								while whichLet < len(pag):
									screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
									whichLet += 1
								whichLet = tempSpot
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+xMarg,charHeight*(len(pag)/lineLen)+yMarg])
					screen.blit(L_mIn,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([mIn,[],[]])
					else:
						pag.insert(whichLet,[mIn,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1



	#-----------------------Space -----------------------------

				if pressed[pygame.K_SPACE] and not rSChek:
					screen.blit(L_S,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([rSp,[],[]])
					else:
						pag.insert(whichLet,[rSp,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1
					rSChek = True



	#-----------------------Numbers -----------------------------


				#Numeral 1
				if pressed[pygame.K_1] and not pressed[pygame.K_LSHIFT]:
					screen.blit(L_Non,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([On,[],[]])
					else:
						pag.insert(whichLet,[On,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#Numeral 2
				if pressed[pygame.K_2] and not pressed[pygame.K_LSHIFT]:
					screen.blit(L_Ntw,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([Tw,[],[]])
					else:
						pag.insert(whichLet,[Tw,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#Numeral 3
				if pressed[pygame.K_3] and not pressed[pygame.K_LSHIFT]:
					screen.blit(L_Nth,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([Th,[],[]])
					else:
						pag.insert(whichLet,[Th,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1


				#Numeral 4
				if pressed[pygame.K_4] and not pressed[pygame.K_LSHIFT]:
					screen.blit(L_Nfo,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([Fo,[],[]])
					else:
						pag.insert(whichLet,[Fo,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#Numeral 5
				if pressed[pygame.K_5] and not pressed[pygame.K_LSHIFT]:
					screen.blit(L_Nfi,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([Fi,[],[]])
					else:
						pag.insert(whichLet,[Fi,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#Numeral 6
				if pressed[pygame.K_6] and not pressed[pygame.K_LSHIFT]:
					screen.blit(L_Nsi,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([Si,[],[]])
					else:
						pag.insert(whichLet,[Si,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#Numeral 7
				if pressed[pygame.K_7] and not pressed[pygame.K_LSHIFT]:
					screen.blit(L_Nse,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([Se,[],[]])
					else:
						pag.insert(whichLet,[Se,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#Numeral 8
				if pressed[pygame.K_8] and not pressed[pygame.K_LSHIFT]:
					screen.blit(L_Nei,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([Ei,[],[]])
					else:
						pag.insert(whichLet,[Ei,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#Numeral 9
				if pressed[pygame.K_9] and not pressed[pygame.K_LSHIFT]:
					screen.blit(L_Nni,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([Ni,[],[]])
					else:
						pag.insert(whichLet,[Ni,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#Numeral 0
				if pressed[pygame.K_0] and not pressed[pygame.K_LSHIFT]:
					screen.blit(L_Nze,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([Ze,[],[]])
					else:
						pag.insert(whichLet,[Ze,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1


					#-------------------------------MODAL LOGIC ------------------------------

					# Logically Possible
				if pressed[pygame.K_2] and pressed[pygame.K_p]:
					for vapp in range(3):
						if whichLet != 0: 
							if whichLet == len(pag):
								screen.blit(L_S,[charWidth*((whichLet-1)%lineLen)+xMarg,charHeight*((whichLet-1)/lineLen)+yMarg])
								pag.pop(whichLet-1)
								whichLet -= 1
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+(xMarg+charWidth),charHeight*(len(pag)/lineLen)+yMarg])
							else:
								pag.pop(whichLet-1)
								whichLet -= 1
								tempSpot = whichLet
								while whichLet < len(pag):
									screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
									whichLet += 1
								whichLet = tempSpot
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+xMarg,charHeight*(len(pag)/lineLen)+yMarg])
					screen.blit(L_mP,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([mP,[],[]])
					else:
						pag.insert(whichLet,[mP,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

					# Logically Possible
				if pressed[pygame.K_2] and pressed[pygame.K_n]:
					for vapp in range(3):
						if whichLet != 0: 
							if whichLet == len(pag):
								screen.blit(L_S,[charWidth*((whichLet-1)%lineLen)+xMarg,charHeight*((whichLet-1)/lineLen)+yMarg])
								pag.pop(whichLet-1)
								whichLet -= 1
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+(xMarg+charWidth),charHeight*(len(pag)/lineLen)+yMarg])
							else:
								pag.pop(whichLet-1)
								whichLet -= 1
								tempSpot = whichLet
								while whichLet < len(pag):
									screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
									whichLet += 1
								whichLet = tempSpot
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+xMarg,charHeight*(len(pag)/lineLen)+yMarg])
					screen.blit(L_mN,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([mN,[],[]])
					else:
						pag.insert(whichLet,[mN,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1


	#------------------- FIRST ORDER LOGIC ----------------



				# Existential Quantifier
				if pressed[pygame.K_1] and pressed[pygame.K_e]:
					for vapp in range(3):
						if whichLet != 0: 
							if whichLet == len(pag):
								screen.blit(L_S,[charWidth*((whichLet-1)%lineLen)+xMarg,charHeight*((whichLet-1)/lineLen)+yMarg])
								pag.pop(whichLet-1)
								whichLet -= 1
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+(xMarg+charWidth),charHeight*(len(pag)/lineLen)+yMarg])
							else:
								pag.pop(whichLet-1)
								whichLet -= 1
								tempSpot = whichLet
								while whichLet < len(pag):
									screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
									whichLet += 1
								whichLet = tempSpot
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+xMarg,charHeight*(len(pag)/lineLen)+yMarg])
					screen.blit(L_fE,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([Ex,[],[]])
					else:
						pag.insert(whichLet,[Ex,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#For all
				if pressed[pygame.K_1] and pressed[pygame.K_a]:
					for vapp in range(3):
						if whichLet != 0: 
							if whichLet == len(pag):
								screen.blit(L_S,[charWidth*((whichLet-1)%lineLen)+xMarg,charHeight*((whichLet-1)/lineLen)+yMarg])
								pag.pop(whichLet-1)
								whichLet -= 1
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+(xMarg+charWidth),charHeight*(len(pag)/lineLen)+yMarg])
							else:
								pag.pop(whichLet-1)
								whichLet -= 1
								tempSpot = whichLet
								while whichLet < len(pag):
									screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
									whichLet += 1
								whichLet = tempSpot
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+xMarg,charHeight*(len(pag)/lineLen)+yMarg])
					screen.blit(L_fA,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([Fa,[],[]])
					else:
						pag.insert(whichLet,[Fa,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#Negation
				if pressed[pygame.K_1] and pressed[pygame.K_n]:
					for vapp in range(3):
						if whichLet != 0: 
							if whichLet == len(pag):
								screen.blit(L_S,[charWidth*((whichLet-1)%lineLen)+xMarg,charHeight*((whichLet-1)/lineLen)+yMarg])
								pag.pop(whichLet-1)
								whichLet -= 1
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+(xMarg+charWidth),charHeight*(len(pag)/lineLen)+yMarg])
							else:
								pag.pop(whichLet-1)
								whichLet -= 1
								tempSpot = whichLet
								while whichLet < len(pag):
									screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
									whichLet += 1
								whichLet = tempSpot
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+xMarg,charHeight*(len(pag)/lineLen)+yMarg])
					screen.blit(L_fN,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([Ne,[],[]])
					else:
						pag.insert(whichLet,[Ne,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#Implies
				if pressed[pygame.K_1] and pressed[pygame.K_i]:
					for vapp in range(3):
						if whichLet != 0: 
							if whichLet == len(pag):
								screen.blit(L_S,[charWidth*((whichLet-1)%lineLen)+xMarg,charHeight*((whichLet-1)/lineLen)+yMarg])
								pag.pop(whichLet-1)
								whichLet -= 1
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+(xMarg+charWidth),charHeight*(len(pag)/lineLen)+yMarg])
							else:
								pag.pop(whichLet-1)
								whichLet -= 1
								tempSpot = whichLet
								while whichLet < len(pag):
									screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
									whichLet += 1
								whichLet = tempSpot
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+xMarg,charHeight*(len(pag)/lineLen)+yMarg])
					screen.blit(L_fI,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([Im,[],[]])
					else:
						pag.insert(whichLet,[Im,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#If and only if
				if pressed[pygame.K_1] and pressed[pygame.K_f]:
					for vapp in range(3):
						if whichLet != 0: 
							if whichLet == len(pag):
								screen.blit(L_S,[charWidth*((whichLet-1)%lineLen)+xMarg,charHeight*((whichLet-1)/lineLen)+yMarg])
								pag.pop(whichLet-1)
								whichLet -= 1
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+(xMarg+charWidth),charHeight*(len(pag)/lineLen)+yMarg])
							else:
								pag.pop(whichLet-1)
								whichLet -= 1
								tempSpot = whichLet
								while whichLet < len(pag):
									screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
									whichLet += 1
								whichLet = tempSpot
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+xMarg,charHeight*(len(pag)/lineLen)+yMarg])
					screen.blit(L_fF,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([Ff,[],[]])
					else:
						pag.insert(whichLet,[Ff,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#And
				if pressed[pygame.K_1] and pressed[pygame.K_d]:
					for vapp in range(3):
						if whichLet != 0: 
							if whichLet == len(pag):
								screen.blit(L_S,[charWidth*((whichLet-1)%lineLen)+xMarg,charHeight*((whichLet-1)/lineLen)+yMarg])
								pag.pop(whichLet-1)
								whichLet -= 1
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+(xMarg+charWidth),charHeight*(len(pag)/lineLen)+yMarg])
							else:
								pag.pop(whichLet-1)
								whichLet -= 1
								tempSpot = whichLet
								while whichLet < len(pag):
									screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
									whichLet += 1
								whichLet = tempSpot
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+xMarg,charHeight*(len(pag)/lineLen)+yMarg])
					screen.blit(L_fD,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([Nd,[],[]])
					else:
						pag.insert(whichLet,[Nd,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

	#----------------------------------------Set Theory---------------------------------------

					#Element of
				if pressed[pygame.K_0] and pressed[pygame.K_e]:
					for vapp in range(3):
						if whichLet != 0: 
							if whichLet == len(pag):
								screen.blit(L_S,[charWidth*((whichLet-1)%lineLen)+xMarg,charHeight*((whichLet-1)/lineLen)+yMarg])
								pag.pop(whichLet-1)
								whichLet -= 1
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+(xMarg+charWidth),charHeight*(len(pag)/lineLen)+yMarg])
							else:
								pag.pop(whichLet-1)
								whichLet -= 1
								tempSpot = whichLet
								while whichLet < len(pag):
									screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
									whichLet += 1
								whichLet = tempSpot
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+xMarg,charHeight*(len(pag)/lineLen)+yMarg])
					screen.blit(L_sEo,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([sEo,[],[]])
					else:
						pag.insert(whichLet,[sEo,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1


					#Not element of
				if pressed[pygame.K_0] and pressed[pygame.K_n]:
					for vapp in range(3):
						if whichLet != 0: 
							if whichLet == len(pag):
								screen.blit(L_S,[charWidth*((whichLet-1)%lineLen)+xMarg,charHeight*((whichLet-1)/lineLen)+yMarg])
								pag.pop(whichLet-1)
								whichLet -= 1
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+(xMarg+charWidth),charHeight*(len(pag)/lineLen)+yMarg])
							else:
								pag.pop(whichLet-1)
								whichLet -= 1
								tempSpot = whichLet
								while whichLet < len(pag):
									screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
									whichLet += 1
								whichLet = tempSpot
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+xMarg,charHeight*(len(pag)/lineLen)+yMarg])
					screen.blit(L_sDc,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([sDc,[],[]])
					else:
						pag.insert(whichLet,[sDc,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

					#Null set
				if pressed[pygame.K_0] and pressed[pygame.K_z]:
					for vapp in range(3):
						if whichLet != 0: 
							if whichLet == len(pag):
								screen.blit(L_S,[charWidth*((whichLet-1)%lineLen)+xMarg,charHeight*((whichLet-1)/lineLen)+yMarg])
								pag.pop(whichLet-1)
								whichLet -= 1
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+(xMarg+charWidth),charHeight*(len(pag)/lineLen)+yMarg])
							else:
								pag.pop(whichLet-1)
								whichLet -= 1
								tempSpot = whichLet
								while whichLet < len(pag):
									screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
									whichLet += 1
								whichLet = tempSpot
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+xMarg,charHeight*(len(pag)/lineLen)+yMarg])
					screen.blit(L_sNs,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([sNs,[],[]])
					else:
						pag.insert(whichLet,[sNs,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1


					#Union
				if pressed[pygame.K_0] and pressed[pygame.K_u]:
					for vapp in range(3):
						if whichLet != 0: 
							if whichLet == len(pag):
								screen.blit(L_S,[charWidth*((whichLet-1)%lineLen)+xMarg,charHeight*((whichLet-1)/lineLen)+yMarg])
								pag.pop(whichLet-1)
								whichLet -= 1
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+(xMarg+charWidth),charHeight*(len(pag)/lineLen)+yMarg])
							else:
								pag.pop(whichLet-1)
								whichLet -= 1
								tempSpot = whichLet
								while whichLet < len(pag):
									screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
									whichLet += 1
								whichLet = tempSpot
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+xMarg,charHeight*(len(pag)/lineLen)+yMarg])
					screen.blit(L_sUn,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([sUn,[],[]])
					else:
						pag.insert(whichLet,[sUn,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

					#Intersection
				if pressed[pygame.K_0] and pressed[pygame.K_i]:
					for vapp in range(3):
						if whichLet != 0: 
							if whichLet == len(pag):
								screen.blit(L_S,[charWidth*((whichLet-1)%lineLen)+xMarg,charHeight*((whichLet-1)/lineLen)+yMarg])
								pag.pop(whichLet-1)
								whichLet -= 1
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+(xMarg+charWidth),charHeight*(len(pag)/lineLen)+yMarg])
							else:
								pag.pop(whichLet-1)
								whichLet -= 1
								tempSpot = whichLet
								while whichLet < len(pag):
									screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
									whichLet += 1
								whichLet = tempSpot
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+xMarg,charHeight*(len(pag)/lineLen)+yMarg])
					screen.blit(L_sIn,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([sIn,[],[]])
					else:
						pag.insert(whichLet,[sIn,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

					#Sub set
				if pressed[pygame.K_0] and pressed[pygame.K_b]:
					for vapp in range(3):
						if whichLet != 0: 
							if whichLet == len(pag):
								screen.blit(L_S,[charWidth*((whichLet-1)%lineLen)+xMarg,charHeight*((whichLet-1)/lineLen)+yMarg])
								pag.pop(whichLet-1)
								whichLet -= 1
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+(xMarg+charWidth),charHeight*(len(pag)/lineLen)+yMarg])
							else:
								pag.pop(whichLet-1)
								whichLet -= 1
								tempSpot = whichLet
								while whichLet < len(pag):
									screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
									whichLet += 1
								whichLet = tempSpot
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+xMarg,charHeight*(len(pag)/lineLen)+yMarg])
					screen.blit(L_sBs,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([sBs,[],[]])
					else:
						pag.insert(whichLet,[sBs,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

					#Super Set
				if pressed[pygame.K_0] and pressed[pygame.K_p]:
					for vapp in range(3):
						if whichLet != 0: 
							if whichLet == len(pag):
								screen.blit(L_S,[charWidth*((whichLet-1)%lineLen)+xMarg,charHeight*((whichLet-1)/lineLen)+yMarg])
								pag.pop(whichLet-1)
								whichLet -= 1
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+(xMarg+charWidth),charHeight*(len(pag)/lineLen)+yMarg])
							else:
								pag.pop(whichLet-1)
								whichLet -= 1
								tempSpot = whichLet
								while whichLet < len(pag):
									screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
									whichLet += 1
								whichLet = tempSpot
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+xMarg,charHeight*(len(pag)/lineLen)+yMarg])
					screen.blit(L_sSs,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([sSs,[],[]])
					else:
						pag.insert(whichLet,[sSs,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

					#Not super set
				if pressed[pygame.K_0] and pressed[pygame.K_o]:
					for vapp in range(3):
						if whichLet != 0: 
							if whichLet == len(pag):
								screen.blit(L_S,[charWidth*((whichLet-1)%lineLen)+xMarg,charHeight*((whichLet-1)/lineLen)+yMarg])
								pag.pop(whichLet-1)
								whichLet -= 1
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+(xMarg+charWidth),charHeight*(len(pag)/lineLen)+yMarg])
							else:
								pag.pop(whichLet-1)
								whichLet -= 1
								tempSpot = whichLet
								while whichLet < len(pag):
									screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
									whichLet += 1
								whichLet = tempSpot
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+xMarg,charHeight*(len(pag)/lineLen)+yMarg])
					screen.blit(L_sNp,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([sNp,[],[]])
					else:
						pag.insert(whichLet,[sNp,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

					#Not Sub set
				if pressed[pygame.K_0] and pressed[pygame.K_v]:
					for vapp in range(3):
						if whichLet != 0: 
							if whichLet == len(pag):
								screen.blit(L_S,[charWidth*((whichLet-1)%lineLen)+xMarg,charHeight*((whichLet-1)/lineLen)+yMarg])
								pag.pop(whichLet-1)
								whichLet -= 1
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+(xMarg+charWidth),charHeight*(len(pag)/lineLen)+yMarg])
							else:
								pag.pop(whichLet-1)
								whichLet -= 1
								tempSpot = whichLet
								while whichLet < len(pag):
									screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
									whichLet += 1
								whichLet = tempSpot
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+xMarg,charHeight*(len(pag)/lineLen)+yMarg])
					screen.blit(L_sNb,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([sNb,[],[]])
					else:
						pag.insert(whichLet,[sNb,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

#--------------------Proof Theory----------------------------------

					#Single Turnstile
				if pressed[pygame.K_8] and pressed[pygame.K_s]:
					for vapp in range(3):
						if whichLet != 0: 
							if whichLet == len(pag):
								screen.blit(L_S,[charWidth*((whichLet-1)%lineLen)+xMarg,charHeight*((whichLet-1)/lineLen)+yMarg])
								pag.pop(whichLet-1)
								whichLet -= 1
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+(xMarg+charWidth),charHeight*(len(pag)/lineLen)+yMarg])
							else:
								pag.pop(whichLet-1)
								whichLet -= 1
								tempSpot = whichLet
								while whichLet < len(pag):
									screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
									whichLet += 1
								whichLet = tempSpot
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+xMarg,charHeight*(len(pag)/lineLen)+yMarg])
					screen.blit(L_pSt,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([pSt,[],[]])
					else:
						pag.insert(whichLet,[pSt,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

					#Not Single Turnstile
				if pressed[pygame.K_8] and pressed[pygame.K_x]:
					for vapp in range(3):
						if whichLet != 0: 
							if whichLet == len(pag):
								screen.blit(L_S,[charWidth*((whichLet-1)%lineLen)+xMarg,charHeight*((whichLet-1)/lineLen)+yMarg])
								pag.pop(whichLet-1)
								whichLet -= 1
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+(xMarg+charWidth),charHeight*(len(pag)/lineLen)+yMarg])
							else:
								pag.pop(whichLet-1)
								whichLet -= 1
								tempSpot = whichLet
								while whichLet < len(pag):
									screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
									whichLet += 1
								whichLet = tempSpot
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+xMarg,charHeight*(len(pag)/lineLen)+yMarg])
					screen.blit(L_pNs,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([pNs,[],[]])
					else:
						pag.insert(whichLet,[pNs,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

					#Double Turnstile
				if pressed[pygame.K_8] and pressed[pygame.K_d]:
					for vapp in range(3):
						if whichLet != 0: 
							if whichLet == len(pag):
								screen.blit(L_S,[charWidth*((whichLet-1)%lineLen)+xMarg,charHeight*((whichLet-1)/lineLen)+yMarg])
								pag.pop(whichLet-1)
								whichLet -= 1
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+(xMarg+charWidth),charHeight*(len(pag)/lineLen)+yMarg])
							else:
								pag.pop(whichLet-1)
								whichLet -= 1
								tempSpot = whichLet
								while whichLet < len(pag):
									screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
									whichLet += 1
								whichLet = tempSpot
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+xMarg,charHeight*(len(pag)/lineLen)+yMarg])
					screen.blit(L_pDt,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([pDt,[],[]])
					else:
						pag.insert(whichLet,[pDt,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

					#Not Double Turnstile
				if pressed[pygame.K_8] and pressed[pygame.K_c]:
					for vapp in range(3):
						if whichLet != 0: 
							if whichLet == len(pag):
								screen.blit(L_S,[charWidth*((whichLet-1)%lineLen)+xMarg,charHeight*((whichLet-1)/lineLen)+yMarg])
								pag.pop(whichLet-1)
								whichLet -= 1
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+(xMarg+charWidth),charHeight*(len(pag)/lineLen)+yMarg])
							else:
								pag.pop(whichLet-1)
								whichLet -= 1
								tempSpot = whichLet
								while whichLet < len(pag):
									screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
									whichLet += 1
								whichLet = tempSpot
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+xMarg,charHeight*(len(pag)/lineLen)+yMarg])
					screen.blit(L_pNd,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([pNd,[],[]])
					else:
						pag.insert(whichLet,[pNd,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

					#Logical Constant
				if pressed[pygame.K_8] and pressed[pygame.K_l]:
					for vapp in range(3):
						if whichLet != 0: 
							if whichLet == len(pag):
								screen.blit(L_S,[charWidth*((whichLet-1)%lineLen)+xMarg,charHeight*((whichLet-1)/lineLen)+yMarg])
								pag.pop(whichLet-1)
								whichLet -= 1
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+(xMarg+charWidth),charHeight*(len(pag)/lineLen)+yMarg])
							else:
								pag.pop(whichLet-1)
								whichLet -= 1
								tempSpot = whichLet
								while whichLet < len(pag):
									screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
									whichLet += 1
								whichLet = tempSpot
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+xMarg,charHeight*(len(pag)/lineLen)+yMarg])
					screen.blit(L_pLc,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(pag):
						pag.append([pLc,[],[]])
					else:
						pag.insert(whichLet,[pLc,[],[]])
						if pag[whichLet+1][0]==dSp:
							pag.pop(whichLet+1)
						else:
							tempSpot = whichLet
							gotIt = False							
							while whichLet <len(pag) and ((whichLet-tempSpot)<lineLen) and not gotIt:								
								if pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									gotIt = True
								whichLet+=1
							whichLet = tempSpot
						tempSpot = whichLet
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1



	#----------------------COMMANDS (enter, backspace, etc)--------------------



				if pressed[pygame.K_LSHIFT] and pressed[pygame.K_EQUALS]:
					supaChek = True
					whichLet -= 1
					for tug in range(len(pag[whichLet][1])):
						screen.blit(l_S,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
						lilWhichLet += 1
					pag[whichLet][1] = []
					lilWhichLet = 0

				if pressed[pygame.K_LSHIFT] and pressed[pygame.K_MINUS]:
					subDummy = 1
					whichLet -= 1
					lilWhichLet = 0
					for tug in range(len(pag[whichLet][2])):
						screen.blit(l_S,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
						lilWhichLet += 1
					pag[whichLet][1] = []


				if pressed[pygame.K_LCTRL] and pressed [pygame.K_s]:
					if whichLet == len(pag):
						screen.blit(L_S,[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
					else:
						screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
					saveName = tkFileDialog.asksaveasfilename()
					saveName = str(saveName)
					pygame.image.save(screen,"curpag.PNG")
					saveIm = Image.open('curpag.PNG')
					saveImSize =  saveIm.size
					pagLen = len(pag)
					pagLenDummy = pagLen
					Xboun, Yboun = 0,0;
					Xboun, Yboun = saveIm.size
					supaSaveCou = 0
					subSaveCou = 0
					yuss, tack, dukh = 0,0,0
					while pagLenDummy > 65536:
						yuss += 1
						pagLenDummy -= 65536
					while pagLenDummy > 256:
						tack += 1
						pagLenDummy -= 256
					while pagLenDummy > 0:
						dukh += 1
						pagLenDummy -= 1
					saveIm.putpixel((Xboun-1,0), (yuss, tack, dukh))
					yuss, tack, dukh = 0,0,0
					for yit in range(len(pag)):
						if yit%3 == 0:
							yuss, tack, dukh = 0,0,0
							if yit+2 < len(pag):
								dukh = pag[yit+2][0]
							if yit+1 < len(pag):
								tack = pag[yit+1][0]
							if yit < len(pag):
								yuss = pag[yit][0]
							saveIm.putpixel((pagLenDummy%(xMarg),pagLenDummy/xMarg), (yuss, tack, dukh))
							pagLenDummy += 1
						if len(pag[yit][1]) > 0:
							saveIm.putpixel(((supaSaveCou%xMarg)+xMarg,supaSaveCou/xMarg), (yit, len(pag[yit][1]), 255))
							yuss, tack, dukh = 0,0,0
							supaSaveCou += 1
							for vapp in range(len(pag[yit][1])):
								if vapp%3 == 0:
									yuss, tack, dukh = 0,0,0
									if vapp+2 < len(pag[yit][1]):
										dukh = pag[yit][1][vapp+2]
									if vapp+1 < len(pag[yit][1]):
										tack = pag[yit][1][vapp+1]
									if vapp < len(pag[yit][1]):
										yuss = pag[yit][1][vapp]
									saveIm.putpixel(((supaSaveCou%xMarg)+xMarg,supaSaveCou/xMarg), (yuss, tack, dukh))
									supaSaveCou += 1
						if len(pag[yit][2]) > 0:
							saveIm.putpixel(((subSaveCou%xMarg)+(2*xMarg),subSaveCou/xMarg), (yit, len(pag[yit][2]), 254))
							yuss, tack, dukh = 0,0,0
							subSaveCou += 1
							for vapp in range(len(pag[yit][2])):
								if vapp%3 == 0:
									if vapp+2 < len(pag[yit][2]):
										dukh = pag[yit][2][vapp+2]
									if vapp+1 < len(pag[yit][2]):
										tack = pag[yit][2][vapp+1]
									if vapp < len(pag[yit][2]):
										yuss = pag[yit][2][vapp]
									saveIm.putpixel(((subSaveCou%xMarg)+(2*xMarg),subSaveCou/xMarg), (yuss, tack, dukh))
									subSaveCou += 1
					pagLenDummy = 0
					saveIm.save(saveName,"png")

				if pressed[pygame.K_LCTRL] and pressed[pygame.K_o]:
					pag = []
					openName = tkFileDialog.askopenfilename()
					openName = str(openName)
					openIm =  Image.open(openName)
					openIm.show()
					Xboun, Yboun = 0,0
					Xboun, Yboun = openIm.size
					stei, ohre, heed = 0,0,0
					stei, ohre, heed = openIm.getpixel((Xboun-1,0))
					pagLenDummy = 0
					pagLenDummy += 65536*stei
					pagLenDummy += 256*ohre
					pagLenDummy += heed
					bink, yat, duss = 0,0,0
					nyih = [bink,yat,duss]
					vfre, klut, prun = 0,0,0
					xBoun = 0
					yBoun = 0
					for yit in range(pagLenDummy):
						if yit%3 == 0:
							xYit = xBoun%(xMarg)
							yYit = yBoun/(xMarg)
							bink, yat, duss = openIm.getpixel((xYit,yYit))
							nyih = [bink,yat,duss]
							pag.append([nyih[0],[],[]])
							if yit+1 < pagLenDummy:
								pag.append([nyih[1],[],[]])
							if yit+2 < pagLenDummy:
								pag.append([nyih[2],[],[]])
							xBoun += 1
							yBoun += 1
					bink, yat, duss = 0,0,0
					xBoun = 1
					yBoun = 0
					for yit in range(pagLenDummy):
						bink, yat, duss = openIm.getpixel(((yit%xMarg)+xMarg,yit/(xMarg*2)))
						if duss == 255:
							for vapp in range(yat):
								if vapp%3 == 0:
									vfre, klut, prun = openIm.getpixel((((yit+(xBoun))%xMarg)+xMarg,(yit+xBoun)/xMarg))
									pag[bink][1].append(vfre)
									if vapp + 1 < yat:
										pag[bink][1].append(klut)
									if vapp + 2 < yat:
										pag[bink][1].append(prun)
									xBoun += 1
							xBoun = 1
						if duss == 254:
							for vapp in range(yat):
								if vapp%3 == 0:
									vfre, klut, prun = openIm.getpixel((((yit+(vapp+1))%xMarg)+xMarg,(yit+vapp)/xMarg))
									pag[bink][1].append(vfre)
									if vapp + 1 < yat:
										pag[bink][2].append(klut)
									if vapp + 2 < yat:
										pag[bink][2].append(prun)
					screen.fill((0,0,0))
					whichLet = 0
					lilWhichLet = 0
					while whichLet < len(pag):
						screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
						if len(pag[whichLet][1]) > 0:
							basePlaceX = charWidth*(whichLet%lineLen)+xMarg
							basePlaceY = charHeight*(whichLet/lineLen)+yMarg
							for toh in range(len(pag[whichLet][1])):
								screen.blit(getLetl(pag[whichLet][1][toh]),[(basePlaceX+lilCharXOffset)+(toh*lilCharWidth),(basePlaceY+lilCharYOffset)])
						if len(pag[whichLet][2]) > 0:
							basePlaceX = charWidth*(whichLet%lineLen)+xMarg
							basePlaceY = charHeight*(whichLet/lineLen)+yMarg
							for toh in range(len(pag[whichLet][2])):
								screen.blit(getLetl(pag[whichLet][2][toh]),[(basePlaceX+lilCharXOffset)+(toh*lilCharWidth),(basePlaceY+lilCharYOffset+lilCharSubBuf)])
						whichLet += 1

				if pressed[pygame.K_r] and pressed[pygame.K_h]:
					print len(pag), whichLet, pag

				if pressed[pygame.K_UP] and not pressed[pygame.K_LSHIFT]:
					if whichLet != len(pag):
						screen.blit(getLet(pag[whichLet][0]),[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					else:
						screen.blit(L_S,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet > lineLen:
						whichLet -= lineLen

				if pressed[pygame.K_UP] and pressed[pygame.K_LSHIFT]:
					for ipp in range(5):
						if whichLet != len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
						else:
							screen.blit(L_S,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
						if whichLet > lineLen:
							whichLet -= lineLen

				if pressed[pygame.K_RIGHT] and not pressed[pygame.K_LSHIFT]:
					if whichLet < len(pag):
						screen.blit(getLet(pag[whichLet][0]),[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
						whichLet += 1

				if pressed[pygame.K_RIGHT] and pressed[pygame.K_LSHIFT]:
					for ipp in range(10):
						if whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
							whichLet += 1

				if pressed[pygame.K_LEFT] and not pressed[pygame.K_LSHIFT]:
					if whichLet:
						if whichLet < len(pag):
							print whichLet
							screen.blit(getLet(pag[whichLet][0]),[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
						else:
							screen.blit(L_S,[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
						whichLet -= 1

				if pressed[pygame.K_LEFT] and pressed[pygame.K_LSHIFT]:
					for ipp in range(10):
						if whichLet:
							if whichLet < len(pag):
								screen.blit(getLet(pag[whichLet][0]),[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
							else:
								screen.blit(L_S,[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet -= 1

				if pressed[pygame.K_DOWN] and not pressed[pygame.K_LSHIFT]:
					if len(pag) != 0:
						if whichLet != len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
						if (whichLet+lineLen) < len(pag):
							whichLet += lineLen
						elif (len(pag)%lineLen) <= (whichLet%lineLen):
							whichLet = len(pag)

				if pressed[pygame.K_DOWN] and pressed[pygame.K_LSHIFT]:
					for ipp in range(5):
						if len(pag) != 0:
							if whichLet != len(pag):
								screen.blit(getLet(pag[whichLet][0]),[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
							if (whichLet+lineLen) < len(pag):
								whichLet += lineLen
							elif (len(pag)%lineLen) <= (whichLet%lineLen):
								whichLet = len(pag)

				if pressed[pygame.K_BACKSPACE]:
					if whichLet != 0: #Make sure you arent at the beginning of the pag.
						dummyCount = 0
						tempSpot = whichLet
						while pag[whichLet-1][0] == dSp and whichLet != 1: #Count how much empty space is behind the cursor
								dummyCount += 1
								whichLet -= 1
						whichLet = tempSpot
						if dummyCount == 0:	#If there is no empty space, set it to one, so just one back space happens
							dummyCount = 1
						if dummyCount > lineLen: #If there is more empty spaces than the length of a line, then set it equal to the length of the line.
							dummyCount = lineLen 
						for ipp in range(dummyCount): #Do a backspace for the number of times we counted.
							if whichLet == len(pag): #If the cursor is at the end of the pagument
								if whichLet%lineLen == 0: #If you are at the beginning of a line, you need to paste an empty space there before you hop up a line
									screen.blit((L_S),[xMarg,charHeight*(len(pag)/lineLen)+(yMarg)])
								screen.blit(L_S,[charWidth*((whichLet-1)%lineLen)+xMarg,charHeight*((whichLet-1)/lineLen)+yMarg])
								if len(pag[whichLet-1][1]) > 0: #If the character had a superscript, paste black where the characters were
									basePlaceX = charWidth*((whichLet-1)%lineLen)+xMarg
									basePlaceY = charHeight*((whichLet-1)/lineLen)+yMarg
									for ipp in range(len(pag[whichLet-1][1])):
										screen.blit(l_S,[(basePlaceX+lilCharXOffset)+(ipp*lilCharWidth),(basePlaceY+lilCharYOffset)])
								if len(pag[whichLet-1][2]) > 0: #If the character had a subscript, paste black where the characters were
									basePlaceX = charWidth*((whichLet-1)%lineLen)+xMarg
									basePlaceY = charHeight*((whichLet-1)/lineLen)+yMarg
									for yit in range(len(pag[whichLet-1][2])):
										screen.blit(l_S,[(basePlaceX+lilCharXOffset)+(yit*lilCharWidth),(basePlaceY+lilCharYOffset+lilCharSubBuf)])	
								pag.pop(whichLet-1) #Remove that character from the pag[]
								whichLet -= 1 #Take a step back
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+(xMarg+charWidth),charHeight*(len(pag)/lineLen)+yMarg]) # Paste an empty spot where you are now
							else: #If you arent at the end of the pagument, you need to shift every letter after the cursor back one.
								if pag[whichLet][0]==dSp: # if there is empty space (dummy space) to the ahead of the cursor, remove the empty space and fill it with the letter.
										pag.insert(whichLet,[dSp,[],[]])
								pag.pop(whichLet-1) #get the letter we are backspacing out of the pag[]
								whichLet -= 1
								tempSpot = whichLet
								while whichLet < len(pag): #for every character after the cursor, paste it.
									screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
									if len(pag[whichLet][1]) > 0: #If its got a superscript, paste that too.
										basePlaceX = charWidth*(whichLet%lineLen)+xMarg
										basePlaceY = charHeight*(whichLet/lineLen)+yMarg
										for ipp in range(len(pag[whichLet][1])):
											screen.blit(getLetl(pag[whichLet][1][ipp]),[(basePlaceX+lilCharXOffset)+(ipp*lilCharWidth),(basePlaceY+lilCharYOffset)])
										for vap in range(3): #and paste some empty space beyond the super script to cover up any left of super script that didnt get erased
											screen.blit(l_S,[(basePlaceX+lilCharXOffset)+((len(pag[whichLet][1])+vap)*lilCharWidth),(basePlaceY+lilCharYOffset)])
									if len(pag[whichLet][2]) > 0: #If its got a subscript, paste it
										basePlaceX = charWidth*(whichLet%lineLen)+xMarg
										basePlaceY = charHeight*(whichLet/lineLen)+yMarg
										for yit in range(len(pag[whichLet][2])):
											screen.blit(getLetl(pag[whichLet][2][yit]),[(basePlaceX+lilCharXOffset)+(yit*lilCharWidth),(basePlaceY+lilCharYOffset+lilCharSubBuf)])
										for nen in range(3):
											screen.blit(l_S,[(basePlaceX+lilCharXOffset)+((len(pag[whichLet][2])+nen)*lilCharWidth),(basePlaceY+lilCharYOffset+lilCharSubBuf)])
									whichLet += 1
								whichLet = tempSpot
								screen.blit((L_S),[charWidth*(len(pag)%lineLen)+xMarg,charHeight*(len(pag)/lineLen)+yMarg]) #Put an empty space at the end of the pag, since the last character got shifted left

				if pressed[pygame.K_BACKSPACE] and pressed[pygame.K_LSHIFT]:
					for hob in range(10):
						if whichLet != 0:
							dummyCount = 0
							tempSpot = whichLet
							while pag[whichLet-1] == dSp:
									dummyCount += 1
									whichLet -= 1
							whichLet = tempSpot
							if dummyCount == 0:
								dummyCount = 1
							if dummyCount > lineLen:
								dummyCount = lineLen 
							for ipp in range(dummyCount):
								if whichLet == len(pag):
									if whichLet%lineLen == 0:
										screen.blit((L_S),[xMarg,charHeight*(len(pag)/lineLen)+(yMarg)])
									screen.blit(L_S,[charWidth*((whichLet-1)%lineLen)+xMarg,charHeight*((whichLet-1)/lineLen)+yMarg])
									if len(pag[whichLet-1][1]) > 0:
										basePlaceX = charWidth*((whichLet-1)%lineLen)+xMarg
										basePlaceY = charHeight*((whichLet-1)/lineLen)+yMarg
										for ipp in range(len(pag[whichLet-1][1])):
											screen.blit(l_S,[(basePlaceX+lilCharXOffset)+(ipp*lilCharWidth),(basePlaceY+lilCharYOffset)])
									if len(pag[whichLet-1][2]) > 0:
										basePlaceX = charWidth*((whichLet-1)%lineLen)+xMarg
										basePlaceY = charHeight*((whichLet-1)/lineLen)+yMarg
										for yit in range(len(pag[whichLet-1][2])):
											screen.blit(l_S,[(basePlaceX+lilCharXOffset)+(yit*lilCharWidth),(basePlaceY+lilCharYOffset+lilCharSubBuf)])
									pag.pop(whichLet-1)
									whichLet -= 1
									screen.blit((L_S),[charWidth*(len(pag)%lineLen)+(xMarg+charWidth),charHeight*(len(pag)/lineLen)+yMarg])
								else:
									if pag[whichLet][0]==dSp: # if there is empty space (dummy space) to the ahead of the cursor, remove the empty space and fill it with the letter.
											pag.insert(whichLet,[dSp,[],[]])
									pag.pop(whichLet-1)
									whichLet -= 1
									tempSpot = whichLet
									while whichLet < len(pag):
										screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
										if len(pag[whichLet][1]) > 0:
											basePlaceX = charWidth*(whichLet%lineLen)+xMarg
											basePlaceY = charHeight*(whichLet/lineLen)+yMarg
											for ipp in range(len(pag[whichLet][1])):
												screen.blit(getLetl(pag[whichLet][1][ipp]),[(basePlaceX+lilCharXOffset)+(ipp*lilCharWidth),(basePlaceY+lilCharYOffset)])
											for vap in range(3):
												screen.blit(l_S,[(basePlaceX+lilCharXOffset)+((len(pag[whichLet][1])+vap)*lilCharWidth),(basePlaceY+lilCharYOffset)])
										if len(pag[whichLet][2]) > 0:
											basePlaceX = charWidth*(whichLet%lineLen)+xMarg
											basePlaceY = charHeight*(whichLet/lineLen)+yMarg
											for yit in range(len(pag[whichLet][2])):
												screen.blit(getLetl(pag[whichLet][2][yit]),[(basePlaceX+lilCharXOffset)+(yit*lilCharWidth),(basePlaceY+lilCharYOffset+lilCharSubBuf)])
											for nen in range(3):
												screen.blit(l_S,[(basePlaceX+lilCharXOffset)+((len(pag[whichLet][2])+nen)*lilCharWidth),(basePlaceY+lilCharYOffset+lilCharSubBuf)])
										whichLet += 1
									whichLet = tempSpot
									screen.blit((L_S),[charWidth*(len(pag)%lineLen)+xMarg,charHeight*(len(pag)/lineLen)+yMarg])




				if pressed[pygame.K_RETURN]:
					if whichLet == len(pag):
						for ipp in range(lineLen-(whichLet%lineLen)):
							screen.blit(L_S,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
							pag.append([dSp,[],[]])
							whichLet += 1
					else:
						tempSpot = whichLet
						for ipp in range(lineLen-(whichLet%lineLen)):
							pag.insert(whichLet,[dSp,[],[]])
							whichLet += 1
						whichLet = tempSpot
						while whichLet < len(pag):
							screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1

# Word Wrap ----------------------------------------vv
				if whichLet != 0: # Make sure its not at the first character
					if whichLet == len(pag): #If you are at the end of the pagument
						if whichLet%lineLen == 0: #Check if you are at the end of a line
							tempSpot = whichLet # Save where we are at, the cursor is going to wander
							dumCou = 0
							if pag[whichLet-1][0] != dSp: #Check if the character to the left is a dummy space
								while pag[whichLet-1][0] != rSp: #Count how many non-space characters are to the left
									dumCou += 1
									whichLet -= 1
								if dumCou > lineLen:
									dumCou = 0
								for dar in range(dumCou): #For the number of characters before a space, put in a dummy space so the word wraps around to the next line
									pag.insert(whichLet,[dSp,[],[]])
									screen.blit(L_S,[charWidth*((whichLet+dar)%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
								while whichLet < len(pag):
									screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
									whichLet+=1
								whichLet = tempSpot+dumCou
					else: #If you arent at the end of the pagument, check every line edge after your char to see if a word needs to get wrapped.
						tempSpot = whichLet
						while whichLet%lineLen!=0:#Go to the end of the line
							whichLet+=1
						# The section below here goes to the end of each line and fills in dummy spaces to wrap words around to the next line
						while whichLet < len(pag):
							tempTSpot = whichLet
							dumCou = 0
							if pag[whichLet-1][0] != dSp:#If the letter to the left of the end of the line isnt a dummy space
								while pag[whichLet-1][0] != rSp: #Count 
									dumCou += 1
									whichLet -= 1
								if dumCou > lineLen:
									dumCou = 0
								for dar in range(dumCou):
									pag.insert(whichLet,[dSp,[],[]])
									screen.blit(L_S,[charWidth*((whichLet+dar)%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
								while whichLet < len(pag):
									screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
									whichLet+=1
							whichLet=tempTSpot+lineLen
						whichLet=tempSpot
						#The section below here goes through each line, and removes orphaned dummy spaces
						while whichLet%lineLen!=0:
							whichLet+=1
						whichLet+=lineLen
						isEnd = False
						while isEnd==False:
							if whichLet >= len(pag):
								isEnd=True
							else:
								if pag[whichLet][0]!=dSp:
									fouLet=True
								if fouLet==True and pag[whichLet][0]==dSp:
									pag.pop(whichLet)
									whichLet+=1
							whichLet-=1
							if whichLet%lineLen==0:
								whichLet+=2*lineLen
						whichLet=tempSpot
						if whichLet%lineLen==0:
							while pag[whichLet][0]!=rSp:
								whichLet+=1

			else:
				
				basePlaceX = charWidth*(whichLet%lineLen)+xMarg
				basePlaceY = charHeight*(whichLet/lineLen)+yMarg

				if supaChek and not subDummy:
					if pressed[pygame.K_LSHIFT] and pressed[pygame.K_MINUS]:
						supaChek = False
						whichLet += 1
						lilWhichLet = 0

				if subDummy and not supaChek:
					if pressed[pygame.K_LSHIFT] and pressed[pygame.K_EQUALS]:
						subDummy = 0
						whichLet += 1
						lilWhichLet = 0

# -------------------------------------------------Letters ----------------------------------------------------------

				#Lower a
				if pressed[pygame.K_a] and not pressed[pygame.K_LSHIFT]:
					screen.blit(l_la,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						pag[whichLet][1].append(a)
					if subDummy and not supaChek:
						pag[whichLet][2].append(a)
					lilWhichLet += 1
				
				#Upper A
				if pressed[pygame.K_a] and pressed[pygame.K_LSHIFT]:
					screen.blit(l_lA,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						pag[whichLet][1].append(A)
					if subDummy and not supaChek:
						pag[whichLet][2].append(A)
					lilWhichLet += 1

				#Lower b
				if pressed[pygame.K_b] and not pressed[pygame.K_LSHIFT]:
					screen.blit(l_lb,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						pag[whichLet][1].append(b)
					if subDummy and not supaChek:
						pag[whichLet][2].append(b)
					lilWhichLet += 1
				
				#Upper B
				if pressed[pygame.K_b] and pressed[pygame.K_LSHIFT]:
					screen.blit(l_lB,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						pag[whichLet][1].append(B)
					if subDummy and not supaChek:
						pag[whichLet][2].append(B)
					lilWhichLet += 1

				#Lower c
				if pressed[pygame.K_c] and not pressed[pygame.K_LSHIFT]:
					screen.blit(l_lc,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						pag[whichLet][1].append(c)
					if subDummy and not supaChek:
						pag[whichLet][2].append(c)
					lilWhichLet += 1
				
				#Upper C
				if pressed[pygame.K_c] and pressed[pygame.K_LSHIFT]:
					screen.blit(l_lC,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						pag[whichLet][1].append(C)
					if subDummy and not supaChek:
						pag[whichLet][2].append(C)
					lilWhichLet += 1

				#Lower d
				if pressed[pygame.K_d] and not pressed[pygame.K_LSHIFT]:
					screen.blit(l_ld,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						pag[whichLet][1].append(d)
					if subDummy and not supaChek:
						pag[whichLet][2].append(d)
					lilWhichLet += 1
				
				#Upper D
				if pressed[pygame.K_d] and pressed[pygame.K_LSHIFT]:
					screen.blit(l_lD,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						pag[whichLet][1].append(D)
					if subDummy and not supaChek:
						pag[whichLet][2].append(D)
					lilWhichLet += 1

				#Lower e
				if pressed[pygame.K_e] and not pressed[pygame.K_LSHIFT]:
					screen.blit(l_le,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						pag[whichLet][1].append(e)
					if subDummy and not supaChek:
						pag[whichLet][2].append(e)
					lilWhichLet += 1
				
				#Upper E
				if pressed[pygame.K_e] and pressed[pygame.K_LSHIFT]:
					screen.blit(l_lE,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						pag[whichLet][1].append(E)
					if subDummy and not supaChek:
						pag[whichLet][2].append(E)
					lilWhichLet += 1

				#Lower f
				if pressed[pygame.K_f] and not pressed[pygame.K_LSHIFT]:
					screen.blit(l_lf,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						pag[whichLet][1].append(f)
					if subDummy and not supaChek:
						pag[whichLet][2].append(f)
					lilWhichLet += 1
				
				#Upper F
				if pressed[pygame.K_f] and pressed[pygame.K_LSHIFT]:
					screen.blit(l_lF,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						pag[whichLet][1].append(F)
					if subDummy and not supaChek:
						pag[whichLet][2].append(F)
					lilWhichLet += 1

				#Lower g
				if pressed[pygame.K_g] and not pressed[pygame.K_LSHIFT]:
					screen.blit(l_lg,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						pag[whichLet][1].append(g)
					if subDummy and not supaChek:
						pag[whichLet][2].append(g)
					lilWhichLet += 1
				
				#Upper G
				if pressed[pygame.K_g] and pressed[pygame.K_LSHIFT]:
					screen.blit(l_lG,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						pag[whichLet][1].append(G)
					if subDummy and not supaChek:
						pag[whichLet][2].append(G)
					lilWhichLet += 1

				#Lower h
				if pressed[pygame.K_h] and not pressed[pygame.K_LSHIFT]:
					screen.blit(l_lh,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						pag[whichLet][1].append(h)
					if subDummy and not supaChek:
						pag[whichLet][2].append(h)
					lilWhichLet += 1
				
				#Upper H
				if pressed[pygame.K_h] and pressed[pygame.K_LSHIFT]:
					screen.blit(l_lH,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						pag[whichLet][1].append(H)
					if subDummy and not supaChek:
						pag[whichLet][2].append(H)
					lilWhichLet += 1

				#Lower i
				if pressed[pygame.K_i] and not pressed[pygame.K_LSHIFT]:
					screen.blit(l_li,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						pag[whichLet][1].append(i)
					if subDummy and not supaChek:
						pag[whichLet][2].append(i)
					lilWhichLet += 1
				
				#Upper I
				if pressed[pygame.K_i] and pressed[pygame.K_LSHIFT]:
					screen.blit(l_lI,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						pag[whichLet][1].append(I)
					if subDummy and not supaChek:
						pag[whichLet][2].append(I)
					lilWhichLet += 1

				#Lower j
				if pressed[pygame.K_j] and not pressed[pygame.K_LSHIFT]:
					screen.blit(l_lj,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						pag[whichLet][1].append(j)
					if subDummy and not supaChek:
						pag[whichLet][2].append(j)
					lilWhichLet += 1
				
				#Upper J
				if pressed[pygame.K_j] and pressed[pygame.K_LSHIFT]:
					screen.blit(l_lJ,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						pag[whichLet][1].append(J)
					if subDummy and not supaChek:
						pag[whichLet][2].append(J)
					lilWhichLet += 1

				#Lower k
				if pressed[pygame.K_k] and not pressed[pygame.K_LSHIFT]:
					screen.blit(l_lk,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						pag[whichLet][1].append(k)
					if subDummy and not supaChek:
						pag[whichLet][2].append(k)
					lilWhichLet += 1
				
				#Upper K
				if pressed[pygame.K_k] and pressed[pygame.K_LSHIFT]:
					screen.blit(l_lK,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						pag[whichLet][1].append(K)
					if subDummy and not supaChek:
						pag[whichLet][2].append(K)
					lilWhichLet += 1

				#Lower l
				if pressed[pygame.K_l] and not pressed[pygame.K_LSHIFT]:
					screen.blit(l_ll,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						pag[whichLet][1].append(l)
					if subDummy and not supaChek:
						pag[whichLet][2].append(l)
					lilWhichLet += 1
				
				#Upper L
				if pressed[pygame.K_l] and pressed[pygame.K_LSHIFT]:
					screen.blit(l_lL,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						pag[whichLet][1].append(L)
					if subDummy and not supaChek:
						pag[whichLet][2].append(L)
					lilWhichLet += 1

				#Lower m
				if pressed[pygame.K_m] and not pressed[pygame.K_LSHIFT]:
					screen.blit(l_lm,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						pag[whichLet][1].append(m)
					if subDummy and not supaChek:
						pag[whichLet][2].append(m)
					lilWhichLet += 1
				
				#Upper M
				if pressed[pygame.K_m] and pressed[pygame.K_LSHIFT]:
					screen.blit(l_lM,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						pag[whichLet][1].append(M)
					if subDummy and not supaChek:
						pag[whichLet][2].append(M)
					lilWhichLet += 1

				#Lower n
				if pressed[pygame.K_n] and not pressed[pygame.K_LSHIFT]:
					screen.blit(l_ln,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						pag[whichLet][1].append(n)
					if subDummy and not supaChek:
						pag[whichLet][2].append(n)
					lilWhichLet += 1
				
				#Upper N
				if pressed[pygame.K_n] and pressed[pygame.K_LSHIFT]:
					screen.blit(l_lN,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						pag[whichLet][1].append(N)
					if subDummy and not supaChek:
						pag[whichLet][2].append(N)
					lilWhichLet += 1

				#Lower o
				if pressed[pygame.K_o] and not pressed[pygame.K_LSHIFT]:
					screen.blit(l_lo,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						pag[whichLet][1].append(o)
					if subDummy and not supaChek:
						pag[whichLet][2].append(o)
					lilWhichLet += 1
				
				#Upper O
				if pressed[pygame.K_o] and pressed[pygame.K_LSHIFT]:
					screen.blit(l_lO,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						pag[whichLet][1].append(O)
					if subDummy and not supaChek:
						pag[whichLet][2].append(O)
					lilWhichLet += 1

				#Lower p
				if pressed[pygame.K_p] and not pressed[pygame.K_LSHIFT]:
					screen.blit(l_lp,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						pag[whichLet][1].append(p)
					if subDummy and not supaChek:
						pag[whichLet][2].append(p)
					lilWhichLet += 1
				
				#Upper P
				if pressed[pygame.K_p] and pressed[pygame.K_LSHIFT]:
					screen.blit(l_lP,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						pag[whichLet][1].append(P)
					if subDummy and not supaChek:
						pag[whichLet][2].append(P)
					lilWhichLet += 1

				#Lower q
				if pressed[pygame.K_q] and not pressed[pygame.K_LSHIFT]:
					screen.blit(l_lq,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						pag[whichLet][1].append(q)
					if subDummy and not supaChek:
						pag[whichLet][2].append(q)
					lilWhichLet += 1
				
				#Upper Q
				if pressed[pygame.K_q] and pressed[pygame.K_LSHIFT]:
					screen.blit(l_lQ,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						pag[whichLet][1].append(Q)
					if subDummy and not supaChek:
						pag[whichLet][2].append(Q)
					lilWhichLet += 1

				#Lower r
				if pressed[pygame.K_r] and not pressed[pygame.K_LSHIFT]:
					screen.blit(l_lr,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						pag[whichLet][1].append(r)
					if subDummy and not supaChek:
						pag[whichLet][2].append(r)
					lilWhichLet += 1
				
				#Upper R
				if pressed[pygame.K_r] and pressed[pygame.K_LSHIFT]:
					screen.blit(l_lR,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						pag[whichLet][1].append(R)
					if subDummy and not supaChek:
						pag[whichLet][2].append(R)
					lilWhichLet += 1

				#Lower s
				if pressed[pygame.K_s] and not pressed[pygame.K_LSHIFT]:
					screen.blit(l_ls,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						pag[whichLet][1].append(s)
					if subDummy and not supaChek:
						pag[whichLet][2].append(s)
					lilWhichLet += 1
				
				#Upper S
				if pressed[pygame.K_s] and pressed[pygame.K_LSHIFT]:
					screen.blit(l_lS,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						pag[whichLet][1].append(S)
					if subDummy and not supaChek:
						pag[whichLet][2].append(S)
					lilWhichLet += 1

				#Lower t
				if pressed[pygame.K_t] and not pressed[pygame.K_LSHIFT]:
					screen.blit(l_lt,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						pag[whichLet][1].append(t)
					if subDummy and not supaChek:
						pag[whichLet][2].append(t)
					lilWhichLet += 1
				
				#Upper T
				if pressed[pygame.K_t] and pressed[pygame.K_LSHIFT]:
					screen.blit(l_lT,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						pag[whichLet][1].append(T)
					if subDummy and not supaChek:
						pag[whichLet][2].append(T)
					lilWhichLet += 1

				#Lower u
				if pressed[pygame.K_u] and not pressed[pygame.K_LSHIFT]:
					screen.blit(l_lu,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						pag[whichLet][1].append(u)
					if subDummy and not supaChek:
						pag[whichLet][2].append(u)
					lilWhichLet += 1
				
				#Upper U
				if pressed[pygame.K_u] and pressed[pygame.K_LSHIFT]:
					screen.blit(l_lU,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						pag[whichLet][1].append(U)
					if subDummy and not supaChek:
						pag[whichLet][2].append(U)
					lilWhichLet += 1

				#Lower v
				if pressed[pygame.K_v] and not pressed[pygame.K_LSHIFT]:
					screen.blit(l_lv,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						pag[whichLet][1].append(v)
					if subDummy and not supaChek:
						pag[whichLet][2].append(v)
					lilWhichLet += 1
				
				#Upper V
				if pressed[pygame.K_v] and pressed[pygame.K_LSHIFT]:
					screen.blit(l_lV,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						pag[whichLet][1].append(V)
					if subDummy and not supaChek:
						pag[whichLet][2].append(V)
					lilWhichLet += 1

				#Lower w
				if pressed[pygame.K_w] and not pressed[pygame.K_LSHIFT]:
					screen.blit(l_lw,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						pag[whichLet][1].append(w)
					if subDummy and not supaChek:
						pag[whichLet][2].append(w)
					lilWhichLet += 1
				
				#Upper W
				if pressed[pygame.K_w] and pressed[pygame.K_LSHIFT]:
					screen.blit(l_lW,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						pag[whichLet][1].append(W)
					if subDummy and not supaChek:
						pag[whichLet][2].append(W)
					lilWhichLet += 1

				#Lower x
				if pressed[pygame.K_x] and not pressed[pygame.K_LSHIFT]:
					screen.blit(l_lx,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						pag[whichLet][1].append(x)
					if subDummy and not supaChek:
						pag[whichLet][2].append(x)
					lilWhichLet += 1
				
				#Upper X
				if pressed[pygame.K_x] and pressed[pygame.K_LSHIFT]:
					screen.blit(l_lX,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						pag[whichLet][1].append(X)
					if subDummy and not supaChek:
						pag[whichLet][2].append(X)
					lilWhichLet += 1

				#Lower y
				if pressed[pygame.K_y] and not pressed[pygame.K_LSHIFT]:
					screen.blit(l_ly,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						pag[whichLet][1].append(y)
					if subDummy and not supaChek:
						pag[whichLet][2].append(y)
					lilWhichLet += 1
				
				#Upper Y
				if pressed[pygame.K_y] and pressed[pygame.K_LSHIFT]:
					screen.blit(l_lY,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						pag[whichLet][1].append(Y)
					if subDummy and not supaChek:
						pag[whichLet][2].append(Y)
					lilWhichLet += 1

				#Lower z
				if pressed[pygame.K_z] and not pressed[pygame.K_LSHIFT]:
					screen.blit(l_lz,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						pag[whichLet][1].append(z)
					if subDummy and not supaChek:
						pag[whichLet][2].append(z)
					lilWhichLet += 1
				
				#Upper Z
				if pressed[pygame.K_z] and pressed[pygame.K_LSHIFT]:
					screen.blit(l_lZ,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						pag[whichLet][1].append(Z)
					if subDummy and not supaChek:
						pag[whichLet][2].append(Z)
					lilWhichLet += 1

#---------------------------------Numerals

				#One
				if pressed[pygame.K_1] and not pressed[pygame.K_LSHIFT]:
					screen.blit(l_Non,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						pag[whichLet][1].append(On)
					if subDummy and not supaChek:
						pag[whichLet][2].append(On)
					lilWhichLet += 1
				
				#Two
				if pressed[pygame.K_2] and not pressed[pygame.K_LSHIFT]:
					screen.blit(l_Ntw,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						pag[whichLet][1].append(Tw)
					if subDummy and not supaChek:
						pag[whichLet][2].append(Tw)
					lilWhichLet += 1

				#Three
				if pressed[pygame.K_3] and not pressed[pygame.K_LSHIFT]:
					screen.blit(l_Nth,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						pag[whichLet][1].append(Th)
					if subDummy and not supaChek:
						pag[whichLet][2].append(Th)
					lilWhichLet += 1
				
				#Four
				if pressed[pygame.K_4] and not pressed[pygame.K_LSHIFT]:
					screen.blit(l_Nfo,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						pag[whichLet][1].append(Fo)
					if subDummy and not supaChek:
						pag[whichLet][2].append(Fo)
					lilWhichLet += 1

				#Five
				if pressed[pygame.K_5] and not pressed[pygame.K_LSHIFT]:
					screen.blit(l_Nfi,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						pag[whichLet][1].append(Fi)
					if subDummy and not supaChek:
						pag[whichLet][2].append(Fi)
					lilWhichLet += 1
				
				#Six
				if pressed[pygame.K_6] and not pressed[pygame.K_LSHIFT]:
					screen.blit(l_Nsi,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						pag[whichLet][1].append(Si)
					if subDummy and not supaChek:
						pag[whichLet][2].append(Si)
					lilWhichLet += 1

				#Seven
				if pressed[pygame.K_7] and not pressed[pygame.K_LSHIFT]:
					screen.blit(l_Nse,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						pag[whichLet][1].append(Se)
					if subDummy and not supaChek:
						pag[whichLet][2].append(Se)
					lilWhichLet += 1
				
				#Eight
				if pressed[pygame.K_8] and not pressed[pygame.K_LSHIFT]:
					screen.blit(l_Nei,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						pag[whichLet][1].append(Ei)
					if subDummy and not supaChek:
						pag[whichLet][2].append(Ei)
					lilWhichLet += 1

				#Nine
				if pressed[pygame.K_9] and not pressed[pygame.K_LSHIFT]:
					screen.blit(l_Nni,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						pag[whichLet][1].append(Ni)
					if subDummy and not supaChek:
						pag[whichLet][2].append(Ni)
					lilWhichLet += 1

				#Zero
				if pressed[pygame.K_0] and not pressed[pygame.K_LSHIFT]:
					screen.blit(l_Nze,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						pag[whichLet][1].append(Ze)
					if subDummy and not supaChek:
						pag[whichLet][2].append(Ze)
					lilWhichLet += 1

#-----------------------------------------------------------Space-----------------------------------------------------

				#Space
				if pressed[pygame.K_SPACE]:
					screen.blit(l_S,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					lilWhichLet += 1

#Word Wrap-------------------------------


		if event.type == pygame.KEYUP:

			if event.key == pygame.K_a:
				aChek = False
			if event.key == pygame.K_b:
				bChek = False	
			if event.key == pygame.K_c:
				cChek = False
			if event.key == pygame.K_d:
				dChek = False
			if event.key == pygame.K_e:
				eChek = False
			if event.key == pygame.K_f:
				fChek = False
			if event.key == pygame.K_g:
				gChek = False
			if event.key == pygame.K_h:
				hChek = False
			if event.key == pygame.K_i:
				iChek = False
			if event.key == pygame.K_j:
				jChek = False
			if event.key == pygame.K_k:
				kChek = False
			if event.key == pygame.K_l:
				lChek = False
			if event.key == pygame.K_m:
				mChek = False
			if event.key == pygame.K_n:
				nChek = False
			if event.key == pygame.K_o:
				oChek = False
			if event.key == pygame.K_p:
				pChek = False
			if event.key == pygame.K_q:
				qChek = False
			if event.key == pygame.K_r:
				rChek = False
			if event.key == pygame.K_s:
				sChek = False
			if event.key == pygame.K_t:
				tChek = False
			if event.key == pygame.K_u:
				uChek = False
			if event.key == pygame.K_v:
				vChek = False
			if event.key == pygame.K_w:
				wChek = False
			if event.key == pygame.K_x:
				xChek = False
			if event.key == pygame.K_y:
				yChek = False
			if event.key == pygame.K_z:
				zChek = False
			if event.key == pygame.K_SPACE:
				rSChek = False
#		try:
#			pag[whichLet-1][0]
#			print 'whichLet:', whichLet, 'len(pag):', len(pag), 'pag[whichLet-1][0]:', pag[whichLet-1][0]
#		except:
#			print 'whichLet:', whichLet, 'len(pag):', len(pag), 'pag[whichLet-1][0]:', 'DNE'

	pygame.display.flip()
	clock.tick(60)

pygame.quit()