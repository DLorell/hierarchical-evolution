import pygame
import numpy as np
from pygame.locals import *
from time import sleep



class BoardView():
    def __init__(self, board_data, agent_positions):

        pygame.display.set_caption("TestBoard")
        self.target_resolution = 1000
        self.hill_color = [255, 255, 255]
        self.agent_color = [0, 0, 0]

        board_data = np.clip(((board_data-np.min(board_data)) / np.max(board_data)), a_min=0.1, a_max=1)
        self.board_data = np.expand_dims(board_data, axis=-1) * np.expand_dims(np.expand_dims(np.array(self.hill_color), axis=0), axis=0)
        self.agent_positions = []
        self.new_agent_positions = agent_positions
        self.agents_need_update = len(agent_positions) > 0
        self.screen = None
        self.update_screen()

    def get_resolution(self):
        return self.target_resolution - (self.target_resolution % self.board_data.shape[0])
    
    def update_screen(self):
        resolution = self.get_resolution()
        self.screen = pygame.display.set_mode((resolution,resolution))
        self.update_board()
    
    def set_agents(self, new_positions):
        self.new_agent_positions = new_positions
        self.agents_need_update = True

    def update_board(self):
        resolution = self.get_resolution()
        cell_size = resolution // self.board_data.shape[0]
        board = pygame.Surface((resolution, resolution))
        board.fill((0, 0, 0))

        for x in range(self.board_data.shape[0]):
            for y in range(self.board_data.shape[1]):
                pygame.draw.rect(board, (*self.board_data[x, y],), (x*cell_size, y*cell_size, cell_size, cell_size))

        if self.agents_need_update:
            for pos in self.agent_positions:
                pygame.draw.rect(board, (*self.board_data[x, y],), (x*cell_size, y*cell_size, cell_size-1, cell_size-1))

            for pos in self.new_agent_positions:
                pygame.draw.circle(board, (*self.agent_color,), (int(round((pos[0]+0.5)*cell_size)), int(round((pos[1]+0.5)*cell_size))), (cell_size//2)-5)

            self.agent_positions = self.new_agent_positions
            self.new_agent_positions = []
            self.agents_need_update = False

        self.screen.blit(board, (0, 0))
        pygame.display.update()
           
    def __repr__(self):
        # TODO
        super().__repr__()
    def __str__(self):
        # TODO
        super().__str__()



def visualtest_boardview():
    board_data = np.array(
        [   
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 1, 0],
            [0, 0, 0, 0, 1, 2, 2, 3, 3, 2, 2, 1],
            [0, 0, 0, 0, 1, 2, 3, 4, 4, 3, 2, 1],
            [0, 0, 0, 0, 1, 2, 3, 4, 4, 3, 2, 1],
            [0, 0, 0, 0, 1, 2, 2, 3, 3, 2, 2, 1],
            [0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 1, 0],
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0]
        ]
    )
    agent_positions1 = np.array([[4, 4]])
    agent_positions2 = np.array([[3, 4],[5, 4],[4, 3],[4, 5]])
    agent_positions3 = np.array([[2, 4],[4, 4],[3, 3],[3, 5],[6, 4],[5, 3],[5, 5],[4, 2],[4, 6]])
    next_positions = [agent_positions2, agent_positions3, agent_positions2, agent_positions1, agent_positions2, agent_positions3]

    bview = BoardView(board_data, agent_positions1)

    i = 0
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
        
        sleep(0.5)
        if i < len(next_positions):
            bview.set_agents(next_positions[i])
            bview.update_board()
        else:
            return

        if i == 2:
            bview.target_resolution += 100
            bview.update_screen()
        
        i += 1

if __name__ == "__main__": 
    visualtest_boardview()
