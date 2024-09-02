import typer
import time


def main():
    prenoms = ["Patrick", "Marie", "Julie", "Paul", "Pierre"]
    with typer.progressbar(prenoms) as progress:
        for prenom in progress:
            time.sleep(1)

#  [####################################]  100%        
if __name__ == '__main__':
    typer.run(main)