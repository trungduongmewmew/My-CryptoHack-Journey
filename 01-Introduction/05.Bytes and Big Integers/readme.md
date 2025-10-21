# Challenge: Bytes and Big Integers  

- **Category**: Introduction / Encoding
- **Points**: 10  

## 📖 Problem Description  

Cryptosystems like RSA works on numbers, but messages are made up of characters. How should we convert our messages into numbers so that mathematical operations can be applied?

The most common way is to take the ordinal bytes of the message, convert them into hexadecimal, and concatenate. This can be interpreted as a base-16/hexadecimal number, and also represented in base-10/decimal.

To illustrate: 
```
message: HELLO  
ascii bytes: [72, 69, 76, 76, 79]  
hex bytes: [0x48, 0x45, 0x4c, 0x4c, 0x4f]  
base-16: 0x48454c4c4f  
base-10: 310400273487  
```  
*Hint:  Python's `PyCryptodome` library implements this with the methods `bytes_to_long()` and `long_to_bytes()`. You will first have to install PyCryptodome and import it with `from Crypto.Util.number import *`.  
Convert the following integer back into a message:  
`11515195063862318899931685488813747395775516287289682636499965282714637259206269`  

## 🤔 Thought Process  

The challenge gives us a integer and ask us to convert it back into a message.
The logic is as follows: 
1.  Take the integer provided by the challenge.  
2.  Convert the integer into bytes using `long_to_bytes`.  

## 🐍 Solution  

We can write a very simple Python script to solve this. Convert the integer into bytes using `long_to_bytes` and then decode it into a message.

### Python Script  
```python  
from Crypto.Util.number import *
integer =11515195063862318899931685488813747395775516287289682636499965282714637259206269
flag = long_to_bytes(integer).decode()
print(flag)
```  
#### 🎯 Flag from the Challenge  
`crypto{3nc0d1n6_4ll_7h3_w4y_d0wn}`  

---

##### 🧠 Key Takeaways 
1. **Text as Numbers: The Basis of Modern Crypto**  
- Public-key cryptosystems like RSA operate on large numbers, not text. This challenge shows the standard method of converting an entire message into a single, massive integer so that mathematical operations can be performed on it.  
2. **The 'PyCryptodome' Library**  
- While the conversion can be done manually, the `PyCryptodome` library provides a standard and reliable way to handle it in Python.  
- `bytes_to_long(bytes_object)`: Converts a byte string into a large integer.  
- `long_to_bytes(integer)`: Converts a large integer into a byte string.  
3. **A Reversible Transformation**  
- This process is a form of encoding, not encryption. It's crucial that the conversion is perfectly reversible, allowing anyone to transform the number back into the original message without any data loss.