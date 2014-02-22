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