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
    
    check.less(all_for_one_fitness[0], 0.0001)
    check.less(all_for_one_fitness[1], 0.0001)
    check.less(all_for_one_fitness[2], 0.0001)
    check.less(all_for_one_fitness[3] - 1, 0.0001)

    check.less(quarter_seventyfive_fitness[0] - 0.25, 0.0001)
    check.less(quarter_seventyfive_fitness[1] - 0.75, 0.0001)
    

