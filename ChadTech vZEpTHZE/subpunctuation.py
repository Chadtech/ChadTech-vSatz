whichChar=punctuation__period
if event.key in whichChar.keys and whichChar.keys.issubset(keys):
	charray.charen[curChar-1][2].append(whichChar)

whichChar=punctuation__comma
if event.key in whichChar.keys and whichChar.keys.issubset(keys):
	charray.charen[curChar-1][2].append(whichChar)

whichChar=punctuation__question
for yit in range(len(whichChar.keys)):
	if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
		charray.charen[curChar-1][2].append(whichChar)

whichChar=punctuation__semicolon
if event.key in whichChar.keys and whichChar.keys.issubset(keys):
	charray.charen[curChar-1][2].append(whichChar)

whichChar=punctuation__colon
for yit in range(len(whichChar.keys)):
	if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
		charray.charen[curChar-1][2].pop(len(charray.charen[curChar-1][2])-1)
		charray.charen[curChar-1][2].append(whichChar)

whichChar=punctuation__exclaimation
for yit in range(len(whichChar.keys)):
	if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
		charray.charen[curChar-1][2].append(whichChar)

whichChar=punctuation__singlequote
if event.key in whichChar.keys and whichChar.keys.issubset(keys):
	charray.charen[curChar-1][2].append(whichChar)

whichChar=punctuation__doublequote
for yit in range(len(whichChar.keys)):
	if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
		charray.charen[curChar-1][2].pop(len(charray.charen[curChar-1][2])-1)
		charray.charen[curChar-1][2].append(whichChar)