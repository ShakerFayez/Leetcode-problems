import pandas as pd

def restaurant_growth(customer: pd.DataFrame) -> pd.DataFrame:
    customer=customer.groupby('visited_on').sum().reset_index()
    customer['average_amount']=customer.amount.rolling(window=7).mean().round(2)
    customer['amount']=customer.amount.rolling(window=7).sum()
    return customer.dropna()[['visited_on','amount','average_amount']]