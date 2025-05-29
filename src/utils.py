from src.vacancy import JobInfo


def keyword_match(items: list[JobInfo], phrase: str) -> list[JobInfo]:
    """Возвращает список вакансий, в которых есть нужное слово или фраза."""
    return [item for item in items if phrase.lower() in repr(item).lower()]


def salary_threshold(items: list[JobInfo], threshold: int) -> list[JobInfo]:
    """Оставляет только те вакансии, где зарплата не меньше заданной."""
    return [item for item in items if item.serialize().get("min_salary", 0) >= threshold]


def sort_by_pay(items: list[JobInfo]) -> list[JobInfo]:
    """Сортирует вакансии по зарплате от самой высокой к низкой."""
    return sorted(items, reverse=True)