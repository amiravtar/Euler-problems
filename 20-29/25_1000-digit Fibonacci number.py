#https://projecteuler.net/problem=25

i=2
t1=1
t2=1

while True:
    a=t1+t2
    t1=t2
    t2=a
    i+=1
    if len(str(a))>=1000:
        print(i)
        break
