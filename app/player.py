import pygame
import os

# Define the path to the player image
PLAYER_IMAGE_PATH = os.path.join("assets", "player.png")

class Player:
    def __init__(self, x, y, size, speed, image_path):
        self.x = x
        self.y = y
        self.size = size
        self.speed = .25
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect(topleft=(x, y))

    def move(self, keys, width, height):
        movement_speed = self.speed
        if keys[pygame.K_a]:
            self.x -= movement_speed
        if keys[pygame.K_d]:
            self.x += movement_speed
        if keys[pygame.K_w]:
            self.y -= movement_speed
        if keys[pygame.K_s]:
            self.y += movement_speed

        self.x = max(0, min(width - self.size, self.x))
        self.y = max(0, min(height - self.size, self.y))

        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
