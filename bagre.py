from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
from time import sleep

class Bagre:
    def __init__(self, server, nick, name, mail, channel):
        self.s = socket(AF_INET, SOCK_STREAM)
        self.s.connect((server,6667))
        sleep(0.5)
        self.s.recv(4096)
        self.nick = nick
        self.name = name
        self.mail = mail
        self.data = ''
        self.channel = channel
        self.command = None
        self.close = False

    def sendCommand(self, cmd):
        cmd = cmd + '\r\n'
        self.s.send(cmd.encode())

    def sendPingResponse(self):
        if self.data.find('PING') != -1:
            self.sendCommand('PONG ' + self.data.split()[1])
            sleep(15)

    def run(self):
        self.sendCommand('NICK ' + self.nick)
        self.sendCommand('USER ' + self.nick + ' ' + self.name + ' ' + self.mail + ' : OpenBSD-BR')
        self.sendCommand('JOIN ' + self.channel)

        self.sendCommand('PRIVMSG ' + self.channel + ' Puff!')

        while self.close == False:
            self.data = self.s.recv(4096)
            self.data = self.data.decode()
            self.sendPingResponse()
            sleep(0.5)

if __name__ == '__main__':
    server = 'irc.freenode.net'
    nick = 'bagre'
    name = 'openbsd-br'
    mail =  'shazaum@gmail.com'
    channel = '#openbsd-br'

    bot = Bagre(server, nick , name , mail, channel)
    bot.run()
