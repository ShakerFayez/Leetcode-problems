import pandas as pd

def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:
    reordered = request_accepted[['accepter_id', 'requester_id', 'accept_date']].rename(columns={'accepter_id': 'requester_id', 'requester_id': 'accepter_id'})
    appended = pd.concat([request_accepted, reordered], ignore_index=True).groupby('requester_id').count().reset_index()
    result = appended.loc[appended['accepter_id'] == appended['accepter_id'].max()][['requester_id', 'accepter_id']].rename(columns={'requester_id': 'id', 'accepter_id': 'num'})
    return result