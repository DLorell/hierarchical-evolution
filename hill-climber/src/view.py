import pygame
import numpy as np
from pygame.locals import *

def main():

    board_data = numpy


    screen = pygame.display.set_mode((1000,1000))
    pygame.display.set_caption("TestBoard")


    cell_size = 
    board = pygame.Surface((cell_size*8, cell_size*8))

    board.fill((255, 255, 255))
    for x in range(0, 8, 2):
        for y in range(0, 8, 2):
            pygame.draw.rect(board, (0,0,0), (x*cell_size, y*cell_size, cell_size, cell_size))


    # Event loop
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        screen.blit(board, (0, 0))
        pygame.display.flip()






if __name__ == "__main__": 
    main()
