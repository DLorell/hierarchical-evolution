import src.view as view
import pytest
import pytest_check as check
import numpy as np
import os
os.environ['SDL_VIDEODRIVER']='dummy'

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

def test_boardview():
    agent_positions = np.array([[4, 4]])
    bview = view.BoardView(board_data, agent_positions)

    check.equal(bview.hill_color, [128, 255, 180])
    check.equal(bview.agent_color, [0, 255, 0])
    check.equal(bview.board_data.shape, (12, 12, 3))
    check.equal(bview.agent_positions.all(), agent_positions.all())
    check.equal(bview.new_agent_positions, [])
    check.is_false(bview.agents_need_update)
    check.is_not_none(bview.screen)


def test_set_agents():
    agent_positions = np.array([[4, 4]])
    bview = view.BoardView(board_data, agent_positions)

    agent_positions1 = np.array([[3, 4],[5, 4],[4, 3],[4, 5]])
    bview.set_agents(agent_positions1)

    check.equal(bview.new_agent_positions.all(), agent_positions1.all())
    check.is_true(bview.agents_need_update)


def test_update_board():
    agent_positions = np.array([[4, 4]])
    bview = view.BoardView(board_data, agent_positions)

    agent_positions1 = np.array([[3, 4],[5, 4],[4, 3],[4, 5]])
    bview.set_agents(agent_positions1)
    bview.update_board()

    check.is_false(bview.agents_need_update)
    check.equal(bview.new_agent_positions, [])
    check.equal(bview.agent_positions.all(), agent_positions1.all())



