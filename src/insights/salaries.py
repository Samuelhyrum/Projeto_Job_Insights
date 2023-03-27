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


def integer(job: Dict, salary: Union[int, str]) -> int:
    if isinstance(salary, str):
        salary = int(salary)
    if isinstance(job["max_salary"], str) and isinstance(
        job["min_salary"], str
    ):
        job["max_salary"] = int(job["max_salary"])
        job["min_salary"] = int(job["min_salary"])

    return job, salary


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        job, salary = integer(job, salary)
        if job["min_salary"] <= (salary) <= (job["max_salary"]):
            return True
        elif job["min_salary"] > (job["max_salary"]):
            raise ValueError
        else:
            return False
    except(ValueError, TypeError, KeyError):
        raise ValueError


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
