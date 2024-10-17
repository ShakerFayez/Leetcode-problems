import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(visits, transactions, on='visit_id', how='left')
    filtered = merged.loc[merged['transaction_id'].isnull()]
    result = filtered.groupby('customer_id')['visit_id'].count().reset_index(name='count_no_trans')
    return result