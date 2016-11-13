import requests
from bs4 import BeautifulSoup


class Scrape(object):
    '''Fecthes a Specific page and finds tags.'''
    def __init__(self, page):
        self.tags = []
        self.page = requests.get(page)
        self.content = self.page.content
        self.href_parser = BeautifulSoup(self.content, "html.parser")

    def __len__(self):
        return len(self.tags)

    def __enter__(self):
        return self

    def __exit__(self, type, error, traceback):
        if error:
            print(error)

    def scrape(self, tag):
        '''scrapes the chosen tag.'''
        for tags in self.href_parser.find_all(tag):
            self.tags.append(tags)
        return self.tags
