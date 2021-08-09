import glob
import os
import pandas as pd


def align_data(sensor_data_dir, abby_data_dir):
    for filepath in glob.iglob(os.path.join(sensor_data_dir, '*.csv')):
        print(filepath)
    for filepath in glob.iglob(os.path.join(abby_data_dir, '*.csv')):
        print(filepath)


if __name__ == '__main__':
    align_data('sensor_data', 'abby_data')
