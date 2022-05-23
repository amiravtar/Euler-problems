# https://projecteuler.net/problem=26



lis = []


def get_cycle(remind, div):
    lis = {}
    left = []
    pos = 0
    while True:
        remind *= 10
        while remind < div:
            pos += 1
            remind *= 10
            left.append(0)
        t = int(remind/div)
        left.append(t)
        pos += 1
        remind = remind % div
        if remind in lis:
            return len(left[lis[remind]::])
        else:
            lis[remind]=pos
        if remind == 0:
            return 0


ma = 1
num = 1
for i in range(2, 1000):
    t = get_cycle(1, i)
    if t > ma:
        ma = t
        num = i
print(num, ma)
