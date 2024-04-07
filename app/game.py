import pygame
from math import sqrt
from app.player import Player
from app.npc import Npc
import os

PLAYER_IMAGE_PATH = os.path.join("assets", "player.png")
NPC_IMAGE_PATH = os.path.join("assets", "npc.png")

class Game:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Homie-Quest")
        self.running = True
        self.player = Player(width // 2 - 25, height // 2 - 25, 50, 5, PLAYER_IMAGE_PATH)
        self.npc = Npc(100, 100, 50, NPC_IMAGE_PATH, "Carnal")
        self.font = pygame.font.Font(None, 24)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        keys = pygame.key.get_pressed()
        self.player.move(keys, self.width, self.height)
        distance = sqrt((self.player.x - self.npc.x) ** 2 + (self.player.y - self.npc.y) ** 2)
        self.npc.show_message = distance < 100
        if self.check_collision(self.player, self.npc):
            self.separate_entities(self.player, self.npc)

    def render(self):
        self.screen.fill((255, 255, 255))
        self.player.draw(self.screen)
        self.npc.draw(self.screen)
        if self.npc.show_message:
            text_surface = self.font.render(self.npc.message, True, (255, 0, 0))
            text_rect = text_surface.get_rect(center=(self.npc.rect.centerx, self.npc.rect.y - 20))
            self.screen.blit(text_surface, text_rect)
        pygame.display.flip()

    def check_collision(self, sprite1, sprite2):
        return sprite1.rect.colliderect(sprite2.rect)

    def separate_entities(self, sprite1, sprite2):
        dx = sprite2.x - sprite1.x
        dy = sprite2.y - sprite1.y
        distance = sqrt(dx ** 2 + dy ** 2)
        move_x = dx / distance * 5
        move_y = dy / distance * 5
        sprite1.x -= move_x
        sprite1.y -= move_y
        sprite1.rect.topleft = (sprite1.x, sprite1.y)
