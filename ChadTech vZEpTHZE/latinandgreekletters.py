if  greekOn==False and slantyOn==False:
	whichChar=greekSet
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			greekOn=True

	whichChar=slantySet
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			slantyOn=True
	######################## Lower case letters
	whichChar=lowercase__a
	if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
		charray.charen.insert(curChar,addChar(whichChar))
		curChar+=1
	whichChar=lowercase__b
	if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
		charray.charen.insert(curChar,addChar(whichChar))
		curChar+=1
	whichChar=lowercase__c
	if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
		charray.charen.insert(curChar,addChar(whichChar))
		curChar+=1
	whichChar=lowercase__d
	if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
		charray.charen.insert(curChar,addChar(whichChar))
		curChar+=1
	whichChar=lowercase__e
	if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
		charray.charen.insert(curChar,addChar(whichChar))
		curChar+=1
	whichChar=lowercase__f
	if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
		charray.charen.insert(curChar,addChar(whichChar))
		curChar+=1
	whichChar=lowercase__g
	if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
		charray.charen.insert(curChar,addChar(whichChar))
		curChar+=1
	whichChar=lowercase__h
	if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
		charray.charen.insert(curChar,addChar(whichChar))
		curChar+=1
	whichChar=lowercase__i
	if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
		charray.charen.insert(curChar,addChar(whichChar))
		curChar+=1
	whichChar=lowercase__j
	if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
		charray.charen.insert(curChar,addChar(whichChar))
		curChar+=1
	whichChar=lowercase__k
	if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
		charray.charen.insert(curChar,addChar(whichChar))
		curChar+=1
	whichChar=lowercase__l
	if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
		charray.charen.insert(curChar,addChar(whichChar))
		curChar+=1
	whichChar=lowercase__m
	if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
		charray.charen.insert(curChar,addChar(whichChar))
		curChar+=1
	whichChar=lowercase__n
	if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
		charray.charen.insert(curChar,addChar(whichChar))
		curChar+=1
	whichChar=lowercase__o
	if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
		charray.charen.insert(curChar,addChar(whichChar))
		curChar+=1
	whichChar=lowercase__p
	if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
		charray.charen.insert(curChar,addChar(whichChar))
		curChar+=1
	whichChar=lowercase__q
	if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
		charray.charen.insert(curChar,addChar(whichChar))
		curChar+=1
	whichChar=lowercase__r
	if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
		charray.charen.insert(curChar,addChar(whichChar))
		curChar+=1
	whichChar=lowercase__s
	if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
		charray.charen.insert(curChar,addChar(whichChar))
		curChar+=1
	whichChar=lowercase__t
	if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
		charray.charen.insert(curChar,addChar(whichChar))
		curChar+=1
	whichChar=lowercase__u
	if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
		charray.charen.insert(curChar,addChar(whichChar))
		curChar+=1
	whichChar=lowercase__v
	if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
		charray.charen.insert(curChar,addChar(whichChar))
		curChar+=1
	whichChar=lowercase__w
	if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
		charray.charen.insert(curChar,addChar(whichChar))
		curChar+=1
	whichChar=lowercase__x
	if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
		charray.charen.insert(curChar,addChar(whichChar))
		curChar+=1
	whichChar=lowercase__y
	if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
		charray.charen.insert(curChar,addChar(whichChar))
		curChar+=1
	whichChar=lowercase__z
	if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
		charray.charen.insert(curChar,addChar(whichChar))
		curChar+=1
	######################### Upper case Letters
	whichChar=uppercase__A
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=uppercase__B
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=uppercase__C
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=uppercase__D
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=uppercase__E
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=uppercase__F
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=uppercase__G
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=uppercase__H
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=uppercase__I
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=uppercase__J
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=uppercase__K
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=uppercase__L
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=uppercase__M
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=uppercase__N
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=uppercase__O
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=uppercase__P
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=uppercase__Q
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=uppercase__R
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=uppercase__S
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=uppercase__T
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=uppercase__U
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=uppercase__V
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=uppercase__W
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=uppercase__X
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=uppercase__Y
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=uppercase__Z
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
elif greekOn==True:
	whichChar=greekSet
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			greekOn=False
	whichChar=greek_lowercasealpha
	if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
		charray.charen.insert(curChar,addChar(whichChar))
		curChar+=1
	whichChar=greek_lowercasebeta
	if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
		charray.charen.insert(curChar,addChar(whichChar))
		curChar+=1
	whichChar=greek_lowercasegamma
	if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
		charray.charen.insert(curChar,addChar(whichChar))
		curChar+=1
	whichChar=greek_lowercasedelta
	if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
		charray.charen.insert(curChar,addChar(whichChar))
		curChar+=1
	whichChar=greek_lowercaseepsilon
	if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
		charray.charen.insert(curChar,addChar(whichChar))
		curChar+=1
	whichChar=greek_lowercasezeta
	if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
		charray.charen.insert(curChar,addChar(whichChar))
		curChar+=1
	whichChar=greek_lowercaseeta
	if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
		charray.charen.insert(curChar,addChar(whichChar))
		curChar+=1
	whichChar=greek_lowercasetheta
	if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
		charray.charen.insert(curChar,addChar(whichChar))
		curChar+=1
	whichChar=greek_lowercaseiota
	if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
		charray.charen.insert(curChar,addChar(whichChar))
		curChar+=1
	whichChar=greek_lowercasekappa
	if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
		charray.charen.insert(curChar,addChar(whichChar))
		curChar+=1
	whichChar=greek_lowercaselambda
	if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
		charray.charen.insert(curChar,addChar(whichChar))
		curChar+=1
	whichChar=greek_lowercasemu
	if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
		charray.charen.insert(curChar,addChar(whichChar))
		curChar+=1
	whichChar=greek_lowercasenu
	if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
		charray.charen.insert(curChar,addChar(whichChar))
		curChar+=1
	whichChar=greek_lowercasexi
	if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
		charray.charen.insert(curChar,addChar(whichChar))
		curChar+=1
	whichChar=greek_lowercaseomicron
	if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
		charray.charen.insert(curChar,addChar(whichChar))
		curChar+=1
	whichChar=greek_lowercasepi
	if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
		charray.charen.insert(curChar,addChar(whichChar))
		curChar+=1
	whichChar=greek_lowercaserho
	if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
		charray.charen.insert(curChar,addChar(whichChar))
		curChar+=1
	whichChar=greek_lowercasesigma
	if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
		charray.charen.insert(curChar,addChar(whichChar))
		curChar+=1
	whichChar=greek_lowercasetau
	if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
		charray.charen.insert(curChar,addChar(whichChar))
		curChar+=1
	whichChar=greek_lowercaseupsilon
	if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
		charray.charen.insert(curChar,addChar(whichChar))
		curChar+=1
	whichChar=greek_lowercasephi
	if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
		charray.charen.insert(curChar,addChar(whichChar))
		curChar+=1
	whichChar=greek_lowercasechi
	if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
		charray.charen.insert(curChar,addChar(whichChar))
		curChar+=1
	whichChar=greek_lowercasepsi
	if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
		charray.charen.insert(curChar,addChar(whichChar))
		curChar+=1
	whichChar=greek_lowercaseomega
	if event.key in whichChar.keys and (not (letCor['LEFTSHIFT'] in keys)) and  (not (letCor['RIGHTSHIFT'] in keys)):
		charray.charen.insert(curChar,addChar(whichChar))
		curChar+=1
	###### Upper case Greek
	whichChar=greek_uppercasealpha
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=greek_uppercasebeta
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=greek_uppercasegamma
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=greek_uppercasedelta
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=greek_uppercaseepsilon
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=greek_uppercasezeta
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=greek_uppercaseeta
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=greek_uppercasetheta
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=greek_uppercaseiota
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=greek_uppercasekappa
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=greek_uppercaselambda
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=greek_uppercasemu
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=greek_uppercasenu
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=greek_uppercasexi
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=greek_uppercaseomicron
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=greek_uppercasepi
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=greek_uppercaserho
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=greek_uppercasesigma
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=greek_uppercasetau
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=greek_uppercaseupsilon
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=greek_uppercasephi
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=greek_uppercasechi
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=greek_uppercasepsi
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=greek_uppercaseomega
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1

elif slantyOn==True:

	whichChar=slantySet
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			slantyOn=False

	whichChar=slanty__a
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=slanty__b
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=slanty__c
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=slanty__d
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=slanty__e
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=slanty__f
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=slanty__g
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=slanty__h
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=slanty__i
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=slanty__j
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=slanty__k
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=slanty__l
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=slanty__m
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=slanty__n
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=slanty__o
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=slanty__p
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=slanty__q
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=slanty__r
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=slanty__s
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=slanty__t
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=slanty__u
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=slanty__v
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=slanty__w
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=slanty__x
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=slanty__y
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1
	whichChar=slanty__z
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			charray.charen.insert(curChar,addChar(whichChar))
			curChar+=1