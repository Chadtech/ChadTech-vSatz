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