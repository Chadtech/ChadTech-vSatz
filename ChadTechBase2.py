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

#set Theory
L_pSt = pygame.image.load('char0.PNG').convert()
L_pNs = pygame.image.load('char1.PNG').convert()
L_pDt = pygame.image.load('char2.PNG').convert()
L_pNd = pygame.image.load('char3.PNG').convert()
L_pLc = pygame.image.load('char4.PNG').convert()

os.chdir(os.path.dirname(os.getcwd()))
os.chdir(os.path.abspath('Cursor'))

#set Theory
L_C = pygame.image.load('char0.PNG').convert()


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

whichLet = 0
tempSpot = whichLet

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
#def defglobals():
#	global curChar 
curChar=0
linCou=0
charCou=0
howManyLefts=0
letCor = {
	
	'BACKSPACE':8,
	'TAB':9,
	'ENTER':13,

	'SPACE':32,

	'SINGLEQUOTE':39,

	'COMMA':44,
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

	'EQUALS':61,

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
	'DARROW':274,
	'RIGHTARROW':275,
	'LEFTARROW':276,

	'RIGHTSHIFT':303,
	'LEFTSHIFT':304,
	'RIGHTCONTROL':305,
	'LEFTCONTROL':306
}

class Char:
	def __init__(self,width,image,keys,isThisCursor):
		self.width=width
		self.image=image
		self.keys=keys #The keys variable, refers to a tuple, who elements are sets, containing valid key combinations to produce that character. The elements of the set are elements of the dictionary
		self.isThisCursor=isThisCursor

class Vort:
	def __init__(self):
		self.charen=[]
	def vortLen(self):
		vortLen = 0
		for yit in range(len(charen)):
			vortLen+=charen[yit].width
		return vortLen

#Invisible Chars

empty=Char(0,l_fS,(set([ letCor['l'], letCor['w'] ]) ),False)
enter=Char(0,l_fS,( set([ letCor['ENTER'] ]) ),False)
wordwrap=Char(0,l_fS,(set([ letCor['l'], letCor['w'] ]) ),False)
backspace=Char(0,l_fS,(set ([ letCor['BACKSPACE'] ]) ),False)

rightarrow=Char(0,l_fS,(set ([ letCor['RIGHTARROW'] ]) ),False)
leftarrow=Char(0,l_fS,(set ([ letCor['LEFTARROW'] ]) ),False)

############Visible Chars

#Space
space=Char(1,L_S,( set([ letCor['SPACE'] ]) ),False)

#Lower Case Chars 
lowercase__a=Char(1,L_la,( set([ letCor['a'] ]) ),False)
lowercase__b=Char(1,L_lb,( set([ letCor['b'] ]) ),False)

#Upper Case Chars
uppercase__A=Char(1,L_lA,( set([ letCor['a'], letCor['LEFTSHIFT'] ]), set([ letCor['a'], letCor['RIGHTSHIFT'] ]) ),False)
uppercase__B=Char(1,L_lB,( set([ letCor['b'], letCor['LEFTSHIFT'] ]), set([ letCor['b'], letCor['RIGHTSHIFT'] ]) ),False)


class Doc:
	def __init__(self):
		self.vorten=[]
	#def addLin():
	#	self.linen.append(Lin())
	#def getlinCou():
	#	return len(linen)

ourDoc= Doc()
ourDoc.vorten.append(Vort())

keys = set([])
quit=False
while quit==False:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			howManyChars=0
			keys.add(event.key)

			whichChar=lowercase__a
			for yit in range(len(whichChar.keys)):
				if keys == whichChar.keys:
					ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
					curChar+=1

			whichChar=lowercase__b
			for yit in range(len(whichChar.keys)):
				if keys == whichChar.keys:
					ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
					curChar+=1

			whichChar=uppercase__A
			for yit in range(len(whichChar.keys)):
				if keys == whichChar.keys:
					ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
					curChar+=1

			whichChar=uppercase__B
			for yit in range(len(whichChar.keys)):
				if keys == whichChar.keys:
					ourDoc.vorten[curVort].charen.insert(curChar,whichChar)
					curChar+=1

			if keys == space.keys:
				ourDoc.vorten[curVort].charen.insert(curChar,space)
				curVort+=1
				ourDoc.vorten.insert(curVort,Vort())
				curChar=0

 			if keys==enter.keys:
				ourDoc.vorten.insert(curVort+1,Vort())
				curVort+=1
				curChar=0
				ourDoc.vorten[curVort].charen.insert(curChar,enter)
				ourDoc.vorten.insert(curVort+1,Vort())
				curVort+=1

			if keys==backspace.keys:
				if curChar!=0 or curVort!=0:
					while len(ourDoc.vorten[curVort].charen)==0:
						ourDoc.vorten.pop(curVort)
						curVort-=1
						curChar=len(ourDoc.vorten[curVort].charen)
					ourDoc.vorten[curVort].charen.pop(curChar-1)
					curChar-=1

			if keys==leftarrow.keys:
				if curChar!=0:
					curChar-=1
				else:
					if curVort!=0:
						curVort-=1
						curChar=len(ourDoc.vorten[curVort])

			if keys==rightarrow.keys:
				if curChar==len(ourDoc.vorten[curVort]):
					if curVort!=len(ourDoc.vorten):
						curVort+=1
						curChar=0
				else:
					curChar+=1

		###############################This section breaks the list of words, into a list of lines containing the words
		blitScreen = []
		thisLin = 0
		blitScreen.append( [0,[]] )
		for yit in range(len(ourDoc.vorten)):
			if ourDoc.vorten[yit].charen==[enter]:
				blitScreen.append( [0,[]] )
				thisLin+=1
			else:
				#print 'this Lins Len', blitScreen[thisLin][0], 'this Vort Len', len(ourDoc.vorten[yit].charen), 'lineLen', lineLen
				if blitScreen[thisLin][0]+len(ourDoc.vorten[yit].charen)<=lineLen:
					blitScreen[thisLin][1].append(ourDoc.vorten[yit])
					#print blitScreen[thisLin][0], ',', len(ourDoc.vorten[yit].charen)
					blitScreen[thisLin][0]+=len(ourDoc.vorten[yit].charen)
				else:
					blitScreen.append( [0,[]] )
					thisLin+=1
					print len(ourDoc.vorten[yit].charen)
					blitScreen[thisLin][0]=len(ourDoc.vorten[yit].charen)
					blitScreen[thisLin][1].append(ourDoc.vorten[yit])

	 	############################This section takes the words in each line, and breaks them down into a list of characters to paste onto the screen
		blitChars=[]
		for yit in range(len(blitScreen)):
			blitChars.append([])
			for vapp in range(len(blitScreen[yit][1])):
				for gno in range(len(blitScreen[yit][1][vapp].charen)):
					#if blitScreen[yit][1][vapp].charen[gno].width:
					blitChars[yit].append(blitScreen[yit][1][vapp].charen[gno])
			#for vapp in range(len(blitChars[yit])):
				#screen.blit(blitChars[yit][vapp].image,[(vapp*charWidth)+xMarg,(yit*(charHeight+lineGap))+yMarg])
			for vapp in range(lineLen):
				#print 'VAPP,',vapp,'len(blitChars[yit]),',len(blitChars[yit]), 'vapp<=len(blitChars[yit]),',vapp<=len(blitChars[yit])
				if vapp<len(blitChars[yit]):
					screen.blit(blitChars[yit][vapp].image,[(vapp*charWidth)+xMarg,(yit*(charHeight+lineGap))+yMarg])
					if blitChars[yit][vapp].isThisCursor==True:
						screen.blit(blitChars[yit][vapp].image,[(vapp*charWidth)+xMarg,(yit*(charHeight+lineGap))+yMarg+charHeight-2])
				else:
					screen.blit(L_C,[(vapp*charWidth)+xMarg,(yit*(charHeight+lineGap))+yMarg])
					if blitChars[yit][vapp].isThisCursor==True:
						screen.blit(blitChars[yit][vapp].image,[(vapp*charWidth)+xMarg,(yit*(charHeight+lineGap))+yMarg+charHeight-2])

		##########################This section pastes our cursor
		
		#howManyChars+=len(blitChars[len(blitChars)-1])+((len(blitChars)-1)*lineLen)
		#screen.blit(L_C,[((howManyChars%lineLen)*charWidth)+xMarg,((howManyChars/lineLen)*(charHeight+lineGap))+yMarg+charHeight-2])
		
		if event.type == pygame.KEYUP:
			keys = set([])
		if event.type == pygame.QUIT:
			quit = True
		#if event.type == pygame.KEY

	pygame.display.flip()
	clock.tick(60)

pygame.quit()

#screen.blit(getLet(pag[whichLet][0]),[charWidth*((whichLet)%lineLen)+xMarg,charHeight*((whichLet)/lineLen)+yMarg])

#screen.blit(image,[x,y])