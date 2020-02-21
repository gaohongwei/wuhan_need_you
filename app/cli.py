import os
import click
from flask.cli import AppGroup

def update():
    """Update all languages."""
    if os.system('pybabel extract -F babel.cfg -k _l -o messages.pot .'):
        raise RuntimeError('extract command failed')
    if os.system('pybabel update -i messages.pot -d app/translations'):
        raise RuntimeError('update command failed')
    os.remove('messages.pot')

def compile():
    """Compile all languages."""
    if os.system('pybabel compile -d app/translations'):
        raise RuntimeError('compile command failed')


def init(lang):
    """Initialize a new language."""
    if os.system('pybabel extract -F babel.cfg -k _l -o messages.pot .'):
        raise RuntimeError('extract command failed')
    if os.system(
            'pybabel init -i messages.pot -d app/translations -l ' + lang):
        raise RuntimeError('init command failed')
    os.remove('messages.pot')

# TODO: how to add description?
def register_command_group(app, groupName, description, commands):
    app_group = AppGroup(groupName)
    for name,func,arg in commands:
        if arg:
            @app_group.command(name)
            @click.argument(arg)
            def command(a):
                return func(a)
        else:
            @app_group.command(name)
            def command(a):
                return func(a)
    app.cli.add_command(app_group)

translate = [
        ('update', update, None),
        ('compile', compile, None),
        ('init', init, 'lang')
        ]
def register_commands(app):
    register_command_group(app, 'translate', 'translate the app', translate)

