import yaml
from robotframework_reportportal import logger
from SDKSimulator.Laser import Laser


class LaserController:
    def __init__(self, laser_config, connection_key):
        self.config = self.parse_config(laser_config)
        self.laser = Laser(self.config, connection_key)
        self.laser_reading = 30
    def parse_config(self, config_file):
        with open(config_file) as file:
            laser_config = yaml.load(file, Loader=yaml.FullLoader)
        logger.info(f'laser config: {laser_config}')
        return laser_config

    def initialize_laser(self):
        """
        calling the sdk/api initialize function, to make the laser ready for action.
        :return: True/False
        """
        return self.laser.init_laser()

    def get_distance_reading(self, subtract_distance = 0):
        """
         requests a distance reading from the laser sdk/api.
        :param subtract_distance: just for testing,to control how the reading will return
        """
        return self.laser.get_reading( self.laser_reading - subtract_distance)
