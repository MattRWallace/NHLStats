from pathlib import Path

import typer
from nhlpy import NHLClient
from sqlitedict import SqliteDict

from shared.utility import Utility


class ExecutionContext:
    _app_name = "nhlpredictor"
    _app_dir_set = False
    
    def __new__(cls):
        if not getattr(cls, '_instance', None):
            cls._instance = super(type(ExecutionContext), cls).__new__(cls)
        return cls._instance

    @property
    def client(self):
        if getattr(self, '_client', None) is None:
            self._client = NHLClient()
        return self._client
    
    @property
    def summarizer_type(self):
        return self._summarizer

    @summarizer_type.setter
    def summarizer_type(self, value):
        self._summarizer = value

    @property
    def database(self):
        if getattr(self, '_database', None) is None:
            self._database = SqliteDict(Utility.get_db_name())
        return self._database
    
    @property
    def is_playoffs(self):
        return self._is_playoffs

    @is_playoffs.setter
    def is_playoffs(self, value: bool):
        self._is_playoffs = value

    @property
    def allow_update(self):
        return self._allow_update

    @allow_update.setter
    def allow_update(self, value: bool):
        self._allow_update = value

    @property
    def app_dir(self) -> Path:
        if self._app_dir is None:
            typer.get_app_dir(ExecutionContext._app_name)
        return self._app_dir

    @app_dir.setter
    def app_dir(self, value: Path):
        if ExecutionContext._app_dir_set:
            # TODO: shouldn't use general excdeption
            raise Exception("File path already set.")
        self._app_dir = value
        ExecutionContext._app_dir_set = True