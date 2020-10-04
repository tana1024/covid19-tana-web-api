import pandas as pd
import json
from ..const import (PCR_POSITIVE_DAILY_DATA_PATH, PCR_POSITIVE_DAILY_JSON_PATH)


def create_json_file():
    df_pcr_positive = pd.read_csv(PCR_POSITIVE＿DAILY_DATA_PATH, encoding='utf-8')
    df_pcr_positive = df_pcr_positive.fillna({'PCR 検査陽性者数(単日)': 0})

    list_pcr_positive = []
    for index, row in df_pcr_positive.iterrows():
        list_date = row['日付'].split('/')
        list_pcr_positive.append({
            'date': '{year}/{month}/{day}'.format(year=list_date[0], month=list_date[1].zfill(2), day=list_date[2].zfill(2)),
            'pcr_positive': str(row['PCR 検査陽性者数(単日)'])
        })

    with open(PCR_POSITIVE＿DAILY_JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(list_pcr_positive, f, indent=2, ensure_ascii=False)
