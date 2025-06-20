from parser.commands import FileCommand, WhereCommand
from parser.main import CSVParser
from types import SimpleNamespace


class TestCSVParser:

    def test_read_the_file_success(self, parser, temp_csv_file, headers, rows):
        file_command = FileCommand(parser)
        file_command.add_argument()
        args = SimpleNamespace(file=temp_csv_file)
        csv_parser = CSVParser(args, [file_command])
        test_headers, test_rows = csv_parser._read_the_file()
        assert test_headers == headers, 'Заголовки не соответствуют заданным.'
        assert test_rows == rows, 'Записи не соответствуют заданным.'

    def test_read_the_file_fail(self):
        args = SimpleNamespace(file='no_exist_file.csv')
        csv_parser = CSVParser(args, [])
        test_headers, test_rows = csv_parser._read_the_file()
        assert test_headers == [], 'Список заголовков должен быть пуст.'
        assert test_rows == [], 'Список записей должен быть пуст.'

    def test_show_result(self, parser, temp_csv_file):
        file_command = FileCommand(parser)
        file_command.add_argument()
        where_command = WhereCommand(parser)
        where_command.add_argument()
        args = SimpleNamespace(file=temp_csv_file, where='name=redmi')
        file_command.bind_arg(args)
        where_command.bind_arg(args)
        csv_parser = CSVParser(args, [file_command])
        result = csv_parser.show_result()
        # проверка отрисовки таблицы tabulate
        assert 'name' in result
        assert 'brand' in result
        assert 'brandprice' in result
        assert 'rating' in result
        assert '╭' in result or '+' in result
