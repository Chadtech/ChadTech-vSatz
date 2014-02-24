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