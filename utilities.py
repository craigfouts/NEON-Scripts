import numpy as np
from pyarrow import csv


def haversine(pos1, pos2):
    r = 6371
    p1, p2 = np.radians(pos1[0]), np.radians(pos2[0])
    dp, dl = np.radians(p2 - p1), np.radians(pos2[1] - pos1[1])
    a = np.sin(dp / 2) ** 2 + np.cos(p1) * np.cos(p2) * np.sin(dl / 2) ** 2
    h = r * 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    return h


def load_df(path, drop_idx=True):
    return csv.read_csv(path).to_pandas().reset_index(drop=drop_idx)
