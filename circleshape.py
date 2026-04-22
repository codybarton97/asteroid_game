import pygame
from constants import LINE_WIDTH
from logger import *

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    # Draw the circle shape to the screen
    def draw(self, screen):
        points = self.triangle()
        
        pygame.draw.polygon(screen, "white", points, LINE_WIDTH)

    # Must override
    def update(self, dt):
        
        pass

    # Takes in another circleshape and return T/F
    def collides_with(self, other):
        dist = self.position.distance_to(other.position)
        r1 = self.radius
        r2 = other.radius

        if dist <= (r1 + r2):
            return True
        else:
            pass
             


        