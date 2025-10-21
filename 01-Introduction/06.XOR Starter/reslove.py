value="label"
xor_value=13
result = ''.join(chr(ord(c) ^ xor_value) for c in value)
print(result)