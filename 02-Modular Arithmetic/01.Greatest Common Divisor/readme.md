# Challenge: Greatest Common Divisor 

- **Category**: Modular Arithmetic
- **Points**: 15  

## 📖 Problem Description  
The Greatest Common Divisor (GCD), sometimes known as the highest common factor, is the largest number which divides two positive integers (a,b).

For a=12,b=8 we can calculate the divisors of a: {1,2,3,4,6,12} and the divisors of b: {1,2,4,8}. Comparing these two, we see that gcd⁡(a,b)=4.

Now imagine we take a=11,b=17. Both a and b are prime numbers. As a prime number has only itself and 11 as divisors, gcd⁡(a,b)=1.

We say that for any two integers a,b if gcd⁡(a,b)=1 then a and b are coprime integers.

If a and b are prime, they are also coprime. If a is prime and b < a then a and b are coprime.

Think about the case for a prime and b>a, why are these not necessarily coprime?

There are many tools to calculate the GCD of two integers, but for this task we recommend looking up [Euclid's Algorithm](https://en.wikipedia.org/wiki/Euclidean_algorithm).

Try coding it up; it's only a couple of lines. Use a=12,b=8 to test it.

Now calculate gcd⁡(a,b) for a=66528,b=52920 and enter it below.
## 🤔 Thought Process  
    The challenge give us number a and b . we can use function `math.gcd` in python to calculate gcd⁡(a,b).  
    
## 🐍 Solution  
```python  
import math
a= 6528
b= 52920
gcd = math.gcd(a, b)
print(f"The GCD of {a} and {b} is {gcd}") 
``` 
#### 🎯 Flag from the Challenge
    24 
    
---

##### 🧠 Key Takeaways

1. **GCD and "Coprime"**  
- The Greatest Common Divisor (GCD) is a foundational concept in modular arithmetic. It is the largest number that divides both integers a and b.
- A critical related concept is "coprime", which occurs when gcd(a, b) = 1. This is essential for understanding modular inverses and the RSA algorithm later on.
2. **Euclid's Algorithm**  
- This challenge introduces Euclid's Algorithm as the classic and highly efficient method for finding the GCD without needing to factor the two numbers.
- Understanding how this algorithm works (based on remainders) is crucial for learning the Extended Euclidean Algorithm later. 
3. **Python's math.gcd() Function**  
- In practical CTF scenarios, Python's built-in `math.gcd(a, b)` function is the fastest and most reliable way to get the result without needing to re-implement the algorithm.