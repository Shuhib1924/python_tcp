import socket

DEST_IP = socket.gethostbyname(socket.gethostname())
DEST_PORT = 12345
ENCODER = "utf-8"
BYTESIZE = 1024

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((DEST_IP, DEST_PORT))
# client_socket.send("hello server".encode(ENCODER))

while True:
    message = client_socket.recv(BYTESIZE).decode(ENCODER)

    if message == "exit":
        client_socket.send("chat running down".encode(ENCODER))
        # client_socket.close()
        print("... disconnected")
        break
    else:
        print(message)
        message = input("message: ")
        client_socket.send(message.encode(ENCODER))

client_socket.close()
