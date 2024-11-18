import pandas as pd

def count_employees(employees: pd.DataFrame) -> pd.DataFrame:
    return (employees
                    .groupby('reports_to', as_index=False)
                    .agg(
                        reports_count=('reports_to','count'),
                        average_age=('age', lambda x: round(x.mean()+1e-10)))
                    .rename(columns ={'reports_to':'employee_id'})
                    .merge(employees[['employee_id', 'name']])
                    [['employee_id', 'name','reports_count', 'average_age']]
 )