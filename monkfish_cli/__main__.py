# this is to be run as a module with python -m monkfish_cli if desired
# see https://typer.tiangolo.com/tutorial/package/#add-a-__main__py
# `python -m monkfish_cli --help`

from .main import app
app(prog_name="monkfish-cli")