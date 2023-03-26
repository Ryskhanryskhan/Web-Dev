import math

n = int(input())
k = int(input())

c = math.floor(k/n)

print(k - c * n)
