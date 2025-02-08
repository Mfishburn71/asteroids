# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
pygame.init

def main():
    print("Starting asteroids!")
    print("Screen width:",SCREEN_WIDTH)
    print("Screen height:",SCREEN_HEIGHT)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen,(0,0,0)) # Fill screen
        pygame.display.flip() # Update screen

if __name__ == "__main__":
    main()