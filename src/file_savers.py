import json
from abc import ABC, abstractmethod

from src.vacancy import JobInfo


class StorageBase(ABC):
    """Абстрактный интерфейс для сохранения и чтения данных."""

    @abstractmethod
    def write(self, items: list[JobInfo]):
        """Сохраняет список в хранилище."""
        pass

    @abstractmethod
    def read(self) -> list[JobInfo]:
        """Загружает данные из хранилища."""
        pass

    @abstractmethod
    def clear(self):
        """Полностью очищает хранилище."""
        pass


class JSONHandler(StorageBase):
    """Класс для работы с JSON-файлом вакансий."""

    def __init__(self, path: str = "data.json"):
        """Устанавливает путь к файлу."""
        self._path = path

    def write(self, items: list[JobInfo]):
        """Добавляет данные в JSON-файл."""
        current = self.read()
        current.extend([item.serialize() for item in items])

        with open(self._path, "w", encoding="utf-8") as file:
            json.dump(current, file, indent=4, ensure_ascii=False)

    def read(self) -> list[JobInfo]:
        """Читает вакансии из JSON-файла и создаёт объекты."""
        try:
            with open(self._path, "r", encoding="utf-8") as file:
                content = json.load(file)
                return [
                    JobInfo(
                        name=el["position"],
                        employer=el["employer"],
                        min_pay=el["min_salary"],
                        max_pay=el["max_salary"],
                        money_unit=el["currency"],
                        link=el["link"]
                    )
                    for el in content
                ]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def clear(self):
        """Полностью очищает файл."""
        try:
            open(self._path, "w", encoding="utf-8").close()
        except Exception as err:
            print(f"Не удалось очистить файл: {err}")