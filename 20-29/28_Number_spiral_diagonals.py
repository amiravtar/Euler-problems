# https://projecteuler.net/problem=28

def ring_cap(r):
    cap = 1
    for i in range(2, r+1):
        cap += (i-1)*8
    return cap


def ring_diffrence(r):
    if r == 1:
        return 0
    else:
        return (r-1)*2


ring = 0
su = 0
for i in range(1001,0,-2):
    ring+=1
print(ring)

for i in range(ring, 1, -1):
    dif=ring_diffrence(i)
    cap=ring_cap(i)

    su+=cap
    su+=cap-(dif*1)
    su+=cap-(dif*2)
    su+=cap-(dif*3)
su+=1
print(su)