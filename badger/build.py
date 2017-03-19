"""
This module contains the logic required to build badger notes and
other badger formats into pretty output formats such as HTML and
latex.
"""

import glob, os
import yaml
import frontmatter
from datetime import datetime
#import filters
import parsedatetime as pdt
#import markdown

# Set-up defaults for the date-time parser
c = pdt.Constants()
c.BirthdayEpoch = 80
p = pdt.Calendar(c)


class Page(object):
    """
    This object represents a page from a notebook. In the case of a
    labbook this might be the page of the day, or in another notebook
    it might be a topic-specific page. Pages are stored as plaintext
    with yaml frontmatter in the same way as Jekyll.
    """

    FIELDS = ["title", "date"]
    REQUIRED_FIELDS = []
    
    def __init__(self):
        """
        Initialise the page.
        """
        pass

    def echo(self):
        """
        Print the note to the CLI.
        """
        print(self.content)
    
    def load(self, filename):
        """
        Load a page from a textfile.

        Parameters
        ----------
        filename : str
           The path to the file to be loaded.
        """
        self.content = frontmatter.load(filename)

        for field in self.REQUIRED_FIELDS:
            if field not in self.content.keys():
                print "[!] {} is not present in the YAML frontmatter.".format(field)
        for field in self.FIELDS:
            if field not in self.content.keys():
                self.content[field] = ""

    def create_frontmatter(self):
        """
        Create the frontmatter for a page.
        """
        pass

        
                
    def save(self, fieldname):
        """
        Save a page to a textfile.

        Parameters
        ----------
        filename : str
           The path to the file to be loaded.
        """
        with open(filename, "w") as f:
            frontmatter.dump(self.content, f)

    def output(self, outfile, filter):
        """
        Output the page using a given filter.

        Parameters
        ----------
        outfile : str
           The output file where the built file should be written.
        filter : badger filter
           The filter which the plaintext file should be pushed through to produce the
           output.
        """
        outputable = filter(self)
        with open(outfile, "w") as f:
            f.write(str(outputable))

class Notebook(object):
    """
    Represents a Badger notebook.
    """

    def __init__():
        pass
