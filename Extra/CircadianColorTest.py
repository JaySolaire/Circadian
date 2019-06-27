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
		pi.set_PWM_dutycycle(24, gpi)		
		pi.set_PWM_dutycycle(22, bpi)
		time.sleep(speed)


#current color values of lights
rpi = 1
bpi = 1
gpi = 1
#ideal color values of lights 
red = 0
blue = 0
green = 0
Click = 0
gameActive = 1
gameWindow = pygame.display.set_mode((300,450))
while(gameActive):
	evList = pygame.event.get()
	for event in evList:
		if event.type == pygame.QUIT:
			gameActive = 0
		if event.type == pygame.MOUSEBUTTONUP:
			Click = Click + 1
		if Click < 8:
			red = 8;
			blue = 20;
			green = 8;
		elif Click == 8:
			red = 200
			blue = 0
			green = 24
		elif Click == 9:
			red = 255
			blue = 8
			green = 64
		elif Click == 10:
			red = 255
			blue = 32
			green = 96
		elif Click == 11:
			red = 255
			blue = 64
			green = 128
		elif Click == 12:
			red = 255
			blue = 200
			green = 200
		elif Click == 13:
			red = 255
			blue = 255
			green = 255
		elif Click == 14:
			red = 220
			blue = 220
			green = 255
		elif Click == 15:
			red = 220
			blue = 200
			green = 255
		elif Click == 16:
			red = 200
			blue = 200
			green = 255
		elif Click == 17:
			red = 20
			blue = 60
			green = 20
		elif Click == 18:
			red = 20
			blue = 60
			green = 20
		elif Click == 19:
			red = 20
			blue = 255
			green = 255
		elif Click == 20:
			red = 0
			blue = 255
			green = 255
		elif Click == 21:
			red = 128
			blue = 255
			green = 128
		elif Click == 22:
			red = 128
			blue = 255
			green = 128
		elif Click == 23:
			red = 255
			blue = 255
			green = 0
			#add special purple before beedd
		elif Click == 24:
			Click = 0
		print (Click)
		Fade(red, blue, green, rpi, bpi, gpi, 0.01)
		rpi = red
		bpi = blue
		gpi = green
pi.stop()
pygame.quit()
quit()