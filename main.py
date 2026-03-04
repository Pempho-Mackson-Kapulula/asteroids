import pygame
from constants import *
from logger import log_state
from player import Player

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    y = SCREEN_HEIGHT / 2
    x = SCREEN_WIDTH / 2
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable,drawable)
    player = Player(x,y)


    running = True
    while running:
        log_state()
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for draw in drawable:
            draw.draw(screen)
        updatable.update(dt)
        
        
        dt = clock.tick(60)/1000  
        pygame.display.flip()
        




    
if __name__ == "__main__":
    main()