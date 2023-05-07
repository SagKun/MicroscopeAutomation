import pandas as pd
import numpy as np
from Controllers.LaserController import LaserController
from Controllers.MicroscopeController import MicroscopeController
from robotframework_reportportal import logger


class ValidateZAxisMovement:
    def __init__(self, microscope_config, laser_config,micro_key,laser_key):
        self.laser_controller = LaserController(laser_config, laser_key)
        self.microscope_controller = MicroscopeController(microscope_config, micro_key)

    def setup_zaxis_test(self):
        """
        this function handles the setup for any z axis only movement test, initializes all hardware,
        and locks all movement except z axis, returns False if any of the actions failed.
        :return:
        """
        # initialize all the hardware components, that might take time, and we want everything ready for the test
        if not self.microscope_controller.initialize_microscope():
            logger.error('microscope could not be initialized, aborting test')
            return False
        if not self.laser_controller.initialize_laser():
            logger.error('laser could not be initialized, aborting test')
            return False

        # lock all degrees of freedom except the z axis
        if not (self.microscope_controller.lock_first_arm_joint() and self.microscope_controller.lock_second_arm_joint()):
            logger.error('could not lock joints, aborting test')
            return False
        if not (self.microscope_controller.lock_x_movement() and self.microscope_controller.lock_y_movement()):
            logger.error('could not lock xy movements, aborting test')
            return False

        # move the microscope to step 0 in the z axis and take and return a laser reading
        current_vector, status = self.microscope_controller.get_motor_status()
        if status == 'failure':
            logger.error('Motor is in failure status in test setup, aborting test')
            return False

        ## this vector_to_move results in no change to x,y and makes z value 0.
        vector_to_move = pd.array([0, 0, -1 * current_vector[2]])
        current_vector, status = self.microscope_controller.move_motor(vector_to_move)
        if status == 'failure':
            logger.error('Motor is in failure status in test setup, aborting test')
            return False
        if current_vector[2] != 0:
            logger.error('Motor is not in 0 step, aborting test')
            return False
        logger.info('setup for zaxis test is completed successfully',also_console=True)
        return True

    def run_zaxis_sanity(self, action_df):
        """
        this functions runs the sanity test, load the test data to a dataframe,iterates each row,
        gets a laser distance measurement,moves the microscope according to the data row,takes
        another laser distance measurement and compares all the expected results in the data row,
        to the actual results.
        :param action_df: a test actions pandas dataframe parsed from a csv file.
        :return:
        """
        motor_start_position,_ = self.microscope_controller.get_motor_status()

        for _, row in action_df.iterrows():
            #creating the expected values
            vector_to_move = np.array([int(row["x_step"]), int(row["y_step"]), int(row["z_step"])])
            expected_position = np.copy(motor_start_position)
            expected_position[2]=int(row["should_be_in_step_z"])
            should_move_mm, expected_status = float(row["should_move_mm"]), row["expected_status"]

            # im faking the laser values,so i'm passing the reading I want to get back,
            # in real life there might be an error tolerance I might need to handle
            laser_reading_prior_movement = self.laser_controller.get_distance_reading()
            actual_position, actual_status = self.microscope_controller.move_motor(vector_to_move)
            laser_reading_after_movement = self.laser_controller.get_distance_reading(should_move_mm)
            actual_movement = round(laser_reading_prior_movement - laser_reading_after_movement,2)

            ## check expected and actual values
            if not np.array_equal(expected_position, actual_position):
                logger.error(
                    f"expected position: {expected_position} does not equal the actual position: {actual_position}")
                return False
            if not expected_status == actual_status:
                logger.error(
                    f"expected status: {expected_status} does not equal the actual status: {actual_status}")
                return False
            if not float(should_move_mm) == actual_movement:
                logger.error(
                    f"expected movement: {should_move_mm} does not equal the actual movement: {actual_movement}")
                return False
        return True
