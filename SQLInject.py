import requests


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
