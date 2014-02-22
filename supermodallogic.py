whichChar=modallogic__possible
if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
	charray.charen[curChar-1][1].append(whichChar)
whichChar=modallogic__necessary
if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
	charray.charen[curChar-1][1].append(whichChar)