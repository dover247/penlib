import os


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

    def search_file(self, filename, path):
        '''searches for files using a path and file name'''
        for path, directories, files in os.walk(path):
            for Filename in files:
                if filename.lower() in Filename.lower():
                    print(os.path.join(path, Filename))
                    self.count.append(Filename)
