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
player_img = pygame.image.load("gun.png")
player_x = disp.current_w * .05
player_y = disp.current_h * .4
player_released = False

def player():
    global player_img, player_x, player_y
    screen.blit(player_img, (player_x, player_y))

# Bullet
bullet_img = pygame.image.load("bullet.png")
bullet_x = player_x + player_img.get_width() * 2 * .51
bullet_y = player_y * .985
bullet_ready = True
bullet_x_change = 10

def __fire_bullet():
    
    while True:
        global bullet_x, bullet_y, bullet_x_change, disp
        def step():
            global bullet_x, bullet_y, bullet_x_change, disp
            if bullet_x > disp.current_w:
                bullet_y += bullet_x_change
                bullet_x -= bullet_x_change
            else:
                bullet_x += bullet_x_change
        step()
        sleep(.01)

def fire_bullet():
    t = Thread(target=__fire_bullet)
    t.daemon = True  # thread dies when main thread exits.
    t.start()

# Main loop
running = True

# Key press functions

def keys_down(key):
    global running, player_x, player_y, player_released, bullet_ready
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
    
    if key == pygame.K_SPACE:
        print("Space key pressed")
        if bullet_ready:
            bullet_ready = False
            fire_bullet()
            sleep(.5)
            bullet_ready = True
            

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
    screen.blit(bullet_img, (bullet_x, bullet_y))
    pygame.display.update()
else:
    print("Quitting Game")
    pygame.quit()
    close(0)