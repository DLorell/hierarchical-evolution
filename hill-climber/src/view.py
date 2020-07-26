import pygame
import numpy as np
from pygame.locals import *

def main():

    resolution = 1000

    board_data = np.array(
        [   
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 1, 0],
            [0, 0, 0, 0, 1, 2, 1, 3, 3, 2, 2, 1],
            [0, 0, 0, 0, 1, 2, 3, 4, 4, 3, 2, 1],
            [0, 0, 0, 0, 1, 2, 3, 4, 4, 3, 2, 1],
            [0, 0, 0, 0, 1, 2, 2, 3, 3, 2, 2, 1],
            [0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 1, 0],
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0]
        ]
    )

    resolution -= resolution % board_data.shape[0]


    screen = pygame.display.set_mode((resolution,resolution))
    pygame.display.set_caption("TestBoard")


    cell_size = resolution // board_data.shape[0]
    board = pygame.Surface((resolution, resolution))

    board.fill((0, 0, 0))
    for x in range(0, board_data.shape[0]):
        for y in range(0, board_data.shape[1]):
            pygame.draw.rect(board, (212,175,55), (x*cell_size, y*cell_size, cell_size-1, cell_size-1))
            


    # Event loop
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        screen.blit(board, (0, 0))
        pygame.display.flip()






if __name__ == "__main__": 
    main()
