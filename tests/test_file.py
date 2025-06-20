# from argparse import ArgumentParser, Namespace
import re
from parser.commands import FileCommand

from .base_class import BaseCommandTestClass


class TestFileCommand(BaseCommandTestClass):
    command_cls = FileCommand

    def test_add_argument(self, parser, command):
        command.add_argument()
        args = parser.parse_args(['--file', 'example.csv'])
        assert (
            re.fullmatch(r'\D+\.csv', args.file) is not None
        ), 'Невалидный файл.'
        assert (
            args.file == 'example.csv'
        ), 'Значение аргумента не соответствует заданному.'

    def test_bind_arg(self, parser, command):
        command.add_argument()
        args = parser.parse_args(['--file', 'example.csv'])
        command.bind_arg(args)
        assert (
            re.fullmatch(r'\D+\.csv', args.file) is not None
        ), 'Невалидный файл.'
        assert (
            command.arg == 'example.csv'
        ), 'Значение аргумента не соответствует заданному.'

    def test_run(self, parser, command, headers, rows):
        command.add_argument()
        args = parser.parse_args(['--file', 'example.csv'])
        command_headers, command_rows = command.run(args, headers, rows)
        assert (
            command_headers == headers
        ), 'Заголовки не соответствуют заданным.'
        assert (
            command_rows == rows
        ), 'Записи не соответствуют заданным.'
