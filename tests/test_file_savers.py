import pytest
import json
import os
from unittest.mock import patch
from src.file_savers import StorageBase, JSONHandler
from src.vacancy import JobInfo

# Тест для проверки абстрактного класса
def test_storage_base():
    with pytest.raises(TypeError):
        StorageBase()

# Фикстура для создания временного файла
@pytest.fixture
def temp_file_path(tmp_path):
    return tmp_path / "test_data.json"

# Тест для проверки метода write и read
def test_json_handler_write_and_read(temp_file_path):
    # Создаем экземпляр JSONHandler с временным путем
    handler = JSONHandler(str(temp_file_path))

    # Создаем тестовые данные
    test_jobs = [
        JobInfo(
            name="Software Engineer",
            employer="Tech Corp",
            min_pay=100000,
            max_pay=200000,
            money_unit="RUB",
            link="http://example.com/job1"
        )
    ]

    # Записываем данные
    handler.write(test_jobs)

    # Читаем данные
    read_jobs = handler.read()

    # Проверяем, что данные записаны и прочитаны корректно
    assert len(read_jobs) == 1
    assert read_jobs[0].name == "Software Engineer"
    assert read_jobs[0].employer == "Tech Corp"

# Тест для проверки метода clear
def test_json_handler_clear(temp_file_path):
    # Создаем экземпляр JSONHandler с временным путем
    handler = JSONHandler(str(temp_file_path))

    # Создаем тестовые данные и записываем их
    test_jobs = [
        JobInfo(
            name="Software Engineer",
            employer="Tech Corp",
            min_pay=100000,
            max_pay=200000,
            money_unit="RUB",
            link="http://example.com/job1"
        )
    ]
    handler.write(test_jobs)

    # Очищаем файл
    handler.clear()

    # Проверяем, что файл пуст
    assert os.path.getsize(temp_file_path) == 0

# Тест для проверки обработки ошибок при чтении
def test_json_handler_read_error(temp_file_path):
    # Создаем экземпляр JSONHandler с временным путем
    handler = JSONHandler(str(temp_file_path))

    # Проверяем, что метод read возвращает пустой список при ошибке
    assert handler.read() == []

# Тест для проверки обработки ошибок при очистке
@patch('builtins.open', side_effect=Exception("Error"))
def test_json_handler_clear_error(mock_open):
    handler = JSONHandler("nonexistent_path")
    handler.clear()  # Проверяем, что ошибка обрабатывается
