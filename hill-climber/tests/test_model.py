import src.model as model
import src.view as model
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

