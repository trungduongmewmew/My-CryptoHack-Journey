# Challenge: Extended GCD 

- **Category**: Modular Arithmetic
- **Points**: 20  

## 📖 Problem Description  
 Let a and b be positive integers.  
 The extended Euclidean algorithm is an efficient way to find integers u,v such that au+bv=gcd(a,b).  
 Later, when we learn to decrypt RSA ciphertexts, we will need this algorithm to calculate the modular inverse of the public exponent.  
 Using the two primes p=26513, q= 32321, find the integers u,v such that p.u+q.v=gcd(p,q).  
 Enter whichever of u and v is the lower number as the flag. 
 *Hint : Knowing that p,q are prime, what would you expect gcd(p,q) to be?*
## 🤔 Thought Process  
  Because p,q are prime so gcd(p,q)=1 ==>  so that p.u+q.v=1 can be rewritten as p.u $\equiv$ 1 (mod q). 
  This means that u is the modular inverse of p modulo q. In Python (version 3.8 and above), you can calculate it directly using the pow() function.  
  
## 🐍 Solution 
```python
from math import gcd
p = 26513
q = 32321
u = pow(p, -1, q)
v =(1 - p * u) // q
print(f"u: {u}, v: {v}")
```  
#### 🎯 Flag from the Challenge  
    -8404  
    
---

##### 🧠 Key Takeaways 
1. **The Purpose of the EEA**  
- The Extended Euclidean Algorithm (EEA) is a fundamental algorithm in cryptography. Its main purpose is to find the integers u and v that satisfy the equation a*u + b*v = gcd(a, b).
2. **The Link to Modular Inverses**  
- This challenge's most critical lesson is the link between the EEA and Modular Inverses. When gcd(a, b) = 1 (as it is with two primes), the equation becomes a*u + b*v = 1.
- This can be rewritten as a*u ≡ 1 (mod b), which means u is the modular inverse of a modulo b.
3. **Python's pow() Function**  
- While the EEA can be implemented manually, Python 3.8+ provides a powerful and fast built-in function: pow(base, -1, modulus).
- This function directly calculates the modular inverse, effectively serving as a modern replacement for manually coding the EEA in CTFs. This is the exact tool used to find the RSA private key.

