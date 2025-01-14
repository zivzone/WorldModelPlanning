from utility.rollout_handling.carracing.car_racing_rollout_generator import RolloutGenerator as CarRacingRolloutGenerator
from utility.rollout_handling.vizdoom.vizdoom_rollout_generator import RolloutGenerator as VizDoomRolloutGenerator

def get_rollout_generator(config):
    if config['game'] == 'CarRacing-v0':
        return CarRacingRolloutGenerator(config, data_output_dir=config['data_generator']['data_output_dir'])
    if config['game'] == 'vizdoom-v0':
        return VizDoomRolloutGenerator(config, data_output_dir=config['data_generator']['data_output_dir'])
    raise Exception(f'No implementation of rollout generator was found for game: {config["game"]}')
