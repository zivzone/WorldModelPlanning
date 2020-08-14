import numpy as np
import math


def brownian_sample(previous_action, upper, lower):  # a_{t+1} = a_t + sqrt(dt) N(0, 1)
    delta = 1. / 50
    dactions_dt = np.random.randn()
    return np.clip(previous_action + math.sqrt(delta) * dactions_dt, lower, upper)


class BaseActionSampler:
    def __init__(self, config, num_actions):
        self.config = config
        self.is_discretize_sampling = config['planning']['is_discretize_sampling']
        self.num_actions = num_actions

    def sample(self, previous_action=None):
        return NotImplemented

    def brownian_sample(self, previous_action):
        return NotImplemented

    def discrete_delta_sample(self, previous_action=None):
        return NotImplemented

    def discrete_action_space(self, action=None):
        return NotImplemented
