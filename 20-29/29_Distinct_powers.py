#https://projecteuler.net/problem=29

powers=set((),)

for i in range(2,101):
    for j in range(2,101):
        powers.add(i**j)
lis=sorted(list(powers))
print(lis)
print(len(lis))