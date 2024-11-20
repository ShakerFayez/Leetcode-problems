import pandas as pd
import numpy as np

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    triangle['triangle'] = np.where(triangle[['x', 'y', 'z']].sum(axis=1) - triangle[['x', 'y', 'z']].max(axis=1) > triangle[['x', 'y', 'z']].max(axis=1), 'Yes', 'No')
    return triangle