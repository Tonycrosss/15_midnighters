import requests
from datetime import datetime


def load_attempts():
    response = requests.get(
        'https://devman.org/api/challenges/solution_attempts/')
    response_json = response.json()
    pages = response_json['number_of_pages']
    start_page = 1
    all_attempts_list = []
    for page in range(pages):
        params = {'page': '{}'.format(start_page)}
        response_json = requests.get(
            'https://devman.org/api/challenges/solution_attempts/',
            params=params).json()
        all_attempts_list.append(response_json['records'])
        start_page += 1
    return all_attempts_list


def get_midnighters(attempts_info):
    midnighters = []
    records = attempts_info[0]
    for record in records:
        record_time = record['timestamp']
        utc_dt = datetime.utcfromtimestamp(record_time)
        month = int(utc_dt.strftime('%m'))
        day = int(utc_dt.strftime('%d'))
        year = 2017
        midnight = datetime(year=year, month=month, day=day, hour=0, minute=00)
        morning = datetime(year=year, month=month, day=day, hour=9, minute=00)
        if midnight < utc_dt < morning:
            midnighters.append(record)
    return midnighters


def print_midnighters(midnighters_info):
    print('В список полуночников входят:')
    unique_midnighters = []
    for midnighter in midnighters_info:
        unique_midnighters.append(midnighter['username'])
    for midnighter in set(unique_midnighters):
        print(midnighter)


if __name__ == '__main__':
    attempts_info = load_attempts()
    midnighters = get_midnighters(attempts_info)
    print_midnighters(midnighters)

