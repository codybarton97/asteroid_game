import pygame
from constants import *
from logger import log_state, log_event
from circleshape import *
from player import *
from asteroidfield import AsteroidField
from asteroid import *
import sys



def main():
    print("Starting Asteroids with pygame version: 2.6.1")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    #
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    #
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)

    field = AsteroidField()

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    ship = Player(x, y)
    #
    while True:
        #
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        screen.fill("black")
        #
        
        updatable.update(dt)
        for a in asteroids:
            if a.collides_with(ship):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        for a in asteroids:
            for s in shots:
                if s.collides_with(a):
                    log_event("asteroid_shot")
                    a.split()
                    s.kill()

        for d in drawable:

            d.draw(screen)
        
        #
        dt = clock.tick(60)/1000 
        pygame.display.flip()
             

        
        
        
if __name__ == "__main__":
    main()
