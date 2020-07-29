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
        self.rel_fitness = self._get_relative_dist()
        self.k = 0

    def __repr__(self):
        ret = "<model.Environment>\n" 
        ret += self.heightmap.__repr__()
        ret += "\n<model.Agent[]>\n"
        for agent in self.agents:
            ret += ("\t" +  agent.__repr__() + "\n")
        return ret
    
    def generate_new_heightmap(self, height, width, base=None):

        base = base if base is not None else np.random.randint(low=0, high=100)

        peakyness = 0.2
        scale = 100
        octaves = 4
        persistence = 0.5 
        lacunarity = 2.0

        hmap = np.zeros((height, width))
        for x in range(height):
            for y in range(width):
                hmap[x,y] = noise.pnoise2(x/scale, 
                                          y/scale, 
                                          octaves=octaves, 
                                          persistence=persistence, 
                                          lacunarity=lacunarity, 
                                          repeatx=1024, 
                                          repeaty=1024, 
                                          base=base)
        
        hmap -= np.min(hmap)
        hmap = np.clip(hmap - peakyness*np.max(hmap), a_min=0, a_max=np.inf)


        for x in range(height):
            mult_x = (height + 100 - x) / height
            hmap[x] = hmap[x] * mult_x
        for y in range(width):
            mult_y = (width + 100 - y) / width
            hmap[:, y] = hmap[:, y] * mult_y

        return hmap

    def _get_relative_dist(self):
        if len(self.agents) == 0:
            return []
        agent_fitness = [self.heightmap[a.x, a.y] for a in self.agents]
        return self._softmax1D(agent_fitness)
    
    def _softmax1D(self, x):
        e_x = np.exp(x - np.max(x))
        return e_x / e_x.sum()





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
