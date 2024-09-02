import typer
import colorama


def main():
    prenom = typer.style("Patrick", bold=True, fg=typer.colors.BRIGHT_RED)
    typer.echo(f"Bonjour {prenom}")
    typer.secho("Bonjour Glécia", fg=typer.colors.RED, bold=True)


if __name__ == '__main__':
    typer.run(main)