import numpy as np
import pandas as pd
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler


class GasPriceBoostingModel:
    def __init__(self, params=None):
        self.default_params = {
            'n_estimators': 100,
            'learning_rate': 0.1,
            'max_depth': 5,
            'min_child_weight': 1,
            'subsample': 0.8,
            'colsample_bytree': 0.8,
            'objective': 'reg:squarederror'
        }
        self.params = params if params else self.default_params
        self.model = XGBRegressor(**self.params)
        self.scaler = StandardScaler()

    def preprocess_features(self, X):
        """Standardize features"""
        return self.scaler.transform(X)

    def fit(self, X, y, eval_set=None):
        """Train the model"""
        X_scaled = self.scaler.fit_transform(X)
        if eval_set:
            eval_set = [(self.preprocess_features(eval_set[0]), eval_set[1])]
        self.model.fit(X_scaled, y, eval_set=eval_set)
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
        importance = self.model.feature_importances_
        return dict(zip(feature_names, importance))
