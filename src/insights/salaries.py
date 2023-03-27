from typing import Union, List, Dict

from src.insights.jobs import read
# from jobs import read


def get_max_salary(path: str) -> int:
    data = read(path)
    lista = []
    for item in data:
        if item["max_salary"].isdigit():
            lista.append(int(item["max_salary"]))
    return max(lista)


def get_min_salary(path: str) -> int:
    data = read(path)
    lista = []
    for item in data:
        if item["min_salary"].isdigit():
            lista.append(int(item["min_salary"]))
    return min(lista)


def none_type(job: Dict) -> int:

    if "min_salary" not in job:
        raise ValueError
    elif "max_salary" not in job:
        raise ValueError


def integer_type(job: Dict, salary: Union[int, str]) -> int:

    if type(job["min_salary"]) not in [int, str]:
        raise ValueError

    elif type(job["max_salary"]) not in [int, str]:
        raise ValueError

    elif type(salary) not in [int, str]:
        raise ValueError


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    salary_range = False

    none_type(job)
    integer_type(job, salary)
    if int(job["min_salary"]) > int(job["max_salary"]):
        raise ValueError
    if int(job["min_salary"]) <= int(salary) <= int(job["max_salary"]):
        salary_range = True
    return salary_range


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    lista = []
    errors = []
    for job in jobs:
        try:
            validate = matches_salary_range(job, salary)
        except ValueError as err:
            errors.append(err)
        else:
            if validate:
                lista.append(job)
    return lista
