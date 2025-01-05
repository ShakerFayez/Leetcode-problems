import pandas as pd

def movie_rating(movies: pd.DataFrame, users: pd.DataFrame, movie_rating: pd.DataFrame) -> pd.DataFrame:
    Users_df = movie_rating.merge(users, on='user_id', how='left')
    Movies_df = movie_rating.merge(movies, on='movie_id', how='left')
    Movies_df = Movies_df[Movies_df['created_at'].dt.to_period('M') == '2020-02']
    user_max_rating_df = Users_df.groupby('name')['rating'].count().reset_index().sort_values(by=['rating', 'name'], ascending=[False, True]).head(1)
    movie_highest_avg_df = Movies_df.groupby('title')['rating'].mean().reset_index().sort_values(by=['rating', 'title'], ascending=[False, True]).head(1)
    res = pd.concat([user_max_rating_df['name'],movie_highest_avg_df['title']]).to_frame()
    res.rename(columns={0:'results'}, inplace=True)
    return res
    