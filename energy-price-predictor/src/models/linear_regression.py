import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler


class GasPriceLinearModel:
    def __init__(self):
        self.model = LinearRegression()
        self.scaler = StandardScaler()

    def preprocess_features(self, X):
        """Standardize features"""
        return self.scaler.transform(X)

    def fit(self, X, y):
        """Train the model"""
        X_scaled = self.scaler.fit_transform(X)
        self.model.fit(X_scaled, y)
        return self

    def predict(self, X):
        """Make predictions"""
        X_scaled = self.preprocess_features(X)
        return self.model.predict(X_scaled)

    def evaluate(self, X, y_true):
        """Evaluate model performance"""
        y_pred = self.predict(X)
        mse = mean_squared_error(y_true, y_pred)
        r2 = r2_score(y_true, y_pred)
        return {
            'RMSE': np.sqrt(mse),
            'R2': r2
        }

    def get_feature_importance(self, feature_names):
        """Get feature importance scores"""
        return dict(zip(feature_names, self.model.coef_))
