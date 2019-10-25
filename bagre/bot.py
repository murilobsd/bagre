#
# Copyright (c) 2019 Murilo Ijanc' <mbsd@m0x.ru>
# Copyright (c) 2019 Guilherme <ggrigon@users.noreply.github.com>
# Copyright (c) 2019 Renato dos Santos <shazaum@gmail.com>
# 
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
# 
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
import ib3
import ib3.auth
import ib3.connection
import ib3.nick
import irc.strings

class Bot(ib3.auth.SASL, ib3.nick.Regain, ib3.connection.SSL, ib3.Bot):
	"""Bot Class"""

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

