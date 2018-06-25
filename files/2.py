#!/usr/bin/python

import socket

def valid_ip(address):
    try: 
        socket.inet_aton(address)
        return True
    except:
        return False

if __name__=="__main__":
    txt = raw_input("Text > ")
    txt = txt.split()
    ips = []
    for word in txt:
        if valid_ip(word):
            ips.append(word)
    
    for ip in ips:
        print ip
        

