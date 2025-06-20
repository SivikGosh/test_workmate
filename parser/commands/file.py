from typing import List, Tuple

from .interfaces import BaseCommand, Row


class FileCommand(BaseCommand):
    """Команда обработки CSV-файла без условий."""

    def add_argument(self) -> None:
        self.parser.add_argument(
            '--file',
            type=str,
            required=True,
            help='Обрабатываемый CSV-файл.'
        )

    def get_key(self) -> str:  # pragma: no cover
        return 'file'

    def run(
        self,
        arg_value: str,
        headers: List[str],
        rows: List[Row]
    ) -> Tuple[List, List]:
        return headers, rows
