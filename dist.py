#!/usr/bin/env python

"""A separate CLI entry point for creating the distribution file.  The
distribution file contains the SQLite database file with the frameset structured
data and the embeddings for various facets of the contained role sets.

"""

from zensols import deepnlp

# initialize the NLP system
deepnlp.init()


if (__name__ == '__main__'):
    from zensols.cli import ConfigurationImporterCliHarness
    harness = ConfigurationImporterCliHarness(
        src_dir_name='src/python',
        app_factory_class='zensols.propbankdb.ApplicationFactory',
        app_config_resource='deploy-resources/app.conf',
        proto_args='proto',
        proto_factory_kwargs={'reload_pattern': r'^zensols.propbankdb'},
    )
    harness.run()
