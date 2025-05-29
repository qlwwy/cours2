import pytest
from unittest.mock import patch, MagicMock
from src.hh_api import AbstractConnector, HHGateway
from src.vacancy import JobInfo

# Тест для проверки абстрактного класса
def test_abstract_connector():
    with pytest.raises(TypeError):
        AbstractConnector()

# Тест для проверки метода ping в HHGateway
@patch('requests.get')
def test_hh_gateway_ping_success(mock_get):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_get.return_value = mock_response

    gateway = HHGateway()
    assert gateway.ping() is True

@patch('requests.get')
def test_hh_gateway_ping_failure(mock_get):
    mock_get.side_effect = requests.RequestException("Connection error")

    gateway = HHGateway()
    assert gateway.ping() is False

# Тест для проверки метода fetch в HHGateway
@patch('requests.get')
def test_hh_gateway_fetch_success(mock_get):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "items": [
            {
                "name": "Software Engineer",
                "employer": {"name": "Tech Corp"},
                "salary": {"from": 100000, "to": 200000, "currency": "RUB"},
                "alternate_url": "http://example.com/job1"
            }
        ]
    }
    mock_get.return_value = mock_response

    gateway = HHGateway()
    jobs = gateway.fetch("Python", 1)
    assert len(jobs) == 1
    assert isinstance(jobs[0], JobInfo)
    assert jobs[0].name == "Software Engineer"

@patch('requests.get')
def test_hh_gateway_fetch_failure(mock_get):
    mock_get.side_effect = requests.RequestException("Fetch error")

    gateway = HHGateway()
    jobs = gateway.fetch("Python", 1)
    assert len(jobs) == 0

# Тест для проверки метода _unpack_job в HHGateway
def test_unpack_job():
    data = {
        "name": "Software Engineer",
        "employer": {"name": "Tech Corp"},
        "salary": {"from": 100000, "to": 200000, "currency": "RUB"},
        "alternate_url": "http://example.com/job1"
    }

    job_info = HHGateway._unpack_job(data)
    assert job_info.name == "Software Engineer"
    assert job_info.employer == "Tech Corp"
    assert job_info.min_pay == 100000
    assert job_info.max_pay == 200000
    assert job_info.money_unit == "RUB"
    assert job_info.link == "http://example.com/job1"
