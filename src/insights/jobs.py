from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, encoding="utf8") as file:
        allFile = csv.DictReader(file, delimiter=",", quotechar='"')
        data = allFile
        lista = []
        for item in data:
            lista.append(item)
    return lista


def get_unique_job_types(path: str) -> List[str]:
    data = read(path)
    lista = []
    for item in data:
        lista.append(item["job_type"])

    jobs = set(lista)
    return jobs


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
