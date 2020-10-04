from .const import (DEATH_DAILY_JSON_PATH)
from .const import (EFFECTIVE_REPRODUCTION_JSON_PATH)
from .const import (PCR_POSITIVE_DAILY_JSON_PATH)
from .const import (PCR_TESTED_DAILY_JSON_PATH)
from .const import (PREFECTURES_JSON_PATH)
from .const import (SERIOUS_JSON_PATH)


class DataManager:

    def __init__(self):
        with open(DEATH_DAILY_JSON_PATH) as f:
            self.death_daily_json = f.read()
        with open(EFFECTIVE_REPRODUCTION_JSON_PATH) as f:
            self.effective_reproduction_json = f.read()
        with open(PCR_POSITIVE_DAILY_JSON_PATH) as f:
            self.pcr_positive_daily_json = f.read()
        with open(PCR_TESTED_DAILY_JSON_PATH) as f:
            self.pcr_tested_daily_json = f.read()
        with open(PREFECTURES_JSON_PATH) as f:
            self.prefectures_json = f.read()
        with open(SERIOUS_JSON_PATH) as f:
            self.serious_json = f.read()
