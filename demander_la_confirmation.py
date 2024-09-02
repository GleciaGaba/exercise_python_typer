import typer


def main(delete: bool = typer.Option(False, help="Suprprime les fichiers trouvés"),
         extension: str = typer.Argument("txt", help="Extension à chercher")):
    """
    # Afficher les fichiers trouvés avec l'extension donnée.
    :param delete:
    :param extension:
    :return:
    """
    extension = typer.prompt("Quelle extension souhaitez-vous chercher?")
    if delete:
        confirm = typer.confirm("Souhaitez vous vraiment supprimer les fichiers?")
        if not confirm:
            typer.echo("On annule l'opération.")
            raise typer.Abort()
    print("Suppression des fichiers.")

if __name__ == '__main__':
    typer.run(main)
