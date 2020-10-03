import pandas as pd
import json
from ..const import (PREFECTURES_DATA_PATH, PREFECTURES, PREFECTURES_JSON_PATH)


def create_json_file():
    df_prefectures = pd.read_csv(PREFECTURES_DATA_PATH, encoding='utf-8')
    df_prefectures = df_prefectures.fillna({'testedPositive': 0, 'peopleTested': 0, 'hospitalized': 0, 'serious': 0,
                                            'discharged': 0, 'deaths': 0, 'effectiveReproductionNumber': 0.0})
    list_pref = []
    for id, prefecture in PREFECTURES.items():
        df_prefecture = df_prefectures.query(f'prefectureNameJ == "{prefecture}"')
        df_sort = df_prefecture.sort_values(['year', 'month', 'date'], ascending=False)
        df_sort = df_sort.reset_index(drop=True)
        latest = str(df_sort.iat[0, 0]) + '/' + str(df_sort.iat[0, 1]).zfill(2) + '/' + str(df_sort.iat[0, 2]).zfill(2)
        list_pref.append({
            'id': id,
            'latest': latest,
            'prefectureNameJ': prefecture,
            'prefectureNameE': str(df_sort['prefectureNameE'][0]),
            'testedPositive': str(df_sort['testedPositive'][0]),
            'peopleTested': str(df_sort['peopleTested'][0]),
            'hospitalized': str(df_sort['hospitalized'][0]),
            'serious': str(df_sort['serious'][0]),
            'discharged': str(df_sort['discharged'][0]),
            'deaths': str(df_sort['deaths'][0]),
            'effectiveReproductionNumber': str(df_sort['effectiveReproductionNumber'][0])
        })

    with open(PREFECTURES_JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(list_pref, f, indent=2, ensure_ascii=False)
