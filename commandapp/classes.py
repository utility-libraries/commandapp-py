# -*- coding=utf-8 -*-
import dataclasses as _dataclasses
import typing as _t


@_dataclasses.dataclass
class Command:
    name: str  # name of the command
    command: _t.Callable  # callback
    config: _t.Dict[str, _t.Any]  # configurations like `name`
