import pandas as pd

# def queries_stats(queries: pd.DataFrame) -> pd.DataFrame:
#     result = queries.groupby('query_name').apply(lambda row: pd.Series({'quality': (row['rating']/row['position']).mean().round(decimals=2), 'poor_query_percentage': ((row['rating'] < 3).mean() * 100).round(2)})).reset_index()
#     return result

def queries_stats(df: pd.DataFrame) -> pd.DataFrame:
    df = df.assign(quality = df.rating / df.position + 1e-10, poor_query_percentage = (df.rating < 3).astype(int)*100)
    return df.groupby("query_name", as_index = False)[["quality","poor_query_percentage"]].mean().round(2)