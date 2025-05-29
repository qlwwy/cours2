import pytest
from src.vacancy import JobInfo

# Тест для создания объекта JobInfo
def test_job_info_creation():
    job = JobInfo(
        name="Software Engineer",
        employer="Tech Corp",
        min_pay=100000,
        max_pay=200000,
        money_unit="RUB",
        link="http://example.com/job1"
    )

    assert job.name == "Software Engineer"
    assert job.employer == "Tech Corp"
    assert job.min_pay == 100000
    assert job.max_pay == 200000
    assert job.money_unit == "RUB"
    assert job.link == "http://example.com/job1"

# Тест для метода _sanitize
def test_sanitize_method():
    assert JobInfo._sanitize(50000) == 50000
    assert JobInfo._sanitize(-10000) == 0
    assert JobInfo._sanitize("invalid") == 0

# Тест для методов сравнения __lt__ и __gt__
def test_comparison_methods():
    job1 = JobInfo(
        name="Software Engineer",
        employer="Tech Corp",
        min_pay=100000,
        max_pay=200000,
        money_unit="RUB",
        link="http://example.com/job1"
    )

    job2 = JobInfo(
        name="Data Scientist",
        employer="Data Inc",
        min_pay=150000,
        max_pay=250000,
        money_unit="RUB",
        link="http://example.com/job2"
    )

    assert (job1 < job2) is True
    assert (job1 > job2) is False

# Тест для метода serialize
def test_serialize_method():
    job = JobInfo(
        name="Software Engineer",
        employer="Tech Corp",
        min_pay=100000,
        max_pay=200000,
        money_unit="RUB",
        link="http://example.com/job1"
    )

    serialized = job.serialize()
    assert serialized["position"] == "Software Engineer"
    assert serialized["employer"] == "Tech Corp"
    assert serialized["min_salary"] == 100000
    assert serialized["max_salary"] == 200000
    assert serialized["currency"] == "RUB"
    assert serialized["link"] == "http://example.com/job1"

# Тест для метода __repr__
def test_repr_method():
    job = JobInfo(
        name="Software Engineer",
        employer="Tech Corp",
        min_pay=100000,
        max_pay=200000,
        money_unit="RUB",
        link="http://example.com/job1"
    )

    repr_str = repr(job)
    assert "Software Engineer" in repr_str
    assert "Tech Corp" in repr_str
    assert "100000" in repr_str
    assert "200000" in repr_str
    assert "RUB" in repr_str
    assert "http://example.com/job1" in repr_str
