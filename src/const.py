import os

# output json path
DEATH_DAILY_JSON_PATH = './created_json/death_daily.json'
EFFECTIVE_REPRODUCTION_JSON_PATH = './created_json/effective_reproduction.json'
PCR_POSITIVE_DAILY_JSON_PATH = './created_json/pcr_positive_daily.json'
PCR_TESTED_DAILY_JSON_PATH = './created_json/pcr_tested_daily.json'
PREFECTURES_JSON_PATH = './created_json/prefectures.json'
SERIOUS_JSON_PATH = './created_json/serious.json'

# source data path
SOURCE_DATA_BASE_PATH = 'data/master_data/data'
DEATH_DAILY_DATA_PATH = os.path.join(SOURCE_DATA_BASE_PATH, 'death_total.csv')
EFFECTIVE_REPRODUCTION_DATA_PATH = os.path.join(SOURCE_DATA_BASE_PATH, 'effective_reproduction_number.csv')
PCR_POSITIVE_DAILY_DATA_PATH = os.path.join(SOURCE_DATA_BASE_PATH, 'pcr_positive_daily.csv')
PCR_TESTED_DAILY_DATA_PATH = os.path.join(SOURCE_DATA_BASE_PATH, 'pcr_tested_daily.csv')
PREFECTURES_DATA_PATH = os.path.join(SOURCE_DATA_BASE_PATH, 'prefectures.csv')
SERIOUS_DATA_PATH = os.path.join(SOURCE_DATA_BASE_PATH, 'serious.csv')

PREFECTURES = {
    '1': '北海道',
    '2': '青森県',
    '3': '岩手県',
    '4': '宮城県',
    '5': '秋田県',
    '6': '山形県',
    '7': '福島県',
    '8': '茨城県',
    '9': '栃木県',
    '10': '群馬県',
    '11': '埼玉県',
    '12': '千葉県',
    '13': '東京都',
    '14': '神奈川県',
    '15': '新潟県',
    '16': '富山県',
    '17': '石川県',
    '18': '福井県',
    '19': '山梨県',
    '20': '長野県',
    '21': '岐阜県',
    '22': '静岡県',
    '23': '愛知県',
    '24': '三重県',
    '25': '滋賀県',
    '26': '京都府',
    '27': '大阪府',
    '28': '兵庫県',
    '29': '奈良県',
    '30': '和歌山県',
    '31': '鳥取県',
    '32': '島根県',
    '33': '岡山県',
    '34': '広島県',
    '35': '山口県',
    '36': '徳島県',
    '37': '香川県',
    '38': '愛媛県',
    '39': '高知県',
    '40': '福岡県',
    '41': '佐賀県',
    '42': '長崎県',
    '43': '熊本県',
    '44': '大分県',
    '45': '宮崎県',
    '46': '鹿児島県',
    '47': '沖縄県'
}