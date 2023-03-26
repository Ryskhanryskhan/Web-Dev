def power(a, n):
    if(n == 0):
        return 1
    elif(n == 1):
        return a
    else:
        return (a * power(a, n-1))

ele = list(map(int, input().split()))
print(power(ele[0], int(ele[1])))