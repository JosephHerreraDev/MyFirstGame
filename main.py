import pygame

#Initilize the pygame
pygame.init()

#Create the screen
screen = pygame.display.set_mode((800,600))

#While cycle to keep the window open
running = True
while running:
    #Checks for all events running
    for event in pygame.event.get():
        #Checks for the event QUIT to close the window
        if event.type == pygame.QUIT:
            running = False
