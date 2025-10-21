# Challenge: Hex

- **Category**: Introduction / Encoding
- **Points**: 5  

## 📖 Problem Description  

When we encrypt something the resulting ciphertext commonly has bytes which are not printable ASCII characters. If we want to share our encrypted data, it's common to encode it into something more user-friendly and portable across different systems.  

Hexadecimal can be used in such a way to represent ASCII strings. First each letter is converted to an ordinal number according to the ASCII table (as in the previous challenge). Then the decimal numbers are converted to base-16 numbers, otherwise known as hexadecimal. The numbers can be combined together, into one long hex string.  

Included below is a flag encoded as a hex string. Decode this back into bytes to get the flag.  
`63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d`

*Hint: In Python, the `bytes.fromhex()` function can be used to convert hex to bytes. The `.hex()` instance method can be called on byte strings to get the hex representation.  

## 🤔 Thought Process  

The challenge give us flag encoded as a hex string and asks us to decode it back into bytes to get the flag.  
The logic is as follows:  
1.  Take the hex string provided by the challenge.  
2.  The hint helpfully points to the `bytes.fromhex()` function in Python, which is designed for exactly this purpose.  
3.  Convert the hex string into bytes using `bytes.fromhex()`. And then, get the flag.  

## 🐍 Solution 
 We can write a very simple Python script to solve this. Convert the hex string into bytes using `bytes.fromhex()`  

### Python Script  
```python  
Hex_value="63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"  
flag = bytes.fromhex(Hex_value).decode()  
print(flag)  
```  

#### 🎯 Flag from the Challenge  
 `crypto{You_will_be_working_with_hex_strings_a_lot}`
  
---

##### 🧠 Key Takeaways 
 1. **Hexadecimal Representation**  
 - Hexadecimal is a crucial method for representing binary data (e.g., ciphertext) in a human-readable text format. Each byte is represented by exactly two hex characters (from 00 to ff).
 2. **Python's Hex Conversion**  
 - Python provides easy-to-use, built-in tools for hex conversion.  
 - `bytes.fromhex('hex_string')`: Converts a hex string into a bytes object.  
 - `.hex()`: Converts a bytes object into a hex string.  
3. **A Foundational CTF Skill**  
- Recognizing and decoding hex is a fundamental skill in CTFs, as you will constantly encounter it when analyzing files, network data, and encrypted outputs.

