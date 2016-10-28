import requests
from bs4 import BeautifulSoup


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
