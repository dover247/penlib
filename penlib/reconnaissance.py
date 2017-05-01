"""Reconnaissance."""
import requests
from bs4 import BeautifulSoup


class Scrape(object):
    """Fecthes a Specific page and finds tags."""

    def __init__(self, page):
        """Start Parser."""
        self.tags = []
        self.page = requests.get(page)
        self.content = self.page.content
        self.href_parser = BeautifulSoup(self.content, "html.parser")

    def __len__(self):
        """Return the amount of tags."""
        return len(self.tags)

    def scrape(self, tag):
        """Scrape the chosen tag."""
        for tags in self.href_parser.find_all(tag):
            self.tags.append(tags)
        return self.tags
