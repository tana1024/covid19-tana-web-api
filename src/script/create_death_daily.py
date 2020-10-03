import pandas as pd
import json
from ..const import (DEATH_DAILY_DATA_PATH, DEATH_DAILY_JSON_PATH)

def create_json_file():
    df_death_daily = pd.read_csv(DEATH_DAILY_DATA_PATH, encoding='utf-8')
    df_death_daily = df_death_daily.fillna({'死亡者数': 0})

    init_death = df_death_daily.at[0, '死亡者数']
    df_death_daily['死亡者数'] = df_death_daily['死亡者数'].diff()
    df_death_daily.at[0, '死亡者数'] = init_death

    list_death = []
    for index, row in df_death_daily.iterrows():
        list_date = row['日付'].split('/')
        list_death.append({
            'date': '{year}/{month}/{day}'.format(year=list_date[0], month=list_date[1].zfill(2), day=list_date[2].zfill(2)),
            'death': str(int(row['死亡者数']))   
        })

    with open(DEATH_DAILY_JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(list_death, f, indent=2, ensure_ascii=False)
