import time
import numpy as np
from robotframework_reportportal import logger


class Microscope:
    def __init__(self, config, connection_key):
        self.z_step_max_range = None
        self.z_step_min_range = None
        self.z_step_to_mm_ratio = None
        self.z_axis_upper_step_limit = None
        self.z_axis_min_step = None
        ## just gets a random 3D vector between 0-3000
        self.motor_current_vector = np.random.randint(0, 3001, size=3)
        self.motor_status = None
        self.set_config(config)

    def initialize_motor(self):
        time.sleep(0.5)
        return True

    def set_config(self, config):
        motor_config = config["motor"]
        self.z_axis_min_step = motor_config['z_axis_min_step']
        self.z_axis_upper_step_limit = motor_config['z_axis_upper_step_limit']
        self.z_step_to_mm_ratio = motor_config['z_step_to_mm_ratio']
        self.z_step_min_range = motor_config['z_step_min_range']
        self.z_step_max_range = motor_config['z_step_max_range']

    def lock_x_movement(self):
        time.sleep(0.03)
        return True

    def lock_y_movement(self):
        time.sleep(0.03)
        return True

    def lock_z_movement(self):
        time.sleep(0.03)
        return True

    def lock_first_arm_joint(self):
        time.sleep(0.03)
        return True

    def lock_second_arm_joint(self):
        time.sleep(0.03)
        return True

    def move_motor(self, step_vector):
        self.motor_status = "success"
        motor_new_vector = self.motor_current_vector + step_vector
        z = motor_new_vector[2]
        if z > self.z_step_max_range:
            motor_new_vector[2] = self.z_step_max_range
            self.motor_status = "failure"
        elif z < self.z_step_min_range:
            motor_new_vector[2] = self.z_step_min_range
            self.motor_status = "failure"
        self.motor_current_vector = motor_new_vector
        time.sleep(0.5)
        return {"position": self.motor_current_vector, "status": self.motor_status}

    def get_motor_status(self):
        return {"position": self.motor_current_vector, "status": self.motor_status}
