class JobInfo:
    """Класс для хранения информации о вакансии"""
    __slots__ = ("_name", "_employer", "_min_pay", "_max_pay", "_money_unit", "_link")

    def __init__(self, name, employer, min_pay, max_pay, money_unit, link):
        """Создаёт объект вакансии."""
        name: str
        employer: str
        min_pay: int | None
        max_pay: int | None
        money_unit: str | None
        link: str

        self._name = name
        self._employer = employer
        self._min_pay = self._sanitize(min_pay)
        self._max_pay = self._sanitize(max_pay)
        self._money_unit = money_unit or "N/A"
        self._link = link

    @staticmethod
    def _sanitize(val):
        """Проверяет зарплату: если число положительное — возвращает его, иначе 0."""
        return val if isinstance(val, int) and val > 0 else 0

    def __lt__(self, other):
        """Сравнивает две вакансии по минимальной зарплате (меньше)."""
        return self._min_pay < other._min_pay

    def __gt__(self, other):
        """Сравнивает две вакансии по минимальной зарплате (больше)."""
        return self._min_pay > other._min_pay

    def serialize(self) -> dict:
        """Возвращает данные вакансии в виде словаря."""
        return {
            "position": self._name,
            "employer": self._employer,
            "min_salary": self._min_pay,
            "max_salary": self._max_pay,
            "currency": self._money_unit,
            "link": self._link
        }

    def __repr__(self):
        """Возвращает краткое текстовое описание вакансии."""
        return f"{self._name} @ {self._employer} | от {self._min_pay} до {self._max_pay} {self._money_unit}\nПодробнее: {self._link}"

    @property
    def name(self):
        """Возвращает название должности."""
        return self._name

    @property
    def employer(self):
        """Возвращает название компании."""
        return self._employer

    @property
    def min_pay(self):
        """Возвращает минимальную зарплату."""
        return self._min_pay

    @property
    def max_pay(self):
        """Возвращает максимальную зарплату."""
        return self._max_pay

    @property
    def money_unit(self):
        """Возвращает валюту зарплаты."""
        return self._money_unit

    @property
    def link(self):
        """Возвращает ссылку на вакансию."""
        return self._link