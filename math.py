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