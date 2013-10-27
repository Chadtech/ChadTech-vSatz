import os
import pygame
import PIL
from PIL import Image

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

doc = []
docLen = 0
docLenDummy = 0

repor = ''

dummyCount = 0

supaChek = False
subDummy = 0

os.chdir('C:\\Users\\NPPSF\\code\\ChadTech\\chars12x16')

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
		return L_lP
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
		return L_lW
	if inp == x:
		return L_lx
	if inp == y:
		return L_ly
	if inp == z:
		return L_lZ

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

	if inp == rSp or inp == dSp:
		return L_S

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

	if inp == mP:
		return L_mP

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




#Load Images

os.chdir('C:\\Users\\NPPSF\\code\\ChadTech\\chars12x16\\Uppercase')

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

os.chdir('C:\\Users\\NPPSF\\code\\ChadTech\\chars12x16\\Lowercase')

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


os.chdir('C:\\Users\\NPPSF\\code\\ChadTech\\chars12x16\\Space')

#space
L_S = pygame.image.load('char0.PNG').convert()

os.chdir('C:\\Users\\NPPSF\\code\\ChadTech\\chars12x16\\ModalLogic')

#Modal Logic
L_mP = pygame.image.load('char0.PNG').convert()
L_mN = pygame.image.load('char1.PNG').convert()

os.chdir('C:\\Users\\NPPSF\\code\\ChadTech\\chars12x16\\FirstOrderLogic')

#First Order Logic
L_fE = pygame.image.load('char0.PNG').convert()
L_fA = pygame.image.load('char1.PNG').convert()
L_fN = pygame.image.load('char2.PNG').convert()
L_fI = pygame.image.load('char3.PNG').convert()
L_fF = pygame.image.load('char4.PNG').convert()
L_fD = pygame.image.load('char5.PNG').convert()

os.chdir('C:\\Users\\NPPSF\\code\\ChadTech\\chars12x16\\Numerals')

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




#4x6 Chars




os.chdir('C:\\Users\\NPPSF\\code\\ChadTech\\chars6x8\\Uppercase')

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

os.chdir('C:\\Users\\NPPSF\\code\\ChadTech\\chars6x8\\Lowercase')

#Capital Letters
l_la = pygame.image.load('char0.PNG').convert()
l_lb = pygame.image.load('char1.PNG').convert()
l_lc = pygame.image.load('char2.PNG').convert()
l_ld = pygame.image.load('char3.PNG').convert()
l_ld = pygame.image.load('char4.PNG').convert()
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

os.chdir('C:\\Users\\NPPSF\\code\\ChadTech\\chars6x8\\Space')

#space
l_S = pygame.image.load('char0.PNG').convert()
l_fS = pygame.image.load('char1.PNG').convert()

screen.fill((0,0,0))

blinker = cursor()
blinker.rect.x = xMarg
blinker.rect.y = yMarg
group.add(blinker)

while quit == False:

	for event in pygame.event.get():

		pressed = pygame.key.get_pressed()

		if event.type == pygame.QUIT:
			print("User asked to quit.")
			quit = True

		if not supaChek and not subDummy:
			blinker.rect.x = ((whichLet%lineLen)*charWidth)+xMarg
			blinker.rect.y = ((whichLet/lineLen)*charHeight)+yMarg
			group.draw(screen)

		if event.type == pygame.KEYDOWN:

			if not supaChek and not subDummy:


	#-----------LETTERS, UPPER CASE AND LOWER CASE--------------

				#Lower a
				if pressed[pygame.K_a] and not pressed[pygame.K_LSHIFT]:
					screen.blit(L_la,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(doc):
						doc.append([a,[],[]])
					else:
						doc.insert(whichLet,[a,[],[]])
						tempSpot = whichLet
						while whichLet < len(doc):
							screen.blit(getLet(doc[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#Upper A
				if pressed[pygame.K_a] and pressed[pygame.K_LSHIFT]:
					screen.blit(L_lA,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(doc):
						doc.append([A,[],[]])
					else:
						doc.insert(whichLet,[A,[],[]])
						tempSpot = whichLet
						while whichLet < len(doc):
							screen.blit(getLet(doc[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#Lower b
				if pressed[pygame.K_b] and not pressed[pygame.K_LSHIFT]:
					screen.blit(L_lb,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(doc):
						doc.append([b,[],[]])
					else:
						doc.insert(whichLet,[b,[],[]])
						tempSpot = whichLet
						while whichLet < len(doc):
							screen.blit(getLet(doc[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#Upper B
				if pressed[pygame.K_b] and pressed[pygame.K_LSHIFT]:
					screen.blit(L_lB,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(doc):
						doc.append([B,[],[]])
					else:
						doc.insert(whichLet,[B,[],[]])
						tempSpot = whichLet
						while whichLet < len(doc):
							screen.blit(getLet(doc[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#Lower C
				if pressed[pygame.K_c] and not pressed[pygame.K_LSHIFT]:
					screen.blit(L_lc,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(doc):
						doc.append([c,[],[]])
					else:
						doc.insert(whichLet,[c,[],[]])
						tempSpot = whichLet
						while whichLet < len(doc):
							screen.blit(getLet(doc[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#Upper C
				if pressed[pygame.K_c] and pressed[pygame.K_LSHIFT]:
					screen.blit(L_lC,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(doc):
						doc.append([C,[],[]])
					else:
						doc.insert(whichLet,[C,[],[]])
						tempSpot = whichLet
						while whichLet < len(doc):
							screen.blit(getLet(doc[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#Lower d
				if pressed[pygame.K_d] and not pressed[pygame.K_LSHIFT]:
					screen.blit(L_ld,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(doc):
						doc.append([d,[],[]])
					else:
						doc.insert(whichLet,[d,[],[]])
						tempSpot = whichLet
						while whichLet < len(doc):
							screen.blit(getLet(doc[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#Upper D
				if pressed[pygame.K_d] and pressed[pygame.K_LSHIFT]:
					screen.blit(L_lD,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(doc):
						doc.append([D,[],[]])
					else:
						doc.insert(whichLet,[D,[],[]])
						tempSpot = whichLet
						while whichLet < len(doc):
							screen.blit(getLet(doc[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#Lower e
				if pressed[pygame.K_e] and not pressed[pygame.K_LSHIFT]:
					screen.blit(L_le,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(doc):
						doc.append([e,[],[]])
					else:
						doc.insert(whichLet,[e,[],[]])
						tempSpot = whichLet
						while whichLet < len(doc):
							screen.blit(getLet(doc[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#Upper E
				if pressed[pygame.K_e] and pressed[pygame.K_LSHIFT]:
					screen.blit(L_lE,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(doc):
						doc.append([E,[],[]])
					else:
						doc.insert(whichLet,[E,[],[]])
						tempSpot = whichLet
						while whichLet < len(doc):
							screen.blit(getLet(doc[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#Lower f
				if pressed[pygame.K_f] and not pressed[pygame.K_LSHIFT]:
					screen.blit(L_lf,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(doc):
						doc.append([f,[],[]])
					else:
						doc.insert(whichLet,[f,[],[]])
						tempSpot = whichLet
						while whichLet < len(doc):
							screen.blit(getLet(doc[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#Upper F
				if pressed[pygame.K_f] and pressed[pygame.K_LSHIFT]:
					screen.blit(L_lF,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(doc):
						doc.append([F,[],[]])
					else:
						doc.insert(whichLet,[F,[],[]])
						tempSpot = whichLet
						while whichLet < len(doc):
							screen.blit(getLet(doc[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

	#-----------------------Space -----------------------------

				if pressed[pygame.K_SPACE]:
					screen.blit(L_S,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(doc):
						doc.append([rSp,[],[]])
					else:
						doc.insert(whichLet,[rSp,[],[]])
						tempSpot = whichLet
						while whichLet < len(doc):
							screen.blit(getLet(doc[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1



	#-----------------------Numbers -----------------------------


				#Numeral 1
				if pressed[pygame.K_1] and not pressed[pygame.K_LSHIFT]:
					screen.blit(L_Non,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(doc):
						doc.append([On,[],[]])
					else:
						doc.insert(whichLet,[On,[],[]])
						tempSpot = whichLet
						while whichLet < len(doc):
							screen.blit(getLet(doc[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#Numeral 2
				if pressed[pygame.K_2] and not pressed[pygame.K_LSHIFT]:
					screen.blit(L_Ntw,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(doc):
						doc.append([Tw,[],[]])
					else:
						doc.insert(whichLet,[Tw,[],[]])
						tempSpot = whichLet
						while whichLet < len(doc):
							screen.blit(getLet(doc[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#Numeral 3
				if pressed[pygame.K_3] and not pressed[pygame.K_LSHIFT]:
					screen.blit(L_Nth,[charWidth*(whichLet%lineLen)+xMarg,charWidth*(whichLet/lineLen)+yMarg])
					if whichLet == len(doc):
						doc.append([Th,[],[]])
					else:
						doc.insert(whichLet,[Th,[],[]])
						tempSpot = whichLet
						while whichLet < len(doc):
							screen.blit(getLet(doc[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#Numeral 4
				if pressed[pygame.K_4] and not pressed[pygame.K_LSHIFT]:
					screen.blit(L_Nfo,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(doc):
						doc.append([Fo,[],[]])
					else:
						doc.insert(whichLet,[Fo,[],[]])
						tempSpot = whichLet
						while whichLet < len(doc):
							screen.blit(getLet(doc[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#Numeral 5
				if pressed[pygame.K_5] and not pressed[pygame.K_LSHIFT]:
					screen.blit(L_Nfi,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(doc):
						doc.append([Fi,[],[]])
					else:
						doc.insert(whichLet,[Fi,[],[]])
						tempSpot = whichLet
						while whichLet < len(doc):
							screen.blit(getLet(doc[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#Numeral 6
				if pressed[pygame.K_6] and not pressed[pygame.K_LSHIFT]:
					screen.blit(L_Nsi,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(doc):
						doc.append([Si,[],[]])
					else:
						doc.insert(whichLet,[Si,[],[]])
						tempSpot = whichLet
						while whichLet < len(doc):
							screen.blit(getLet(doc[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#Numeral 7
				if pressed[pygame.K_7] and not pressed[pygame.K_LSHIFT]:
					screen.blit(L_Nse,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(doc):
						doc.append([Se,[],[]])
					else:
						doc.insert(whichLet,[Se,[],[]])
						tempSpot = whichLet
						while whichLet < len(doc):
							screen.blit(getLet(doc[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#Numeral 8
				if pressed[pygame.K_8] and not pressed[pygame.K_LSHIFT]:
					screen.blit(L_Nei,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(doc):
						doc.append([Ei,[],[]])
					else:
						doc.insert(whichLet,[Ei,[],[]])
						tempSpot = whichLet
						while whichLet < len(doc):
							screen.blit(getLet(doc[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#Numeral 9
				if pressed[pygame.K_9] and not pressed[pygame.K_LSHIFT]:
					screen.blit(L_Nni,[charHeight*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(doc):
						doc.append([Ni,[],[]])
					else:
						doc.insert(whichLet,[Ni,[],[]])
						tempSpot = whichLet
						while whichLet < len(doc):
							screen.blit(getLet(doc[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#Numeral 0
				if pressed[pygame.K_0] and not pressed[pygame.K_LSHIFT]:
					screen.blit(L_Nze,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(doc):
						doc.append([Ze,[],[]])
					else:
						doc.insert(whichLet,[Ze,[],[]])
						tempSpot = whichLet
						while whichLet < len(doc):
							screen.blit(getLet(doc[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1



	#------------------- FIRST ORDER LOGIC ----------------



				# Existential Quantifier
				if pressed[pygame.K_1] and pressed[pygame.K_e]:
					for i in range(3):
						if whichLet != 0: 
							if whichLet == len(doc):
								screen.blit(L_mP,[charWidth*((whichLet-1)%lineLen)+xMarg,charHeight*((whichLet-1)/lineLen)+yMarg])
								doc.pop(whichLet-1)
								whichLet -= 1
								screen.blit((L_S),[charWidth*(len(doc)%lineLen)+(xMarg+charWidth),charHeight*(len(doc)/lineLen)+yMarg])
							else:
								doc.pop(whichLet-1)
								whichLet -= 1
								tempSpot = whichLet
								while whichLet < len(doc):
									screen.blit(getLet(doc[whichLet]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
									whichLet += 1
								whichLet = tempSpot
								screen.blit((L_S),[charWidth*(len(doc)%lineLen)+xMarg,charHeight*(len(doc)/lineLen)+yMarg])
					screen.blit(L_fE,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(doc):
						doc.append([mP,[],[]])
					else:
						doc.insert(whichLet,[mP,[],[]])
						tempSpot = whichLet
						while whichLet < len(doc):
							screen.blit(getLet(doc[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#For all
				if pressed[pygame.K_1] and pressed[pygame.K_a]:
					for i in range(3):
						if whichLet != 0: 
							if whichLet == len(doc):
								screen.blit(L_S,[charWidth*((whichLet-1)%lineLen)+xMarg,charHeight*((whichLet-1)/lineLen)+yMarg])
								doc.pop(whichLet-1)
								whichLet -= 1
								screen.blit((L_S),[charWidth*(len(doc)%lineLen)+(xMarg+charWidth),charHeight*(len(doc)/lineLen)+yMarg])
							else:
								doc.pop(whichLet-1)
								whichLet -= 1
								tempSpot = whichLet
								while whichLet < len(doc):
									screen.blit(getLet(doc[whichLet]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
									whichLet += 1
								whichLet = tempSpot
								screen.blit((L_S),[charWidth*(len(doc)%lineLen)+xMarg,charHeight*(len(doc)/lineLen)+yMarg])
					screen.blit(L_fA,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(doc):
						doc.append([Fa,[],[]])
					else:
						doc.insert(whichLet,[Fa,[],[]])
						tempSpot = whichLet
						while whichLet < len(doc):
							screen.blit(getLet(doc[whichLet]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#Negation
				if pressed[pygame.K_1] and pressed[pygame.K_n]:
					for i in range(2):
						if whichLet != 0: 
							if whichLet == len(doc):
								screen.blit(L_S,[charWidth*((whichLet-1)%lineLen)+xMarg,charHeight*((whichLet-1)/lineLen)+yMarg])
								doc.pop(whichLet-1)
								whichLet -= 1
								screen.blit((L_S),[charWidth*(len(doc)%lineLen)+(xMarg+charWidth),charHeight*(len(doc)/lineLen)+yMarg])
							else:
								doc.pop(whichLet-1)
								whichLet -= 1
								tempSpot = whichLet
								while whichLet < len(doc):
									screen.blit(getLet(doc[whichLet]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
									whichLet += 1
								whichLet = tempSpot
								screen.blit((L_S),[charWidth*(len(doc)%lineLen)+xMarg,charHeight*(len(doc)/lineLen)+yMarg])
					screen.blit(L_fN,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(doc):
						doc.append(Ne)
					else:
						doc.insert(whichLet,Ne)
						tempSpot = whichLet
						while whichLet < len(doc):
							screen.blit(getLet(doc[whichLet]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#Implies
				if pressed[pygame.K_1] and pressed[pygame.K_i]:
					for i in range(2):
						if whichLet != 0: 
							if whichLet == len(doc):
								screen.blit(L_S,[charWidth*((whichLet-1)%lineLen)+xMarg,charHeight*((whichLet-1)/lineLen)+yMarg])
								doc.pop(whichLet-1)
								whichLet -= 1
								screen.blit((L_S),[charWidth*(len(doc)%lineLen)+(xMarg+charWidth),charHeight*(len(doc)/lineLen)+yMarg])
							else:
								doc.pop(whichLet-1)
								whichLet -= 1
								tempSpot = whichLet
								while whichLet < len(doc):
									screen.blit(getLet(doc[whichLet]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
									whichLet += 1
								whichLet = tempSpot
								screen.blit((L_S),[charWidth*(len(doc)%lineLen)+xMarg,charHeight*(len(doc)/lineLen)+yMarg])
					screen.blit(L_fI,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(doc):
						doc.append(Im)
					else:
						doc.insert(whichLet,Im)
						tempSpot = whichLet
						while whichLet < len(doc):
							screen.blit(getLet(doc[whichLet]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#If and only if
				if pressed[pygame.K_1] and pressed[pygame.K_f]:
					for i in range(2):
						if whichLet != 0: 
							if whichLet == len(doc):
								screen.blit(L_S,[charWidth*((whichLet-1)%lineLen)+xMarg,charHeight*((whichLet-1)/lineLen)+yMarg])
								doc.pop(whichLet-1)
								whichLet -= 1
								screen.blit((L_S),[charWidth*(len(doc)%lineLen)+(xMarg+charWidth),charHeight*(len(doc)/lineLen)+yMarg])
							else:
								doc.pop(whichLet-1)
								whichLet -= 1
								tempSpot = whichLet
								while whichLet < len(doc):
									screen.blit(getLet(doc[whichLet]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
									whichLet += 1
								whichLet = tempSpot
								screen.blit((L_S),[charWidth*(len(doc)%lineLen)+xMarg,charHeight*(len(doc)/lineLen)+yMarg])
					screen.blit(L_fF,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(doc):
						doc.append(Ff)
					else:
						doc.insert(whichLet,Ff)
						tempSpot = whichLet
						while whichLet < len(doc):
							screen.blit(getLet(doc[whichLet]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1

				#And
				if pressed[pygame.K_1] and pressed[pygame.K_d]:
					for i in range(3):
						if whichLet != 0: 
							if whichLet == len(doc):
								screen.blit(L_S,[charWidth*((whichLet-1)%lineLen)+xMarg,charHeight*((whichLet-1)/lineLen)+yMarg])
								doc.pop(whichLet-1)
								whichLet -= 1
								screen.blit((L_S),[charWidth*(len(doc)%lineLen)+(xMarg+charWidth),charHeight*(len(doc)/lineLen)+yMarg])
							else:
								doc.pop(whichLet-1)
								whichLet -= 1
								tempSpot = whichLet
								while whichLet < len(doc):
									screen.blit(getLet(doc[whichLet]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
									whichLet += 1
								whichLet = tempSpot
								screen.blit((L_S),[charWidth*(len(doc)%lineLen)+xMarg,charHeight*(len(doc)/lineLen)+yMarg])
					screen.blit(L_fD,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet == len(doc):
						doc.append(Nd)
					else:
						doc.insert(whichLet,Nd)
						tempSpot = whichLet
						while whichLet < len(doc):
							screen.blit(getLet(doc[whichLet]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1
						whichLet = tempSpot
					whichLet += 1



	#----------------------COMMANDS (enter, backspace, etc)--------------------



				if pressed[pygame.K_LSHIFT] and pressed[pygame.K_EQUALS]:
					supaChek = True
					whichLet -= 1

				if pressed[pygame.K_LSHIFT] and pressed[pygame.K_MINUS]:
					subDummy = 1
					whichLet -= 1

				if pressed[pygame.K_LCTRL] and pressed [pygame.K_s]:
					if whichLet == len(doc):
						screen.blit(L_S,[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
					else:
						screen.blit(getLet(doc[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])	
					os.chdir('C:\\Users\\NPPSF\\code\\ChadTech')
					pygame.image.save(screen,"doc.PNG")
					saveIm = Image.open('doc.PNG')
					docLen = len(doc)
					docLenDummy = docLen
					Xboun, Yboun = 0,0
					Xboun, Yboun = saveIm.size
					supaSaveCou = 0
					subSaveCou = 0
					yuss, tack, dukh = 0,0,0
					print docLenDummy
					while docLenDummy > 65536:
						yuss += 1
						docLenDummy -= 65536
					while docLenDummy > 256:
						tack += 1
						docLenDummy -= 256
					while docLenDummy > 0:
						dukh += 1
						docLenDummy -= 1
					print dukh
					saveIm.putpixel((Xboun-1,0), (yuss, tack, dukh))
					yuss, tack, dukh = 0,0,0
					for yit in range(len(doc)):
						if yit%3 == 0:
							yuss, tack, dukh = 0,0,0
							if yit+2 < len(doc):
								dukh = doc[yit+2][0]
							if yit+1 < len(doc):
								tack = doc[yit+1][0]
							if yit < len(doc):
								yuss = doc[yit][0]
							saveIm.putpixel((docLenDummy%(xMarg),docLenDummy/xMarg), (yuss, tack, dukh))
							docLenDummy += 1
						if len(doc[yit][1]) > 0:
							print len(doc[yit][1])
							saveIm.putpixel(((supaSaveCou%xMarg)+xMarg,supaSaveCou/xMarg), (yit, len(doc[yit][1]), 255))
							yuss, tack, dukh = 0,0,0
							supaSaveCou += 1
							for vapp in range(len(doc[yit][1])):
								if vapp%3 == 0:
									if vapp+2 < len(doc[yit][1]):
										dukh = doc[yit][1][vapp+2]
									if vapp+1 < len(doc[yit][1]):
										tack = doc[yit][1][vapp+1]
									if vapp < len(doc[yit][1]):
										yuss = doc[yit][1][vapp]
									saveIm.putpixel(((supaSaveCou%xMarg)+xMarg,supaSaveCou/xMarg), (yuss, tack, dukh))
									supaSaveCou += 1
						if len(doc[yit][2]) > 0:
							saveIm.putpixel(((subSaveCou%xMarg)+(2*xMarg),subSaveCou/xMarg), (yit, len(doc[yit][2]), 254))
							yuss, tack, dukh = 0,0,0
							subSaveCou += 1
							for vapp in range(len(doc[yit][2])):
								if vapp%3 == 0:
									if vapp+2 < len(doc[yit][2]):
										dukh = doc[yit][2][vapp+2]
									if vapp+1 < len(doc[yit][2]):
										tack = doc[yit][2][vapp+1]
									if vapp < len(doc[yit][2]):
										yuss = doc[yit][2][vapp]
									saveIm.putpixel(((subSaveCou%xMarg)+(2*xMarg),subSaveCou/xMarg), (yuss, tack, dukh))
									subSaveCou += 1
					docLenDummy = 0
					saveIm.save('doc.PNG',"png")

				if pressed[pygame.K_LCTRL] and pressed[pygame.K_o]:
					doc = []
					os.chdir('C:\\Users\\NPPSF\\code\\ChadTech')
					openIm =  Image.open('doc.PNG')
					Xboun, Yboun = 0,0
					Xboun, Yboun = openIm.size
					stei, ohre, heed = 0,0,0
					stei, ohre, heed = openIm.getpixel((Xboun-1,0))
					docLenDummy = 0
					docLenDummy += 65536*stei
					docLenDummy += 256*ohre
					docLenDummy += heed
					print docLenDummy
					bink, yat, duss = 0,0,0
					nyih = [bink,yat,duss]
					vfre, klut, prun = 0,0,0
					xBoun = 0
					yBoun = 0
					for yit in range(docLenDummy):
						if yit%3 == 0:
							xYit = xBoun%(xMarg)
							yYit = yBoun/(xMarg)
							bink, yat, duss = openIm.getpixel((xYit,yYit))
							nyih = [bink,yat,duss]
							doc.append([nyih[0],[],[]])
							if yit+1 < docLenDummy:
								doc.append([nyih[1],[],[]])
							if yit+2 < docLenDummy:
								doc.append([nyih[2],[],[]])
							xBoun += 1
							yBoun += 1
					bink, yat, duss = 0,0,0
					xBoun = 0
					yBoun = 0
					for yit in range(docLenDummy):
						bink, yat, duss = openIm.getpixel(((yit%xMarg)+xMarg,yit/(xMarg*2)))
						if duss == 255:
							for vapp in range(yat):
								if vapp%3 == 0:
									vfre, klut, prun = openIm.getpixel((((yit+(vapp+1))%xMarg)+xMarg,(yit+vapp)/xMarg))
									doc[bink][1].append(vfre)
									if vapp + 1 < yat:
										doc[bink][1].append(klut)
									if vapp + 2 < yat:
										doc[bink][1].append(prun)
						if duss == 254:
							for vapp in range(yat):
								if vapp%3 == 0:
									vfre, klut, prun = openIm.getpixel((((yit+(vapp+1))%xMarg)+xMarg,(yit+vapp)/xMarg))
									doc[bink][1].append(vfre)
									if vapp + 1 < yat:
										doc[bink][2].append(klut)
									if vapp + 2 < yat:
										doc[bink][2].append(prun)
					screen.fill((0,0,0))
					whichLet = 0
					lilWhichLet = 0
					while whichLet < len(doc):
						screen.blit(getLet(doc[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
						if len(doc[whichLet][1]) > 0:
							basePlaceX = charWidth*(whichLet%lineLen)+xMarg
							basePlaceY = charHeight*(whichLet/lineLen)+yMarg
							for toh in range(len(doc[whichLet][1])):
								print 'whichLet 1 toh,', doc[whichLet][1][toh], 'toh,', toh, 'len doc whichLet 1 toh,', len(doc[whichLet][1]), 'The Doc:', doc[whichLet][1]
								screen.blit(getLetl(doc[whichLet][1][toh]),[(basePlaceX+lilCharXOffset)+(toh*lilCharWidth),(basePlaceY+lilCharYOffset)])
						if len(doc[whichLet][2]) > 0:
							basePlaceX = charWidth*(whichLet%lineLen)+xMarg
							basePlaceY = charHeight*(whichLet/lineLen)+yMarg
							for toh in range(len(doc[whichLet][2])):
								screen.blit(getLetl(doc[whichLet][2][toh]),[(basePlaceX+lilCharXOffset)+(toh*lilCharWidth),(basePlaceY+lilCharYOffset+lilCharSubBuf)])
						whichLet += 1

				if pressed[pygame.K_r] and pressed[pygame.K_h]:
					print len(doc), whichLet, doc

				if pressed[pygame.K_UP] and not pressed[pygame.K_LSHIFT]:
					if whichLet != len(doc):
						screen.blit(getLet(doc[whichLet][0]),[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					else:
						screen.blit(L_S,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
					if whichLet > lineLen:
						whichLet -= lineLen

				if pressed[pygame.K_UP] and pressed[pygame.K_LSHIFT]:
					for ipp in range(5):
						if whichLet != len(doc):
							screen.blit(getLet(doc[whichLet][0]),[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
						else:
							screen.blit(L_S,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
						if whichLet > lineLen:
							whichLet -= lineLen

				if pressed[pygame.K_RIGHT] and not pressed[pygame.K_LSHIFT]:
					if whichLet < len(doc):
						screen.blit(getLet(doc[whichLet][0]),[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
						whichLet += 1

				if pressed[pygame.K_RIGHT] and pressed[pygame.K_LSHIFT]:
					for ipp in range(10):
						if whichLet < len(doc):
							screen.blit(getLet(doc[whichLet][0]),[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
							whichLet += 1

				if pressed[pygame.K_LEFT] and not pressed[pygame.K_LSHIFT]:
					if whichLet:
						if whichLet < len(doc):
							screen.blit(getLet(doc[whichLet][0]),[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
						else:
							screen.blit(L_S,[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
						whichLet -= 1

				if pressed[pygame.K_LEFT] and pressed[pygame.K_LSHIFT]:
					for ipp in range(10):
						if whichLet:
							if whichLet < len(doc):
								screen.blit(getLet(doc[whichLet][0]),[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
							else:
								screen.blit(L_S,[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet -= 1

				if pressed[pygame.K_DOWN] and not pressed[pygame.K_LSHIFT]:
					if len(doc) != 0:
						if whichLet != len(doc):
							screen.blit(getLet(doc[whichLet][0]),[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
						if (whichLet+lineLen) < len(doc):
							whichLet += lineLen
						elif (len(doc)%lineLen) <= (whichLet%lineLen):
							whichLet = len(doc)

				if pressed[pygame.K_DOWN] and pressed[pygame.K_LSHIFT]:
					for ipp in range(5):
						if len(doc) != 0:
							if whichLet != len(doc):
								screen.blit(getLet(doc[whichLet][0]),[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
							if (whichLet+lineLen) < len(doc):
								whichLet += lineLen
							elif (len(doc)%lineLen) <= (whichLet%lineLen):
								whichLet = len(doc)

				if pressed[pygame.K_BACKSPACE]:
					if whichLet != 0:
						dummyCount = 0
						tempSpot = whichLet
						while doc[whichLet-1] == dSp:
								dummyCount += 1
								whichLet -= 1
						whichLet = tempSpot
						if dummyCount == 0:
							dummyCount = 1
						if dummyCount > lineLen:
							dummyCount = lineLen 
						for ipp in range(dummyCount):
							if whichLet == len(doc):
								if whichLet%lineLen == 0:
									screen.blit((L_S),[xMarg,charHeight*(len(doc)/lineLen)+(yMarg)])
								screen.blit(L_S,[charWidth*((whichLet-1)%lineLen)+xMarg,charHeight*((whichLet-1)/lineLen)+yMarg])
								if len(doc[whichLet-1][1]) > 0:
									basePlaceX = charWidth*((whichLet-1)%lineLen)+xMarg
									basePlaceY = charHeight*((whichLet-1)/lineLen)+yMarg
									for ipp in range(len(doc[whichLet-1][1])):
										screen.blit(l_S,[(basePlaceX+lilCharXOffset)+(ipp*lilCharWidth),(basePlaceY+lilCharYOffset)])
								if len(doc[whichLet-1][2]) > 0:
									basePlaceX = charWidth*((whichLet-1)%lineLen)+xMarg
									basePlaceY = charHeight*((whichLet-1)/lineLen)+yMarg
									for yit in range(len(doc[whichLet-1][2])):
										screen.blit(l_S,[(basePlaceX+lilCharXOffset)+(yit*lilCharWidth),(basePlaceY+lilCharYOffset+lilCharSubBuf)])
								doc.pop(whichLet-1)
								whichLet -= 1
								screen.blit((L_S),[charWidth*(len(doc)%lineLen)+(xMarg+charWidth),charHeight*(len(doc)/lineLen)+yMarg])
							else:
								doc.pop(whichLet-1)
								whichLet -= 1
								tempSpot = whichLet
								while whichLet < len(doc):
									screen.blit(getLet(doc[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
									if len(doc[whichLet][1]) > 0:
										basePlaceX = charWidth*(whichLet%lineLen)+xMarg
										basePlaceY = charHeight*(whichLet/lineLen)+yMarg
										for ipp in range(len(doc[whichLet][1])):
											screen.blit(getLetl(doc[whichLet][1][ipp]),[(basePlaceX+lilCharXOffset)+(ipp*lilCharWidth),(basePlaceY+lilCharYOffset)])
										for vap in range(3):
											screen.blit(l_S,[(basePlaceX+lilCharXOffset)+((len(doc[whichLet][1])+vap)*lilCharWidth),(basePlaceY+lilCharYOffset)])
									if len(doc[whichLet][2]) > 0:
										basePlaceX = charWidth*(whichLet%lineLen)+xMarg
										basePlaceY = charHeight*(whichLet/lineLen)+yMarg
										for yit in range(len(doc[whichLet][2])):
											screen.blit(getLetl(doc[whichLet][2][yit]),[(basePlaceX+lilCharXOffset)+(yit*lilCharWidth),(basePlaceY+lilCharYOffset+lilCharSubBuf)])
										for nen in range(3):
											screen.blit(l_S,[(basePlaceX+lilCharXOffset)+((len(doc[whichLet][2])+nen)*lilCharWidth),(basePlaceY+lilCharYOffset+lilCharSubBuf)])
									whichLet += 1
								whichLet = tempSpot
								screen.blit((L_S),[charWidth*(len(doc)%lineLen)+xMarg,charHeight*(len(doc)/lineLen)+yMarg])

				if pressed[pygame.K_BACKSPACE] and pressed[pygame.K_LSHIFT]:
					for hob in range(10):
						if whichLet != 0:
							dummyCount = 0
							tempSpot = whichLet
							while doc[whichLet-1] == dSp:
									dummyCount += 1
									whichLet -= 1
							whichLet = tempSpot
							if dummyCount == 0:
								dummyCount = 1
							if dummyCount > lineLen:
								dummyCount = lineLen 
							for ipp in range(dummyCount):
								if whichLet == len(doc):
									if whichLet%lineLen == 0:
										screen.blit((L_S),[xMarg,charHeight*(len(doc)/lineLen)+(yMarg)])
									screen.blit(L_S,[charWidth*((whichLet-1)%lineLen)+xMarg,charHeight*((whichLet-1)/lineLen)+yMarg])
									if len(doc[whichLet-1][1]) > 0:
										basePlaceX = charWidth*((whichLet-1)%lineLen)+xMarg
										basePlaceY = charHeight*((whichLet-1)/lineLen)+yMarg
										for ipp in range(len(doc[whichLet-1][1])):
											screen.blit(l_S,[(basePlaceX+lilCharXOffset)+(ipp*lilCharWidth),(basePlaceY+lilCharYOffset)])
									if len(doc[whichLet-1][2]) > 0:
										basePlaceX = charWidth*((whichLet-1)%lineLen)+xMarg
										basePlaceY = charHeight*((whichLet-1)/lineLen)+yMarg
										for yit in range(len(doc[whichLet-1][2])):
											screen.blit(l_S,[(basePlaceX+lilCharXOffset)+(yit*lilCharWidth),(basePlaceY+lilCharYOffset+lilCharSubBuf)])
									doc.pop(whichLet-1)
									whichLet -= 1
									screen.blit((L_S),[charWidth*(len(doc)%lineLen)+(xMarg+charWidth),charHeight*(len(doc)/lineLen)+yMarg])
								else:
									doc.pop(whichLet-1)
									whichLet -= 1
									tempSpot = whichLet
									while whichLet < len(doc):
										screen.blit(getLet(doc[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
										if len(doc[whichLet][1]) > 0:
											basePlaceX = charWidth*(whichLet%lineLen)+xMarg
											basePlaceY = charHeight*(whichLet/lineLen)+yMarg
											for ipp in range(len(doc[whichLet][1])):
												screen.blit(getLetl(doc[whichLet][1][ipp]),[(basePlaceX+lilCharXOffset)+(ipp*lilCharWidth),(basePlaceY+lilCharYOffset)])
											for vap in range(3):
												screen.blit(l_S,[(basePlaceX+lilCharXOffset)+((len(doc[whichLet][1])+vap)*lilCharWidth),(basePlaceY+lilCharYOffset)])
										if len(doc[whichLet][2]) > 0:
											basePlaceX = charWidth*(whichLet%lineLen)+xMarg
											basePlaceY = charHeight*(whichLet/lineLen)+yMarg
											for yit in range(len(doc[whichLet][2])):
												screen.blit(getLetl(doc[whichLet][2][yit]),[(basePlaceX+lilCharXOffset)+(yit*lilCharWidth),(basePlaceY+lilCharYOffset+lilCharSubBuf)])
											for nen in range(3):
												screen.blit(l_S,[(basePlaceX+lilCharXOffset)+((len(doc[whichLet][2])+nen)*lilCharWidth),(basePlaceY+lilCharYOffset+lilCharSubBuf)])
										whichLet += 1
									whichLet = tempSpot
									screen.blit((L_S),[charWidth*(len(doc)%lineLen)+xMarg,charHeight*(len(doc)/lineLen)+yMarg])




				if pressed[pygame.K_RETURN]:
					if whichLet == len(doc):
						for ipp in range(lineLen-(whichLet%lineLen)):
							screen.blit(L_S,[charWidth*(whichLet%lineLen)+xMarg,charHeight*(whichLet/lineLen)+yMarg])
							doc.append([dSp,[],[]])
							whichLet += 1
					else:
						tempSpot = whichLet
						for ipp in range(lineLen-(whichLet%lineLen)):
							doc.insert(whichLet,[dSp,[],[]])
							whichLet += 1
						whichLet = tempSpot
						while whichLet < len(doc):
							screen.blit(getLet(doc[whichLet]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])
							whichLet += 1


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

				#Lower a
				if pressed[pygame.K_a] and not pressed[pygame.K_LSHIFT]:
					screen.blit(l_la,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						doc[whichLet][1].append(a)
					if subDummy and not supaChek:
						doc[whichLet][2].append(a)
					lilWhichLet += 1
				
				#Upper A
				if pressed[pygame.K_a] and pressed[pygame.K_LSHIFT]:
					screen.blit(l_lA,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						doc[whichLet][1].append(A)
					if subDummy and not supaChek:
						doc[whichLet][2].append(A)
					lilWhichLet += 1

				#Lower b
				if pressed[pygame.K_b] and not pressed[pygame.K_LSHIFT]:
					screen.blit(l_lb,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						doc[whichLet][1].append(b)
					if subDummy and not supaChek:
						doc[whichLet][2].append(b)
					lilWhichLet += 1
				
				#Upper B
				if pressed[pygame.K_b] and pressed[pygame.K_LSHIFT]:
					screen.blit(l_lB,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					if supaChek and not subDummy:
						doc[whichLet][1].append(B)
					if subDummy and not supaChek:
						doc[whichLet][2].append(B)
					lilWhichLet += 1

				#Space
				if pressed[pygame.K_SPACE]:
					screen.blit(l_S,[(basePlaceX+lilCharXOffset)+(lilWhichLet*lilCharWidth),(basePlaceY+lilCharYOffset)+(subDummy*lilCharSubBuf)])
					lilWhichLet += 1

#		repor = ''
#		for ipp in range(len(doc)):
#			repor += str(doc[ipp])
#		print whichLet, len(doc), subDummy, supaChek, lilWhichLet, repor

	pygame.display.flip()
	clock.tick(20)

pygame.quit()
