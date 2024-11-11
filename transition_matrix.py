
import numpy as np
import pandas as pd
import random

T = np.zeros((3, 3))
P = np.zeros((3, 3))

# action_opponent_1 : action of the opponent with 1 step before
# action_opponent_2 : action of the opponent with 2 steps before

action_opponent_1, action_opponent_2 = None, None

def transition_matrix_agent(observation, configuration):
    global T, P, action_opponent_1, action_opponent_2
    if observation.step > 1:
        action_opponent_1 = observation.lastOpponentAction
        T[action_opponent_2, action_opponent_1] += 1
        P = np.divide(T, np.maximum(1, T.sum(axis=1)).reshape(-1, 1))
        action_opponent_2 = action_opponent_1
        if np.sum(P[action_opponent_1, :]) == 1:
            return int((np.random.choice(
                [0, 1, 2],
                p=P[action_opponent_1, :]
            ) + 1) % 3)
        else:
            return int(np.random.randint(3))

    else:
        if observation.step == 1:
            action_opponent_2 = observation.lastOpponentAction
        return int(np.random.randint(3))
