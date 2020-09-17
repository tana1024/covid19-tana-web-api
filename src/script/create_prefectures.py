import pandas as pd
from ..const import (PREFECTURES_DATA_PATH)


def create_json_file():
    prefectures_df = pd.read_csv(PREFECTURES_DATA_PATH, encoding='utf-8')
    print(prefectures_df)
