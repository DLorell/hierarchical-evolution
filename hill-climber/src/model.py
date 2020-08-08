import numpy as np
import noise
import time

class Agent():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return "<model.Agent> at ({},{})".format(self.x, self.y)

class Environment():
    def __init__(self, h=500, w=500, heightmap=None, agents=None):
        self.heightmap = heightmap if heightmap is not None \
                                   else self.generate_new_heightmap(h, w)
        
        self._temperature = 3

        self.agents = [Agent(h//2, w//2)] if agents is None else agents
        self.rel_fitness = self._get_relative_dist()
        self.k = 0
        self.max_pop = 50
        

    def __repr__(self):
        ret = "<model.Environment>\n" 
        ret += self.heightmap.__repr__()
        ret += "\n<model.Agent[]>\n"
        for agent in self.agents:
            ret += ("\t" +  agent.__repr__() + "\n")
        if len(self.agents) == 0:
            ret += "\t []"
        return ret
    
    def generate_new_heightmap(self, height, width, base=None):

        base = base if base is not None else np.random.randint(low=0, high=100)

        peakyness = 0.2
        x_scale = 100 * (height/500)
        y_scale = 100 * (width/500)
        octaves = 4
        persistence = 0.5 
        lacunarity = 2.0

        hmap = np.zeros((height, width))
        for x in range(height):
            for y in range(width):
                hmap[x,y] = noise.pnoise2(x/x_scale, 
                                          y/y_scale, 
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
        hmap = hmap / np.max(hmap)

        return hmap

    def step(self):
        t = time.time()

        reproduction_dist = self._get_reproduction_dist()

        """ 
        # Old method. Stochasticity makes it take too long when there are many agents.

        new_agents = []
        while len(new_agents) < self.max_pop:
            lucky_idx = np.random.randint(0, len(self.agents))
            reproductive_success = np.random.choice([0, 1], p=[1-reproduction_dist[lucky_idx], reproduction_dist[lucky_idx]])
            if not reproductive_success:
                continue
            children = self._mutate(self.agents[lucky_idx])
            remaining_spots = self.max_pop - len(new_agents)
            if remaining_spots >= len(children):
                children = children[:remaining_spots]
            new_agents += children
        """

        # New method: Simply multiply the reproduction dist by max_pop and round. That's how many children
        # each agent gets.
        children_per_agent = np.rint(reproduction_dist * self.max_pop).astype('int')
        children = []
        for agent, num_children in zip(self.agents, children_per_agent):
            children += self._mutate(agent, num_children)


        self.agents = children
        self.rel_fitness = self._get_relative_dist()

    def _get_relative_dist(self):
        if len(self.agents) == 0:
            return []
        agent_fitness = [self.heightmap[a.x, a.y] * self._temperature for a in self.agents]
        return self._softmax1D(agent_fitness)
    
    def _get_reproduction_dist(self):
        uniform = np.ones_like(self.rel_fitness) / len(self.rel_fitness)
        interpolated = (1-self.k) * self.rel_fitness + self.k * uniform
        return interpolated

    def _mutate(self, agent, num_children):
        x = agent.x
        y = agent.y

        positions = [
            (x+1, y),
            (x-1, y),
            (x, y+1), 
            (x, y-1),
            (x+1, y+1),
            (x+1, y-1),
            (x-1, y-1),
            (x-1, y+1)
        ]
        positions = [pos for pos in positions if self._is_legal(pos)]
        np.random.shuffle(positions)

        children = []
        for i in range(num_children):
            pos = positions[i%len(positions)]
            children.append(Agent(*pos))

        return children

    def _is_legal(self, pos):
        assert len(pos) == 2
        x = pos[0]
        y = pos[1]
        if x < 0 or x >= self.heightmap.shape[0] or y < 0 or y >= self.heightmap.shape[1]:
            return False
        return True

    def _softmax1D(self, x):
        e_x = np.exp(x - np.max(x))
        return e_x / e_x.sum()





def visualtest_generate_new_heightmap():

    import sys
    sys.path.append('src')
    from view import BoardView
    import pygame 
    from pygame.locals import QUIT
    import time

    pygame.init()

    environment = Environment(h=250, w=250)
    bview = BoardView(environment.heightmap, [(a.x, a.y) for a in environment.agents])
    environment.k = 0
    environment.max_pop = 100

    tick_rate = 0.01
    t = time.time()
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
                #environment.step()
                #bview.set_agents([(a.x, a.y) for a in environment.agents])
                #bview.update_board()
            
        #"""
        if time.time() - t >= tick_rate:
            t = time.time()
            environment.step()
            bview.set_agents([(a.x, a.y) for a in environment.agents])
            bview.update_board()
        #"""


if __name__ == "__main__": 
    visualtest_generate_new_heightmap()
