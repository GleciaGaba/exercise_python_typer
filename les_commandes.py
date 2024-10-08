import typer

app = typer.Typer()


def main(delete: bool = typer.Option(False, help="Supprime les fichiers trouvés"),
         extension: str = typer.Argument("txt", help="Extension à chercher")):
    """
    Afficher les fichiers trouvés avec l'extension donnée.
    :param delete:
    :param extension:
    :return:
    """
    typer.echo(f"Recherche des fichiers avec l'extension {extension}.")
    if delete:
        typer.echo("Suppression des fichiers")


@app.command("search")
def search_py():
    main(delete=False, extension="py")


@app.command("delete")
def delete_py():
    main(delete=True, extension="py")


if __name__ == '__main__':
    app()
