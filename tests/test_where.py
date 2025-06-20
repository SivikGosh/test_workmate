from parser.commands import WhereCommand

import pytest
from pytest_lazyfixture import lazy_fixture  # type: ignore

from .base_class import BaseCommandTestClass


class TestWhereCommand(BaseCommandTestClass):
    command_cls = WhereCommand

    def test_add_argument(self, parser, command):
        command.add_argument()
        args = parser.parse_args(['--where', 'column=value'])
        assert (
            args.where == 'column=value'
        ), 'Значение аргумента не соответствует заданному.'

    def test_get_key(self, command):
        key = command.get_key()
        assert key == 'where', 'Ключ не совпадает.'

    def test_bind_arg(self, parser, command):
        command.add_argument()
        args = parser.parse_args(['--where', 'column=value'])
        command.bind_arg(args)
        assert (
            command.arg == 'column=value'
        ), 'Значение аргумента не соответствует заданному.'

    @pytest.mark.parametrize(
        ('arg_value', 'expected'),
        [
            ('name=redmi', lazy_fixture('filtered_row')),
            ('name>redmi', lazy_fixture('rows')),
            ('name<redmi', lazy_fixture('rows')),
            ('brand=xiaomi', lazy_fixture('filtered_row')),
            ('brand>xiaomi', lazy_fixture('rows')),
            ('brand<xiaomi', lazy_fixture('rows')),
            ('brandprice>1000', lazy_fixture('filtered_max_price_row')),
            ('brandprice<400', lazy_fixture('filtered_row')),
            ('brandprice=149', lazy_fixture('filtered_row')),
            ('rating>4.8', lazy_fixture('filtered_max_rating_row')),
            ('rating<4.8', lazy_fixture('filtered_row')),
            ('rating=4.1', lazy_fixture('filtered_row')),
            ('сolumn>value', lazy_fixture('rows')),
            ('сolumn<value', lazy_fixture('rows')),
            ('сolumn=value', lazy_fixture('rows')),
            ('сolumn', lazy_fixture('rows')),
        ],
    )
    def test_run(self, parser, command, headers, rows, arg_value, expected):
        command.add_argument()
        args = parser.parse_args(['--where', arg_value])
        command_headers, command_rows = command.run(args.where, headers, rows)
        assert (
            command_headers == headers
        ), 'Заголовки не соответствуют заданным.'
        assert (
            command_rows == expected
        ), 'Записи не соответствуют заданным.'
