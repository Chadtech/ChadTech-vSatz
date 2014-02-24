
whichChar=math__equals
if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
	charray.charen[curChar-1][2].append(whichChar)

whichChar=math__greaterthan
for yit in range(len(whichChar.keys)):
	if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
		charray.charen[curChar-1][2].pop(len(charray.charen[curChar-1][2])-1)
		charray.charen[curChar-1][2].append(whichChar)

whichChar=math__greaterthanorequal
for yit in range(len(whichChar.keys)):
	if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
		charray.charen[curChar-1][2].pop(len(charray.charen[curChar-1][2])-1)
		charray.charen[curChar-1][2].pop(len(charray.charen[curChar-1][2])-1)
		charray.charen[curChar-1][2].append(whichChar)

whichChar=math__lessthan
for yit in range(len(whichChar.keys)):
	if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
		charray.charen[curChar-1][2].pop(len(charray.charen[curChar-1][2])-1)
		charray.charen[curChar-1][2].append(whichChar)

whichChar=math__lessthanorequal
for yit in range(len(whichChar.keys)):
	if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
		charray.charen[curChar-1][2].pop(len(charray.charen[curChar-1][2])-1)
		charray.charen[curChar-1][2].pop(len(charray.charen[curChar-1][2])-1)
		charray.charen[curChar-1][2].append(whichChar)

whichChar=math__division
for yit in range(len(whichChar.keys)):
	if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
		charray.charen[curChar-1][2].pop(len(charray.charen[curChar-1][2])-1)
		charray.charen[curChar-1][2].pop(len(charray.charen[curChar-1][2])-1)
		charray.charen[curChar-1][2].append(whichChar)

whichChar=math__approximately
for yit in range(len(whichChar.keys)):
	if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
		charray.charen[curChar-1][2].pop(len(charray.charen[curChar-1][2])-1)
		charray.charen[curChar-1][2].pop(len(charray.charen[curChar-1][2])-1)
		charray.charen[curChar-1][2].append(whichChar)

whichChar=math__plus
for yit in range(len(whichChar.keys)):
	if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
		charray.charen[curChar-1][2].pop(len(charray.charen[curChar-1][2])-1)
		charray.charen[curChar-1][2].pop(len(charray.charen[curChar-1][2])-1)
		charray.charen[curChar-1][2].append(whichChar)

whichChar=math__minus
if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
	charray.charen[curChar-1][2].append(whichChar)

whichChar=math__multiply
for yit in range(len(whichChar.keys)):
	if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
		charray.charen[curChar-1][2].pop(len(charray.charen[curChar-1][2])-1)
		charray.charen[curChar-1][2].pop(len(charray.charen[curChar-1][2])-1)
		charray.charen[curChar-1][2].append(whichChar)

whichChar=math__forwardslash
for yit in range(len(whichChar.keys)):
	if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys) and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
		charray.charen[curChar-1][2].append(whichChar)

whichChar=math__backslash
for yit in range(len(whichChar.keys)):
	if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
		charray.charen[curChar-1][2].append(whichChar)

whichChar=math__QED
for yit in range(len(whichChar.keys)):
	if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
		charray.charen[curChar-1][2].pop(len(charray.charen[curChar-1][2])-1)
		charray.charen[curChar-1][2].pop(len(charray.charen[curChar-1][2])-1)
		charray.charen[curChar-1][2].append(whichChar)

whichChar=math__squareroot
for yit in range(len(whichChar.keys)):
	if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
		charray.charen[curChar-1][2].pop(len(charray.charen[curChar-1][2])-1)
		charray.charen[curChar-1][2].pop(len(charray.charen[curChar-1][2])-1)
		charray.charen[curChar-1][2].append(whichChar)

whichChar=math__plusminus
for yit in range(len(whichChar.keys)):
	if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
		charray.charen[curChar-1][2].pop(len(charray.charen[curChar-1][2])-1)
		charray.charen[curChar-1][2].pop(len(charray.charen[curChar-1][2])-1)
		charray.charen[curChar-1][2].append(whichChar)

whichChar=math__integral
for yit in range(len(whichChar.keys)):
	if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
		charray.charen[curChar-1][2].pop(len(charray.charen[curChar-1][2])-1)
		charray.charen[curChar-1][2].pop(len(charray.charen[curChar-1][2])-1)
		charray.charen[curChar-1][2].append(whichChar)

whichChar=math__notequal
for yit in range(len(whichChar.keys)):
	if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
		charray.charen[curChar-1][2].pop(len(charray.charen[curChar-1][2])-1)
		charray.charen[curChar-1][2].pop(len(charray.charen[curChar-1][2])-1)
		charray.charen[curChar-1][2].append(whichChar)

whichChar=math__angle
for yit in range(len(whichChar.keys)):
	if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
		charray.charen[curChar-1][2].pop(len(charray.charen[curChar-1][2])-1)
		charray.charen[curChar-1][2].pop(len(charray.charen[curChar-1][2])-1)
		charray.charen[curChar-1][2].append(whichChar)

whichChar=math__triangle
for yit in range(len(whichChar.keys)):
	if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
		charray.charen[curChar-1][2].pop(len(charray.charen[curChar-1][2])-1)
		charray.charen[curChar-1][2].pop(len(charray.charen[curChar-1][2])-1)
		charray.charen[curChar-1][2].append(whichChar)

whichChar=math__gradient
for yit in range(len(whichChar.keys)):
	if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
		charray.charen[curChar-1][2].pop(len(charray.charen[curChar-1][2])-1)
		charray.charen[curChar-1][2].pop(len(charray.charen[curChar-1][2])-1)
		charray.charen[curChar-1][2].append(whichChar)

whichChar=math__divides
for yit in range(len(whichChar.keys)):
	if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
		charray.charen[curChar-1][2].pop(len(charray.charen[curChar-1][2])-1)
		charray.charen[curChar-1][2].append(whichChar)

whichChar=math__doesntdivide
for yit in range(len(whichChar.keys)):
	if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
		charray.charen[curChar-1][2].pop(len(charray.charen[curChar-1][2])-1)
		charray.charen[curChar-1][2].pop(len(charray.charen[curChar-1][2])-1)
		charray.charen[curChar-1][2].append(whichChar)

whichChar=math__infinity
for yit in range(len(whichChar.keys)):
	if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
		charray.charen[curChar-1][2].pop(len(charray.charen[curChar-1][2])-1)
		charray.charen[curChar-1][2].pop(len(charray.charen[curChar-1][2])-1)
		charray.charen[curChar-1][2].append(whichChar)