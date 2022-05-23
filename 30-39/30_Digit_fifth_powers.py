#https://projecteuler.net/problem=30
num=2
lis=[]
while num<200000:
    su=0
    dig=[int (x) for x in str(num)]
    for i in dig:
        su+=i**5
    if su == num:
        lis.append(su)
        print(num,su)
    num+=1
print(sum(lis))