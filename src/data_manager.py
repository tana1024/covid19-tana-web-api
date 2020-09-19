from .const import (PREFECTURES_JSON_PATH)


class DataManager:

    def __init__(self):
        with open(PREFECTURES_JSON_PATH) as f:
            self.prefectures_json = f.read()
