import pygame
from constants import *

def main():
    pygame.init()
    screen_size = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # print("Starting asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")
    screen_color = (0, 0, 0)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        screen_size.fill(screen_color)
        pygame.display.flip()
    
    

if __name__ == "__main__":
    main()