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

whichChar=misc__asterisk
for yit in range(len(whichChar.keys)):
	if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
		charray.charen.insert(curChar,addChar(whichChar))
		curChar+=1