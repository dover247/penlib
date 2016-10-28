from socket import *


class NetFuzzer(object):
    '''Fuzzer For Network Services'''
    def __init__(self, host, port):
        self.sock = socket()
        self.host = host
        self.port = port

    def __len__(self):
        return len(self.buffer)

    def __enter__(self):
        return self

    def __exit__(self, type, error, traceback):
        if error:
            print(error)

    def buildbuffer(self, chars, length):
        '''creates a buffer'''
        self.buffer = chars * length
        return self.buffer

    def fuzz(self):
        '''fuzzez the target'''
        self.sock.settimeout(10)
        self.sock.connect((self.host, self.port))
        self.sock.recv(recvsize)
        self.sock.send(self.buffer.encode())
        self.sock.recv(recvsize)
        return self.sock.recv(4096)

    def status(self):
        '''checks if service is still running'''
        service = socket()
        service.settimeout(10)
        service.connect((self.host, self.port))
        if service.recv(4096):
            return True
        return False
