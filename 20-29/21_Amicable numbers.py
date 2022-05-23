# https://projecteuler.net/problem=21

import math


def get_divisors(num):
    lis = []
    for i in range(1, int(num/2)+1):
        if num % i == 0:
            lis.append(i)
    return lis


def is_amicable(num):
    b=sum(get_divisors(num))
    if sum(get_divisors(b))==num and num != b:
        return True
    else:
        return False

lis=[]
for i in range(1,10001):
    if is_amicable(i):
        lis.append(i)

print(sum(lis))

