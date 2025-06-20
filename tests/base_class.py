from parser.commands import BaseCommand
from typing import Type

import pytest


class BaseCommandTestClass:
    command_cls: Type[BaseCommand]

    @pytest.fixture
    def command_class(self):
        return self.command_cls
