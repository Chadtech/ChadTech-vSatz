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
greekOn = False

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

##### keys is the set of pressed down keys
##### pressing down a key adds that key to
##### keys, and lifting up the key removes
##### it
keys = set([])

##### This is the main loop.
##### if an event happens, ChadTech runs through
##### every possible key and sees if the newly pressed
##### key and keys set meet the triggering criteria

greekKeyActivate=False

while quit==False:
	for event in pygame.event.get():

		if not (letCor['LEFTSHIFT'] in keys) and not (letCor['RIGHTSHIFT'] in keys):
			shiftCou = 1

		if event.type == pygame.KEYDOWN:
			##### Add the newly pressed key to kes
			keys.add(event.key)

			execfile('checkscripttype.py')

			######################## Check if this is a super script or sub script

			if whichScript == 'normal':

				#### 
				execfile('latinandgreekletters.py')

				#########################Punctuation

				execfile('punctuation.py')

				######################### Numerals

				execfile('numerals.py')

				######################### Modal Logic Characters

				execfile('modallogic.py')

				######################## First order logic

				execfile('firstorderlogic.py')

				######################### Math

				execfile('math.py')

				########################### Brackets

				execfile('brackets.py')

				######################### Misc

				execfile('misc.py')

				######################### Proof Theory

				execfile('prooftheory.py')

				######################### Set Theory

				execfile('settheory.py')

				######################### Alexander Hamilton

				execfile('alexanderhamilton.py')

				######################### Commandy keys

				##### Commandy keys are keys that issue commands, rather than add characters.
				##### Backspace, and arrow keys are examples of this
				execfile('commandykeys.py')

			########################################## Saving DOcuments

				execfile('save.py')

				######################################## Opening Documents

				execfile('open.py')

			else: #Else, as in whichscript!='normal'

				if whichScript == 'superscript':

					###### Letters, as well as numerals
					execfile('superlatinandgreek.py')

					###### Modal logic
					execfile('supermodallogic.py')

					###### Punctuation
					execfile('superpunctuation.py')

					##### first order logic
					execfile('superfirstorderlogic.py')

					##### Math
					execfile('supermath.py')

					##### Brackets
					execfile('superbrackets.py')

					##### Misc
					execfile('supermisc.py')

					##### Proof theory
					execfile('superprooftheory.py')

					##### set theory
					execfile('supersettheory.py')

				if whichScript == 'subscript':

					###### Letters, as well as numerals
					execfile('sublatinandgreek.py')

					###### Modal logic
					execfile('submodallogic.py')

					###### Punctuation
					execfile('subpunctuation.py')

					##### first order logic
					execfile('subfirstorderlogic.py')



		############################## Fill the screen with black

		screen.fill((0,0,0))

		############################ Generate the images on the screen

		execfile('screenblit.py')

		######################################
		
		if event.type == pygame.KEYUP:
			keys.remove(event.key)
			greekKeyActivate=False
		if event.type == pygame.QUIT:
			quit = True

	pygame.display.flip()
	clock.tick(60)

pygame.quit()
