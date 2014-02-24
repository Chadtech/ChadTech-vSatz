whichChar=brackets__leftparentheses
for yit in range(len(whichChar.keys)):
	if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
		charray.charen[curChar-1][2].append(whichChar)

whichChar=brackets__rightparentheses
for yit in range(len(whichChar.keys)):
	if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
		charray.charen[curChar-1][2].append(whichChar)

whichChar=brackets__leftbracket
for yit in range(len(whichChar.keys)):
	if event.key in whichChar.keys[yit]:
		charray.charen[curChar-1][2].append(whichChar)

whichChar=brackets__rightbracket
for yit in range(len(whichChar.keys)):
	if event.key in whichChar.keys[yit]:
		charray.charen[curChar-1][2].append(whichChar)

whichChar=brackets__leftcurly
for yit in range(len(whichChar.keys)):
	if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
		charray.charen[curChar-1][2].pop(len(charray.charen[curChar-1][2])-1)
		charray.charen[curChar-1][2].append(whichChar)

whichChar=brackets__rightcurly
for yit in range(len(whichChar.keys)):
	if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
		charray.charen[curChar-1][2].pop(len(charray.charen[curChar-1][2])-1)
		charray.charen[curChar-1][2].append(whichChar)

whichChar=brackets__leftchevron
for yit in range(len(whichChar.keys)):
	if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
		charray.charen[curChar-1][2].pop(len(charray.charen[curChar-1][2])-1)
		charray.charen[curChar-1][2].pop(len(charray.charen[curChar-1][2])-1)
		charray.charen[curChar-1][2].append(whichChar)

whichChar=brackets__rightchevron
for yit in range(len(whichChar.keys)):
	if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
		charray.charen[curChar-1][2].pop(len(charray.charen[curChar-1][2])-1)
		charray.charen[curChar-1][2].pop(len(charray.charen[curChar-1][2])-1)
		charray.charen[curChar-1][2].append(whichChar)