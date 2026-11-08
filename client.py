import socket
import struct
from des import encrypt

key = "133457799BBCDFF1"

message = "Transaction ID: 1001, Amount: 5000 EGP"

encrypted = encrypt(message, key)

print("Original transaction:")
print(message)

print("\nEncrypted transaction:")
print(encrypted)

data = bytes.fromhex(encrypted)

client = socket.socket()

client.connect(("127.0.0.1", 5000))

client.sendall(struct.pack("!I", len(data)))

client.sendall(data)

print("\nTransaction sent successfully!")

client.close()
