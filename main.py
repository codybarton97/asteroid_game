import pygame
from constants import *
from logger import log_state, log_event
from circleshape import *
from player import *
from asteroidfield import AsteroidField
from asteroid import *
import sys

def main():
    # Game Intro
    print("Starting Asteroids with pygame version: 2.6.1")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    # Initialize pygame
    pygame.init()
    # Creates a clock object to track time
    clock = pygame.time.Clock()
    # Stores delta time
    dt = 0
    # Creates a screen object
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)

    # Creates the asteroid field object
    field = AsteroidField()
    # Creates a player object
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    ship = Player(x, y)
    # Main Game Loop
    while True:
        #
        log_state()
        #
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #
        screen.fill("black")
        #
        updatable.update(dt)
        #
        for a in asteroids:
            if a.collides_with(ship):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        #
        for a in asteroids:
            for s in shots:
                if s.collides_with(a):
                    log_event("asteroid_shot")
                    a.split()
                    s.kill()
        #
        for d in drawable:
            d.draw(screen)
        #
        dt = clock.tick(60)/1000 
        pygame.display.flip()
             

        
        
        
if __name__ == "__main__":
    main()
