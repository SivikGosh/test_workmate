import logging
from typing import List, Tuple

from .interfaces import BaseCommand, Condition, Row

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')


class AggregateCommand(BaseCommand):
    """Команда агрегации по условиям 'avg', 'min', 'max'."""

    def add_argument(self):
        self.parser.add_argument(
            '--aggregate',
            type=str,
            required=False,
            help='Агрегация по условию "avg", "min" или "max" '
                 '("поле:значение").'
        )

    def get_key(self):
        return 'aggregate'

    def run(
        self,
        arg_value: str,
        headers: List[str],
        rows: List[Row]
    ) -> Tuple[List, List]:

        if '=' not in arg_value:
            logging.error(
                f'В команде {self.get_key()} '
                f'невалидные данные. \n'
                f'Итог: данные не отфильтрованы.'
            )
            return headers, rows

        column, value = arg_value.split('=')
        condition = self.condition(column, value)

        if condition.value == 'avg':
            operation, result = self._avg(condition, headers, rows)

        if condition.value == 'min':
            operation, result = self._min(condition, headers, rows)

        if condition.value == 'max':
            operation, result = self._max(condition, headers, rows)

        return operation, result

    def _avg(
        self,
        condition: Condition,
        headers: List[str],
        rows: List[Row]
    ) -> Tuple[List, List]:

        total = 0.0

        if condition.column in headers:
            for row in rows:
                row_value = getattr(row, condition.column)

                try:
                    row_value = float(row_value)
                except ValueError:
                    logging.error(
                        f'В методе {self.__class__._avg.__name__} '
                        f'класса {self.__class__.__name__} '
                        f'невалидные данные. \n'
                        f'Описание: поле {condition.column} '
                        f'нельзя агрегировать. \n'
                        f'Итог: данные не отфильтрованы.'
                    )
                    return headers, rows

                total += row_value

        return ['avg'], [[str(round(total / len(rows), 2))]]

    def _min(
        self,
        condition: Condition,
        headers: List[str],
        rows: List[Row]
    ) -> Tuple[List, List]:

        row_values = []

        if condition.column in headers:
            for row in rows:
                row_value = getattr(row, condition.column)

                try:
                    row_value = float(row_value)
                except ValueError:
                    logging.error(
                        f'В методе {self.__class__._avg.__name__} '
                        f'класса {self.__class__.__name__} '
                        f'невалидные данные. \n'
                        f'Описание: поле {condition.column} '
                        f'нельзя агрегировать. \n'
                        f'Итог: данные не отфильтрованы.'
                    )
                    return headers, rows

                row_values.append(row_value)

        return ['min'], [[str(min(row_values))]]

    def _max(
        self,
        condition: Condition,
        headers: List[str],
        rows: List[Row]
    ) -> Tuple[List, List]:

        row_values = []

        if condition.column in headers:
            for row in rows:
                row_value = getattr(row, condition.column)

                try:
                    row_value = float(row_value)
                except ValueError:
                    logging.error(
                        f'В методе {self.__class__._avg.__name__} '
                        f'класса {self.__class__.__name__} '
                        f'невалидные данные. \n'
                        f'Описание: поле {condition.column} '
                        f'нельзя агрегировать. \n'
                        f'Итог: данные не отфильтрованы.'
                    )
                    return headers, rows

                row_values.append(row_value)

        return ['max'], [[str(max(row_values))]]
