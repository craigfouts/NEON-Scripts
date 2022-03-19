import numpy as np

def haversine(pos1, pos2):
    r = 6371
    p1, p2 = np.radians(pos1[0]), np.radians(pos2[0])
    dp, dl = np.radians(p2 - p1), np.radians(pos2[1] - pos1[1])
    a = np.sin(dp / 2) ** 2 + np.cos(p1) * np.cos(p2) * np.sin(dl / 2) ** 2
    result = r * 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    return result
