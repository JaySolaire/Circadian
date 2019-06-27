import pygame
import time
import datetime
pygame.init()
#gameWindow = pygame.display.set_mode((300,450))
time.sleep(4)
print("hi")
currentTime = datetime.datetime.now()
gameActive = 1
while (gameActive):
		evList = pygame.event.get()
		for event in evList:
			if event.type == pygame.QUIT:
				print("quit")
				time.sleep(1)
				gameActive = 0
			print ("loop ends")
		print ("====================================== main loop ends")
		time.sleep(1)
		