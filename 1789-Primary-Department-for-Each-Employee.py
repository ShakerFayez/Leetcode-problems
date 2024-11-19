import pandas as pd

def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
  employee['d_cnt'] = employee.groupby('employee_id').department_id.transform('count')
  return employee.query("(primary_flag == 'Y') | (d_cnt == 1)").iloc[:,[0,1]]