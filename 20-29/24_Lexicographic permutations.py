# https://projecteuler.net/problem=24


from itertools import permutations

param = []
for i in range(0, 10):
    param.append(i)
perm = permutations(param)
lis = []
for i in list(perm):
    lis.append(i)
lis = sorted(lis)
print(''.join(map(str, [x for x in lis[1000000]])))
