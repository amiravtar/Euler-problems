# https://projecteuler.net/problem=23
#take a 1 or 2 for run

def is_abundant(num):
    lis = []
    for i in range(1, int(num/2)+1):
        if num % i == 0:
            lis.append(i)
    return sum(lis) > num


abundant_lis = []
# for i in range(12,28124):
#     if is_abundant(i):
#         abundant_lis.append(i)
# print(abundant_lis)

abundant_sums = set([])

for i in abundant_lis:
    for j in abundant_lis:
        if i+j <= 28123:
            abundant_sums.add(i+j)

lis_non_abundant = [x for x in range(1, 28124) if x not in abundant_sums]
print(sum(lis_non_abundant))
