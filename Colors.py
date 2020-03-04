import pygame
import pigpio
import time
import datetime
import random
pygame.init()
pi= pigpio.pi()

class LightValue:

    def __init__(self,x):
        self.__x = x

    def get(self):
        return self.__x

    def set(self, x):
        self.__x = x

        
def ChangeLight(currentLight, ideal):
    if currentLight.get() < ideal.get():
        currentLight.set(currentLight.get() +1)
    if currentLight.get() > ideal.get():
        currentLight.set(currentLight.get() -1)
        
def SetRGBValues(red, green, blue, rval, gval, bval): #sets ideal values
    red.set(rval)
    green.set(gval)
    blue.set(bval)
        

def Fade(red, green, blue, rpi, gpi, bpi, speed):
    while (rpi.get() != red.get() or gpi.get() != green.get() or bpi.get() != blue.get()):
        ChangeLight(rpi, red)
        ChangeLight(gpi, green)
        ChangeLight(bpi, blue)
        pi.set_PWM_dutycycle(17, rpi.get())
        pi.set_PWM_dutycycle(22, gpi.get())		
        pi.set_PWM_dutycycle(24, bpi.get())
        time.sleep(speed)

def PartyLight(rpi, gpi, bpi, speed):
    while (1):
        evList = pygame.event.get()
        for event in evList:
            if event.type == pygame.QUIT:
                print("out of the Party, Quit")
                return 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                msPos = pygame.mouse.get_pos()
                if not (p1box.collidepoint(msPos) or p2box.collidepoint(msPos)):
                    print("out of the Party :(")
                    return 2
                elif p1box.collidepoint(msPos):
                    speed = 0
                elif p2box.collidepoint(msPos):  
                    speed = 0.01
        red.set(random.randint(0,2) * 127)
        green.set(random.randint(0,2) * 127)
        blue.set(random.randint(0,2) * 127)              
        if (red.get() == 0 and blue.get() == 0 and green.get() ==0):
            SetRGBValues(red, green, blue, 255,255,255)
        Fade(red, green, blue, rpi, bpi, gpi, speed)
        time.sleep(0.2)



        
def Circadian(rpi, gpi, bpi, stars):
    hour = 0
    evList= pygame.event.clear()
    while (1):
        
        ##Collecting Events, Quit Conditions
        #print("Circadian loop start")
        evList = pygame.event.get()
        for event in evList:
            if event.type == pygame.QUIT:
                print("out of Circadian, Quit")
                return 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                msPos = pygame.mouse.get_pos()
                if not (r11box.collidepoint(msPos) or r12box.collidepoint(msPos)):
                    print("out of Circadian")
                    return 2
                elif r11box.collidepoint(msPos):
                    stars = 0
                elif r12box.collidepoint(msPos):  
                    stars = 1
        ##Collecting Time, Hour Changes
        currentTime = datetime.datetime.now()
        if currentTime.hour < hour:
            hour = 0
            if stars == 0:
                SetRGBValues(red, green, blue, 0, 0, 0)
            else:
                SetRGBValues(red, green, blue, 10, 10, 20)
            Fade(red, green, blue, rpi, gpi, bpi, 0.05)
        if currentTime.hour > hour:
            print("Hour Change!")
            hour +=1
            if currentTime.hour < 8:
                if stars == 0:
                    SetRGBValues(red, green, blue, 0, 0, 0)
                else:
                    SetRGBValues(red, green, blue, 10, 10, 20) 
            elif currentTime.hour == 8:
                SetRGBValues(red, green, blue, 192, 32, 0)
            elif currentTime.hour == 9:
                SetRGBValues(red, green, blue, 224, 128, 0)
            elif currentTime.hour == 10:
                SetRGBValues(red, green, blue, 255, 192, 128)
            elif currentTime.hour == 11:
                SetRGBValues(red, green, blue, 255,224,192)
            elif currentTime.hour == 12:
                SetRGBValues(red, green, blue, 255,255,192)
            elif currentTime.hour == 13:
                SetRGBValues(red, green, blue, 255,255,255)
            elif currentTime.hour == 14:
                SetRGBValues(red, green, blue, 224,255,224)
            elif currentTime.hour == 15:
                SetRGBValues(red, green, blue, 192,255,224)
            elif currentTime.hour == 16:
                SetRGBValues(red, green, blue, 192,255,255)
            elif currentTime.hour == 17:
                SetRGBValues(red, green, blue, 192,240,255)
            elif currentTime.hour == 18:
                SetRGBValues(red, green, blue, 224,224,255)
            elif currentTime.hour == 19:
                SetRGBValues(red, green, blue, 224,192,255)
            elif currentTime.hour == 20:
                SetRGBValues(red, green, blue, 240,192,255)
            elif currentTime.hour == 21:
                SetRGBValues(red, green, blue, 240,128,255)
            elif currentTime.hour == 22:
                SetRGBValues(red, green, blue, 255,128,255)
            elif currentTime.hour == 23:
                SetRGBValues(red, green, blue, 128,0,128)
            Fade(red, green, blue, rpi, gpi, bpi, 0.05)
            
###Main

#window
gameWindow = pygame.display.set_mode((300,450))
gameActive = 1;
daylight = 0
stars = 0

#Light Values (current vs ideal)
rpi = LightValue(255)
gpi = LightValue(255)
bpi = LightValue(255)
red = LightValue(255)
green = LightValue(255)
blue = LightValue(255)

#Defining buttons (R,G,B) (Xstart,Ystart,Xlen,Ylen)
rubox = pygame.draw.rect(gameWindow, (255,50,50), (210, 0, 90, 39))     #red up
gubox = pygame.draw.rect(gameWindow, (50,255,50), (210, 160, 90, 39))   #green up
bubox = pygame.draw.rect(gameWindow, (50,50,255), (210, 80, 90, 39))    #blue up

rdbox = pygame.draw.rect(gameWindow, (153,0,0), (210, 40, 90, 39))      #red down
gdbox = pygame.draw.rect(gameWindow, (0,153,0), (210, 200, 90, 39))     #green down
bdbox = pygame.draw.rect(gameWindow, (0,0,153), (210, 120, 90, 39))     #blue down

r1box = pygame.draw.rect(gameWindow, (255,0,0), (0, 0, 200, 39))        #red
r2box = pygame.draw.rect(gameWindow, (255,128,0), (0, 40, 200, 39))     #orange
r3box = pygame.draw.rect(gameWindow, (255,255,0), (0, 80, 200, 39))     #yellow
r4box = pygame.draw.rect(gameWindow, (128,255,0), (0, 120, 200, 39))    #green
r5box = pygame.draw.rect(gameWindow, (0,255,128), (0, 160, 200, 39))    #blueishgreen
r6box = pygame.draw.rect(gameWindow, (0,255,255), (0, 200, 200, 39))    #bluegreen
r7box = pygame.draw.rect(gameWindow, (0,128,255), (0, 240, 200, 39))    #mostlyblue
r8box = pygame.draw.rect(gameWindow, (0,0,255), (0, 280, 200, 39))      #blue
r9box = pygame.draw.rect(gameWindow, (153,51,255), (0, 320, 200, 39))   #purple
r10box = pygame.draw.rect(gameWindow, (255,0,255), (0, 360, 200, 39))   #light purple

r11box = pygame.draw.rect(gameWindow, (51,255,100), (0, 400, 200, 39))  #Daylight/Circadian Button
r12box = pygame.draw.rect(gameWindow, (51,255,100), (210, 400, 100, 39))#Stars button

wbox = pygame.draw.rect(gameWindow, (255,255,255), (210, 280, 99, 29))  #white/increase brightness
bbox = pygame.draw.rect(gameWindow, (10,10,10), (210, 310, 99, 29))     #black/decrease brightness

p1box = pygame.draw.rect(gameWindow, (255,0,235), (210, 340, 99, 29))   #party 1 box
p2box = pygame.draw.rect(gameWindow, (235,0,255), (210, 370, 99, 29))   #party 2 box


#import images
sun = pygame.image.load("sun.png")
gameWindow.blit(sun, r11box )
starspic = pygame.image.load("stars.png")
gameWindow.blit(starspic, r12box )

##Main loop
while(gameActive):
    evList = pygame.event.get()
    for event in evList:
        if event.type == pygame.QUIT:
            gameActive = 0
        if event.type == pygame.MOUSEBUTTONUP:
            msPos = pygame.mouse.get_pos()	
            daylight = 0 #pulls out of circadian at every click, but then puts it back in if that was the click
            if r1box.collidepoint(msPos):
                SetRGBValues(red, green, blue, 255,0,0)
            elif r2box.collidepoint(msPos):
                SetRGBValues(red, green, blue, 255, 128, 0)
            elif r3box.collidepoint(msPos):
                SetRGBValues(red, green, blue, 255, 255, 0)
            elif r4box.collidepoint(msPos):
                SetRGBValues(red, green, blue, 128, 255,0)
            elif r5box.collidepoint(msPos):
                SetRGBValues(red, green, blue, 0,255,128)
            elif r6box.collidepoint(msPos):
                SetRGBValues(red, green, blue, 0,255,255)
            elif r7box.collidepoint(msPos):
                SetRGBValues(red, green, blue, 0,128,255)
            elif r8box.collidepoint(msPos):
                SetRGBValues(red, green, blue, 0,0,255)
            elif r9box.collidepoint(msPos):
                SetRGBValues(red, green, blue, 153,51,255)
            elif r10box.collidepoint(msPos):
                SetRGBValues(red, green, blue, 255,0,255)
            
            elif r11box.collidepoint(msPos):
                daylight = 1
                stars = 0
            elif r12box.collidepoint(msPos):
                daylight = 1    
                stars = 1
    
            elif p1box.collidepoint(msPos):
                PartyLight(rpi, bpi, gpi, 0)
            elif p2box.collidepoint(msPos):
                PartyLight(rpi, bpi, gpi, 0.01)
               
            elif wbox.collidepoint(msPos):
                SetRGBValues(red, green, blue, 255,255,255)
            elif bbox.collidepoint(msPos):
                SetRGBValues(red, green, blue, 0,0,0)
			
            elif rubox.collidepoint(msPos):
                red.set(red.get() + 10)	
            elif gubox.collidepoint(msPos):
                green.set(green.get() + 10)
            elif bubox.collidepoint(msPos):
                blue.set(blue.get() + 10)
            elif rdbox.collidepoint(msPos):
                red.set(red.get() - 10) 
            elif gdbox.collidepoint(msPos):
                green.set(green.get() - 10)
            elif bdbox.collidepoint(msPos):
                    blue.set(blue.get() - 10)
            if red.get() > 255:
                red.set(255)
            if green.get()>255:
                green.set(255)
            if blue.get() > 255:
                blue.set(255)
            if red.get() < 0:
                red.set(0)
            if green.get() < 0:
                green.set(0)
            if blue.get() < 0:
                blue.set(0)
            if daylight == 1:
                evList= pygame.event.clear()
                daylight = Circadian(rpi, gpi, bpi, stars) #returns 0 to quit
                if daylight == 0:
                    gameActive = 0
            Fade(red, green, blue, rpi, gpi, bpi, 0.01)
pi.stop()
pygame.quit()
quit()

