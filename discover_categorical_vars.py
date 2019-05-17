import pandas as pd


def cat_indices(df):
    categorical_features_indices = np.where(df.dtypes != np.float)[0]
    return categorical_features_indices
