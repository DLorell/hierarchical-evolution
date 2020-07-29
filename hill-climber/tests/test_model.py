import src.model as model
import src.view as view
import pytest
import pytest_check as check
import numpy as np
import os
os.environ['SDL_VIDEODRIVER']='dummy'


def test_agent():
    agent = model.Agent(3,4)
    check.equal(agent.x, 3)
    check.equal(agent.y, 4)

def test_generate_new_heightmap():
    environment = model.Environment(h=500, w=500)
    check.is_not_none(environment.heightmap)

def test_get_relative_dist():
    environment = model.Environment(h=500, w=500)

    agents = [
        model.Agent(0, 0),
        model.Agent(0, 1),
        model.Agent(0, 2),
        model.Agent(0, 3),
    ]
    environment.agents = agents

    environment.heightmap[0, 0] = 1
    environment.heightmap[0, 1] = 1
    environment.heightmap[0, 2] = 1
    environment.heightmap[0, 3] = 1
    equal_fitness = environment._get_relative_dist()

    environment.heightmap[0, 0] = 0
    environment.heightmap[0, 1] = 0
    environment.heightmap[0, 2] = 0
    environment.heightmap[0, 3] = 10
    all_for_one_fitness = environment._get_relative_dist()

    agents = [
        model.Agent(0, 0),
        model.Agent(0, 1)
    ]
    environment.heightmap[0, 0] = 0.1
    environment.heightmap[0, 1] = 0.3
    quarter_seventyfive_fitness = environment._get_relative_dist()

    for fitness in equal_fitness:
        check.equal(fitness, 0.25)
    
    check.less(all_for_one_fitness[0] - 0, 0.001)
    check.less(all_for_one_fitness[1] - 0, 0.001)
    check.less(all_for_one_fitness[2] - 0, 0.001)
    check.less(all_for_one_fitness[3] - 1, 0.001)

    check.less(quarter_seventyfive_fitness[0] - 0.25, 0.001)
    check.less(quarter_seventyfive_fitness[1] - 0.75, 0.001)
    
def test_get_reproduction_dist():
    environment = model.Environment(h=500, w=500)

    agents = [
        model.Agent(0, 0),
        model.Agent(0, 1),
        model.Agent(0, 2),
        model.Agent(0, 3),
    ]
    environment.agents = agents

    environment.heightmap[0, 0] = 8
    environment.heightmap[0, 1] = 6
    environment.heightmap[0, 2] = 4
    environment.heightmap[0, 3] = 2
    environment.rel_fitness = environment._get_relative_dist()

    environment.k = 1
    totally_equal = environment._get_reproduction_dist()
    environment.k = 0
    most_unequal = environment._get_reproduction_dist()
    environment.k = 0.5
    halfway_equal = environment._get_reproduction_dist()

    for elt in totally_equal:
        check.equal(elt, 0.25)

    check.less(most_unequal[3], most_unequal[2])
    check.less(most_unequal[2], most_unequal[1])
    check.less(most_unequal[1], most_unequal[0])

    for i in range(len(halfway_equal)):
        check.almost_equal(halfway_equal[i], 0.5*totally_equal[i] + 0.5*most_unequal[i])



