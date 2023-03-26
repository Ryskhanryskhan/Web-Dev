n = int(input())
arr = list(map(int, input().split()))

s = set(arr)

s = sorted(s)

print(s[-2])