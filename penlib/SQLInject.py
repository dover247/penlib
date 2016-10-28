import requests

class SQLInject(object):
    '''SQL Injection.'''
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

    def urlinject(self, injection):
        '''Inject in url.'''
        page = requests.get(self.url + injection)
        errors = re.findall('You have an error in your SQL syntax;',
                            page.content.decode())
        for error in errors:
            if error:
                self.errors.append(error)
                return True
        return False

    def forminject(self, injection):
        '''Sql inject into a form.'''
        page = request.post(self.url, data=injection)
        return page.content()
