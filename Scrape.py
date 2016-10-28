<<<<<<< HEAD
import requests
from bs4 import BeautifulSoup


class Scrape(object):
    '''Fecthes a Specific page and finds links'''
    def __init__(self, page):
        self.page = requests.get(page)
        self.content = self.page.content
        self.href_parser = BeautifulSoup(self.content, "html.parser")

    def __len__(self):
        return len(self.href_parser.findAll('a'))

    def __enter__(self):
        return self

    def __exit__(self, type, error, traceback):
        if error:
            print(error)

    '''within finding all "a" tags prints the reference links'''
    def scrape(self):
        for link in self.href_parser.findAll("a"):
            print(link.get("href"))
=======
import requests
from bs4 import BeautifulSoup


class Scrape(object):
    '''Fecthes a Specific page and finds links'''
    def __init__(self, page):
        self.page = requests.get(page)
        self.content = self.page.content
        self.href_parser = BeautifulSoup(self.content, "html.parser")

    def __len__(self):
        return len(self.href_parser.findAll('a'))

    def __enter__(self):
        return self

    def __exit__(self, type, error, traceback):
        if error:
            print(error)

    '''within finding all "a" tags prints the reference links'''
    def scrape(self):
        for link in self.href_parser.findAll("a"):
            print(link.get("href"))
>>>>>>> origin/master
