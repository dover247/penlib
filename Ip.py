import re
import requests


class Ip(object):
    '''Fetches ip using http://checkip.dyndns.org'''
    def __init__(self):
        self.url = 'http://checkip.dyndns.org'

    def __enter__(self):
        return self

    def __exit__(self, type, error, traceback):
        if error:
            print(error)

    '''requests a page and uses regular expressions to extract the Ip
        and returns the value'''
    def get(self):
        request = requests.get(self.url)
        ip = re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3}", request.text)[0]
        return ip
