
#### Characters added into the document array are added as an element of an 'addChar' array. the 0th element is the character, 
#### the first and second are for super scripts and sub scripts. 3 squared with an index number 'i sub Z' would look like
#### [numeralThree, [numeralTwo],[lowercasei,settheory__subset,uppercaseZ]]
####

def addChar(input):
	return [input,[],[]]

#### pygame events have a .key property that is an integer. 
#### letcor ('letter correspondence') is a dictionary so 
#### I can type a string of the key without having to
#### remember the number

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

#### Each possible characer is a unique character object. 
#### My terminology through out this program is poor
#### a Char object is a KIND of character object
#### but often I use 'char' or 'character' to refer
#### to specific elements in the document array

class Char:
	def __init__(self,lilimage,image,keys,keyDig):
		self.lilimage=lilimage
		self.image=image
		self.keys=keys #The keys variable, refers to a tuple, who elements are sets, containing valid key combinations to produce that character. The elements of the set are elements of the dictionary
		self.keyDig=keyDig

#### This is the document object
#### Charen (pronounced 'Sharon')
#### is an array of all the
#### characters items in the
#### document

class Doc:
	def __init__(self):
		self.charen=[]