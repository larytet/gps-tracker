#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import re

'''
Create an INET, STREAMing socket
'''
def open_server_socket(port=4444):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), port))
    return s

def get_coordinates(data):
    result = False
    
def client_thread(clientsocket):
    chunks = []
    bytes_received = 0
    data = clientsocket.recv(2048)
    clientsocket.send("#")
    result, id, coordinates = get_coordinates(data)
    print(id, coordinates)
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
