import yaml
from SDKSimulator.Microscope import Microscope
from robotframework_reportportal import logger


class MicroscopeController:
    def __init__(self, config_file, connection_key):
        self.config = self.parse_config(config_file)
        self.microscope = Microscope(self.config, connection_key)
    def parse_config(self,config_file):
        """
        this function parses a given microscope .yml file to a yaml object.
        :param config_file: path to config file
        :return: yaml config object
        """
        with open(config_file) as file:
            microscope_config = yaml.load(file, Loader=yaml.FullLoader)
        logger.info(f'microscope config: {microscope_config}', also_console=True)
        return microscope_config

    def initialize_microscope(self):
        """
        initializes the motor to be ready for movement,
        applying microscope configuration.
        :return: True/False
        """
        self.microscope.initialize_motor()
        self.microscope.set_config(self.config)
        return True

    def lock_x_movement(self):
        """
        calling the sdk/api motor's x-axis locking function, to make the motor ready for action.
        :return: True/False
        """
        logger.info("x movement locked.", also_console=True)
        return self.microscope.lock_x_movement()

    def lock_y_movement(self):
        """
        calling the sdk/api motor's y-axis locking function, to make the motor ready for action.
        :return: True/False
        """
        logger.info("y movement locked.", also_console=True)
        return self.microscope.lock_y_movement()

    def lock_z_movement(self):
        """
        calling the sdk/api motor's z-axis locking function, to make the motor ready for action.
        :return: True/False
        """
        logger.info("y movement locked.", also_console=True)
        return self.microscope.lock_z_movement()

    def lock_first_arm_joint(self):
        """
        calling the sdk/api first arm locking function, to make the motor ready for action.
        :return: True/False
        """
        logger.info("first arm joint locked", also_console=True)
        return self.microscope.lock_first_arm_joint()

    def lock_second_arm_joint(self):
        """
        calling the sdk/api second arm locking function, to make the motor ready for action.
        :return: True/False
        """
        logger.info("second arm joint locked", also_console=True)
        return self.microscope.lock_second_arm_joint()

    def initialize_motor(self):
        """
        calling the sdk/api motor initialization function, to make the motor ready for action.
        :return: True/False
        """
        logger.info("motor initialized", also_console=True)
        return self.microscope.initialize_motor()

    def get_motor_status(self):
        """
        calling the sdk/api and returns the current motor step vector and status as an object.
        :return: {np.array(3),string}
        """
        status = self.microscope.get_motor_status()
        return status['position'], status['status']

    def move_motor(self, step_vector):
        """
                :param step_vector: numpy array that represents a 3d vector of steps the motor should move in x,y,z direction.
                """
        status = self.microscope.move_motor(step_vector)
        return status['position'], status['status']


