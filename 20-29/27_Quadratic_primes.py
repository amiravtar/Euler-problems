# https://projecteuler.net/problem=27

from math import sqrt,floor

prims = set((),)



def is_prime(num):
    num=abs(num)
    if num % 2 == 0:
        return num == 2
    if num % 3 == 0:
        return num == 3
    h = int(sqrt(num)+1)
    i = 2
    while(i <= h):
        if num % i == 0:
            return False
        i+=1
    return True


def get_max_primes(a, b):
    if not is_prime(b):
        return 0
    n = 0
    while(is_prime((n*n)+(n*a)+b)):
        n += 1
    return n


ma = 1
valu = (1, 1)
for i in range(-999, 999,2):
    for j in range(-999, 999):
        t = get_max_primes(i, j)
        if t > ma:
            ma = t
            valu = (i, j)
print(ma,valu,valu[0]*valu[1])
