import pandas as pd


class DataFileReader:

    def read_csv(self, file_path):
        data = pd.read_csv(file_path)
        return data
