import pandas as pd

def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    len_df = len(seat.index)
    temp = seat[\student\].copy()
    for i in range(len_df):
        seat.loc[i, \student\] = temp[i-1] if i%2 else temp[(i+1) % len_df]
    if len_df % 2:
        seat.loc[len_df-1, \student\] = temp[len_df-1]

    return seat
    