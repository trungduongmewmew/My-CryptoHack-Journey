flag_xor_key=bytes.fromhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')
# falg ^key=data => flag=data^key
for key in range(256):
    flag=[]
    for b in flag_xor_key:
        flag.append(b^key)
    flag_bytes=bytes(flag)
    if b'crypto' in flag_bytes:
        print(flag_bytes)
        break