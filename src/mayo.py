#!/usr/bin/env python3
from settings import Settings

import socket
import re

class Mayo(object):
    def __init__(self):
        self.settings = Settings()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.sock.connect((self.settings.host, self.settings.port))
        self.sock.send(("PASS %s\r\n" % self.settings.oauth).encode('utf-8'))
        self.sock.send(("NICK %s\r\n" % self.settings.nick).encode('utf-8'))
        self.sock.send(("JOIN #%s\r\n" % self.settings.channel).encode('utf-8'))
        
    def run(self):
        self.connect();

        data = ""
        
        while True:
            try:
                data = data + self.sock.recv(1024).decode('utf-8')
                data_split = re.split(r"[~\r\n]+", data)
                data = data_split.pop()

                for line in data_split:
                    line = str.rstrip(line)
                    line = str.split(line)

                    if len(line) >= 1:
                        if line[0] == "PING":
                            con.send(bytes('PONG %s\r\n' % line[1], 'utf-8'))

                        if line[1] == 'PRIVMSG':
                            print(line)

            except socket.error:
                print("Socket error")

            except socket.timeout:
                print("Socket timeout")
                            
Mayo().run()
