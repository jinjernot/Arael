import pygame

class Npc:
    def __init__(self, x, y, size, image_path, message):
        self.x = x
        self.y = y
        self.size = size
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (size, size))
        self.message = message
        self.rect = self.image.get_rect(topleft=(x, y))
        self.font = pygame.font.Font(None, 24)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def generate_message(self, screen):
        text_surface = self.font.render(self.message, True, (255, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
