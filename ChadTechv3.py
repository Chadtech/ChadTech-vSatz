import os
import pygame
import PIL
from PIL import Image
import Tkinter, tkFileDialog
brunk = Tkinter.Tk()
brunk.withdraw()

#### Beginning Screen resolution
screenWidth=1366
screenHeight=724

##### In the codee screen acts as a canvas for our characters
##### But screen as its defined, it just the window
screen = pygame.display.set_mode((1000,500),pygame.RESIZABLE)

#### The number of pixels between lines.
#### If you dont want any super scrpits
#### a line gap of 0 works great
#### if you want to garauntee that all
#### superscripts and subscripts
#### will be displayed properly
#### a line gap of 16 suffices
####
#### ChadTech asks the user what linegap
#### They want, so '1' is just a place
#### holder
####
#### Its necessary that it is defined
#### prior to the user being asked
#### (rather than it being defined
#### in the moment of the user 
#### answering), to avoid the possibility
#### of the lineGap not ever being defined
#### (if the user just hits 'okay' without
#### selecting a linegap)
####
####
lineGap =1

#### Set the window title
pygame.display.set_caption("ChadTech vSatz",)

#### Set the window icon
#### I could never get this to work
#### so icon.PNG is a 1x1 pixel image
#### of (0,0,255)
pygame.display.set_icon(pygame.image.load("icon.PNG").convert())

##### Load the enormous amount of images
execfile('loadimages.py')

pygame.init()
clock = pygame.time.Clock()

#### These define the size of each character (12x16 for big images, 6x8 for small)
charWidth=12
charHeight=16
lilcharWidth=6
lilcharHeight=8

#### These are so the subscripts and super scripts
#### of a character item can be placed in the proper
#### relative location to the character they are
#### a superscript or subscript of
####
#### For example a superscript is 9 pixels to the right
#### and 8 pixels above its owner
### subscript, 9 pixels to the right, and 16 pixels below
lilCharOffsetX = 9
lilCharOffsetSuperSetY = -8
lilCharOffsetSubSetY=16

##### These are the margins of the document.
##### Aside from being visually important
##### Theey also act as an argument
##### in storing the document data
xMarg = (8*charWidth)-charWidth
yMarg = (2*charHeight)

##### curChar tells ChadTech what character we are at
##### which is important for knoing where to blit
#### the cursor, and where to add new characters
curChar=0

#### A unique feature of ChadTech is the 'exponential
#### backspace'. If you hold shift while doing
#### repetitive pressed of keys like backspace
#### or the arrow keys. Each key triggers
#### an expontentially large number of the acts.
#### so if you hold shift and press backspace
#### three times, you will backspace
#### 73 times (8^0+8^1+8^64)
shiftCou = 1
shiftMag = 8

#### This string tells ChadTech if we are adding
#### characters, superscripts, subscripts, or
#### greek characters. 

whichScript = 'normal'
greekOn = 'Yes'

windX=0
windY=0

##### If true the ChadTech menu closes (short for 'Size Found')
sizeFou = False
##### If true ChadTech closes
quit=False

execfile('functionsClassesAndDictionaries.py')

#### Script to define all the different kinds of characters
execfile('characters.py')

#### Dictionary mapping numbers to char objects
execfile('charLet.py')

while sizeFou == False:
	
	##### The script to generate the intro screen
	##### as well as check if a size and linegap
	##### have been selected
	execfile('sizeFou.py')

##### If the user didnt select a lineGap
##### Set it to be equal to 4
if lineGap==1:
	lineGap = 4

##### If the user didnt select a window size
##### set it equal to 1000x500
if windX ==0 and windY ==0:
	windX = 1000
	windY = 500
screen = pygame.display.set_mode((windX,windY),pygame.RESIZABLE)

##### Set the length of each line of text,
##### and the number of lines per page
##### as a function of the size of the screen
lineLen=(windX-(2*xMarg))/charWidth
lineNum=(windY-(2*yMarg))/(charHeight+lineGap)

##### charray (short for Characacter Array, and pronounced 'Sherry')
##### Is the main document of our code
##### Presently, there is no reason to create another
##### Doc object.
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

					print 'GOT HERE lowercase Greek'

					whichChar=greekSet
					for yit in range(len(whichChar.keys)):
						if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
							whichScript=='normal'

					whichChar=greek_lowercasealpha
					print 'EVENT KEY', event.key, whichChar.keys, (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys))
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

					whichChar=greek_lowercaseepsilon
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

				whichChar=firstorderlogic__altnegation
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
									charray.charen.append(addChar(charLet[onNum]))
								if twNum!=161 and twNum!=0:
									charray.charen.append(addChar(charLet[twNum]))

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
											charray.charen[charSpot][1].append(charLet[partSuper])
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
										charray.charen[charSpot][2].append(charLet[partSub])
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
			if linCou%lineNum==0:
				pagen.append([])
			pagen[len(pagen)-1].append(yit)
			linCou+=1

		whichPag=cursorLine/lineNum

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
		screen.blit(L_C,[xMarg+(cursorChar*charWidth),yMarg+(cursorLine%lineNum)*(charHeight+lineGap)])

		######################################
		
		if event.type == pygame.KEYUP:
			keys.remove(event.key)
			greekKeyActivate=False
		if event.type == pygame.QUIT:
			quit = True

	pygame.display.flip()
	clock.tick(60)

pygame.quit()
