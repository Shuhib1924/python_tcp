import socket

# print(socket.gethostname())
# print(socket.gethostbyname(socket.gethostname()))

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((socket.gethostbyname(socket.gethostname()), 12345))
server_socket.listen()
print("server started")
while True:
    client_socket, client_address = server_socket.accept()
    print(type(client_socket))
    print(client_socket)
    print(type(client_address))
    print(client_address)
    print(f"Connected to {client_address}")
    # client_socket.close()
    client_socket.send("you are connected".encode("utf-8"))
