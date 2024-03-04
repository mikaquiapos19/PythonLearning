import pygame #tutorial from Clear Code
from sys import exit #closes any kind of code once you call it

pygame.init() #initiates pygame
screen = pygame.display.set_mode((800, 400)) #creating a display surface - parameter -tuple: width, height
pygame.display.set_caption('Test Game')
clock = pygame.time.Clock() #regulates fps for the game


while True:
    for event in pygame.event.get(): #loops through events; get events
        if event.type == pygame.QUIT: #allows us to close window
            pygame.quit() #un initialise pygame
            exit() 
    #draw all our elements
    #update everything
    pygame.display.update() #updates the display surface 
    clock.tick(60) #game running at 60fps minimum 