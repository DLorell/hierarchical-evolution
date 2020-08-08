import pygame
import time
import numpy as np
from pygame.locals import QUIT
from src.view import BoardView
from src.model import Agent, Environment

class EvoSim():
    def __init__(self):
        self.map_size = 200
        self.max_pop = 100
        self.k = 0.25

        self.tick_rate = 0.005

    def start(self):
        pygame.init()

        environment = Environment(h=self.map_size, w=self.map_size)
        environment.k = self.k
        environment.max_pop = self.max_pop

        bview = BoardView(environment.heightmap, [(a.x, a.y) for a in environment.agents])

        t = time.time()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                   
            if time.time() - t >= self.tick_rate:
                t = time.time()
                environment.step()
                bview.set_agents([(a.x, a.y) for a in environment.agents])
                bview.update_board()
                



    def __repr__(self):
        # TODO
        return super().__repr__()

    def __str__(self):
        # TODO
        return super().__str__()

