import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(employee, department, left_on='departmentId', right_on='id', how='inner', suffixes=['_emp', '_dept'])
    merged['rank'] = merged.groupby('departmentId')['salary'].rank(method='dense', ascending=False)
    result = merged.loc[merged['rank'] <= 3][['name_dept', 'name_emp', 'salary']].rename(columns={'name_dept': 'Department', 'name_emp': 'Employee', 'salary': 'Salary'})
    return result