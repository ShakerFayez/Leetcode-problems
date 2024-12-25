import pandas as pd

def price_at_given_date(products: pd.DataFrame) -> pd.DataFrame:
  return products.groupby('product_id').apply(lambda g: g[g['change_date'].dt.strftime('%Y-%m-%d') <= '2019-08-16'].sort_values('change_date')['new_price'].iloc[-1] if min(g['change_date']).strftime('%Y-%m-%d') <= '2019-08-16' else 10).reset_index().rename(columns={0:'price'})
    