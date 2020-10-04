import pandas as pd
import json
from ..const import (EFFECTIVE_REPRODUCTION_DATA_PATH, EFFECTIVE_REPRODUCTION_JSON_PATH)


def create_json_file():
    df_reproduction = pd.read_csv(EFFECTIVE_REPRODUCTION_DATA_PATH, encoding='utf-8')
    df_reproduction = df_reproduction.fillna({'実効再生産数': 0.00})

    list_reproduction = []
    for index, row in df_reproduction.iterrows():
        list_date = row['日付'].split('/')
        list_reproduction.append({
            'date': '{year}/{month}/{day}'.format(year=list_date[0], month=list_date[1].zfill(2), day=list_date[2].zfill(2)),
            'effective_reproduction': str(row['実効再生産数'])
        })

    with open(EFFECTIVE_REPRODUCTION_JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(list_reproduction, f, indent=2, ensure_ascii=False)
