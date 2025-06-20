from parser.commands import FileCommand, WhereCommand
from parser.main import filter_commands_and_bind_arg, main
from unittest.mock import MagicMock, patch


def test_main(monkeypatch):
    monkeypatch.setattr('sys.argv', ['prog', '--file', 'example.csv'])
    mock_csv_parser = MagicMock()
    mock_csv_parser.show_result.return_value = 'ok'
    with patch('parser.main.CSVParser', return_value=mock_csv_parser):
        result = main()
    mock_csv_parser.show_result.assert_called_once()
    assert result == 'ok'


def test_bind_arg_and_filter_commands(parser):
    file_command = FileCommand(parser)
    file_command.add_argument()
    where_command = WhereCommand(parser)
    where_command.add_argument()
    args = parser.parse_args(
        ['--file', 'example.csv', '--where', 'column=value']
    )
    filtered_commands = filter_commands_and_bind_arg(
        args, [file_command, where_command]
    )
    assert (
        filtered_commands == [file_command, where_command]
    ), 'Список команд отфильтрован некорректно.'
