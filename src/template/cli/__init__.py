import click

from ..__about__ import __version__


@click.group(context_settings={'help_option_names': ['-h', '--help']}, invoke_without_command=True)
@click.version_option(version=__version__, prog_name='template')
@click.pass_context
def template(ctx: click.Context):
    click.echo('Hello world!')
