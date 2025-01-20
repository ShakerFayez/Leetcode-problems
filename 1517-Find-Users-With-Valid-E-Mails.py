import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    filtered_users = users[users['mail'].str.contains(r'^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\.com$', regex=True)]
    return filtered_users