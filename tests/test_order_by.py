from parser.commands import OrderByCommand

import pytest
from pytest_lazyfixture import lazy_fixture  # type: ignore

from .base_class import BaseCommandTestClass


class TestAggretageCommand(BaseCommandTestClass):
    command_cls = OrderByCommand

    def test_add_argument(self, parser, command):
        command.add_argument()
        args = parser.parse_args(['--order-by', 'column=value'])
        assert (
            args.order_by == 'column=value'
        ), 'Значение аргумента не соответствует заданному.'

    def test_get_key(self, command):
        key = command.get_key()
        assert key == 'order_by', 'Ключ не совпадает.'

    def test_bind_arg(self, parser, command):
        command.add_argument()
        args = parser.parse_args(['--order-by', 'column=value'])
        command.bind_arg(args)
        assert (
            command.arg == 'column=value'
        ), 'Значение аргумента не соответствует заданному.'

    @pytest.mark.parametrize(
        ('arg_value', 'expected'),
        [
            ('name=asc', lazy_fixture('asc_name_rows')),
            ('name=desc', lazy_fixture('desc_name_rows')),
            ('brand=asc', lazy_fixture('rows')),
            ('brand=desc', lazy_fixture('desc_brand_rows')),
            ('brandprice=asc', lazy_fixture('desc_name_rows')),
            ('brandprice=desc', lazy_fixture('asc_name_rows')),
            ('rating=asc', lazy_fixture('desc_brand_rows')),
            ('rating=desc', lazy_fixture('rows')),
            ('сolumn=asc', lazy_fixture('rows')),
            ('сolumn=value', lazy_fixture('rows')),
            ('сolumn', lazy_fixture('rows')),
        ],
    )
    def test_run(self, parser, command, headers, rows, arg_value, expected):
        command.add_argument()
        args = parser.parse_args(['--order-by', arg_value])
        command_headers, command_rows = command.run(
            args.order_by,
            headers,
            rows
        )
        assert (
            command_headers == headers
        ), 'Заголовки не соответствуют заданным.'
        assert (
            command_rows == expected
        ), 'Записи не соответствуют заданным.'
