import typer

from . import models 

app = typer.Typer()

@app.command()
def translate(text: str):
    result = models.translate(text)
    typer.echo(result)

# to enable subcommands while we only have one
@app.command()
def dummy():
    return

# @app.command()
# def hello(name: str):
#     print(f"Hello {name}")


# @app.command()
# def goodbye(name: str, formal: bool = False):
#     if formal:
#         print(f"Goodbye Ms. {name}. Have a good day.")
#     else:
#         print(f"Bye {name}!")

