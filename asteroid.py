from constants import *
from circleshape import *
from logger import *
import random

# Class for Asteroid obstacles
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.center = (x, y)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)
        
    # Split the asteroids when hit with a bullet
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            v1 = self.velocity.rotate(angle)
            v2 = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            x, y = self.position
            astr1 = Asteroid(x, y, new_radius)
            astr2 = Asteroid(x, y, new_radius)
            astr1.velocity = v1 * 1.2
            astr2.velocity = v2 * 1.2

