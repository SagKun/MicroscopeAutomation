import time

from robotframework_reportportal import logger


class Laser:
    def __init__(self, config, connection_key):
        self.config = config

    def init_laser(self):
        time.sleep(0.2)
        return True

    def get_reading(self, reading_to_return):
        reading_to_return = round(reading_to_return,2)
        return reading_to_return
