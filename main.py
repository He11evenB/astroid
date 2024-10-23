import pygame
from constants import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen_size = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen_color = (0, 0, 0)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        screen_size.fill(screen_color)
        pygame.display.flip()
        clock.tick(60)
        dt = clock.get_time()

    
    

if __name__ == "__main__":
    main()