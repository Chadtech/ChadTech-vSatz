if event.key in space.keys:
	charray.charen.insert(curChar,addChar(space))
	curChar+=1

if event.key in enter.keys:
	charray.charen.insert(curChar,addChar(enter))
	curChar+=1

if event.key in backspace.keys:
	##### Backspaces need to happen as part of other ChadTech activities
	execfile('backspace.py')


if event.key in backspace.keys and ((letCor['LEFTSHIFT'] in keys) or (letCor['RIGHTSHIFT'] in keys)):
	for yit in [0]*shiftCou:
		if curChar!=0:
			charray.charen.pop(curChar-1)
			curChar-=1
	shiftCou=shiftCou*shiftMag

if event.key in backspace.keys and ((letCor['LEFTCONTROL'] in keys) or (letCor['RIGHTCONTROL'] in keys)):
	for yit in [0]*6:
		if curChar!=0:
			charray.charen.pop(curChar-1)
			curChar-=1

if event.key in leftarrow.keys:
	if curChar>0:
		curChar-=1

if event.key in leftarrow.keys and ((letCor['LEFTSHIFT'] in keys) or (letCor['RIGHTSHIFT'] in keys)):
	for yit in [0]*shiftCou:
		if curChar>0:
			curChar-=1
	shiftCou=shiftCou*shiftMag

if event.key in leftarrow.keys and ((letCor['LEFTCONTROL'] in keys) or (letCor['RIGHTCONTROL'] in keys)):
	for yit in [0]*6:
		if curChar>0:
			curChar-=1

if event.key in rightarrow.keys:
	if curChar<(len(charray.charen)):
		curChar+=1

if event.key in rightarrow.keys and ((letCor['LEFTSHIFT'] in keys) or (letCor['RIGHTSHIFT'] in keys)):
	for yit in [0]*shiftCou:
		if curChar<(len(charray.charen)):
			curChar+=1

if event.key in rightarrow.keys and ((letCor['LEFTCONTROL'] in keys) or (letCor['RIGHTCONTROL'] in keys)):
	for yit in [0]*6:
		if event.key in rightarrow.keys:
			if curChar<(len(charray.charen)):
				curChar+=1

if event.key in uparrow.keys:
	for yit in [0]*lineLen:
		if curChar>0:
			curChar-=1


if event.key in downarrow.keys:
	for yit in [0]*lineLen:
		if curChar<(len(charray.charen)):
			curChar+=1