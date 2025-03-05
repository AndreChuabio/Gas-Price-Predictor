import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from typing import Tuple, List, Dict


class DataProcessor:
    def __init__(self):
        self.scaler = StandardScaler()

    def load_data(self, filepath: str) -> pd.DataFrame:
        """Load data from CSV file"""
        return pd.read_csv(filepath)

    def clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """Clean the dataset"""
        # Remove duplicates
        df = df.drop_duplicates()

        # Handle missing values
        df = df.fillna(method='ffill')  # Forward fill
        df = df.fillna(method='bfill')  # Backward fill for any remaining NaNs

        return df

    def prepare_features(self,
                         df: pd.DataFrame,
                         target_col: str,
                         feature_cols: List[str] = None) -> Tuple[np.ndarray, np.ndarray]:
        """Prepare features and target variables"""
        if feature_cols is None:
            feature_cols = [col for col in df.columns if col != target_col]

        X = df[feature_cols].values
        y = df[target_col].values

        return X, y

    def create_time_features(self, df: pd.DataFrame, date_col: str) -> pd.DataFrame:
        """Create time-based features"""
        df = df.copy()
        df[date_col] = pd.to_datetime(df[date_col])

        # Extract time components
        df['year'] = df[date_col].dt.year
        df['month'] = df[date_col].dt.month
        df['quarter'] = df[date_col].dt.quarter

        # Create cyclical features for month
        df['month_sin'] = np.sin(2 * np.pi * df['month']/12)
        df['month_cos'] = np.cos(2 * np.pi * df['month']/12)

        return df

    def scale_features(self, X: np.ndarray) -> np.ndarray:
        """Scale features using StandardScaler"""
        return self.scaler.fit_transform(X)

    def process_pipeline(self,
                         filepath: str,
                         target_col: str,
                         date_col: str = None,
                         feature_cols: List[str] = None) -> Tuple[np.ndarray, np.ndarray]:
        """Complete data processing pipeline"""
        # Load data
        df = self.load_data(filepath)

        # Clean data
        df = self.clean_data(df)

        # Create time features if date column is specified
        if date_col:
            df = self.create_time_features(df, date_col)

        # Prepare features
        X, y = self.prepare_features(df, target_col, feature_cols)

        # Scale features
        X_scaled = self.scale_features(X)

        return X_scaled, y
