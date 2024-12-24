import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    logs[\nunique\] = logs.rolling(window=3)[\num\].apply(lambda x:x.nunique())
    return logs.loc[logs[\nunique\] == 1,\num\].drop_duplicates().to_frame(name=\ConsecutiveNums\)