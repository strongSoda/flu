import click

@click.command()
@click.option('--name',prompt='Your good name?', default='World',help='your name')
def hello(name):
    """CLI to generate beautiful & optimised website scaffolds"""
    click.echo('Hello, {}!'.format(name))

if __name__ == '__main__':
    hello()
