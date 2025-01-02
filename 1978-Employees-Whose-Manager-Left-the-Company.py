import pandas as pd

def find_employees(employees: pd.DataFrame) -> pd.DataFrame:
    result = employees.loc[~(employees['manager_id'].isin(employees['employee_id'])) & (employees['salary'] < 30000) & (pd.isna(employees['manager_id']) == False)][['employee_id']].sort_values(by='employee_id')
    return result