full_cipher_text = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
part_of_plain_text = "crypto{"
part_of_cipher_text =bytes.fromhex(full_cipher_text[:14])
part_of_plain_text_bytes = part_of_plain_text.encode()
key = bytes([a ^ b for a, b in zip(part_of_cipher_text, part_of_plain_text_bytes)])
print("Key:", key)
# output the key is myXORkey => maybe key full is myXORkey 
full_key="myXORkey"
full_key_bytes = full_key.encode()
full_cipher_text_bytes = bytes.fromhex(full_cipher_text)
# 1. Create a repeating key LONG ENOUGH to exceed the ciphertext length: (full_key_bytes * (len... + 1))
# 2. SLICE the long key to match the EXACT ciphertext length: [...][:len(full_cipher_text_bytes)]
# 3. XOR the ciphertext with the sliced key: bytes([a ^ b for a, b in zip(...)])
full_plain_text_bytes = bytes([a ^ b for a, b in zip(full_cipher_text_bytes, (full_key_bytes * (len(full_cipher_text_bytes) // len(full_key_bytes) + 1))[:len(full_cipher_text_bytes)])])
full_plain_text = full_plain_text_bytes.decode()
print(full_plain_text)