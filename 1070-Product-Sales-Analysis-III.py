import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    # Merge sales and product tables
    merged_df = sales.merge(product, how='left', on='product_id')
    
    # Find the first year of sale for each product
    first_year_df = merged_df.groupby('product_id')['year'].min().reset_index()
    
    # Merge the first year information back to the merged dataframe to get the corresponding quantity and price
    result_df = first_year_df.merge(merged_df, how='inner', on=['product_id', 'year']).rename(columns = {'year' : 'first_year'})
    
    return result_df[['product_id', 'first_year', 'quantity', 'price']]