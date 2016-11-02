# Penlib
A Python3 Penetration Testing Package

# Requirements
- bs4
- requests

# Installing Penlib
pip install penlib

# Importing specific features
from penlib import *

# Creating the Object
netgear = RouterDAuth()

# Retreiving Passwords
netgear.getpasswords("netgear")

# Setting the target router web interface login page
netgear.target("http://192.168.1.1/")

# Using retrieved credentials and attempt login
netgear.check(netgear.usernames, netgear.passwords)
