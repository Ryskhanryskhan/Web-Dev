n = int(input())
a = list(map(int, input().split()))

check = False
for i in range(1, n):
    if(a[i] > 0 and a[i-1] >0) or (a[i]<0 and a[i-1]<0):
        check = True
    
    
if check:
    print("YES")
else:
    print("NO")