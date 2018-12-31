# -*- coding: utf-8 -*-

"""Console script for {{cookiecutter.project_slug}}."""
# enable absolute imports of this module for Python2.x
from __future__ import absolute_import
from __future__ import unicode_literals  # unicode support for py2

import click

from .{{cookiecutter.project_slug}} import run


@click.command(context_settings=dict(help_option_names=['-h', '--help']))
def main(args=None):
    """
    CLI tool to

    Example usages:


    """
    try:
        run(args)
    except Exception as e:
        # all other exceptions
        raise click.ClickException(e)


if __name__ == "__main__":
    main()  # pragma: no cover
