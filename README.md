# Penlib
A Python3 Penetration Testing Package

# Installing Penlib
pip3 install penlib (Linux)

python3 -m pip install penlib (Windows)

# Example Code
from penlib import exploitation

# Creating the Object
netgear = exploitation.RouterDAuth()

# Retreiving Passwords
netgear.getpasswords("netgear")

# Setting the target router web interface login page
netgear.target("http://192.168.1.1/")

# Using retrieved credentials and attempt login
netgear.check(netgear.usernames, netgear.passwords)
