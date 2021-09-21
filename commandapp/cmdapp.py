# -*- coding=utf-8 -*-
import sys
import argparse as ap
import typing as t
import types
import logging
import traceback

from .classes import *
from . import command_parser as cmdparser


logger = logging.getLogger(__package__)
logger.setLevel(logging.WARNING)


MISSING = object()


class CommandApp(object):
    r"""

    """

    def __init__(self, *, parser: ap.ArgumentParser = MISSING, auto_type: bool = True):
        if parser is MISSING:
            logger.debug("No parser provided")
            parser = get_default_parser()

        self.parser = parser
        self._is_prepared: bool = False

        self.auto_type = auto_type

        self.registered: t.Dict[str, t.Union[Command, callable]] = {}

    def prepare(self):
        logger.info("App gets prepared")
        registered = self.registered.copy()
        self.registered.clear()

        helper = self.parser.add_subparsers(  # create helper for new sup-commands
            title="command",
            dest='CommandApp_command',
            help='available commands')

        for command in registered.values():  # got through each registered command (registered: Tuple[callable, kwargs])
            command = cmdparser.add_subparser(helper, command, auto_type=self.auto_type)
            self.registered[command.name] = command

        self._is_prepared = True

    def run(self):
        if not self.is_prepared:
            self.prepare()
        logger.info("App runs")
        if len(sys.argv) <= 1:
            self.parser.print_usage()
            sys.exit(-1)
        namespace: ap.Namespace = self.parser.parse_args()
        runconfig = namespace.__dict__.copy()
        commandname = runconfig.pop('CommandApp_command')
        command = self.registered[commandname]
        try:
            command.command(**runconfig)
        except Exception as exception:
            tb = iter(traceback.extract_tb(exception.__traceback__))
            next(tb)  # remove first item
            traceback.print_list(tb)
            print(*traceback.format_exception_only(type(exception), exception), sep="", end="", file=sys.stderr)
            sys.exit(-1)

    @property
    def is_prepared(self) -> bool:
        return self._is_prepared

    def register(self, command: t.Callable = None, **config):
        r"""

        :param command:
        :param config:
        :return:
        """
        command: types.FunctionType
        if callable(command):
            # @app.register
            # def new_cmd(): ...
            name = command.__qualname__  # temporary name (gets overwritten in .prepare())
            self.registered[name] = Command(name, command, config)
            return command
        else:
            # @app.register(name=...)
            # def new_cmd(): ...
            def shell(f):
                return self.register(f, **config)

            return shell

    #
    #
    #

    @property
    def version(self):
        return getattr(self, '_version')

    @version.setter
    def version(self, val: t.AnyStr):
        setattr(self, '_version', val)


def get_default_parser() -> ap.ArgumentParser:
    return ap.ArgumentParser(
        formatter_class=ap.ArgumentDefaultsHelpFormatter,
        add_help=True
    )
