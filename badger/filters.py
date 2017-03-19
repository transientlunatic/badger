
from jinja2 import Template, Environment, FileSystemLoader
import pypandoc, os

class Filter(object):
    def __init__(self, page, theme=None):
        """
        Make an output filter for a page object.
        
        Parameter
        ---------
        page : badger page
           The page which is being output.
        """
	if theme == None:
            theme = "{}/layouts/{}".format(os.environ['BADGER'], self.name)
        self.env = Environment(loader=FileSystemLoader(theme))
        self.page = page

    def __str__(self):
        if 'layout' not in self.page.content.keys():
            layout = "body"
        else:
            layout = self.page.content['layout']
        return self.env.get_template('{}.{}'.format(layout, self.extension)).render(meta=self.page.content, body=self.text())

    def __repr__(self):
        return self.__str__()

class HTML(Filter):
    name = "html"
    extension = "html"
    def text(self):
        return pypandoc.convert_text(str(self.page.content.content), self.name, format='md')

class Latex(Filter):
    name = "latex"
    extension = "tex"
    def text(self):
        return pypandoc.convert_text(str(self.page.content.content), self.name, format='md')

    
filters = {"latex": Latex, "html": HTML}
