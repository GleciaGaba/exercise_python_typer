import typer

# argument par default
def main(extension: str = "txt"):
    """ Affiche les fichiers trouvés avec l'extension données

    :return:
    """
    typer.echo(f"Recherche de fichiers avec l'extension {extension}.")


typer.run(main)


def main_1(extension: str = typer.Argument(..., help="Extension à chercher")):
    """ Affiche les fichiers trouvés avec l'extension données

    :return:
    """
    typer.echo(f"Recherche de fichiers avec l'extension {extension}.")


typer.run(main_1)

# il faudra passer l'argument 'python main_01.py txt'
def main_2(extension: str):
    """ Affiche les fichiers trouvés avec l'extension données

    :return:
    """
    typer.echo(f"Recherche de fichiers avec l'extension {extension}.")


typer.run(main)