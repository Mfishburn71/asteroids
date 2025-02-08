# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    print("Starting asteroids!")
    print("Screen width:",SCREEN_WIDTH)
    print("Screen height:",SCREEN_HEIGHT)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # Create player

    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black") # Fill screen
        updatable.update(dt) # Update player

        for asteroid in asteroids: # Check for collisions
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    asteroid.split()
                    shot.kill()
                    break

        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip() # Update screen
        dt = Clock.tick(60) / 1000

if __name__ == "__main__":
    main()