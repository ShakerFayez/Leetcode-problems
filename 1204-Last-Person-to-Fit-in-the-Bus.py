import pandas as pd

def last_passenger(queue: pd.DataFrame) -> pd.DataFrame:
    queue= queue.sort_values(by='turn',ascending=True)
    queue['total_weight']= queue['weight'].cumsum()
    queue= queue[queue['total_weight']<=1000].sort_values(by='total_weight',ascending=False)
    return queue.head(1)[['person_name']]