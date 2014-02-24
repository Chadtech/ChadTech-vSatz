whichChar=punctuation__period
if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
	charray.charen.insert(curChar,addChar(whichChar))
	curChar+=1
whichChar=punctuation__comma
if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
	charray.charen.insert(curChar,addChar(whichChar))
	curChar+=1
whichChar=punctuation__question
for yit in range(len(whichChar.keys)):
	if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
		charray.charen.insert(curChar,addChar(whichChar))
		curChar+=1
whichChar=punctuation__exclaimation
for yit in range(len(whichChar.keys)):
	if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
		charray.charen.insert(curChar,addChar(whichChar))
		curChar+=1
whichChar=punctuation__semicolon
if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
	charray.charen.insert(curChar,addChar(whichChar))
	curChar+=1
whichChar=punctuation__colon
for yit in range(len(whichChar.keys)):
	if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
		charray.charen.insert(curChar,addChar(whichChar))
		curChar+=1
whichChar=punctuation__singlequote
if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
	charray.charen.insert(curChar,addChar(whichChar))
	curChar+=1
whichChar=punctuation__doublequote
for yit in range(len(whichChar.keys)):
	if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
		charray.charen.insert(curChar,addChar(whichChar))
		curChar+=1