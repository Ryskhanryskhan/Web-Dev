def min(a,b,c,d):
    arr = [a, b, c, d]
    arr.sort()
    return arr[0]

ele = list(map(int, input().split()))
print(min(ele[0], ele[1], ele[2], ele[3]))