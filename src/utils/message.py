#!/usr/bin/env python3

class Message:

    def __init(self, socket):
        self.sock = socket

    def _decode(self, data):
        """Decode helper function."""
        if type(data) is bytes:
            return data.decode('utf8')
        return data
        
    def get_message(self, data):
        return {
            'channel' = re.findall(r'^:.+\![a-zA-Z0-9_]+@[a-zA-Z0-9_]+.+ PRIVMSG (.*?) :', _decode(data))[0],
            'username' = re.findall(r'^:([a-zA-Z0-9_]+)\!', _decode(data))[0],
            'message' = re.findall(r'PRIVMSG #[a-zA-Z0-9_]+ :(.+)', _decode(data))[0]
        }

    def send_message(self, channel, message):
        self.sock.send('PRIVMSG %s :%s\n' % (channel, message.encode('utf-8')))
