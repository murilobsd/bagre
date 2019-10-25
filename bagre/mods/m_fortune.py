"""
    Módulo fortnune
"""
#
# Copyright (c) 2019 Murilo Ijanc' <mbsd@m0x.ru>
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
import os
import random
import re
import shutil
import urllib.request

from bagre import LOGGER

# Url do arquivo de db
URL = "https://m0x.ru/fortune-br"
# caminho onde sera salvo o db
DB_PATH = "/tmp/fortune-br"
# conteudo do db (cache)
DB_CONTENT = None 

def download_db(file_out):
    """download db"""
    try:
        with urllib.request.urlopen(URL) as response, open(file_out, 'wb') as out_file:
           shutil.copyfileobj(response, out_file)
    except Exception as e:
        LOGGER.exception(e)
        raise ValueError('Falha ao baixar o db fortune: %s' % str(e))

def init():
    """init checa se ja baixou o banco de dados."""
    # o db ja foi baixado?
    global DB_CONTENT
    if not os.path.exists(DB_PATH):
        download_db(DB_PATH)
    # Possui conteudo?
    if not DB_CONTENT:
        with open(DB_PATH, 'r') as f:
            DB_CONTENT = f.read()

def run():
    """roda o comando do modulo."""
    init()
    fortunes = re.split(r'%', DB_CONTENT)
    if len(fortunes) == 0:
        LOGGER.warning("não existem frases no db ou o formato não é suportado.")
        return "" 
    return random.choice(fortunes)

init()
