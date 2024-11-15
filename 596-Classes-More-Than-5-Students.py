import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    grouped = courses.groupby('class')[['student']].nunique().reset_index().rename(columns={'student': 'student_count'})
    result = grouped.loc[grouped['student_count'] >= 5][['class']]
    return result