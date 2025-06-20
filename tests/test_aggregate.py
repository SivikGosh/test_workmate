from parser.commands import AggregateCommand

import pytest
from pytest_lazyfixture import lazy_fixture  # type: ignore

from .base_class import BaseCommandTestClass


class TestAggretageCommand(BaseCommandTestClass):
    command_cls = AggregateCommand

    def test_add_argument(self, parser, command):
        command.add_argument()
        args = parser.parse_args(['--aggregate', 'column=value'])
        assert (
            args.aggregate == 'column=value'
        ), 'Значение аргумента не соответствует заданному.'

    def test_get_key(self, command):
        key = command.get_key()
        assert key == 'aggregate', 'Ключ не совпадает.'

    def test_bind_arg(self, parser, command):
        command.add_argument()
        args = parser.parse_args(['--aggregate', 'column=value'])
        command.bind_arg(args)
        assert (
            command.arg == 'column=value'
        ), 'Значение аргумента не соответствует заданному.'

    @pytest.mark.parametrize(
        ('arg_value', 'expected_header', 'expected_result'), [
            ('brandprice=avg', ['avg'], [['782.33']]),
            ('brandprice=min', ['min'], [['149.0']]),
            ('brandprice=max', ['max'], [['1199.0']]),
            ('rating=avg', ['avg'], [['4.6']]),
            ('rating=min', ['min'], [['4.1']]),
            ('rating=max', ['max'], [['4.9']]),
            (
                'name=avg',
                ['name', 'brand', 'brandprice', 'rating'],
                lazy_fixture('rows')
            ),
            (
                'name=min',
                ['name', 'brand', 'brandprice', 'rating'],
                lazy_fixture('rows')
            ),
            (
                'name=max',
                ['name', 'brand', 'brandprice', 'rating'],
                lazy_fixture('rows')
            ),
            (
                'column',
                ['name', 'brand', 'brandprice', 'rating'],
                lazy_fixture('rows')
            ),
        ])
    def test_run(
        self,
        parser,
        command,
        headers,
        rows,
        arg_value,
        expected_header,
        expected_result
    ):
        command.add_argument()
        args = parser.parse_args(['--aggregate', arg_value])
        command_headers, command_rows = command.run(
            args.aggregate,
            headers,
            rows
        )
        assert (
            command_headers == expected_header
        ), 'Заголовки не соответствуют заданным.'
        assert (
            command_rows == expected_result
        ), 'Записи не соответствуют заданным.'
