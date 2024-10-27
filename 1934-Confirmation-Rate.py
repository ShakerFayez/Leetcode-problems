import pandas as pd

def confirmation_rate(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
    
    df_total = confirmations.groupby('user_id')['action'].count().reset_index()

    df_conf  =confirmations[confirmations.action =='confirmed'
                           ].groupby('user_id')['action'].count().reset_index()

    df = signups.merge(df_total, how = 'left'
               ).merge(df_conf , how = 'left', on = 'user_id')

    df['confirmation_rate'] =  ((df.action_y)/ (df.action_x)).round(2)   

    return df.iloc[:,[0,4]].fillna(0)