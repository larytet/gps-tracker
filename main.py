#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import re
import threading
import sys

'''
Create an INET, STREAMing socket
'''
def open_server_socket(port=4444):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    hostname = "0.0.0.0"  #socket.gethostname()
    s.bind((hostname, port))
    print("Bound {0}:{1}".format(hostname, port))
    return s

'''
I am getting something like 
3G*1452592884*005F*UD2,130418,145006,V,32.180737,N,34.8552780
'''
def get_coordinates(data):
    m = re.match("\[3G.+,([0-9.]+),N,([0-9.]+),.+\]", data)

    result = (m != None)
    id, c1, c2 = None, None, None
    if result:
        id = m.group(1)
        c1 = m.group(2)
        c2 = m.group(4)
    else:
        print("Failed to parse '{}'".format(data))
    return result, id, c1, c2
    
def client_thread(clientsocket, address):
    while True:
        data = clientsocket.recv(2048)
        if data == "":
            print("Close {0}".format(address))
            clientsocket.shutdown()
            clientsocket.close()
            break
        clientsocket.send("[OK]\n")
        result, id, c1, c2 = get_coordinates(data)
        if result:
            print(id, c1, c2)
    #sys.exit()
    
clients = {}

def accept_loop():
    while True:
        (clientsocket, address) = server_socket.accept()
        print("Accepted connection from {0}".format(address))
        ct = threading.Thread(target=client_thread, args=(clientsocket,address))
        ct.run()
        clients[(clientsocket, address)] = ct

port = 4444
server_socket = open_server_socket(port)
print("Listen on port {0}".format(port))
server_socket.listen(5)
try:
    accept_loop()
except KeyboardInterrupt:
    print("I got Ctrl-C, exiting")
    for (clientsocket, _), ct in clients.iteritems():
        try:
            clientsocket.shutdown()
            clientsocket.close()
        except:
            pass
        ct.exit()
    for (clientsocket, _), ct in clients.iteritems():
        ct.join()
