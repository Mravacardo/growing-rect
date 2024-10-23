import pygame
pygame.init()
screen = pygame.display.set_mode([500,500])
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
yellow = (255,255,0)
black = (0,0,0)
purple = (255,0,255)

screen.fill(white)

class myRect():
    def __init__(self,colour, pos, width, height, wid=0):
        self.colour = colour
        self.pos = pos
        self.width = width
        self.wid = wid
        self.scrn = screen

    def draw(self):
        pygame.draw.rect(self.scrn, self.colour, self.pos, self.width, self.height, self.wid )

    def grow(self,x):
        self.width += x
        self.height += y
        pygame.draw.rect(self.scrn, self.colour, self.pos, self.width, self.height, self.wid )

position = (200,200)
width = 100
height = 50
wid = 2
pygame.draw.rect(screen, red, position, width, height, wid)
pygame.display.update()

blueRect = myRect(blue, position, width+60, height+60)
redRect = myRect(red, position, width+40, height+40)
yellowRect = myRect(yellow, position, width, height, 5)
greenRect = myRect(green, position, 20)
purpleRect = myRect(purple, position, width+120, height+120)

while(1):
    for event in pygame.event.get():
        if (event.type == pygame.MOUSEBUTTONDOWN):
            blueRect.draw()
            redRect.draw()
            yellowRect.draw()
            greenRect.draw()
            purpleRect.draw()
            pygame.display.update()
        elif (event.type == pygame.MOUSEBUTTONUP):
            blueRect.grow(2)
            redRect.grow(2)
            yellowRect.grow(2)
            greenRect.grow(2)
            purpleRect.grow(2)
            pygame.display.update()
        elif (event.type == pygame.MOUSEMOTION):
            pos = pygame.mouse.get_pos()
            blackRect = myRect(black, pos, 5)
            blackRect.draw()
            pygame.display.update()

        elif event.type == pygame.QUIT:
            pygame.quit()
