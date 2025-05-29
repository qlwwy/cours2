import pytest
from src.vacancy import JobInfo


# Создаем тестовые данные
@pytest.fixture
def test_jobs():
    return [
        JobInfo(
            name="Software Engineer",
            employer="Tech Corp",
            min_pay=100000,
            max_pay=200000,
            money_unit="RUB",
            link="http://example.com/job1"
        ),
        JobInfo(
            name="Data Scientist",
            employer="Data Inc",
            min_pay=150000,
            max_pay=250000,
            money_unit="RUB",
            link="http://example.com/job2"
        ),
        JobInfo(
            name="DevOps Engineer",
            employer="Cloud Ltd",
            min_pay=120000,
            max_pay=220000,
            money_unit="RUB",
            link="http://example.com/job3"
        )
    ]

