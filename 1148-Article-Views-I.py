import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    result = pd.DataFrame(views.loc[views['author_id']==views['viewer_id']]['author_id'].sort_values().unique(), columns=['id'])
    return result
