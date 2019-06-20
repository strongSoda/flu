import click
from hello import hello

@click.command()
def flu():
    hello()

if __name__ == '__main__':
    flu()
