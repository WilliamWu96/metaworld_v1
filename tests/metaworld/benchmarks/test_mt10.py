import numpy as np
import pytest

from metaworld.benchmarks import MT10
from metaworld.envs.mujoco.env_dict import HARD_MODE_CLS_DICT


def test_augment_observation():
    """Test that the last 40 elements of obs array are sliced off correctly."""
    env = MT10()
    for i in range(env.num_tasks):
        env.set_task(i)
        obs, _, _, _ = env.step(env.action_space.sample())
        assert obs[-10:][i] == 1
        obs = env.reset()
        assert obs[-10:][i] == 1

