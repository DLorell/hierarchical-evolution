import numpy as np
import noise

class Agent():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return "<model.Agent> at ({},{})".format(self.x, self.y)

class Environment():
    def __init__(self, h=500, w=500, heightmap=None, agents=[]):
        self.heightmap = heightmap if heightmap is not None \
                                   else self.generate_new_heightmap(h, w)
        
        self.agents = agents
        #self.rel_fitness = self._get_relative_dist()
        self.k = 0

    def __repr__(self):
        ret = "<model.Environment>\n" 
        ret += self.heightmap.__repr__()
        ret += "\n<model.Agent[]>\n"
        for agent in self.agents:
            ret += ("\t" +  agent.__repr__() + "\n")
        return ret
    
    def generate_new_heightmap(self, height, width):
        num_peaks = 10
        peaks = [(np.random.choice(list(range(height))), 
                  np.random.choice(list(range(height)))) for _ in range(num_peaks)]
        hmap = np.zeros((height, width))
        for peak in peaks:
            hmap[peak[0], peak[1]] = 1

        return hmap






def visualtest_generate_new_heightmap():
    import sys
    sys.path.append('src')
    from view import BoardView
    import pygame 
    from pygame.locals import QUIT

    environment = Environment(h=500, w=500)
    bview = BoardView(environment.heightmap, [])

    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return


if __name__ == "__main__": 
    visualtest_generate_new_heightmap()
