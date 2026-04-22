import pygame
from constants import *
from circleshape import *
from shot import *

# Class for the Player Character
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x,  y, PLAYER_RADIUS)
        self.rotation = 0
        self.cd_timer = 0
    
    # Creates a triangle hitbox 
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    # Rotate the Player model
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    # Key bindings
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
            
        if keys[pygame.K_d]:
            self.rotate(dt)
        
        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_SPACE]:
            if self.cd_timer > 0:
                pass
            else:
                self.cd_timer = PLAYER_SHOOT_COOLDOWN_SECONDS
                self.shoot()
        
        self.cd_timer -= dt

    # Move the player model across the screen
    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    # Allows Player to shoot a bullet
    def shoot(self):
        x, y = self.position
        shot = Shot(x, y)
        aim = pygame.Vector2(0, 1)
        
        shot.velocity = aim.rotate(self.rotation) * PLAYER_SHOOT_SPEED


          