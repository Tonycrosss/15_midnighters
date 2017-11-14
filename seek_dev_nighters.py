import requests
import pytz
from datetime import datetime
from datetime import time


def load_attempts():
    current_page = 1
    all_attempts_list = []
    pages_quantity = 10
    for page in range(pages_quantity):
        params = {'page': str(current_page)}
        response_json = requests.get(
            'https://devman.org/api/challenges/solution_attempts/',
            params=params).json()
        all_attempts_list.extend(response_json['records'])
        current_page += 1
    return all_attempts_list


def get_midnighters(attempts_info):
    midnight = time(hour=0, minute=0, microsecond=0)
    morning = time(hour=9, minute=0, microsecond=0)
    solve_attempts = []
    records = attempts_info
    for record in records:
        record_timezone = pytz.timezone(record['timezone'])
        record_time = record['timestamp']
        localized_record_time = record_timezone.localize(datetime.fromtimestamp(record_time))
        if midnight < localized_record_time.time() < morning:
            solve_attempts.append(record)
    return solve_attempts


def print_midnighters(solve_attempts):
    print('В список полуночников входят:')
    unique_midnighters = set(midnighter['username'] for midnighter
                             in solve_attempts)
    for midnighter in unique_midnighters:
        print(midnighter)


if __name__ == '__main__':
    attempts_info = load_attempts()
    solve_attempts = get_midnighters(attempts_info)
    print_midnighters(solve_attempts)

