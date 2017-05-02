"""Reconnaissance."""
<<<<<<< HEAD
import requests
from bs4 import BeautifulSoup
=======
import time
import smtplib
import logging
import requests
from bs4 import BeautifulSoup


class Smtp_Verify(object):
    """Look for veryfied email users."""

    def __init__(self, target_ip, target_port):
        """Store Recipiants."""
        logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")
        self.exisiting_recipiants = []
        self.non_existing_recipiants = []
        self.target_ip = target_ip
        self.target_port = target_port

    def report_users(self):
        """Report Feature."""
        logging.info("Existing Users: [{}]".format(len(self.non_existing_recipiants)))
        logging.info("Non Exsiting Users: [{}]".format(len(self.non_existing_recipiants)))

    def verify(self, user, interval):
        """Verify target using vrfy command."""
        try:
            target = smtplib.SMTP(self.target_ip, self.target_port, timeout=4)
            time.sleep(interval)
            return_code, account = target
            if return_code == 252:
                logging.info("Code: [{}] Existing Recipiant: {}".format(return_code, user))
                self.existing_recipiants.append(target)
            elif return_code == 550:
                logging.info("Code: [{}] Non Existing Recipiant: {}".format(return_code, user))
                self.non_existing_recipiants.append(target)
            elif return_code == 503:
                logging.info("Code: [{}] Authentication Required For Service")
            elif return_code == 500:
                logging.info("Code: [{}] Vrfy Not Supported By Service")
        except KeyboardInterrupt:
            self.report_users()
            exit()
        except ConnectionRefusedError:
            logging.info("{} [NO SMTP SERVICE FOUND]".format(self.target_ip))
        except smtplib.socket.timeout:
            logging.info("{} [DOWN]".format(self.target_ip))
        finally:
            time.sleep(interval)
>>>>>>> origin/master


class Scrape(object):
    """Fecthes a Specific page and finds tags."""

    def __init__(self, page):
        """Start Parser."""
        self.tags = []
        self.page = requests.get(page)
        self.content = self.page.content
        self.href_parser = BeautifulSoup(self.content, "html.parser")

    def __len__(self):
        """Return the amount of tags."""
        return len(self.tags)

    def scrape(self, tag):
        """Scrape the chosen tag."""
        for tags in self.href_parser.find_all(tag):
            self.tags.append(tags)
        return self.tags
