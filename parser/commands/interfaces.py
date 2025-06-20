from abc import ABC, abstractmethod
from argparse import ArgumentParser, Namespace
from typing import List, NamedTuple, Tuple


class Condition(NamedTuple):
    """Условие, установленное в аргументе."""
    column: str
    value: str


class Row(NamedTuple):
    """Строка обрабатываемого CSV-файла."""
    name: str
    brand: str
    brandprice: str
    rating: str


class BaseCommand(ABC):
    """Общий интерфейс аргумента командной строки."""

    def __init__(self, parser: ArgumentParser) -> None:
        self.parser = parser
        self.arg: str
        self.condition = Condition

    @abstractmethod
    def add_argument(self) -> None:
        pass

    @abstractmethod
    def get_key(self) -> str:
        pass

    @abstractmethod
    def run(
        self,
        arg_value: str,
        headers: List[str],
        rows: List[Row]
    ) -> Tuple[List, List]:
        pass

    def bind_arg(self, args: Namespace) -> None:
        self.arg = getattr(args, self.get_key(), '')
