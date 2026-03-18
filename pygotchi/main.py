# main.py
import pygame
import time
import os
from gotchi import Gotchi

# --- Constants ---
BG_COLOR = (255, 255, 255)
TICK_INTERVAL = 1  # seconds per gametick
IMG_SIZE = (150, 150)  # scaled image size

# --- Initialize Pygame ---
pygame.init()
BASE_DIR = os.path.dirname(__file__)
screen_width = 250
screen_height = 300
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("PyGotchi")
font = pygame.font.SysFont(None, 24)
clock = pygame.time.Clock()

# --- Paths for images ---
IMG_ALIVE = os.path.join(BASE_DIR, "images", "Platypus.png")
IMG_RIP   = os.path.join(BASE_DIR, "images", "RIP.png")

# --- Load and scale images ---
if not os.path.exists(IMG_ALIVE):
    raise FileNotFoundError(f"Image not found: {IMG_ALIVE}")
img_alive = pygame.image.load(IMG_ALIVE)
img_alive = pygame.transform.scale(img_alive, IMG_SIZE)

if os.path.exists(IMG_RIP):
    img_rip = pygame.image.load(IMG_RIP)
    img_rip = pygame.transform.scale(img_rip, IMG_SIZE)
else:
    img_rip = img_alive  # fallback

# --- Create Gotchi ---
g = Gotchi("Frits")
last_tick = time.time()
running = True

# --- Buttons setup ---
feed_button = pygame.Rect(30, 220, 80, 30)
play_button = pygame.Rect(140, 220, 80, 30)

while running:
    screen.fill(BG_COLOR)

    # --- Draw Gotchi image ---
    if g.alive:
        screen.blit(img_alive, (50, 50))
    else:
        screen.blit(img_rip, (50, 50))

    # --- Draw stats ---
    stats_text = f"Age: {g.age}  Happiness: {g.happiness}  Hunger: {g.hunger}"
    text_surface = font.render(stats_text, True, (0,0,0))
    screen.blit(text_surface, (10, 10))

    # --- Draw buttons ---
    pygame.draw.rect(screen, (0,200,0), feed_button)   # green feed
    pygame.draw.rect(screen, (0,0,200), play_button)   # blue play
    feed_text = font.render("FEED", True, (255,255,255))
    play_text = font.render("PLAY", True, (255,255,255))
    screen.blit(feed_text, (feed_button.x + 10, feed_button.y + 5))
    screen.blit(play_text, (play_button.x + 10, play_button.y + 5))

    pygame.display.flip()

    # --- Gametick ---
    now = time.time()
    if now - last_tick >= TICK_INTERVAL:
        g.gametick()
        last_tick = now
        if not g.alive:
            print(f"{g.name} died!")

    # --- Event handling ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                g.feed()
            elif event.key == pygame.K_p:
                g.play()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if feed_button.collidepoint(event.pos):
                g.feed()
            elif play_button.collidepoint(event.pos):
                g.play()

    clock.tick(30)  # 30 fps

pygame.quit()
