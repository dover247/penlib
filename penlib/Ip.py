import re
import requests


class Ip(object):
    '''Fetches ip using http://checkip.dyndns.org.'''
    def __init__(self):
        self.url = 'http://checkip.dyndns.org'

    def __enter__(self):
        return self

    def __exit__(self, type, error, traceback):
        if error:
            print(error)

    def get(self):
        '''Requests a page and uses regular expressions to extract the Ip
            and returns the value.'''
        request = requests.get(self.url)
        ip = re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3}", request.text)[0]
        return ip
