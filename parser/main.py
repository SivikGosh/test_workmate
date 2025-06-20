from argparse import ArgumentParser, Namespace
from typing import List

from .commands import BaseCommand
from .parser import CSVParser


def collect_commands_and_add_arg(parser: ArgumentParser) -> List[BaseCommand]:
    """Собрать все имеющиеся классы команд и добавить аргумент."""
    commands = []
    for command_cls in BaseCommand.__subclasses__():
        command = command_cls(parser)  # type: ignore
        command.add_argument()
        commands.append(command)
    return commands


def filter_commands_and_bind_arg(
    args: Namespace,
    commands: List[BaseCommand]
) -> List[BaseCommand]:
    """Отфильтровать используемые команды и присвоить значение аргумента."""
    filtered_commands = []
    for command in commands:
        key = command.get_key()
        value = getattr(args, key, None)
        if value not in (None, '', False):
            command.bind_arg(args)
            filtered_commands.append(command)
    return filtered_commands


def main():
    parser = ArgumentParser()
    commands = collect_commands_and_add_arg(parser)
    args = parser.parse_args()
    active_commands = filter_commands_and_bind_arg(args, commands)
    result = CSVParser(args, active_commands)
    return result.show_result()


if __name__ == '__main__':  # pragma: no cover
    result = main()
    print(result)
