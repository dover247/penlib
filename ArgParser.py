from argparse import *


class ArgParser(ArgumentParser):
    '''Program Usage. Returns arguments being passed'''
    def option(self, arg, optional_arg, descr=''):
        self.add_argument(arg, optional_arg, help=descr)

    '''parses arguments'''
    def parse(self):
        return self.parse_args()
