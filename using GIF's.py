import pygame
from PIL import Image


pygame.init()
# Resizing the window
screen = pygame.display.set_mode(
    
    (
        pygame.display.Info().current_w * .6,
        pygame.display.Info().current_h * .7 
        
    )
        )
# Set window title
pygame.display.set_caption("<A name for the game>")
# Set window icon
pygame.display.set_icon(pygame.image.load("cool.png"))

running = True

def keys(key):
    global running
    if key == pygame.K_ESCAPE:
        running = False
    

def event_loop():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            keys(event.key)

while running:
    event_loop() # Call the event loop

pygame.quit()