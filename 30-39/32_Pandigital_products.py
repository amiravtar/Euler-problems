# https://projecteuler.net/problem=32

def check_pandigit(a, b, c):
    a, b, c = (str(a), str(b), str(c))
    if len(a)+len(b)+len(c) != 9:
        return False
    d = a+b+c
    for i in range(1, 10):
        if str(i) not in d:
            return False
        if d.count(str(i)) > 1:
            return False
    return True


loop = ((1, 1000), (10, 100))
pans = set()
for i in loop:
    for a in range(i[0], i[0]*10):
        for b in range(i[1], i[1]*10):
            c = a*b
            if len(str(a))+len(str(b))+len(str(c)) > 9:
                break
            if check_pandigit(a, b, c):
                pans.add(c)
print(sum(pans))
