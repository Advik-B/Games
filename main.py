import pygame
import asyncio
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

# Key press functions

async def keys_down(key):
    global running
    if key == pygame.K_ESCAPE:
        print("Escape key pressed")
        running = False

async def keys_up(key):
    global running
    if key == pygame.K_ESCAPE:
        running = False
        print("Escape key released")

# Event loop

async def event_loop():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            await keys_down(event.key)
        elif event.type == pygame.KEYUP:
            await keys_up(event.key)

while running:
    asyncio.run(event_loop()) # Call the event loop
    screen.fill('#7289DA')
    pygame.display.update()
else:
    print("Quitting")
    pygame.quit()