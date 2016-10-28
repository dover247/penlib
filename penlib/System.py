from platform import *


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
