from src.script import create_death_daily
from src.script import create_effective_reproduction
from src.script import create_pcr_positive_daily
from src.script import create_pcr_tested_daily
from src.script import create_prefectures
from src.script import create_serious

if __name__ == '__main__':
    create_death_daily.create_json_file()
    create_effective_reproduction.create_json_file()
    create_pcr_positive_daily.create_json_file()
    create_pcr_tested_daily.create_json_file()
    create_prefectures.create_json_file()
    create_serious.create_json_file()
