#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import re
import threading
import sys
import timeit
import time
import datetime
import collections
import enum

'''
Create an INET, STREAMing socket
'''
def open_server_socket(port=4444):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2.0)
    hostname = "0.0.0.0"  #socket.gethostname()
    while True:
        try:
            s.bind((hostname, port))
            break
        except:
            print("Failed to bind {0}:{1}".format(hostname, port))
            time.sleep(2.0)
    print("Bound {0}:{1}".format(hostname, port))
    return s

class ParsingResult(enum.Enum):
    Ok = 0
    Prompt = 1
    Failed = 2

'''
I am getting something like 
[3G*1452592884*005F*UD2,130418,145006,V,32.180737,N,34.8552780,65,55,5]
'''
def get_coordinates(data):
    pattern_prompt = "\[3G.([0-9]+)*.+,0,0,[0-9]+\]"
    pattern_coordinates = "\[3G.([0-9]+).+,([0-9.]+),N,([0-9.]+),.+\]"
    m_coordinates = re.match(pattern_coordinates, data)

    result = ParsingResult.Failed
    id, c1, c2 = None, None, None
    if m_coordinates:
        id = m_coordinates.group(1)
        c1 = m_coordinates.group(2)
        c2 = m_coordinates.group(3)
        result = ParsingResult.Ok
    else:
        m_prompt = re.match(pattern_prompt, data)
        if m_prompt:
            result = ParsingResult.Prompt

    return result, id, c1, c2
    
def get_coordinates_url(c1, c2):
    return "http://maps.google.com/maps?q=n{0},e{1}".format(c1, c2)

def close_socket(clientsocket, address):
    try:
        clientsocket.shutdown()
    except:
        pass
    try:
        clientsocket.close()
    except:
        pass

class Stopwatch():
    def __init__(self):
        self.start = timeit.default_timer()
        self.thread_aborted = False

    def elapsed(self):
        return timeit.default_timer()-self.start
    def elapsed_str(self):
        return "{0:.3f}".format(self.elapsed())
    
def client_thread(clientsocket, address, stopwatch):
    while True:
        try:
            data = clientsocket.recv(2048)
        except:
            if stopwatch.thread_aborted:
                print("{0}: Aborting thread {1}".format(stopwatch.elapsed_str(), address))
                break
            # probably timeout 
            continue
        timestamp = datetime.datetime.now()
        #clientsocket.send("[OK]\n")
        result, id, c1, c2 = get_coordinates(data)
        if result == ParsingResult.Ok:
            url = get_coordinates_url(c1, c2)
            print("{0}: {1} {2} {3} from {4}".format(stopwatch.elapsed_str(), str(timestamp), id, url, address))
            break
        elif result == ParsingResult.Failed:
            print("{0}: Failed to parse '{1}' from {2}".format(stopwatch.elapsed_str(), data, address))
        if data == "":
            break

    print("{0}: close {1}".format(stopwatch.elapsed_str(), address))
    close_socket(clientsocket, address)
    #sys.exit()
    
clients = {}

def accept_loop():
    while True:
        try:
            (clientsocket, address) = server_socket.accept()
        except socket.timeout:
            time.sleep(0.1)
            continue
        
        stopwatch = Stopwatch()
        print("Accepted connection from {0}".format(address))
        ct = threading.Thread(target=client_thread, args=(clientsocket, address, stopwatch))
        
        ct.run()
        clients[(clientsocket, address)] = (ct, stopwatch)

port = 4444
server_socket = open_server_socket(port)
print("Listen on port {0}".format(port))
server_socket.listen(5)
try:
    accept_loop()
except KeyboardInterrupt:
    print("I got Ctrl-C, exiting")
    for (clientsocket, address), (ct, stopwatch) in clients.iteritems():
        stopwatch.thread_aborted = True
    for (clientsocket, _), (ct, _) in clients.iteritems():
        if ct.isAlive():
            ct.join()
    for (clientsocket, address) in clients():
        close_socket(clientsocket, address)
