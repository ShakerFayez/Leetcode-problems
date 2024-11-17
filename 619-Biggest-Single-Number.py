import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    result = my_numbers.groupby('num')[['num']].count().reset_index(names='nums')
    return pd.DataFrame({'num': [result.loc[result['num']==1]['nums'].max()]})