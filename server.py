import socket
import struct
from des import decrypt

key = "133457799BBCDFF1"

def receive_exactly(connection, size):

    data = b""

    while len(data) < size:

        part = connection.recv(size - len(data))

        if not part:
            raise ConnectionError("Connection closed")

        data += part

    return data


server = socket.socket()

server.bind(("127.0.0.1", 5000))

server.listen(1)

print("Server waiting for client...")

connection, address = server.accept()

print("Client connected!")

length_data = receive_exactly(connection, 4)

length = struct.unpack("!I", length_data)[0]

encrypted = receive_exactly(connection, length)

encrypted_hex = encrypted.hex()

message = decrypt(encrypted_hex, key)

print("\nDecrypted transaction:")
print(message)

connection.close()
server.close()
