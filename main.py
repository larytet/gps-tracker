#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

'''
Create an INET, STREAMing socket
'''
def open_server_socket(port=4444):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), port))
    return s

def client_thread(clientsocket):
    chunks = []
    bytes_received = 0
    chunk = clientsocket.recv(2048)
    print(chunk)
    clientsocket.close()
    
clients = {}

port = 4444
server_socket = open_server_socket(port)
print("Listen on port {0}".format(port))
server_socket.listen(5)
while True:
    (clientsocket, address) = server_socket.accept()
    print("Accepted connection from {0} {1}".format(clientsocket, address))
    ct = threading.Thread(target=client_thread, args=(clientsocket,))
    ct.run()
    clients[(clientsocket, address)] = ct
