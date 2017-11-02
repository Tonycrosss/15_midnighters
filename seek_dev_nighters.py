import requests
from datetime import datetime


def load_attempts():
    response = requests.get('https://devman.org/api/challenges/solution_attempts/')
    response_json = response.json()
    pages = response_json['number_of_pages']
    start_page = 1
    all_attempts_list = []
    for page in range(pages):
        response_json = requests.get('https://devman.org/api/challenges/solution_attempts/?page={}'.format(start_page)).json()
        all_attempts_list.append(response_json['records'])
        start_page += 1
    return all_attempts_list


def get_midnighters(response):
    midnight = datetime(2017, month=11, day=1, hour=0, minute=00)
    morning = datetime(2017, month=11, day=1, hour=9, minute=00)
    midnighters = []
    records = response[0]
    for record in records:
        print(record)
        record_time = record['timestamp']
        utc_dt = datetime.utcfromtimestamp(record_time)
        if midnight < utc_dt < morning:
            midnighters.append(record)
    return midnighters


if __name__ == '__main__':
    attempts_info = load_attempts()
    print(attempts_info)
    midnighters = get_midnighters(attempts_info)
    print(midnighters)

