import requests
from datetime import datetime


def load_attempts():
    response = requests.get(
        'https://devman.org/api/challenges/solution_attempts/')
    response_json = response.json()
    pages = response_json['number_of_pages']
    current_page = 1
    all_attempts_list = []
    for page in range(pages):
        params = {'page': '{}'.format(current_page)}
        response_json = requests.get(
            'https://devman.org/api/challenges/solution_attempts/',
            params=params).json()
        all_attempts_list.append(response_json['records'])
        current_page += 1
    all_attempts_list_flat = [item for sublist in all_attempts_list for
                              item in sublist]
    # Ужасное, на мое мнение решение для объединения всех листов в один,
    # Подскажите, как лучше сделать ?
    # По поводу гет запроса - там же 10 страниц, вот 10 обращений и идет
    # перечитал либу всю и стаковерфлоу, везде циклом вытаскивают
    return all_attempts_list_flat


def get_midnighters(attempts_info):
    solve_attempts = []
    print(attempts_info)
    records = attempts_info
    for record in records:
        record_time = record['timestamp']
        utc_dt = datetime.utcfromtimestamp(record_time)
        month = int(utc_dt.month)
        day = int(utc_dt.day)
        year = 2017
        midnight = datetime(year=year, month=month, day=day, hour=0, minute=00)
        morning = datetime(year=year, month=month, day=day, hour=9, minute=00)
        if midnight < utc_dt < morning:
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

