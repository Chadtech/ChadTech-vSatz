
whichChar=math__equals
if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
	charray.charen[curChar-1][1].append(whichChar)

whichChar=math__greaterthanorequal
for yit in range(len(whichChar.keys)):
	if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
		charray.charen[curChar-1][1].pop(len(charray.charen[curChar-1][1])-1)
		charray.charen[curChar-1][1].pop(len(charray.charen[curChar-1][1])-1)
		charray.charen[curChar-1][1].append(whichChar)
