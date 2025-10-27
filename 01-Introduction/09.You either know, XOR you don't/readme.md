# Challenge: Favourite byte 

- **Category**: Introduction / Encoding
- **Points**: 30  

## 📖 Problem Description  

I've encrypted the flag with my secret key, you'll never be able to guess it.  
*Hint: Remember the flag format and how it might help you in this challenge!*  
`0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104`

## 🤔 Thought Process  

Here is the step-by-step logic to solve the problem:

1.  Analyze the Problem The challenge provides only a hex string (the ciphertext). We are told this is the result of Plaintext ⊕ Key, but the key is unknown.

2.  Identify the Hint We have a crucial hint: the flag format is crypto{FLAG}.

3.  Perform a Known-Plaintext Attack

- Because we know the format, we know the first 7 bytes of the plaintext (the string "crypto{").

- Based on the properties of XOR (where Ciphertext ⊕ Plaintext = Key), we can XOR the first 7 bytes of the ciphertext with the 7 known bytes of the plaintext.

- This will reveal the first 7 bytes of the key.

4.  Deduce and Repeat the Key

- From this key fragment, we must deduce the full key based on context.

- If the full key is shorter than the ciphertext, we must repeat the key (e.g., keykeykey...) until its length is greater than or equal to the ciphertext's length.

5. Final Decryption

- Finally, we XOR the entire ciphertext with the full, repeated key.

- This will reverse the encryption and reveal the original plaintext (the flag).

## 🐍 Solution  

```python
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
print(full_plain_text))  
```  
#### 🎯 Flag from the Challenge  

     crypto{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}  
     
---

##### 🧠 Key Takeaways  
1. **The Known-Plaintext Attack (KPA)**
- This challenge is a classic example of a Known-Plaintext Attack. If you know (or can guess) a part of the plaintext, you can recover the corresponding part of the key using the XOR property: Key = Plaintext ⊕ Ciphertext.
2. **Exploiting Predictable Formats**
- In CTFs, predictable data like flag formats (crypto{...}, flag{...}) is a common vulnerability. This known prefix provides the exact plaintext needed to launch a KPA and recover the beginning of the key.  
3. **Reconstructing Repeating Keys**
- When a cipher uses a repeating key (like a Vigenère cipher), recovering even a small portion of the key can be enough to deduce the full key, especially if it's a meaningful word or phrase. Once the full key is known, you can generate the full keystream to decrypt the entire message