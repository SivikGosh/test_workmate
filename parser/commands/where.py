import logging
from typing import List, Tuple

from .interfaces import BaseCommand, Condition, Row

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')


class WhereCommand(BaseCommand):
    """Команда фильтрации записей по условиям '>', '<', '='."""

    def add_argument(self) -> None:
        self.parser.add_argument(
            '--where',
            type=str,
            required=False,
            help='Фильтрация по условию ">", "<" или "=" '
                 '("поле:значение").'
        )

    def get_key(self) -> str:
        return 'where'

    def run(
        self,
        arg_value: str,
        headers: List[str],
        rows: List[Row]
    ) -> Tuple[List, List]:

        if not any(op in arg_value for op in ('>', '<', '=')):
            logging.error(
                f'В команде {self.get_key()} '
                f'невалидные данные. \n'
                f'Итог: данные не отфильтрованы.'
            )

        if '>' in arg_value:
            column, value = arg_value.split('>')
            condition = self.condition(column, value)
            headers, rows = self._more(condition, headers, rows)

        if '<' in arg_value:
            column, value = arg_value.split('<')
            condition = self.condition(column, value)
            headers, rows = self._less(condition, headers, rows)

        if '=' in arg_value:
            column, value = arg_value.split('=')
            condition = self.condition(column, value)
            headers, rows = self._equal(condition, headers, rows)

        return headers, rows

    def _more(
        self,
        condition: Condition,
        headers: List[str],
        rows: List[Row]
    ) -> Tuple[List, List]:

        filtered_rows = []

        if condition.column not in headers:
            return headers, rows

        for row in rows:
            row_value = getattr(row, condition.column)

            try:
                condition_value = float(condition.value)
                row_value = float(row_value)
            except Exception as e:
                logging.error(
                    f'{type(e).__name__} '
                    f'в методе {self.__class__._more.__name__} '
                    f'класса {self.__class__.__name__}. \n'
                    f'Описание: "{e}". \n'
                    f'Итог: данные не отфильтрованы.'
                )
                return headers, rows

            if row_value > condition_value:
                filtered_rows.append(row)

        return headers, filtered_rows

    def _less(
        self,
        condition: Condition,
        headers: List[str],
        rows: List[Row]
    ) -> Tuple[List, List]:

        filtered_rows = []

        if condition.column not in headers:
            return headers, rows

        for row in rows:
            row_value = getattr(row, condition.column)

            try:
                condition_value = float(condition.value)
                row_value = float(row_value)
            except Exception as e:
                logging.error(
                    f'{type(e).__name__} '
                    f'в методе {self.__class__._more.__name__} '
                    f'класса {self.__class__.__name__}. \n'
                    f'Описание: "{e}". \n'
                    f'Итог: данные не отфильтрованы.'
                )
                return headers, rows

            if row_value < condition_value:
                filtered_rows.append(row)

        return headers, filtered_rows

    def _equal(
        self,
        condition: Condition,
        headers: List[str],
        rows: List[Row]
    ) -> Tuple[List, List]:

        filtered_rows = []

        if condition.column not in headers:
            return headers, rows

        for row in rows:
            row_value = getattr(row, condition.column)
            condition_value: str | float

            try:
                condition_value = float(condition.value)
                row_value = float(row_value)
                if condition_value == row_value:
                    filtered_rows.append(row)
            except ValueError:
                condition_value = condition.value
                if condition_value in row_value:
                    filtered_rows.append(row)

        return headers, filtered_rows
