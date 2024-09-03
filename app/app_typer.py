import typer
from typing import Optional
from pathlib import Path

app = typer.Typer()


@app.command('run')
def main(extension: str,
         directory: Optional[str] = typer.Option(None, "--directory", "-d", help="Dossier dans lequel checher."),
         delete: bool = typer.Option(False, "--delete", "-del", help="Supprime les fichiers trouvés.")):
    """
    Affiche les fichiers trouvés avec l'extension donnéé.
    :param extension: Extension du fichier à rechercher.
    :param directory: Répertoire où effectuer la recherche.
    :param delete: Supprime les fichiers trouvés si True.
    :return:

    """

    # Définir le répertoire de recherche

    if not directory:
        directory = Path(__file__).parent / 'data'  # Répertoire courant si aucun répertoire n'est fourni
    else:
        directory = Path(directory)
    # Vérifier si le répertoire existe
    if not directory.exists():
        typer.secho(f"Le dossier '{directory}' n'existe pas.", fg=typer.colors.RED)
        raise typer.Exit()

    files = directory.rglob(f"*.{extension}")
    if delete:
        typer.confirm("Voulez-vous vraiment suprimer tous les fichiers trouvés ?", abort=True)
        for file in files:
            file.unlink()
            typer.secho(f"Suppression du fichier {file}", fg=typer.colors.RED)
    else:
        typer.secho(f"Fichier trouvés l'extension {extension} :", bg=typer.colors.BLUE, fg=typer.colors.BRIGHT_WHITE)
        for file in files:
            typer.echo(file)

@app.command()
def search(extension: str):
    """Chercher les fichiers avec l'extension donnée."""
    main(extension=extension, directory=None, delete=False)

@app.command()
def delete(extension: str):
    """Supprimer les fichiers avec l'extension donnée"""
    main(extension=extension, directory=None, delete=True)

if __name__ == '__main__':
    app()
