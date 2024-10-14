import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    result = products.loc[(products['low_fats']=='Y') & (products['recyclable']=='Y')]['product_id'].to_frame()
    return result