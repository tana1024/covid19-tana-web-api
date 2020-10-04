import pandas as pd
import json
from ..const import (PCR_TESTED_DAILY_DATA_PATH, PCR_TESTED_DAILY_JSON_PATH)


def create_json_file():
    df_pcr_tested = pd.read_csv(PCR_TESTED_DAILY_DATA_PATH, encoding='utf-8')
    df_pcr_tested = df_pcr_tested.fillna({'PCR 検査実施件数(単日)': 0})

    list_pcr_tested = []
    for index, row in df_pcr_tested.iterrows():
        list_date = row['日付'].split('/')
        list_pcr_tested.append({
            'date': '{year}/{month}/{day}'.format(year=list_date[0], month=list_date[1].zfill(2), day=list_date[2].zfill(2)),
            'pcr_tested': str(row['PCR 検査実施件数(単日)'])
        })

    with open(PCR_TESTED_DAILY_JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(list_pcr_tested, f, indent=2, ensure_ascii=False)
