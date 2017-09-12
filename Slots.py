import pygame
import random
import sys
import time

pygame.init()
red = (255,0,0)
black = (0,0,0)
white = (255,255,255)
green = (0,200,0)
yellow = (0,255,0)
blue = (0,0,200)
bright_blue = (0,0,250)
jackpotwhite = (238,238,238)
#all my colors

display_width = 800
display_height = 600
#display of the screen

firstloc = (295,300)
secondloc = (382,300)
thirdloc = (469,300)
#locations of the items

gameDisplay = pygame.display.set_mode((display_width, display_height))
greeting = ("Welcome to Slots. Press s to start!")
backloc = (-100,-150)

pygame.display.set_caption('Slots')
c = pygame.image.load('/Users/peterdunbar/Downloads/Cherry-512_py.png')
c = pygame.transform.scale(c,(45,45))
s = pygame.image.load('/Users/peterdunbar/Downloads/7_py.png')
s = pygame.transform.scale(s, (45,45))
b = pygame.image.load('/Users/peterdunbar/Downloads/Bar_PNG.png')
b = pygame.transform.scale(b, (45,45))
h = pygame.image.load('/Users/peterdunbar/Downloads/heart-png.png')
h = pygame.transform.scale(h, (45,45))
background_image = pygame.image.load('/Users/peterdunbar/Downloads/slot_machine.png').convert()
#loading all the images and scaling them


global d
d = {0 : c , 1 : s, 2 : b, 3 : h}
#list for the dicionary number for the images

def start():
    small = pygame.font.SysFont('none', 18)
    x = small.render(greeting, True, red)
    gameDisplay.blit(x, (100,100))
    #displays start

def score():
    large = pygame.font.SysFont('none', 30)
    b = large.render(str(count), True, red)
    gameDisplay.blit(b, (620,60))
    #displays the score of the game

def intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(red)
        global big
        big = pygame.font.SysFont('none', 80)
        t = big.render('SLOTS', True, white)
        gameDisplay.blit(t, (200,200))
        #Showing the text Font

        mouse = pygame.mouse.get_pos()
        if 150+100 > mouse[0] > 150 and 450 + 60 > mouse[1] > 450:
            #measures x axis and y axis, and shows it bright_green if its 
            pygame.draw.rect(gameDisplay, yellow, (100,450,150,60))
            d = big.render("Play", True, black)
            gameDisplay.blit(d, (100,450))
            if event.type == pygame.MOUSEBUTTONDOWN:
                break
        else:
            pygame.draw.rect(gameDisplay, green, (100,450,150,60))
            d = big.render("Play", True, blue)
            gameDisplay.blit(d, (100,450))
        
            
        if 550+150 > mouse[0] > 550 and 450 + 60 > mouse[1] > 450:
            pygame.draw.rect(gameDisplay, blue, (550,450,150,60))
            a = big.render("Quit", True, black)
            gameDisplay.blit(a, (550,450))
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                quit()
        else:
            pygame.draw.rect(gameDisplay, blue, (550,450,150,60))
            a = big.render("Quit", True, green)
            gameDisplay.blit(a, (550,450))
                           
        print(mouse)
        pygame.display.update()
        
    
        
        
    

def cherry(loc, dem):
    gameDisplay.blit(c, loc)
    pygame.display.update()
    time.sleep(.2)
    gameDisplay.fill(jackpotwhite, rect = dem)
    pygame.display.update()
    #displays the cherrys location

def seven(loc, dem):
    gameDisplay.blit(s, loc)
    pygame.display.update()
    time.sleep(.2)
    gameDisplay.fill(jackpotwhite, rect = dem)
    pygame.display.update()
    #displays the seven location

def bar(loc, dem):
    gameDisplay.blit(b, loc)
    pygame.display.update()
    time.sleep(.2)
    gameDisplay.fill(jackpotwhite, rect = dem)
    pygame.display.update()
    #displays the bar location

def heart(loc, dem):
    gameDisplay.blit(h, loc)
    pygame.display.update()
    time.sleep(.2)
    gameDisplay.fill(jackpotwhite, rect = dem)
    pygame.display.update()
    #displays the  heart location
    
def final(loc):
    r = random.randint(0,3)
    lst.append(r)
    gameDisplay.blit(d[r], loc)
    pygame.display.update()
    time.sleep(.1)
    
def evaluate():
    global count
    global lst
    if lst == [0,0,0]:
        count += 500
    elif lst == [0,0,1]:
        count += 200
    elif lst == [0,0,2]:
        count += 200
    elif lst == [0,0,3]:
        count += 200
    elif lst == [0,1,0]:
        count += 200
    elif lst == [0,1,1]:
        count += 200
    elif lst == [0,1,2]:
        count += 100
    elif lst == [0,1,3]:
        count += 100
    elif lst == [0,2,0]:
        count += 200
    elif lst == [0,2,1]:
        count += 100
    elif lst == [0,2,2]:
        count += 200
    elif lst == [0,2,3]:
        count += 100
    elif lst == [0,3,0]:
        count += 200
    elif lst == [0,3,1]:
        count += 100
    elif lst == [0,3,2]:
        count += 100
    elif lst == [0,3,3]:
        count += 200
    elif lst == [1,0,0]:
        count += 200
    elif lst == [1,0,1]:
        count += 200
    elif lst == [1,0,2]:
        count += 100
    elif lst == [1,0,3]:
        count += 100
    elif lst == [1,1,0]:
        count += 200
    elif lst == [1,1,1]:
        count += 500
    elif lst == [1,1,2]:
        count += 200
    elif lst == [1,1,3]:
        count += 200
    elif lst == [1,2,0]:
        count += 100
    elif lst == [1,2,1]:
        count += 200
    elif lst == [1,2,2]:
        count += 200
    elif lst == [1,2,3]:
        count += 100
    elif lst == [1,3,0]:
        count += 100
    elif lst == [1,3,1]:
        count += 100
    elif lst == [1,3,2]:
        count += 100
    elif lst == [1,3,3]:
        count += 200
    elif lst == [2,0,0]:
        count += 200
    elif lst == [2,0,1]:
        count += 100
    elif lst == [2,0,2]:
        count += 200
    elif lst == [2,0,3]:
        count += 100
    elif lst == [2,1,0]:
        count += 100
    elif lst == [2,1,1]:
        count += 200
    elif lst == [2,1,2]:
        count += 200
    elif lst == [2,1,3]:
        count += 100
    elif lst == [2,2,0]:
        count += 200
    elif lst == [2,2,1]:
        count += 200
    elif lst == [2,2,2]:
        count += 500
    elif lst == [2,2,3]:
        count += 200
    elif lst == [2,3,0]:
        count += 100
    elif lst == [2,3,1]:
        count += 100
    elif lst == [2,3,2]:
        count += 200
    elif lst == [2,3,3]:
        count += 200
    elif lst == [3,0,0]:
        count += 200
    elif lst == [3,0,1]:
        count += 100
    elif lst == [3,0,2]:
        count += 100
    elif lst == [3,0,3]:
        count += 200
    elif lst == [3,1,0]:
        count += 100
    elif lst == [3,1,1]:
        count += 200
    elif lst == [3,1,2]:
        count += 100
    elif lst == [3,1,3]:
        count += 200
    elif lst == [3,2,0]:
        count += 100
    elif lst == [3,2,1]:
        count += 100
    elif lst == [3,2,2]:
        count += 200
    elif lst == [3,2,3]:
        count += 200
    elif lst == [3,3,0]:
        count += 200
    elif lst == [3,3,1]:
        count += 200
    elif lst == [3,3,2]:
        count += 200
    elif lst == [3,3,3]:
        count += 500       
        
    #picks final image, then puts that number into a list


#--------------Main Loop-----------------
intro()

gameExit = False
count = 0
lst = []
while not gameExit:
    for event in pygame.event.get():
        print(event)
        #getting events in program
        if event.type == pygame.QUIT:
            gameExit = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                #checks if a key is hit down, and if its the s key
                
                cherry(firstloc, [288,300,79,78])
                seven(firstloc, [288,300,79,78])
                bar(firstloc, [288,300,79,78])
                heart(firstloc, [288,300,79,78])
                #displaying the images at location, second is where to fill and how large
                
                final(firstloc)
                #displaying the final image the casino picked
                cherry(secondloc, [375,300, 79, 78])
                seven(secondloc, [375,300, 79, 78])
                bar(secondloc, [375,300, 79, 78])
                heart(secondloc, [375,300, 79, 78])
                
                final(secondloc)
                
                cherry(thirdloc, [462,300,79,78])
                seven(thirdloc, [462,300,79,78])
                bar(thirdloc, [462,300,79,78])
                heart(thirdloc, [462,300,79,78])
                
                final(thirdloc)
                evaluate()
                lst = []
                time.sleep(1)
                
              
    
    gameDisplay.blit(background_image, backloc)
    q = pygame.font.SysFont('none', 80)
    z = q.render('QUIT', True, white)
    gameDisplay.blit(z, (600,150))
    gameDisplay.fill(jackpotwhite, [288,300,252,78])
    start()
    score()
    pygame.display.update()

    
             
pygame.quit()
quit()
