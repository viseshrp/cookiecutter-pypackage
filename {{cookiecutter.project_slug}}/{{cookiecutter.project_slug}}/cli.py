# -*- coding: utf-8 -*-

"""Console script for {{cookiecutter.project_slug}}."""
# enable absolute imports of this module for Python2.x
from __future__ import absolute_import
from __future__ import unicode_literals  # unicode support for py2

import click

from .{{cookiecutter.project_slug}} import run
from . import __version__


@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.version_option(__version__, '-v', '--version')
@click.argument('myarg')
def main(myarg):
    """
    CLI tool to

    Example usages:


    """
    try:
        run(myarg)
    except Exception as e:
        # all other exceptions
        raise click.ClickException(e)


if __name__ == "__main__":
    main()  # pragma: no cover
