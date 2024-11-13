import pandas as pd

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    filtered = activity.loc[(activity['activity_date'] > '2019-06-27') & (activity['activity_date'] <= '2019-07-27')]
    grouped = filtered.groupby('activity_date')[['user_id']].nunique().reset_index()
    grouped.columns = ['day', 'active_users']
    return grouped