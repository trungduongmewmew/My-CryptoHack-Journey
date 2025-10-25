# Challenge: Favourite byte 

- **Category**: Introduction / Encoding
- **Points**: 20  

## 📖 Problem Description  

For the next few challenges, you'll use what you've just learned to solve some more XOR puzzles.

I've hidden some data using XOR with a single byte, but that byte is a secret. Don't forget to decode from hex first.  

`73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d`

## 🤔 Thought Process   

The challenge give us a result of xoring data with a single byte. However, this byte is not mentioned so we need to try all 256 bytes to find a meaningfyl flag. 

## 🐍 Solution 
```python
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
```  

#### 🎯 Flag from the Challenge   
    `crypto{0x10_15_my_f4v0ur173_by7e}`  
    
---

##### 🧠 Key Takeaways

1. **First, decode the hex**
- If the input is a hex string, call bytes.fromhex() first, then apply XOR  

2. **“Single byte” = a value 0..255**
- One byte has 8 bits → \(2^8 = 256\) possible values (`0x00`–`0xFF`)
- If you don’t know the key, brute-force all keys from `0` to `255`

3. **XOR is its own inverse**  
- If `cipher = plaintext XOR key` then `plaintext = cipher XOR key`. You can recover the plaintext by XOR-ing the cipher with the same single byte key  

4. **Simple and safe brute-force**  
- A loop like `for key in range(256)` is enough to try every possibility.

5. **Filter results by printable characters or patterns**  
- Prioritize outputs with a high ratio of printable characters. Look for flag indicators like `flag{`, `crypto{`, or `CTF{` to quickly identify the correct result.