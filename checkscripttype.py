if whichScript == 'normal':

	whichChar=superSet
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			whichScript = 'superscript'

	whichChar=subSet
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			whichScript = 'subscript'

	whichChar=slantySet
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			if slantyChek == False:
				slantyChek=True
			else:
				slantyChek=False

	whichChar=greekSet
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			greekKeyActivate=True

if greekKeyActivate==False:
	
	whichChar=greekSet
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			whichScript ='normal'
			execfile('backspace.py')

if whichScript == 'superscript':
	whichChar=subSet
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			whichScript = 'normal'
			execfile('backspace.py')

if whichScript == 'subscript':
	whichChar=superSet
	for yit in range(len(whichChar.keys)):
		if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
			whichScript = 'normal'