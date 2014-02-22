whichChar=oPen
for yit in range(len(whichChar.keys)):
	if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
		openName=tkFileDialog.askopenfilename()
		openName = str(openName)
		openIm = Image.open(openName)
		xSize,ySize = openIm.size
		charray = Doc()
		red,green,blue = openIm.getpixel((0,0))
		whatsGoinOn='addingChars'
		for yit in range(ySize*xMarg):
			if whatsGoinOn=='addingChars':
				red,green,blue = openIm.getpixel((yit/(ySize),yit%(ySize)))
				onNum=0
				twNum=0
				onNum+=blue
				twNum+=(red*16)
				onNum+=(green%16)*16
				twNum+=(green/16)
				if onNum!=161 and onNum!=0:
					charray.charen.append(addChar(charLet[onNum]))
				if twNum!=161 and twNum!=0:
					charray.charen.append(addChar(charLet[twNum]))
				if onNum==161 or twNum==161:
					whatsGoinOn='addingSuperscripts'
					even=True
			elif whatsGoinOn=='addingSuperscripts':
				red,green,blue = openIm.getpixel((yit/(ySize),yit%(ySize)))
				if (red,green,blue)!=(0,0,162):
					if (red,green,blue)!=(0,0,0):
						if even==True:
							charSpot=0
							charSpot+=blue
							charSpot+=green*256
							charSpot+=red*65536
							charSpot-=1
							even=False
						elif even!=True:
							partSuper=0
							partSuper+=blue
							partSuper+=green*256
							partSuper+=red*65536
							print 'PARTSUPER',partSuper,'CHARSPOT',charSpot,'RGB',(red,green,blue)
							charray.charen[charSpot][1].append(charLet[partSuper])
							even=True
				else:
					whatsGoinOn='addingSubscripts'
					even=True
			elif whatsGoinOn=='addingSubscripts':
				red,green,blue = openIm.getpixel((yit/(ySize),yit%(ySize)))
				if (red,green,blue)!=(0,0,0):
					if even==True:
						charSpot=0
						charSpot+=blue
						charSpot+=green*256
						charSpot+=red*65536
						charSpot-=1
						even=False
					elif even!=True:
						partSub=0
						partSub+=blue
						partSub+=green*256
						partSub+=red*65536
						print 'PART SUB',partSub,'CHARSPOT',charSpot,'RGB',(red,green,blue)
						charray.charen[charSpot][2].append(charLet[partSub])
						even=True
		curChar=len(charray.charen)-1