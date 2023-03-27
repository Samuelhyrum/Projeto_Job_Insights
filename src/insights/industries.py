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
    data = jobs
    lista = []
    for item in data:
        if item["industry"] == industry:
            lista.append(item)
    return lista
