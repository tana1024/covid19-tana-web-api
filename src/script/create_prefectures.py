import pandas as pd
from ..const import (PREFECTURES_DATA_PATH, PREFECTURES)


def create_json_file():
    df_prefectures = pd.read_csv(PREFECTURES_DATA_PATH, encoding='utf-8')
    df_prefectures = df_prefectures.fillna({'testedPositive': 0, 'peopleTested': 0, 'hospitalized': 0, 'serious': 0,
                                            'discharged': 0, 'deaths': 0, 'effectiveReproductionNumber': 0.0})
    for id, prefecture in PREFECTURES.items():
        list_pref = []

        df_prefecture = df_prefectures.query(f'prefectureNameJ == "{prefecture}"')
        df_prefecture = df_prefecture.reset_index(drop=True)
        df_sort = df_prefecture.sort_values(['year', 'month', 'date'], ascending=False)
        latest = str(df_sort.iat[0, 0]) + '/' + str(df_sort.iat[0, 1]).zfill(2) + '/' + str(df_sort.iat[0, 2]).zfill(2)
        df_sum = df_prefecture.groupby('prefectureNameJ').sum()
        list_pref.append({
            'id': id,
            'latest': latest,
            'prefectureNameJ': prefecture,
            'prefectureNameE': df_prefecture['prefectureNameE'][0],
            'testedPositive': df_sum['testedPositive'][0]
        })
        print(list_pref)
