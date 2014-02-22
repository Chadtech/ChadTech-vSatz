############################ Turn charray into vorten
vorten=[]
forward=0
vorten.append([])
whichChar=0
vortChar=0
cursorVort=0
for yit in charray.charen:
	whichChar+=1
	#Add this char to vorten
	if yit!=addChar(space) and yit!=addChar(enter):
		vorten[forward].append(yit)
	if yit==addChar(space):
		vorten[forward].append(yit)
		vorten.append([])
		forward+=1
	if yit==addChar(enter):
		if vorten[forward]==[]:
			vorten[forward].append(yit)
			vorten.append([])
			forward+=1
		else:
			vorten.append([])
			forward+=1
			vorten[forward].append(yit)
			vorten.append([])
			forward+=1
	#Check if its the current char
	if whichChar==curChar:
		cursorVort=forward
		vortChar=len(vorten[forward])
############################### Turn vorten in Linen
linen = []
linen.append([0,[]])
thisLin=0
cursorLine=0
whichVort=0
vortInLin=0
for yit in vorten:
	#Add vort to Linen
	if yit==[addChar(enter)]:
		linen.append([0,[]])
		thisLin+=1
	else:
		if (linen[thisLin][0]+len(yit))<=lineLen:
			linen[thisLin][1].append(yit)
			linen[thisLin][0]+=len(yit)
		else:
			linen.append([0,[]])
			thisLin+=1
			linen[thisLin][0]=len(yit)
			linen[thisLin][1].append(yit)
	#Check if its the current line
	if whichVort==cursorVort:
		cursorLine=thisLin
		vortInLin=len(linen[thisLin][1])
	whichVort+=1
lineChar=0
cursorChar=0
for yit in range(vortInLin-1):
	lineChar+=len(linen[cursorLine][1][yit])
cursorChar=lineChar+vortChar
############################ Turn lines into pagen
pagen=[]
linCou=0
for yit in linen:
	if linCou%lineNum==0:
		pagen.append([])
	pagen[len(pagen)-1].append(yit)
	linCou+=1
whichPag=cursorLine/lineNum
############################ Turn pagen back into charen, and blit
blitCharen=[]
yitCou=0
#For the linen in pagen
for yit in pagen[whichPag]:
	blitCharen.append([])
	#for the vorten in linen
	for vapp in yit[1]:
		#for the charen in vorten
		for gno in vapp:
			blitCharen[yitCou].append(gno)
	#Paste every char in line of pag		
	for vapp in range(lineLen):
		if vapp<len(blitCharen[yitCou]):
			screen.blit(blitCharen[yitCou][vapp][0].image,[(vapp*charWidth)+xMarg,yitCou*(charHeight+lineGap)+yMarg])
			for dukh in range(len(blitCharen[yitCou][vapp][1])):
				screen.blit(blitCharen[yitCou][vapp][1][dukh].lilimage,[(vapp*charWidth)+(dukh*lilcharWidth)+xMarg+lilCharOffsetX,(yitCou*(charHeight+lineGap))+lilCharOffsetSuperSetY+yMarg])
			for dukh in range(len(blitCharen[yitCou][vapp][2])):
				screen.blit(blitCharen[yitCou][vapp][2][dukh].lilimage,[(vapp*charWidth)+(dukh*lilcharWidth)+xMarg+lilCharOffsetX,(yitCou*(charHeight+lineGap))+lilCharOffsetSubSetY+yMarg])
		else:
			screen.blit(L_S,[(vapp*charWidth)+xMarg,yitCou*(charHeight+lineGap)+yMarg])
	yitCou+=1
screen.blit(L_C,[xMarg+(cursorChar*charWidth),yMarg+(cursorLine%lineNum)*(charHeight+lineGap)])