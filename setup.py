from setuptools import setup, find_packages


setup(name='penlib',
        author="George Sauceda",
        author_email="secondclass325@gmail.com",
        url="https://github.com/dover247/penlib/",
        version='0.1.5',
        description='A Python Penetration Package',
        packages=find_packages(),
        install_requires=['bs4', 'requests'])
