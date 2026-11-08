
from des import des

key = "133457799BBCDFF1"

plaintext = "pay 1000pay 1000"

plaintext_bytes = plaintext.encode()

block1 = plaintext_bytes[:8]
block2 = plaintext_bytes[8:]

print("Plaintext:", plaintext)
print()

print("Block 1:", block1.decode())
print("Block 2:", block2.decode())
print()

block1_hex = block1.hex()
block2_hex = block2.hex()

ciphertext1 = des(block1_hex, key)
ciphertext2 = des(block2_hex, key)

print("Ciphertext Block 1:", ciphertext1)
print("Ciphertext Block 2:", ciphertext2)
print()

ciphertext = ciphertext1 + ciphertext2

print("Complete Ciphertext:", ciphertext)
print()

if ciphertext1 == ciphertext2:
    print("ECB RESULT: Both ciphertext blocks are identical!")
else:
    print("Ciphertext blocks are different.")

