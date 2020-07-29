#!/usr/bin/env python3
import requests
import socket

def check_localhost():
        localhost = socket.gethostbyname('localhost')
        print(localhost)
        if localhost == '127.0.0.1':
                return True

def check_connectivity():
        request = requests.get("http://www.google.com")
        print(request)
        if request.status_code == 200:
                return True

check_localhost()
check_connectivity()
