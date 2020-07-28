import src.model as model
import pytest
import pytest_check as check
import numpy as np
import os
os.environ['SDL_VIDEODRIVER']='dummy'


def test_agent():
    agent = model.Agent(3,4)
    check.equal(agent.x, 3)
    check.equal(agent.y, 4)