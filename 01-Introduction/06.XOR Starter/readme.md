# Challenge: XOR Starter 

- **Category**: Introduction / Encoding
- **Points**: 10  

## 📖 Problem Description   

XOR is a bitwise operator which returns 0 if the bits are the same, and 1 otherwise. In textbooks the XOR operator is denoted by `⊕`, but in most challenges and programming languages you will see the caret `^` used instead.  
| A | B | Output |  
|:-:|:-:|:------:|  
| 0 | 0 | 0 |  
| 0 | 1 | 1 |  
| 1 | 0 | 1 |  
| 1 | 1 | 0 |  
  

For longer binary numbers we XOR bit by bit: `0110 ^ 1010 = 1100`. We can XOR integers by first converting the integer from decimal to binary. We can XOR strings by first converting each character to the integer representing the Unicode character.  
Given the string `label`, XOR each character with the integer `13`. Convert these integers back to a string and submit the flag as `crypto{new_string}`.

 *Hint: The Python `pwntools` library has a convenient `xor()` function that can XOR together data of different types and lengths. But first, you may want to implement your own function to solve this.

## 🤔 Thought Process  

We have the string `label` and the integer `13`, we need to xor each character of the string with the integer `13`.  
The logic is as follows: 
1.  Convert each character of the string to the integer representing the Unicode character
2.  And then xor with `13`
3.  Convert back to string

## 🐍 Solution  

We can write a very simple Python script to solve this.  Using `ord()` convert to ascii and `chr()` convert to string.

### Python Script

```python
value="label"
xor_value=13
result = ''.join(chr(ord(c) ^ xor_value) for c in value)
print(result)  
```

#### 🎯 Flag from the Challenge  

    `crypto{aloha}`  
    
---

##### 🧠 Key Takeaways  

1. **The XOR Operation (^)**  
- This challenge introduces the fundamental XOR bitwise operation, represented by the ^ symbol in Python and other languages. It's a cornerstone of many cryptographic algorithms due to its speed and simplicity.
2. **XOR's Reversibility (Self-Inverse Property)**  
- A critical property of XOR is that it's its own inverse. This means if you XOR a result with the same key, you get the original data back.
- `(Plaintext ^ Key) ^ Key = Plaintext`
- This reversibility is the basis for many simple ciphers.
3. **Applying Math to Text**
- Bitwise operations work on numbers, not directly on characters. The standard pattern for this is to use `ord()` to convert a character to its integer value, perform the operation, and then use `chr()` to convert the resulting integer back to a character.
