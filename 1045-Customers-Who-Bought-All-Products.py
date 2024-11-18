import pandas as pd

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(customer, product, how='outer', on='product_key')
    grouped = merged.groupby('customer_id')[['product_key']].nunique().reset_index()
    result = grouped.loc[grouped['product_key']==product['product_key'].count()][['customer_id']]
    return result