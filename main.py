
'''
Create an INET, STREAMing socket
'''
def open_server_socket(port=4444):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), port))

def client_thread(clientsocket):
    chunks = []
    bytes_received = 0
    chunk = self.sock.recv(2048)
    print(chunk)
    
clients = {}

server_socket = open_server_socket()
server_socket.listen(5)
while True:
    (clientsocket, address) = serversocket.accept()
    ct = threading.Thread(target=client_thread, args=(clientsocket,))
    ct.run()
    clients[(clientsocket, address)] = ct
