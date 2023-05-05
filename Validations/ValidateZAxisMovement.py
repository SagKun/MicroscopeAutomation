from Controllers.LaserController import LaserController
from Controllers.MicroscopeController import MicroscopeController


class ValidateZAxisMovement:
    def __init__(self, microscope_config, laser_config):
        laser_cont = LaserController(laser_config)
        micro_con = MicroscopeController(microscope_config)

    def run_sanity(self, action_data):
        pass
