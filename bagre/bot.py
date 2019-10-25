"""
    O módulo bot é responsável pelas tarefas relacionadas ao bot,
    como por exemplo autenticar, conexão, envio de mensagens.
"""
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
from ib3 import auth, connection, nick, Bot as ib3bot
from irc import strings as istrings


class Bot(auth.SASL, nick.Regain, connection.SSL, ib3bot):
    """Bot Class"""

    def on_privmsg(self, conn, event):
        """mensagem privadas"""
        self.do_command(conn, event, event.arguments[0])

    def on_pubmsg(self, conn, event):
        """checa se alguem citou windows nas mensagens do canal"""
        args = event.arguments[0].split(':', 1)
        if len(args) > 1:
            to_user = istrings.lower(args[0])
            if to_user == istrings.lower(conn.get_nickname()):
                self.do_command(conn, event, args[1].strip())

        to_nick = event.target
        if to_nick == conn.get_nickname():
            to_nick = event.source.nick

        if 'windows' in args[0] or 'Windows' in args[0]:
            conn.privmsg(to_nick, 'mesmo pagando é uma bosta')

    def do_command(self, conn, event, cmd):
        """executa o comando"""
        target = event.target
        if target == conn.get_nickname():
            target = event.source.nick

        if cmd == 'disconnect':
            self.disconnect()
        elif cmd == 'die':
            self.die()
        elif cmd == '!help':
            conn.privmsg(
                target, 'Ainda não tenho um help ou ajuda para mostrar')
        elif cmd == '!fortune':
            conn.privmsg(to, 'reformulando...')
        else:
            conn.privmsg(target, 'What does "{}" mean?'.format(cmd))
