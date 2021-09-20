# -*- coding=utf-8 -*-
import argparse as ap
import dataclasses
import typing as t
import logging


logger = logging.getLogger(__package__)
logger.setLevel(logging.WARNING)


MISSING = object()


class CommandApp(object):
    r"""

    """

    def __init__(self, *, parser: ap.ArgumentParser = MISSING):
        if parser is MISSING:
            logger.debug("No parser provided")
            parser = get_default_parser()

        self.parser = parser
        self._is_prepared: bool = False

        self.registered: t.Dict[str, Command] = {}

    def prepare(self):
        logger.info("App gets prepared")
        self._is_prepared = True

    def run(self):
        if not self.is_prepared:
            self.prepare()
        logger.info("App runs")

    @property
    def is_prepared(self) -> bool:
        return self._is_prepared

    def register(self, cmd: t.Callable = None, **kwargs):
        pass

    #
    #
    #

    @property
    def version(self):
        return getattr(self, '_version')

    @version.setter
    def version(self, val: t.AnyStr):
        setattr(self, '_version', val)


@dataclasses.dataclass
class Command:
    name: str  # name of the command
    command: t.Callable  # callback
    config: t.Dict[str, t.Any]  # configurations like `name`


def get_default_parser() -> ap.ArgumentParser:
    return ap.ArgumentParser(
        formatter_class=ap.ArgumentDefaultsHelpFormatter,
        add_help=True
    )
