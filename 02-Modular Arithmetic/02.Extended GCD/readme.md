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


