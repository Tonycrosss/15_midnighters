# import requests
from pytz import timezone
from datetime import datetime

a = [{"page": 2, "number_of_pages": 10, "records": [{"timestamp": 1509560141.19362, "username": "mmmixaleva9", "timezone": "Europe/Moscow"}, {"timestamp": 1509558769.369071, "username": "mmmixaleva9", "timezone": "Europe/Moscow"}, {"timestamp": 1509558349.187281, "username": "id220830480", "timezone": "Europe/Moscow"}, {"timestamp": 1509555412.242069, "username": "mmmixaleva9", "timezone": "Europe/Moscow"}, {"timestamp": 1509548550.652064, "username": "ksushazhukova", "timezone": "Europe/Moscow"}, {"timestamp": 1509548338.934214, "username": "ksushazhukova", "timezone": "Europe/Moscow"}, {"timestamp": 1509548077.286869, "username": "david5", "timezone": "Europe/Moscow"}, {"timestamp": 1509547355.098574, "username": "VadimKonstantinov", "timezone": "Europe/Moscow"}, {"timestamp": 1509544921.995801, "username": "n1p3r", "timezone": "Europe/Moscow"}, {"timestamp": 1509544199.360267, "username": "VadimKonstantinov", "timezone": "Europe/Moscow"}, {"timestamp": 1509543887.391252, "username": "VadimKonstantinov", "timezone": "Europe/Moscow"}, {"timestamp": 1509540776.0, "username": "4pydev", "timezone": "Europe/Moscow"}, {"timestamp": 1509540163.810636, "username": "4pydev", "timezone": "Europe/Moscow"}, {"timestamp": 1509537549.216942, "username": "n1p3r", "timezone": "Europe/Moscow"}, {"timestamp": 1509537271.867359, "username": "ksushazhukova", "timezone": "Europe/Moscow"}, {"timestamp": 1509536442.0, "username": "paganismrus", "timezone": "Europe/Moscow"}, {"timestamp": 1509532543.0, "username": "4pydev", "timezone": "Europe/Moscow"}, {"timestamp": 1509531831.499586, "username": "tonycross", "timezone": "Europe/Moscow"}, {"timestamp": 1509531101.553042, "username": "1984skv", "timezone": "Europe/Moscow"}, {"timestamp": 1509529738.108275, "username": "LizzaVeta", "timezone": "Europe/Moscow"}, {"timestamp": 1509528178.150226, "username": "\u041d\u0438\u043a\u0438\u0442\u0430\u0412\u0438\u043b\u043a\u043e\u0432", "timezone": "Europe/Moscow"}, {"timestamp": 1509528000.684672, "username": "ivankharkov1", "timezone": "Europe/Moscow"}, {"timestamp": 1509527266.942425, "username": "ivankharkov1", "timezone": "Europe/Moscow"}, {"timestamp": 1509525871.810377, "username": "1984skv", "timezone": "Europe/Moscow"}, {"timestamp": 1509523089.032927, "username": "gnamail62", "timezone": "Europe/Moscow"}, {"timestamp": 1509507447.779879, "username": "id20215347", "timezone": "Europe/Moscow"}, {"timestamp": 1509496598.104068, "username": "ereminkostya", "timezone": "Asia/Vladivostok"}, {"timestamp": 1509490275.492773, "username": "\u0410\u043b\u0435\u043a\u0441\u0430\u043d\u0434\u0440\u0427\u0438\u0440\u043a\u043e\u0432", "timezone": "Europe/Moscow"}, {"timestamp": 1509489906.779843, "username": "\u0410\u043b\u0435\u043a\u0441\u0430\u043d\u0434\u0440\u0427\u0438\u0440\u043a\u043e\u0432", "timezone": "Europe/Moscow"}, {"timestamp": 1509482072.473037, "username": "1984skv", "timezone": "Europe/Moscow"}]}]


def load_attempts():
    pages = 1
    for page in range(pages):
        # FIXME подключить загрузку данных из API
        yield {
            'username': 'bob',
            'timestamp': 0,
            'timezone': 'Europe/Moscow',
        }


def get_midnighters(response):
    midnight = datetime(2017, month=11, day=1, hour=0, minute=00)
    morning = datetime(2017, month=11, day=1, hour=9, minute=00)
    print(midnight)
    print(morning)
    fmt = '%Y-%m-%d %H:%M:%S %Z%z'
    records = response[0]['records']
    for record in records:
        record_time = record['timestamp']
        utc_dt = datetime.utcfromtimestamp(record_time)
        if midnight < utc_dt < morning:
            print(utc_dt)


if __name__ == '__main__':
  get_midnighters(a)
