import logging
from typing import List, Tuple

from .interfaces import BaseCommand, Condition, Row

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')


class OrderByCommand(BaseCommand):
    """Команда сортировки записей по условиям 'asc' и 'desc'."""

    def add_argument(self) -> None:
        self.parser.add_argument(
            '--order-by',
            type=str,
            required=False,
            help='Обрабатываемый CSV-файл.'
        )

    def get_key(self) -> str:
        return 'order_by'

    def run(
        self,
        arg_value: str,
        headers: List[str],
        rows: List[Row]
    ) -> Tuple[List, List]:

        if (
            '=' not in arg_value
            or not any(x in arg_value for x in ('asc', 'desc'))
        ):
            logging.error(
                f'В команде {self.get_key()} '
                f'невалидные данные. \n'
                f'Итог: данные не отфильтрованы.'
            )
            return headers, rows

        column, value = arg_value.split('=')
        condition = self.condition(column, value)

        if condition.value == 'asc':
            operation, result = self._asc(condition, headers, rows)

        if condition.value == 'desc':
            operation, result = self._desc(condition, headers, rows)

        return operation, result

    def _asc(
        self,
        condition: Condition,
        headers: List[str],
        rows: List[Row]
    ) -> Tuple[List, List]:

        if condition.column not in headers:
            return headers, rows
        rows = sorted(
            rows,
            key=lambda r: self.__try_cast(getattr(r, condition.column))
        )
        return headers, rows

    def _desc(
        self,
        condition: Condition,
        headers: List[str],
        rows: List[Row]
    ) -> Tuple[List, List]:

        if condition.column in headers:
            rows = sorted(
                rows,
                key=lambda r: self.__try_cast(getattr(r, condition.column)),
                reverse=True
            )
        return headers, rows

    def __try_cast(self, value):
        try:
            return (0, float(value))
        except (ValueError, TypeError):
            return (1, value)
