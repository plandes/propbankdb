#!/usr/bin/env python

"""Demonstrate role access from the database as a complete CLI application.

"""
__author__ = 'Paul Landes'

from dataclasses import dataclass
import logging
import itertools as it
from io import StringIO
from zensols.cli import CliHarness, ProgramNameConfigurator
from zensols.propbankdb import Function, Roleset, Role, Database

logger = logging.getLogger(__name__)
CONFIG = """
[cli]
apps = list: log_cli, app

[log_cli]
class_name = zensols.cli.LogConfigurator
format = ${program:name}: %%(message)s
log_name = ${program:name}
level = debug

[import]
sections = list: fs_imp

[fs_imp]
type = import
config_files = list:
  resource(zensols.util): resources/default.conf,
  resource(zensols.deeplearn): resources/default.conf,
  resource(zensols.deepnlp): resources/default.conf,
  resource(zensols.deeplearn): resources/obj.conf,
  resource(zensols.deepnlp): resources/obj.conf,
  resource(zensols.propbankdb): resources/default.conf,
  resource(zensols.propbankdb): resources/obj.yml,
  resource(zensols.propbankdb): resources/embed.yml

[app]
class_name = ${program:name}.Application
db = instance: pbdb_db
"""


@dataclass
class Application(object):
    """Demonstrate role access from the database.

    """
    db: Database

    def show(self, limit: int = 1):
        """Show roles and their embeddings.

        :param limit: the number of roles to output

        """
        rs: Roleset
        for rs in it.islice(self.db.roleset_stash.values(), limit):
            print(rs)
            role: Role
            for role in rs.roles:
                f: Function = role.function
                print(f'  {role.description}: {role.embedding.shape}')
                if f.has_description:
                    print(f'    f: {role.function.label}: {f.embedding.shape}')


if (__name__ == '__main__'):
    CliHarness(
        app_config_resource=StringIO(CONFIG),
        app_config_context=ProgramNameConfigurator(
            None, default='roleshow').create_section(),
        proto_factory_kwargs={'reload_pattern': '^roleshow'},
    ).run()
