import numpy as np
from datetime import datetime, timedelta
from sklearn.base import BaseEstimator, TransformerMixin
from tqdm import tqdm


class CO2DataExtractor(BaseEstimator, TransformerMixin):
    def __init__(self, cols=None):
        self.cols = list(cols) if cols else None
    def fit(self, X, y=None):
        return self  # Nothing to do
    def transform(self, X):
        X_transform = X[self.cols] if self.cols else None
        return X_transform


class WindSpeedComputer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self  # Nothing to do
    def transform(self, X):
        veloXaxs = X['veloXaxs']
        veloYaxs = X['veloYaxs']
        veloZaxs = X['veloZaxs']
        wind_speed = np.sqrt(veloXaxs**2+veloYaxs**2+veloZaxs**2)
        x_transform = X.copy()
        x_transform['windSpeed'] = wind_speed
        return x_transform


class WindDirComputer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self  # Nothing to do
    def transform(self, X):
        veloXaxs = X['veloXaxs']
        veloYaxs = X['veloYaxs']
        wind_dir = np.mod(np.arctan2(-veloYaxs, veloXaxs)*180/np.pi+280, 360)
        X_transform = X.copy()
        X_transform['windDir'] = wind_dir
        return X_transform


class WindDataExtractor(BaseEstimator, TransformerMixin):
    def __init__(self, cols=None):
        self.cols = list(cols) if cols else None
    def fit(self, X, y=None):
        return self  # Nothing to do
    def transform(self, X):
        X_transform = X[self.cols] if self.cols else X
        return X_transform


class FlightTimeConverter(BaseEstimator, TransformerMixin):
    def __init__(self, ref=datetime(1970, 1, 1, 0, 0, 0)):
        self.ref = ref
    def fit(self, X, y=None):
        return self  # Nothing to do
    def transform(self, X):
        delta = np.array([timedelta(0, s) for s in tqdm(X['datetime'])])
        X_transform = X.copy()
        X_transform['datetime'] = self.ref + delta
        return X_transform


class FlightDataExtractor(BaseEstimator, TransformerMixin):
    def __init__(self, cols=None, flight_id=None):
        self.cols = list(cols) if cols else None
        self.flight_id = flight_id
    def fit(self, X, y=None):
        return self  # Nothing to do
    def transform(self, X):
        X_transform = X[self.cols] if self.cols else X
        if self.flight_id is not None:
            return X_transform[X_transform['flight_id'] == self.flight_id]
        return X_transform
