import pygame #tutorial from Clear Code
from sys import exit #closes any kind of code once you call it

pygame.init() #initiates pygame
screen = pygame.display.set_mode((800, 400)) #creating a display surface - parameter -tuple: width, height
pygame.display.set_caption('Test Game')
clock = pygame.time.Clock() #regulates fps for the game
test_font = pygame.font.Font('font/Pixeltype.ttf', 50) #(font type, font size)

sky_surface = pygame.image.load('graphics/Sky.png')
ground_surface = pygame.image.load('graphics/ground.png')
text_surface = test_font.render('My game', False, 'Black') #(text, AA, colour) #False for AA because of pixel art. Otherwise, make it True

while True:
    for event in pygame.event.get(): #loops through events; get events
        if event.type == pygame.QUIT: #allows us to close window
            pygame.quit() #un initialise pygame
            exit() 
    #draw all our elements
    #update everything

    screen.blit(sky_surface, (0,0)) #block image transfer (surface, pos) pos = left, top
    screen.blit(ground_surface, (0,300))
    screen.blit(text_surface,(300, 50)) #for text

    pygame.display.update() #updates the display surface 
    clock.tick(60) #game running at 60fps minimum 