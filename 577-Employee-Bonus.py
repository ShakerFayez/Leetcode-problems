import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(employee, bonus, on='empId', how='left')
    result = merged.loc[(merged['bonus']<1000) | merged['bonus'].isnull()][['name', 'bonus']]
    return result