import typer
from typing import Optional
from pathlib import Path

app = typer.Typer()


def main(extension: str,
         directory: Optional[str] = typer.Argument(None, help="Dossier dans lequel checher."),
         delete: bool = typer.Option(False, help="Supprime les fichiers trouvés.")):
    """
    Affiche les fichiers trouvés avec l'extension donnéé.
    :param extension:
    :param directory:
    :param delete:
    :return:

    """


if __name__ == '__main__':
    typer.run(main)
