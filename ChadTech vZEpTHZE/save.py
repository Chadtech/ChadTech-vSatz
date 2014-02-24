whichChar=save
for yit in range(len(whichChar.keys)):
	if event.key in whichChar.keys[yit] and whichChar.keys[yit].issubset(keys):
		##### Backspace the 's' we just added to the document
		charray.charen.pop(curChar-1)
		curChar-=1
		##### Get the name of the file
		saveName=tkFileDialog.asksaveasfilename()
		saveName=str(saveName)
		###### Make sure the file gets a name. If the Users hits cancel the name is '', therefore we shouldnt save anything
		if saveName!='':
			##### Paste Each page onto the screen and take a picture of it naming it 'pag'+page Number+'.PNG'
			hsyCou=0
			screen.fill((0,0,0))
			#Pag (hsy) in pagen
			for hsy in pagen:
				blitCharen=[]
				yitCou=0
				#For the linen in pag (hsy)
				for yit in hsy:
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
				##### Print 'Pag' on the screen
				screen.blit(L_lP,[windX-84,0])	
				screen.blit(L_la,[windX-72,0])
				screen.blit(L_lg,[windX-60,0])	

				##### Print the Pag number
				screen.blit(numbersToNumerals[(hsyCou)%10],[windX-12,0])
				if hsyCou>9:
					screen.blit(numbersToNumerals[hsyCou/10],[windX-24,0])
				if hsyCou>99:
					screen.blit(numbersToNumerals[hsyCou/100],[windX-36,0])
				if hsyCou>999:
					screen.blit(numbersToNumerals[hsyCou/1000],[windX-48,0])
				pygame.image.save(screen,'pag'+str(hsyCou)+'.PNG')
				screen.fill((0,0,0))
				hsyCou+=1
			###### Stitch pages together
			stXs,stYs = 0,0
			for hsy in range(len(pagen)):
				filName="pag"+str(hsy)+".PNG"
				thX, thY=Image.open(filName).size
				stXs=thX
				stYs+=thY
			stImage = Image.new('RGB',(stXs,stYs),'black')
			for hsy in range(len(pagen)):
				stImage.paste(Image.open('pag'+str(hsy)+'.PNG'),(0,hsy*windY,stXs,windY+(hsy*windY)))
			############## Put the character in the pixel
			#############################################
			####### Make an array of all the character digits
			charCodes=[]
			for yit in charray.charen:
				charCodes.append(yit[0].keyDig)
			pixelCharCodes=[]
			##### Make an array of all the superScript digits, where the even indexed elements are the character they belong to, and the odd indexed elements are the character digits
			superRay =[]
			for yit in range(len(charray.charen)):
				for vapp in range(len(charray.charen[yit][1])):
					superRay.append(yit)
					superRay.append(charray.charen[yit][1][vapp].keyDig)
			###### Add '161' to the CharCodes array so that we can end it with the signal that there are superscripts
			#if len(superRay):
			charCodes.append(161) 
			###### Store the charCodes as pixel values
			pixelCharCodes=[]
			# Make sure there is an event amount of CharCodes, 0s wont be read
			if len(charCodes)%2==1:
				charCodes.append(0)
			for yit in range(len(charCodes)/2):
				red, green, blue = 0,0,0
				# ((_,_),(_,_),(=,=)) -v
				blue=(charCodes[yit*2])%256 
				# ((_,_),(_,+),(_,_)) -v
				green+=((charCodes[yit*2])/256)%16 # This value should not exceed 16. Problems will occur if it does, the modulus is present to store the value incorrectly, where it would otherwise crash the whole program
				# ((=,=),(_,_),(_,_)) -v
				red=((charCodes[(yit*2)+1])/16)%256 # This value should not exceed 256. The justification is similar to the one given in the comment above
				# ((_,_),(+,_),(_,_)) -v
				green+=((charCodes[(yit*2)+1])%16)*16 
				#### What is going on here?
				#### I need to store the character digits in the pixels
				#### If I store the digit in a color value, I am constrained to 256 possible characters, which I consider too low
				#### If I store the digit in all three color values I have 16,777,216 possible characters, which is excessive
				#### Thus, I am left with the more difficult task of storing two character digits in 3 pixel values, leading me to a cozy 4096 possible characters
				#### The way I am doing this is re-allocating the three 16^2 color values, into two 16^3 chacacter digit values //// (16*16)*(16*16)*(16*16) = (16*16*16)*(16*16*16) .  Character Digit<(16*16*16)
				pixelCharCodes.append((red,green,blue))
			##### Make an array of all the subcript digits, where the even indexed elements are the character they belong to, and the odd indexed elements are the character digits
			subRay =[]
			for yit in range(len(charray.charen)):
				for vapp in range(len(charray.charen[yit][2])):
					subRay.append(yit)
					subRay.append(charray.charen[yit][2][vapp].keyDig)
			##### Store the superScripts as pixel values
			for yit in range(len(superRay)/2):
				red, green, blue = 0,0,0
				##### The location of the superscript needs to be stored one higher than its actual value. 
				##### This is to avoid the unlikely circumstance that the superscript corresponds to the
				##### First letter (the zeroth letter).
				#####
				##### The first letter, stored as a zero, would be transparent to the open function
				blue = (superRay[yit*2]+1)%256
				green = ((superRay[yit*2]+1)/256)%256
				red = (superRay[yit*2]+1)/65536
				pixelCharCodes.append((red,green,blue))
				blue = superRay[(yit*2)+1]%256
				green = (superRay[(yit*2)+1]/256)%256
				red = superRay[(yit*2)+1]/65536
				pixelCharCodes.append((red,green,blue))
			pixelCharCodes.append((0,0,162))
			##### Store the subScripts as pixel values
			for yit in range(len(subRay)/2):
				red, green, blue = 0,0,0
				blue = (subRay[yit*2]+1)%256
				green = ((subRay[yit*2]+1)/256)%256
				red = (subRay[yit*2]+1)/65536
				pixelCharCodes.append((red,green,blue))
				blue = subRay[(yit*2)+1]%256
				green = (subRay[(yit*2)+1]/256)%256
				red = subRay[(yit*2)+1]/65536
				pixelCharCodes.append((red,green,blue))
			##### Put the pixels on the image
			for yit in range(len(pixelCharCodes)):
				stImage.putpixel( (yit/stYs,yit%stYs), pixelCharCodes[yit] )
			##### Then save the image
			try:
				if '.PNG' in saveName:
					stImage.save(saveName,"png")
				else:
					stImage.save(saveName+'.PNG',"png")
			except:
				pass