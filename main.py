import socket

HOST_IP = socket.gethostbyname(socket.gethostname())
HOST_PORT = 12345
ENCODER = "utf-8"
BYTESIZE = 1024

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST_IP, HOST_PORT))
server_socket.listen()

print("server is running...")
client_socket, client_address = server_socket.accept()
client_socket.send("you are connected".encode(ENCODER))

while True:
    message = client_socket.recv(BYTESIZE).decode(ENCODER)

    if message == "exit":
        client_socket.send("quit".encode(ENCODER))
        # client_socket.close()
        print("... disconnected")
        break
    else:
        print(message)
        message = input("message: ")
        client_socket.send(message.encode(ENCODER))

client_socket.close()
