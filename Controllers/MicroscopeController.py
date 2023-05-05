from robotframework_reportportal import logger


class MicroscopeController:
    def __init__(self, config_file):
        self.config = config_file

    def initialize_microscope(self):
        pass

    def lock_x_movement(self):
        pass

    def lock_y_movement(self):
        pass

    def lock_z_movement(self):
        pass

    def lock_first_arm_joint(self):
        pass

    def lock_second_arm_joint(self):
        pass

    def initialize_motor(self):
        pass

    def get_motor_status(self):
        pass

    def move_motor(self, step_vector):
        """
        :param step_vector: numpy array that represents how many steps the motor should move in x,y,z direction.
        """

        # check that vector is within step bound
        pass
