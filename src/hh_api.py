from abc import ABC, abstractmethod

import requests

from src.vacancy import JobInfo


class AbstractConnector(ABC):
    """Базовый класс для подключения к сайту с вакансиями."""

    @abstractmethod
    def ping(self):
        """Проверка подключения к серверу."""
        pass

    @abstractmethod
    def fetch(self, search_term: str, limit: int = 20) -> list[JobInfo]:
        """Загружает список вакансий по ключевому слову."""
        pass


class HHGateway(AbstractConnector):
    """Обработчик API для сайта hh.ru."""
    _api_url = "https://api.hh.ru/vacancies"

    def ping(self):
        """Проверка доступа к hh.ru."""
        try:
            response = requests.get(self._api_url)
            response.raise_for_status()
            return True
        except requests.RequestException as error:
            print(f"Ошибка соединения с hh.ru: {error}")
            return False

    def fetch(self, search_term: str, limit: int = 20) -> list[JobInfo]:
        """Получает вакансии с сайта hh.ru."""
        if not self.ping():
            return []

        params = {
            "text": search_term,
            "per_page": limit,
            "page": 0
        }

        try:
            resp = requests.get(self._api_url, params=params)
            resp.raise_for_status()
            found = resp.json().get("items", [])
            return [self._unpack_job(item) for item in found]
        except requests.RequestException as error:
            print(f"Ошибка при загрузке данных: {error}")
            return []

    @staticmethod
    def _unpack_job(data: dict) -> JobInfo:
        """Преобразует словарь с данными в объект JobInfo."""
        pay = data.get("salary") or {}

        return JobInfo(
            name=data.get("name", "Не указано"),
            employer=data.get("employer", {}).get("name", "Не указано"),
            min_pay=pay.get("from"),
            max_pay=pay.get("to"),
            money_unit=pay.get("currency"),
            link=data.get("alternate_url")
        )