#### This script is run in a while loop immediately after ChadTech is started
#### It serves to give the user options regarding lineGap and screen size
#### It checks where the mouse is, and for mouse clicks
#### if the mouse is clicked in certain regions (the buttons)
#### The button is highlighted by an certain image (selected.png) to indicate
#### that that option is currently selected
#### When the 'button', labeled 'okay' is pressed the main text operation
#### of ChadTech begins

#### The loop first checks if the mouse button is pressed
#### if it is pressed, it checks what region of the screen it
#### was pressed in. If the region was a button, it assigns
#### values to the linegap, or the window dimensions

#### Blit the intro screen
screen.blit(introscreen,[0,0])	

for event in pygame.event.get():
	if event.type == 5:

		mouX,mouY = event.pos

		##################################3
		########### Okay Check

		################################################3
		####################                  Row ZE 400
		if (mouX>307 and mouX<449) and (mouY>67 and mouY<92):
			windX=400
			windY=400
		if (mouX>465 and mouX<607) and (mouY>67 and mouY<92):
			windX=400
			windY=200
		if (mouX>619 and mouX<761) and (mouY>67 and mouY<92):
			windX=400
			windY=267
		if (mouX>775 and mouX<918) and (mouY>67 and mouY<92):
			windX=400
			windY=300

		################################################3
		####################                  Row TW 600
		if (mouX>307 and mouX<449) and (mouY>107 and mouY<132):
			windX=600
			windY=600
		if (mouX>465 and mouX<607) and (mouY>107 and mouY<132):
			windX=600
			windY=300
		if (mouX>619 and mouX<761) and (mouY>107 and mouY<132):
			windX=600
			windY=400
		if (mouX>775 and mouX<918) and (mouY>107 and mouY<132):
			windX=600
			windY=450

		################################################3
		####################                  Row TH 800
		if (mouX>307 and mouX<449) and (mouY>147 and mouY<172):
			windX=800
			windY=800
		if (mouX>465 and mouX<607) and (mouY>147 and mouY<172):
			windX=800
			windY=400
		if (mouX>619 and mouX<761) and (mouY>147 and mouY<172):
			windX=800
			windY=533
		if (mouX>775 and mouX<918) and (mouY>147 and mouY<172):
			windX=800
			windY=600

		################################################3
		####################                  Row FO 1000
		if (mouX>307 and mouX<449) and (mouY>187 and mouY<212):
			windX=1000
			windY=1000
		if (mouX>465 and mouX<607) and (mouY>187 and mouY<212):
			windX=1000
			windY=500
		if (mouX>619 and mouX<761) and (mouY>187 and mouY<212):
			windX=1000
			windY=667
		if (mouX>775 and mouX<918) and (mouY>187 and mouY<212):
			windX=1000
			windY=750

		################################################3
		####################                  Row FI 1200
		if (mouX>307 and mouX<449) and (mouY>227 and mouY<252):
			windX=1200
			windY=1200
		if (mouX>465 and mouX<607) and (mouY>227 and mouY<252):
			windX=1200
			windY=600
		if (mouX>619 and mouX<761) and (mouY>227 and mouY<252):
			windX=1200
			windY=800
		if (mouX>775 and mouX<918) and (mouY>227 and mouY<252):
			windX=1200
			windY=900

		################################################3
		####################                  Row SI 1400
		if (mouX>307 and mouX<449) and (mouY>267 and mouY<292):
			windX=1400
			windY=1400
		if (mouX>465 and mouX<607) and (mouY>267 and mouY<292):
			windX=1400
			windY=700
		if (mouX>619 and mouX<761) and (mouY>267 and mouY<292):
			windX=1400
			windY=933
		if (mouX>775 and mouX<918) and (mouY>267 and mouY<292):
			windX=1400
			windY=1050

		################################################3
		####################                  Row SE 1600
		if (mouX>307 and mouX<449) and (mouY>307 and mouY<332):
			windX=1600
			windY=1600
		if (mouX>465 and mouX<607) and (mouY>307 and mouY<332):
			windX=1600
			windY=800
		if (mouX>619 and mouX<761) and (mouY>307 and mouY<332):
			windX=1600
			windY=1067
		if (mouX>775 and mouX<918) and (mouY>307 and mouY<332):
			windX=1600
			windY=1200

		################################################3
		####################                  Row EI 1800
		if (mouX>307 and mouX<449) and (mouY>347 and mouY<372):
			windX=1800
			windY=1800
		if (mouX>465 and mouX<607) and (mouY>347 and mouY<372):
			windX=1800
			windY=900
		if (mouX>619 and mouX<761) and (mouY>347 and mouY<372):
			windX=1800
			windY=1200
		if (mouX>775 and mouX<918) and (mouY>347 and mouY<372):
			windX=1800
			windY=1350

		################################################3
		####################                  line Gap
		if (mouX>307 and mouX<449) and (mouY>407 and mouY<432):
			lineGap = 0
		if (mouX>465 and mouX<607) and (mouY>407 and mouY<432):
			lineGap = 4
		if (mouX>619 and mouX<761) and (mouY>407 and mouY<432):
			lineGap = 8
		if (mouX>775 and mouX<918) and (mouY>407 and mouY<432):
			lineGap = 16

		################################################3
		####################                  OKAY
		if (mouX>307 and mouX<449) and (mouY>447 and mouY<472):
			sizeFou = True

		####################################### 157, 40
	if event.type == pygame.QUIT:
		quit=True
		sizeFou=True

#### If the window and linegap options are selected, paste the selected image

if windX==400 and windY==400:
	screen.blit(selected,(308,67))
if windX==400 and windY==200:
	screen.blit(selected,(464,67))
if windX==400 and windY==267:
	screen.blit(selected,(620,67))
if windX==400 and windY==300:
	screen.blit(selected,(776,67))

###############################################
if windX==600 and windY==600:
	screen.blit(selected,(308,107))
if windX==600 and windY==300:
	screen.blit(selected,(464,107))
if windX==600 and windY==400:
	screen.blit(selected,(620,107))
if windX==600 and windY==450:
	screen.blit(selected,(776,107))

###############################################
if windX==800 and windY==800:
	screen.blit(selected,(308,147))
if windX==800 and windY==400:
	screen.blit(selected,(464,147))
if windX==800 and windY==533:
	screen.blit(selected,(620,147))
if windX==800 and windY==600:
	screen.blit(selected,(776,147))

###############################################
if windX==1000 and windY==1000:
	screen.blit(selected,(308,187))
if windX==1000 and windY==500:
	screen.blit(selected,(464,187))
if windX==1000 and windY==667:
	screen.blit(selected,(620,187))
if windX==1000 and windY==750:
	screen.blit(selected,(776,187))

###############################################
if windX==1200 and windY==1200:
	screen.blit(selected,(308,227))
if windX==1200 and windY==600:
	screen.blit(selected,(464,227))
if windX==1200 and windY==800:
	screen.blit(selected,(620,227))
if windX==1200 and windY==900:
	screen.blit(selected,(776,227))

###############################################
if windX==1400 and windY==1400:
	screen.blit(selected,(308,267))
if windX==1400 and windY==700:
	screen.blit(selected,(464,267))
if windX==1400 and windY==933:
	screen.blit(selected,(620,267))
if windX==1400 and windY==1050:
	screen.blit(selected,(776,267))

###############################################
if windX==1600 and windY==1600:
	screen.blit(selected,(308,307))
if windX==1600 and windY==800:
	screen.blit(selected,(464,307))
if windX==1600 and windY==1067:
	screen.blit(selected,(620,307))
if windX==1600 and windY==1200:
	screen.blit(selected,(776,307))

###############################################
if windX==1800 and windY==1800:
	screen.blit(selected,(308,347))
if windX==1800 and windY==900:
	screen.blit(selected,(464,347))
if windX==1800 and windY==1200:
	screen.blit(selected,(620,347))
if windX==1800 and windY==1350:
	screen.blit(selected,(776,347))

###############################################
if lineGap == 0:
	screen.blit(selected,(308,407))
if lineGap == 4:
	screen.blit(selected,(464,407))
if lineGap == 8:
	screen.blit(selected,(620,407))
if lineGap == 16:
	screen.blit(selected,(776,407))

pygame.display.flip()
