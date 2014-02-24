whichChar=prooftheory__singleturnstile
for yit in range(len(whichChar.keys)):
	if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
		charray.charen[curChar-1][2].pop(len(charray.charen[curChar-1][2])-1)
		charray.charen[curChar-1][2].pop(len(charray.charen[curChar-1][2])-1)
		charray.charen[curChar-1][2].append(whichChar)

whichChar=prooftheory__doubleturnstile
for yit in range(len(whichChar.keys)):
	if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
		charray.charen[curChar-1][2].pop(len(charray.charen[curChar-1][2])-1)
		charray.charen[curChar-1][2].pop(len(charray.charen[curChar-1][2])-1)
		charray.charen[curChar-1][2].append(whichChar)

whichChar=prooftheory__notsingleturnstile
for yit in range(len(whichChar.keys)):
	if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
		charray.charen[curChar-1][2].pop(len(charray.charen[curChar-1][2])-1)
		charray.charen[curChar-1][2].pop(len(charray.charen[curChar-1][2])-1)
		charray.charen[curChar-1][2].append(whichChar)

whichChar=prooftheory__notdoubleturnstile
for yit in range(len(whichChar.keys)):
	if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
		charray.charen[curChar-1][2].pop(len(charray.charen[curChar-1][2])-1)
		charray.charen[curChar-1][2].pop(len(charray.charen[curChar-1][2])-1)
		charray.charen[curChar-1][2].append(whichChar)

whichChar=prooftheory__logicalconstant
for yit in range(len(whichChar.keys)):
	if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
		charray.charen[curChar-1][2].pop(len(charray.charen[curChar-1][2])-1)
		charray.charen[curChar-1][2].pop(len(charray.charen[curChar-1][2])-1)
		charray.charen[curChar-1][2].append(whichChar)