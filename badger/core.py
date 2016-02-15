import ConfigParser
import os
from os.path import expanduser, join
from slugify import slugify
import datetime

import frontmatter

class Configuration():
    """
    Handle the configuration of Badger
    """
    def __init__(self):
        home = expanduser("~")
        self.config = ConfigParser.ConfigParser()
        self.path = join(home, '.badger')
        self.config.read(self.path)

    def set(self, cat, subcat, value):
        self.config.set(cat, subcat, value)
        with open(self.path, 'wb') as configfile:
            self.config.write(configfile)
    

class Notebook():
    """
    A notebook is a collection of notes.
    """

    def __init__(self, name):
        home = expanduser("~")
        
        self.name = name
        
        self.badger_config = ConfigParser.ConfigParser()
        config_path = join(home, '.badger')
        self.badger_config.read(config_path)

        self.foldername = join(home, self.badger_config.get('locations', 'notebook'))
        self.foldername = join(self.foldername, slugify(self.name))
        if os.path.exists(self.foldername):
            pass

    def exists(self):
        return os.path.exists(self.foldername)

    def create(self):
        home = expanduser("~")
        
        self.foldername = join(home, self.badger_config.get('locations', 'notebook'))
        self.foldername = join(self.foldername, slugify(self.name))

        if os.path.exists(self.foldername):
            print "Notebook {} already exists.".format(self.name)
            return 0

        if not os.path.exists(self.foldername):
            os.makedirs(self.foldername)
            os.makedirs(join(self.foldername, '.badger'))
            os.makedirs(join(self.foldername, '.projects'))
            os.makedirs(join(self.foldername, '.repositories'))
        print "A new notebook has been created at {}".format(self.foldername)

        
class Project():
    """ A badger project is the highest category of information."""
    def __init__(self, notebook, name):
        self.config = Configuration()
        self.name = name
        self.notebook = notebook
        

    def create(self):
        if self.notebook.exists():
        
            self.project_dir = join(self.notebook.foldername, '.projects')
            self.project_cfg = join(self.project_dir, slugify(self.name))

            if os.path.exists(self.project_cfg):
                print "Project {}/{} already exists.".format(self.notebook.name, self.name)
                return False
            
            with open(self.project_cfg,'w') as config_file:
                config_prj = ConfigParser.ConfigParser()
                config_prj.add_section('metadata')
                config_prj.set('metadata', 'name', self.name)
            return True
        
        else:
            print "The notebook {} does not seem to exist.".format(self.notebook.name)
            return False

        
class Note():
    """

    """
    def __init__(self, notebook, project, text):
        self.config = Configuration()
        self.notebook = notebook
        self.project = project
        self.text = text
    
    def create(self):
        dt = datetime.datetime.now()
        meta = {'date':dt}
        
        folder = join(self.notebook.foldername, str(dt.year), str(dt.month), str(dt.day))
        if not os.path.exists(folder): os.makedirs(folder)
        with open(join(folder, "{0.year}-{0.month}-{0.day}.{0.hour}-{0.minute}-{0.second}.note".format(dt)), 'w') as f:
            for key, value in meta.iteritems():
                f.write("---\n")
                f.write("{}: {}\n".format(key, value))
                f.write("---\n")
            f.write(self.text)
        pass
