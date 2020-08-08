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
    environment = model.Environment(h=10, w=10)
    check.is_not_none(environment.heightmap)
    check.greater_equal(np.min(environment.heightmap), 0)
    check.less_equal(np.max(environment.heightmap), 1)

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

def test_mutate():
    agents = [
        model.Agent(0, 0),
        model.Agent(9, 9),
        model.Agent(0, 4),
        model.Agent(4,4)
    ]

    environment = model.Environment(h=10, w=10, agents=agents)

    top_corner_children = environment._mutate(agents[0], 2)
    extreme_corner_children = environment._mutate(agents[1], 2)
    edge_children = environment._mutate(agents[2], 3)
    middle_children = environment._mutate(agents[3], 4)

    extreme_corner_children_looped = environment._mutate(agents[1], 4)

    check.equal(len(top_corner_children), 2)
    check.equal(len(extreme_corner_children), 2)
    check.equal(len(edge_children), 3)
    check.equal(len(middle_children), 4)
    check.equal(len(extreme_corner_children_looped), 4)

    top_corners = [(0, 1), (1, 0)]
    check.equal(set([(a.x, a.y) for a in top_corner_children]), set(top_corners))

    extreme_corners = [(9,8), (8, 9)]
    check.equal(set([(a.x, a.y) for a in extreme_corner_children]), set(extreme_corners))

    edge_uns = [(0, 3), (0, 5), (1, 4)]
    check.equal(set([(a.x, a.y) for a in edge_children]), set(edge_uns))

    middles = [(4, 3), (3, 4), (4, 5), (5, 4)]
    check.equal(set([(a.x, a.y) for a in middle_children]), set(middles))

    extreme_corners_looped = [(9,8), (8, 9), (8,8)]
    check.equal(set([(a.x, a.y) for a in extreme_corner_children_looped]), set(extreme_corners_looped))




    

