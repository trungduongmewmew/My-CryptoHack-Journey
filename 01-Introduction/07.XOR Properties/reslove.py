def xor_bytes(a,b):
    """XOR two byte strings of equal length."""
    if len(a) != len(b):
        raise ValueError("Byte strings must be of equal length")
    return bytes(x ^ y for x, y in zip(a, b))

key1=bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
key1_xor_key2=bytes.fromhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")
key2_xor_key3=bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
falg_xor_key123=bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf") 
key2=xor_bytes(key1,key1_xor_key2)
key3=xor_bytes(key2,key2_xor_key3)
xor123=xor_bytes(key1,key2_xor_key3)
flag=xor_bytes(falg_xor_key123,xor123)
print(flag.decode())
  