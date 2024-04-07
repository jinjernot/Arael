import pygame
import sys
from app.game import Game

def main():
    # Initialize Pygame
    pygame.init()

    WIDTH, HEIGHT = 800, 600
    
    # Create a Game object
    game = Game(WIDTH, HEIGHT)

    # Main loop
    while game.running:
        game.handle_events()
        game.update()
        game.render()

    # Quit Pygame
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
