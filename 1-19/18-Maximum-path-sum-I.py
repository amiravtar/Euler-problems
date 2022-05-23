# https://projecteuler.net/problem=18

nums = []

row = list(map(int, list(input().split(' '))))
while(row[0] != ''):
    nums.append(row)
    row =input()
    if row=='':
        break
    else:
        row=list(map(int, list(row.split(' '))))


max_sum = 0
selected = 0

for i, y in enumerate(nums):
    if i > 0:
        if nums[i][selected] > nums[i][selected+1]:
            max_sum += nums[i][selected]
        else:
            max_sum += nums[i][selected+1]
            selected += 1
    else:
        max_sum += nums[0][0]
    print(i, selected, nums[i][selected], sep=",")
print(max_sum)
