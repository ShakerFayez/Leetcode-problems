import pandas as pd

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(project, employee, on='employee_id', how='inner')
    result = merged.groupby('project_id')['experience_years'].mean().round(decimals=2).reset_index(name='average_years')
    return result