# https://projecteuler.net/problem=22

def get_score(word: str):
    word = word.upper()
    su = 0
    for i in word:
        su += ord(i)-64
    return su


data = ""

with open("20-29/22/names.txt") as file:
    data = file.readline()

data = sorted(data.replace('"', "").split(","))

su = 0
for i, y in enumerate(data):
    su += get_score(y)*(i+1)
print(su)
