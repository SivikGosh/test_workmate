import csv
import logging
from argparse import Namespace
from collections import namedtuple
from dataclasses import dataclass
from typing import List, Tuple

from tabulate import tabulate  # type: ignore

from .commands import BaseCommand

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')


@dataclass
class CSVParser:
    """Чтение входного файла и обработка всех команд."""

    args: Namespace
    commands: list[BaseCommand]

    def show_result(self) -> str:
        headers, rows = self._read_the_file()
        for command in self.commands:
            headers, rows = command.run(command.arg, headers, rows)
        return tabulate(rows, headers, 'rounded_outline')

    def _read_the_file(self) -> Tuple[List, List]:
        try:
            with open(self.args.file, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                headers = next(reader)
                Row = namedtuple('Row', headers)  # type: ignore
                rows = [Row(*row) for row in reader]
                return headers, rows
        except Exception as e:
            logging.critical(
                f'{type(e).__name__} '
                f'в методе {self.__class__._read_the_file.__name__} '
                f'класса {self.__class__.__name__}. \n'
                f'Описание: "{e}".'
            )
        return [], []
