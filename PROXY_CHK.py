#!/usr/bin/python
#coding: utf-8

# ( -- IMPORTS -- ) #
import requests
import os
import time
from threading import Thread

# ( -- LOGO / INFO -- ) #
bugs = '''
    ____  ____  ____   _____  ____   __  ____ _   _ _  __
   / __ \|  _ \|  _ \ / _ \ \/ /\ \ / / / ___| | | | |/ /
  / / _` | |_) | |_) | | | \  /  \ V / | |   | |_| | ' / 
 | | (_| |  __/|  _ <| |_| /  \   | |  | |___|  _  | . \ 
  \ \__,_|_|   |_| \_\\___/_/\_\  |_|___\____|_| |_|_|\_\
   \____/                          |_____|               
\n[$] BUGS PROXY CHECKER.
[$] URL = ("https://www.Brazzers.com/BUGS").
[$] SCRIPT PROGRAMMED BY BUGS WITH PYTHON2.
'''
# ---------------------------------- ## ---------------------------------- ## ---------------------------------- #

def main():
    def tryproxies(proxy):
        with open('VALID PROXIES.txt', 'a+') as validproxiesfile:
            try:
                rs = requests.head('https://www.google.com/', proxies={'https': proxy}, timeout=20)
                print(rs.status_code, '\n httpproxy', proxy, "Elapsed Time: %s" % (time.time() - start))
                if rs.status_code == 200:
                    validproxiesfile.write('http/https://' + proxy + '\n')
            except Exception as e:
                print(e, proxy, "Elapsed Time: %s" % (time.time() - start))
            try:
                rs = requests.head('https://www.google.com/', proxies={'https': 'socks5://' + proxy}, timeout=20)
                print(rs.status_code, '\n socks5proxy', proxy, "Elapsed Time: %s" % (time.time() - start))
                if rs.status_code == 200:
                    validproxiesfile.write('socks5://' + proxy + '\n')
            except Exception as e:
                print(e, proxy, "Elapsed Time: %s" % (time.time() - start))
            try:
                rs = requests.head('https://www.google.com/', proxies={'https': 'socks4://' + proxy}, timeout=20)
                print(rs.status_code, '\n socks4proxy', proxy, "Elapsed Time: %s" % (time.time() - start))
                if rs.status_code == 200:
                    validproxiesfile.write('socks4://' + proxy + '\n')
            except Exception as e:
                print(e, proxy, "Elapsed Time: %s" % (time.time() - start))

    start = time.time()
    threadlist = []

    try:
        os.remove('workingproxies.txt')
    except Exception:
        pass

    with open(raw_input('[$] ENTER YOUR PROXIES PATH: '), 'r') as file:
        for proxy in file:
            proxy = proxy.strip()
            t = Thread(target=tryproxies, args=(proxy,))
            t.start()
            threadlist.append(t)

# ---------------------------------- ## ---------------------------------- ## ---------------------------------- #

if __name__ == '__main__':
    main()