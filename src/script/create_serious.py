import pandas as pd
import json
from ..const import (SERIOUS_DATA_PATH, SERIOUS_JSON_PATH)


def create_json_file():
    df_serious = pd.read_csv(SERIOUS_DATA_PATH, encoding='utf-8')
    df_serious = df_serious.fillna({'serious': 0})

    list_serious = []
    for index, row in df_serious.iterrows():
        list_date = row['date'].split('/')
        list_serious.append({
            'date': '{year}/{month}/{day}'.format(year=list_date[0], month=list_date[1].zfill(2), day=list_date[2].zfill(2)),
            'serious': str(row['serious'])   
        })

    with open(SERIOUS_JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(list_serious, f, indent=2, ensure_ascii=False)
