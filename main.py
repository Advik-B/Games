import pygame
import asyncio
from threading import Thread
from time import sleep
from sys import exit as close
# from PIL import Image


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

# Player character
disp = pygame.display.Info()
player_img = pygame.image.load("sport-car.png")
player_x = disp.current_w * .05
player_y = disp.current_h * .4
player_released = False

def player():
    global player_img, player_x, player_y
    screen.blit(player_img, (player_x, player_y))

# Main loop
running = True

# Key press functions

def keys_down(key):
    global running, player_x, player_y, player_released
    if key == pygame.K_ESCAPE:
        print("Escape key pressed")
        running = False
    if key == pygame.K_UP:
        print("Up key pressed")
        while player_released is False:
            player_y -= 10
            sleep(.03)
        else:
            player_released = False
 
        
    if key == pygame.K_DOWN:
        print("Down key pressed")
        while player_released is False:
            player_y += 10
            sleep(.03)
        else:
            player_released = False

    close(0)


def keys_up(key):
    global running, player_x, player_y, player_released
    if key == pygame.K_ESCAPE:
        running = False
        print("Escape key released")
 
    if key == pygame.K_UP:
        print("Up key realesed")
        player_released = True

    if key == pygame.K_DOWN:
        print("Down key released")
        player_released  = True

    close(0)

# Event loop

async def event_loop():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            t = Thread(target=keys_down, args=(event.key,))
            t.daemon = True  # thread dies when main thread exits.
            t.start()
        elif event.type == pygame.KEYUP:
            t = Thread(target=keys_up, args=(event.key,))
            t.daemon = True  # thread dies when main thread exits.
            t.start()

while running:
    asyncio.run(event_loop()) # Call the event loop
    screen.fill('#7289DA')
    player()
    pygame.display.update()
else:
    print("Quitting Game")
    pygame.quit()
    close(0)