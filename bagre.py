import argparse
import logging

import irc.strings

import ib3
import ib3.auth
import ib3.connection
import ib3.nick

import os


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(name)s %(levelname)s: %(message)s',
    datefmt='%Y-%m-%dT%H:%M:%SZ'
)
logging.captureWarnings(True)

logger = logging.getLogger('saslbot')

nick = os.environ['NICK']
passwd = os.environ['PASSWD']
channel = os.environ['CHANNEL']

class Bagre(ib3.auth.SASL, ib3.nick.Regain, ib3.connection.SSL, ib3.Bot):
    def on_privmsg(self, conn, event):
        self.do_command(conn, event, event.arguments[0])

    def on_pubmsg(self, conn, event):
        args = event.arguments[0].split(':', 1)
        if len(args) > 1:
            to = irc.strings.lower(args[0])
            if to == irc.strings.lower(conn.get_nickname()):
                self.do_command(conn, event, args[1].strip())
        
        toNick = event.target
        if toNick == conn.get_nickname():
            toNick = event.source.nick

        if 'windows' in args[0] or 'Windows' in args[0]:
            conn.privmsg(toNick, 'mesmo pagando é uma bosta')
        

    def do_command(self, conn, event, cmd):
        to = event.target
        if to == conn.get_nickname():
            to = event.source.nick

        if cmd == 'disconnect':
            self.disconnect()
        elif cmd == 'die':
            self.die()
        elif cmd == '!help':
            conn.privmsg(to, 'Ainda não tenho um help ou ajuda para mostrar')
        elif cmd == '!fortune':
            txt = os.popen('fortune fortune-br').read()
            for txt in txt.split('\n'):
                conn.privmsg(to, txt)
        else:
            conn.privmsg(to, 'What does "{}" mean?'.format(cmd))

if __name__ == '__main__':
    bot = Bagre(
        server_list=[('chat.freenode.net', 6697)],
        nickname=nick,
        realname=nick,
        ident_password=passwd,
        channels=[channel],
    )
    try:
        bot.start()
    except KeyboardInterrupt:
        bot.disconnect('KeyboardInterrupt!')
    except Exception:
        logger.exception('Killed by unhandled exception')
        bot.disconnect('Exception!')
        raise SystemExit()