from typing import List, Dict
from src.insights.jobs import read
# from jobs import read


def get_unique_industries(path: str) -> List[str]:
    data = read(path)
    lista = []
    for item in data:
        if item["industry"]:
            lista.append(item["industry"])

    industry = set(lista)
    return industry


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    raise NotImplementedError
