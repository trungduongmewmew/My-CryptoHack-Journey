from math import gcd
p = 26513
q = 32321
u = pow(p, -1, q)
v =(1 - p * u) // q
print(f"u: {u}, v: {v}")