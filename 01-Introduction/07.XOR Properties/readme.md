# Challenge: XOR Properties 

- **Category**: Introduction / Encoding
- **Points**: 15  

## 📖 Problem Description 

In the last challenge, you saw how XOR worked at the level of bits. In this one, we're going to cover the properties of the XOR operation and then use them to undo a chain of operations that have encrypted a flag. Gaining an intuition for how this works will help greatly when you come to attacking real cryptosystems later, especially in the block ciphers category.  

There are four main properties we should consider when we solve challenges using the XOR operator  
```
Commutative: A ⊕ B = B ⊕ A
Associative: A ⊕ (B ⊕ C) = (A ⊕ B) ⊕ C
Identity: A ⊕ 0 = A
Self-Inverse: A ⊕ A = 0
```  

Let's break this down. Commutative means that the order of the XOR operations is not important. Associative means that a chain of operations can be carried out without order (we do not need to worry about brackets). The identity is 0, so XOR with 0 "does nothing", and lastly something XOR'd with itself returns zero.  

Let's put this into practice! Below is a series of outputs where three random keys have been XOR'd together and with the flag. Use the above properties to undo the encryption in the final line to obtain the flag.  

```
KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf
```  
*Hint :  Before you XOR these objects, be sure to decode from hex to bytes.  


## 🤔 Thought Process  

We can use the properties of XOR to undo the encryption.  
1. KEY2 ^ KEY1 = A => KEY2 = A ^ KEY1
2. KEY2 ^ KEY3 = B => KEY2 = B ^ KEY3
3. FLAG ^ KEY1 ^ KEY3 ^ KEY2 = C =>FLAG = C ^ KEY1 ^ (KEY2 ^ KEY3)

  
## 🐍 Solution   

```python
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

```
#### 🎯 Flag from the Challenge  

    `crypto{x0r_i5_ass0c1at1v3}`  
    
---

##### 🧠 Key Takeaways  

1. **XOR is its Own Inverse (Self-Inverse)**

- This challenge's core lesson is the Self-Inverse property: A ^ A = 0. This is what makes XOR useful for encryption, as it allows us to "cancel out" or "remove" a key. By XORing the final ciphertext with the same keys, we reverse the encryption.

2. **XOR is Associative and Commutative**

- The Associative property (A ^ (B ^ C) = (A ^ B) ^ C) means the order of operations in a long chain doesn't matter. This allowed us to re-group the keys (FLAG ^ (KEY1 ^ KEY2 ^ KEY3)) and find a simple path to the solution, as hinted by the flag itself.

3. **XORData Must Be in Bytes (or Integers)**

- A crucial practical step, emphasized by the hint, is that bitwise operations like XOR cannot be performed on hex strings. You must always decode your hex strings into bytes (using bytes.fromhex()) or convert them to integers (int(hex_string, 16)) before applying mathematical operators.


