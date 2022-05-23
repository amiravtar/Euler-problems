# https://projecteuler.net/problem=20

from ipaddress import ip_address


fac = 1
for i in range(1, 101):
    fac *= i
s = 0
for i in str(fac):
    s += int(i)
print(s)
