import typer


def main(delete: bool = typer.Option(False, help="Supprime les fichiers trouvés"), extension: str = typer.Argument("txt", help="Extension à chercher")):
    """
    Aficher les fichiers trouvés avec l'extension donnée.
    :param delete:
    :param extension:
    :return:
    """
    print(delete)
    typer.echo(f"Recherche des fichiers avec l'extension {extension}.")


if __name__ == '__main__':
    typer.run(main)
