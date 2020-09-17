import pandas as pd
from ..const import (PREFECTURES_DATA_PATH)


def create_json_file():
    df_prefectures = pd.read_csv(PREFECTURES_DATA_PATH, encoding='utf-8')
    df_prefectures = df_prefectures.fillna({'testedPositive': 0, 'peopleTested': 0, 'hospitalized': 0, 'serious': 0, 'discharged': 0, 
                            'deaths': 0, 'effectiveReproductionNumber': 0.0})
    for row in df_prefectures.iterrows():
        print(row)
