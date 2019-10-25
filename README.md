# bagre
Bot para o #openbsd-br na freenode.

## Instalando

Sugerimos caso seja para colaboração usar um ambiente virtual, por
exemplo:

```sh
git clone ...
cd ...
python3 -m venv venv
. ./venv/bin/activate
(venv) bagre $
```

```sh
git clone ...
cd ...
# talvez será necessário ter privilégios
python3 setup.py install
```

## Utilizando

O bot é bem simples, você pode passar por linha de comando ou pelas
variáveis de ambiente as informações necessárias.

### Comando help
```sh
bot --help
           [-c CHANNELS]

Bot do canal #openbsd-br

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  -v, --verbose         acrecente mais v para ficar mais verbose, -vvv.
  -s SERVER, --server SERVER
                        host do servidor, irc.freenode.org
  -p PORT, --port PORT  porta, 6667
  -n NICK, --nick NICK  nickname
  -P PASSWD, --passwd PASSWD
                        senha
  -c CHANNELS, --channels CHANNELS
                        lista de canais, #openbsd-br,#openbsd
```

### Rodando o bot

```
bot -s irc.freenode.org -p 6667 -n meubot -p minhasenha -c #openbsd-br,#openbsd
```

## Comandos
!help

## TODO
- [ ] !karma
- [ ] !version

## Desenvolvimento

Alguns comandos que ajudarão a manter o código usável. Existe o
**Makefile** para facilitar a vida, corriga os erros que forem
aparecendo.

```sh
make pep8
make lint
```
