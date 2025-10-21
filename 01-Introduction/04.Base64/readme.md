# Challenge: Base64  

- **Category**: Introduction / Encoding
- **Points**: 10  

## 📖 Problem Description  

Another common encoding scheme is Base64, which allows us to represent binary data as an ASCII string using an alphabet of 64 characters. One character of a Base64 string encodes 6 binary digits (bits), and so 4 characters of Base64 encode three 8-bit bytes.

Base64 is most commonly used online, so binary data such as images can be easily included into HTML or CSS files.

Take the below hex string, decode it into bytes and then encode it into Base64.

`72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf`

 In Python, after importing the base64 module with import base64, you can use the  `base64.b64encode()` function. Remember to decode the hex first as the challenge description states.  

 ## 🤔 Thought Process  
 The challenge gives us a hex string and asks us to decode it into bytes and then encode it into Base64.  
 The logic is as follows:  
 1.  Take the hex string provided by the challenge.  
 2.  Convert the hex string into bytes using `bytes.fromhex()`.  
 3.  Encode the bytes into Base64 using `base64.b64encode()`.  

 ## 🐍 Solution  
 We can write a very simple Python script to solve this. Convert the hex string into bytes using `bytes.fromhex()` and then encode it into Base64 using `base64.b64encode()`.
 
 ### Python Script  
 ```python  
 import base64  
 Hex_value="72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
 flag = base64.b64encode(bytes.fromhex(Hex_value)).decode()  
 print(flag)
 ```  
 #### 🎯 Flag from the Challenge  
 `crypto/Base+64+Encoding+is+Web+Safe/`  
 
 ---
 
 ##### 🧠 Key Takeaways
 1. **Base64 for Data Portability**  
 - The primary use of Base64 is to encode binary data (like images or ciphertext) into a safe, printable ASCII text format, making it suitable for text-based protocols and formats like HTML or JSON.
 2. **Python's 'base64' Module**  
 - Python's standard `base64` library is the essential tool for this encoding.
 - `base64.b64encode(bytes_object)`: Encodes a `bytes` object into its Base64 representation.
 - `base64.b64decode(base64_string)`: Decodes a Base64 string or bytes back into the original `bytes` object.  
 3. **Identifying Base64 Strings**  
 - A key recognition skill is to look for a string composed of uppercase letters `(A-Z)`, lowercase letters `(a-z)`, numbers `(0-9)`, and potentially `+` and `/`. The string might also end with `= or ==` which are used for padding.