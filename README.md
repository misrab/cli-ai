# cli-py

A template for a python cli using typer and poetry.

## Setup

To install locally without pip, run

`poetry install`

For publishing, see [poetry instructions](https://typer.tiangolo.com/tutorial/package/#try-your-cli-program).

The default cli name is `monkfish-cli`. Change this to your desired cli name in the folowing:

- `monkfish_cli` folder name
- `/monkfish_cli/__main__.py` variable `prog_name` for usage as a python module
- `pyproject.toml`

## Usage

Once installed, run

`monkfish-cli --help`

## Acknowledgements

Based on the fantastic [typer](https://typer.tiangolo.com) library.

Packaging is handled using [poetry](https://python-poetry.org/).

[pipx](https://github.com/pypa/pipx) is used for isolated environments.
