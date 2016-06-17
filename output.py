import bluetooth
import re
import pygame,sys
from pygame.locals import *

WINDOWWIDTH=800
WINDOWHEIGHT=800
WHITE     = (255, 255, 255)
BLACK     = (  0,   0,   0)
RED       = (255,   0,   0)
GREEN     = (  0, 255,   0)
DARKGREEN = (  0, 155,   0)
DARKGRAY  = ( 40,  40,  40)
BLUE=(0,0,255)
BGCOLOR = BLACK

server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
port = 1
server_sock.bind(("", port))
server_sock.listen(1)

client_sock, address = server_sock.accept()
print "Accepted connection from ", address

w=60
gap=2
def draw_grid(map_environment):
    global  w,gap
    numrows=len(map_environment)
    numcols=len(map_environment[0])
    for i in range(numcols):
        for j in range(numrows):
            if map_environment[i][j]<0.2:
                color=(225,225,225)
                pygame.draw.rect(DISPLAYSURF,color,((w+gap)*i,(w+gap)*j,w,w))
            elif map_environment[i][j]<0.4:
                color=(180,180,180)
                pygame.draw.rect(DISPLAYSURF,color,((w+gap)*i,(w+gap)*j,w,w))
            elif map_environment[i][j]<0.6:
                color=(120,120,120)
                pygame.draw.rect(DISPLAYSURF,color,((w+gap)*i,(w+gap)*j,w,w))
            elif map_environment[i][j]<0.8:
                color=(75,75,75)
                pygame.draw.rect(DISPLAYSURF,color,((w+gap)*i,(w+gap)*j,w,w))
            elif map_environment[i][j]<1:
                color=(25,25,25)
                pygame.draw.rect(DISPLAYSURF,color,((w+gap)*i,(w+gap)*j,w,w))
            elif map_environment[i][j]==1:
                color=(0,0,0)
                pygame.draw.rect(DISPLAYSURF,color,((w+gap)*i,(w+gap)*j,w,w))
class my_bot(object):
    def __init__(self):
        self.botimg=pygame.image.load('bot.png')
        self.ypos=13.4*w/2# xpos,ypos is coordinate of centre
        self.xpos=13.4*w/2
        self.direction='North'
        self.size=self.botimg.get_width()
    def display(self):
        DISPLAYSURF.blit(self.botimg,(self.xpos-(self.size/2),self.ypos-(self.size/2)))
    def forward(self):
        if self.direction=='West':    
            for counter in range(w+gap):
                DISPLAYSURF.fill(WHITE)
                draw_grid(map_environment)
                self.ypos=self.ypos-1
                self.display()
                pygame.display.update()
                pygame.time.wait(50)
        elif self.direction=='North':
            for counter in range(w+gap):
                DISPLAYSURF.fill(WHITE)
                draw_grid(map_environment)
                self.xpos=self.xpos-1
                self.display()
                pygame.display.update()
                pygame.time.wait(50)
        elif self.direction=='East':
            for counter in range(w+gap):
                DISPLAYSURF.fill(WHITE)
                draw_grid(map_environment)
                self.ypos=self.ypos+1
                self.display()
                pygame.display.update()
                pygame.time.wait(50)
        elif self.direction=='South':
            for counter in range(w+gap):
                DISPLAYSURF.fill(WHITE)
                draw_grid(map_environment)
                self.xpos=self.xpos+1
                self.display()
                pygame.display.update()
                pygame.time.wait(50)
    # sense refers to clockwise or anticlockwise
    def turn(self,sense):
        if sense=='clockwise':
            #imgrect=self.botimg.get_rect()
            for angle in range(90):
                DISPLAYSURF.fill(WHITE)
                draw_grid(map_environment)
                #self.botimg=pygame.transform.rotate(self.botimg,angle)
                rotatedsurf=pygame.transform.rotate(self.botimg,angle)
                oldCenter=(self.xpos,self.ypos)
                rotrect=rotatedsurf.get_rect()
                rotrect.center=oldCenter
                DISPLAYSURF.blit(rotatedsurf,rotrect)
                pygame.display.update()
                pygame.time.wait(50)
            if angle>=89:
                if self.direction=='North':
                    self.direction='West'
                elif self.direction=='West':
                    self.direction='South'
                elif self.direction=='South':
                    self.direction='East'
                elif self.direction=='East':
                    self.direction='North'         
            
        elif sense=='anticlockwise':
            for angle in range(90):
                DISPLAYSURF.fill(WHITE)
                draw_grid(map_environment)
                #self.botimg=pygame.transform.rotate(self.botimg,-angle)
                rotatedsurf=pygame.transform.rotate(self.botimg,-angle)
                oldCenter=(self.xpos,self.ypos)
                rotrect=rotatedsurf.get_rect()
                rotrect.center=oldCenter
                DISPLAYSURF.blit(rotatedsurf,rotrect)
                pygame.display.update()
            if angle>=89:
                if self.direction=='North':
                    self.direction='East'
                elif self.direction=='East':
                    self.direction='South'
                elif self.direction=='South':
                    self.direction='West'
                elif self.direction=='West':
                    self.direction='North'
pygame.init()
#FPSCLOCK=pygame.time.Clock()
DISPLAYSURF=pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
pygame.display.set_caption('ITSP MAP')
Jockey=my_bot()
counter = 0
while True:
    map_width = 13
    map_environment = [[0.00 for i in range(map_width)] for j in range(map_width)]
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    data = client_sock.recv(1024)
    row = 0
    column = 0
    for prob in re.findall(r"[-+]?\d*\.\d+|\d+", data):
        map_environment[row][column] = float(prob)
        column += 1
        if column == map_width:
            column = 0
            row += 1
        if row == map_width:
            break
    for x in map_environment:
       print x
    print ""
    motion = data[-1]
    DISPLAYSURF.fill(WHITE)
    draw_grid(map_environment)# will draw grid according to map
    if motion=='F':
        Jockey.forward()
    elif motion=='R':
        Jockey.turn('anticlockwise')
        Jockey.forward()
    elif motion=='U':
        Jockey.turn('clockwise')
        Jockey.turn('clockwise')
        Jockey.forward()
    elif motion=='L':
        Jockey.turn('clockwise')
        Jockey.forward()    
    pygame.display.update()     
    #pygame.time.wait(600)    
