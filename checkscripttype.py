if whichScript == 'normal':

	whichChar=superSet
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			whichScript = 'superscript'
			charray.charen[curChar-1][1]=[]

	whichChar=subSet
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			whichScript = 'subscript'

	whichChar=slantySet
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			slantyKeyActivate=True

	whichChar=greekSet
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			greekKeyActivate=True

if whichScript == 'superscript':
	whichChar=subSet
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			whichScript = 'normal'

if whichScript == 'subscript':
	whichChar=superSet
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			whichScript = 'normal'