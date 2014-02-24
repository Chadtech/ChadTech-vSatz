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
	print 'GOT HERE'
	for yit in [0]*2:
		if curChar!=0:
			charray.charen.pop(curChar-1)
			curChar-=1
	charray.charen.insert(curChar,addChar(whichChar))
	curChar+=1