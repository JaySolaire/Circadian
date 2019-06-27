import pygame
import pigpio
import time
import datetime
pygame.init()
pi= pigpio.pi()

		
		
def Fade(red, blue, green, rpi, bpi, gpi, speed):
	while (rpi != red or bpi != blue or gpi != green):
		if rpi < red:
			rpi+=1
		if rpi > red:
			rpi -=1
		if bpi < blue:
			bpi+=1
		if bpi > blue:
			bpi-=1
		if gpi < green:
			gpi+=1
		if gpi > green:
			gpi-=1
		pi.set_PWM_dutycycle(17, rpi)
		pi.set_PWM_dutycycle(24, bpi)		
		pi.set_PWM_dutycycle(22, gpi)
		time.sleep(speed)
#		print("red =",rpi)
#	print("done")

def Circadian(rpi, bpi, gpi, stars):
	#gameActive = 1
	hour = 0
	while (1):
		print("Circadian loop start")
		evList = pygame.event.get()
		for event in evList:
			if event.type == pygame.QUIT:
				print("out of Circadian, Quit")
				return 0
			if event.type == pygame.MOUSEBUTTONDOWN:
				msPos = pygame.mouse.get_pos()
				if !(r11box.collidepoint(msPos) || r12box.collidepoint(msPos)):
				print("out of Circadian")
			 	return 2
		currentTime = datetime.datetime.now()
		if (currentTime.hour > hour):
			print("Hour Change!")
			hour += 1
			if currentTime.hour < 8:
				if stars == 0:
					red = 0;
					blue = 0;
					green = 0;
				else:
					red = 10;
					blue = 20;
					green = 10;
			elif currentTime.hour == 8:
				red = 200
				blue = 0
				green = 24
			elif currentTime.hour == 9:
				red = 255
				blue = 8
				green = 64
			elif currentTime.hour == 10:
				red = 255
				blue = 32
				green = 96
			elif currentTime.hour == 11:
				red = 255
				blue = 64
				green = 128
			elif currentTime.hour == 12:
				red = 255
				blue = 150
				green = 200
			elif currentTime.hour == 13:
				red = 255
				blue = 255
				green = 255
			elif currentTime.hour == 14:
				red = 255
				blue = 220
				green = 255
			elif currentTime.hour == 15:
				red = 220
				blue = 200
				green = 255
			elif currentTime.hour == 16:
				red = 200
				blue = 200
				green = 255
			elif currentTime.hour == 17:
				red = 200
				blue = 200
				green = 255
			elif currentTime.hour == 18:
				red = 160
				blue = 200
				green = 255
			elif currentTime.hour == 19:
				red = 40
				blue = 255
				green = 255
			elif currentTime.hour == 20:
				red = 20
				blue = 255
				green = 255
			elif currentTime.hour == 21:
				red = 128
				blue = 255
				green = 128
			elif currentTime.hour == 22:
			
				red = 196
				blue = 255
				green = 128
			elif currentTime.hour == 23:
				red = 255
				blue = 255
				green = 0
			Fade(red, blue, green, rpi, bpi, gpi, 0.05)
			rpi = red
			bpi = blue
			gpi = green
		elif currentTime.hour < hour:
			hour = 0
		



##DECLARING VARIABLES//////////////////////////////////////////////
#window
gameWindow = pygame.display.set_mode((300,450))
gameActive = 1;
#Daylight button and Stars
daylight = 0
stars = 0
#current color values of lights
rpi = 0
bpi = 0
gpi = 0
#ideal color values of lights 
red = 0
blue = 0
green = 0

##COLOR CHANGERS///////////////////////////////////////////////////
#red up
rubox = pygame.draw.rect(gameWindow, (255,50,50), (210, 0, 90, 39))
#blue up
bubox = pygame.draw.rect(gameWindow, (50,50,255), (210, 80, 90, 39))
#green up
gubox = pygame.draw.rect(gameWindow, (50,255,50), (210, 160, 90, 39))
#red down
rdbox = pygame.draw.rect(gameWindow, (153,0,0), (210, 40, 90, 39))
#blue down
bdbox = pygame.draw.rect(gameWindow, (0,0,153), (210, 120, 90, 39))
#green down
gdbox = pygame.draw.rect(gameWindow, (0,153,0), (210, 200, 90, 39))

##PRESETS/////////////////////////////(R,G,B) (Xstart,Ystart,Xlen,Ylen)
#1- RED
r1box = pygame.draw.rect(gameWindow, (255,0,0), (0, 0, 200, 39))
#2- ORANGE
r2box = pygame.draw.rect(gameWindow, (255,128,0), (0, 40, 200, 39))
#3
r3box = pygame.draw.rect(gameWindow, (255,255,0), (0, 80, 200, 39))
#4
r4box = pygame.draw.rect(gameWindow, (128,255,0), (0, 120, 200, 39))
#5
r5box = pygame.draw.rect(gameWindow, (0,255,128), (0, 160, 200, 39))
#6
r6box = pygame.draw.rect(gameWindow, (0,255,255), (0, 200, 200, 39))
#7
r7box = pygame.draw.rect(gameWindow, (0,128,255), (0, 240, 200, 39))
#8
r8box = pygame.draw.rect(gameWindow, (0,0,255), (0, 280, 200, 39))
#9
r9box = pygame.draw.rect(gameWindow,  (153,51,255), (0, 320, 200, 39))
#10
r10box = pygame.draw.rect(gameWindow, (255,0,255), (0, 360, 200, 39))
#11-- DAYLIGHT
r11box = pygame.draw.rect(gameWindow, (51,255,100), (0, 400, 200, 39))
#12-- STARS
r12box = pygame.draw.rect(gameWindow, (51,255,100), (210, 400, 100, 39))

##BRIGHTNESS/////////////////////////////////////////////////////////
#white
wbox = pygame.draw.rect(gameWindow, (255,255,255), (210, 280, 99, 59))
#black
bbox = pygame.draw.rect(gameWindow, (10,10,10), (210, 340, 99, 59))

##IMAGES////////////////////////////////////////////////////////////
sun = pygame.image.load("sun.png")
gameWindow.blit(sun, r11box )
starspic = pygame.image.load("stars.png")
gameWindow.blit(starspic, r12box )

##MAIN PROGRAM//////////////////////////////////////////////////////
pygame.display.update()
while(gameActive):
	evList = pygame.event.get()
	for event in evList:
		if event.type == pygame.QUIT:
			gameActive = 0
		if event.type == pygame.MOUSEBUTTONUP:
			msPos = pygame.mouse.get_pos()	
			daylight = 0
			if r1box.collidepoint(msPos):
				red = 255
				green = 0
				blue = 0
			elif r2box.collidepoint(msPos):
				red = 255
				green = 128
				blue = 0
			elif r3box.collidepoint(msPos):
				red = 255
				green = 255
				blue = 0
			elif r4box.collidepoint(msPos):
				red = 128
				green = 255
				blue = 0
			elif r5box.collidepoint(msPos):
				red = 0
				green = 255
				blue = 128
			elif r6box.collidepoint(msPos):
				red = 0
				green = 255
				blue = 255
			elif r7box.collidepoint(msPos):
				red = 0
				green = 128
				blue = 255
			elif r8box.collidepoint(msPos):
				red = 0
				green = 0
				blue = 255
			elif r9box.collidepoint(msPos):
				red = 153
				green = 51
				blue = 255
			elif r10box.collidepoint(msPos):
				red = 255
				green = 0
				blue = 255
			elif r11box.collidepoint(msPos):
				daylight = 1
				stars = 0
			elif r12box.collidepoint(msPos):
				daylight = 1
				stars = 1
			elif wbox.collidepoint(msPos):
				red = 255
				blue = 255
				green = 255
			elif bbox.collidepoint(msPos):
				red = 0
				blue = 0
				green = 0
			elif bubox.collidepoint(msPos):
				blue += 10
			elif rubox.collidepoint(msPos):
				red += 10
			elif gubox.collidepoint(msPos):
				green += 10
			elif bdbox.collidepoint(msPos):
				blue -= 10
			elif rdbox.collidepoint(msPos):
				red -= 10
			elif gdbox.collidepoint(msPos):
				green -= 10
		if red > 255:
			red = 255
		if blue > 255:
			blue = 255
		if green > 255:
			green = 255
		if red < 0:
			red = 0
		if blue < 0:
			blue = 0
		if green < 0:
			green = 0
		if daylight == 1:
			evList = pygame.event.clear()
			daylight = Circadian(rpi, bpi, gpi, stars) #returns 0 to quit
			if daylight == 0:
				gameActive = 0
		Fade(red, blue, green, rpi, bpi, gpi, 0.01)
		rpi = red
		bpi = blue
		gpi = green		
pi.stop()
pygame.quit()
quit()