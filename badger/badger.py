import click
import os
import build as bld
import filters
import yaml
from datetime import datetime

config= None
for loc in os.curdir, os.path.expanduser("~"), "/etc/badger":
    try: 
        with open(os.path.join(loc,"badger.conf")) as source:
            config = yaml.load(source)
    except IOError:
        pass


def get_notebook_meta(notebook):
    if "extension" not in config['notebooks'][notebook]:
        config['notebooks'][notebook]['extension'] = ".notes"
        config['notebooks'][notebook]['title'] = notebook
    return config['notebooks'][notebook]
    
@click.group()
def cli():
    """
    Badger is a command-line note-management tool designed for
    managing an academic work-flow.

    """
    pass

@cli.command()
@click.argument("notebook")
@click.argument("note")
def show(notebook, note):
    """
    Print the contents of a note to the terminal.
    """

    meta = get_notebook_meta(notebook)
    filepath = os.path.join(meta['location'], note+meta['extension'])
    page = bld.Page()
    page.load(filepath)
    page.echo()
    

@cli.command()
@click.argument("notebook")
@click.argument("note")
@click.argument("outfile")
@click.option("--format", default="html")
def build(notebook, note, outfile, format):
    """

    Build a badger notebook to a pretty output format, 
    for example latex or HTML.

    """
    meta = get_notebook_meta(notebook)
    filepath = os.path.join(meta['location'], note+meta['extension'])
    page = bld.Page()
    page.load(filepath)
    filt = filters.filters[format]
    page.output(outfile, filt)
    


@cli.command()
@click.argument("notebook")
@click.argument("expression")
def find(notebook, expression):
    """
    Find a note file. 
    """
    import subprocess
    meta = get_notebook_meta(notebook)
    click.echo(subprocess.check_output(["find", meta['location'], "-name", expression+".*"]))
    

@cli.command()
@click.argument("notebook")
@click.argument("title", required=False)
def edit(notebook, title):
    """
    Edit a note.
    """
    click.echo(config)
    import subprocess
    if title is None:
        title = datetime.now().strftime('%Y-%m-%d')
    date = datetime.now().strftime('%Y-%m-%d')
    meta = get_notebook_meta(notebook)
    filepath = os.path.join(meta['location'], title+meta['extension'])
    if os.path.isfile(filepath) :
        # If the file exists already just go ahead and open it
        pass
    else:
        #Otherwise we'll need to make it from a template first.
        from jinja2 import Template, Environment, FileSystemLoader
        import shutil
        fro = os.path.join(meta['location'], title)
        to = os.path.join(meta['location'], title+meta['extension'])
        to_dir = os.path.join(meta['location'], title)
        os.mkdir(to_dir)
        env = Environment(loader=FileSystemLoader(config['templates']))
        a = env.get_template(notebook+".temp").render(date=date, title=title)
        with open(to, "w") as f:
            f.write(a)
    subprocess.call([config["editor"], filepath])
    pass



if __name__ == '__main__':
    badger_greetings()


