a = int(input())
b = int(input())

if(a != 1 and b != 1):
    print("YES")
if((a == 1 and b != 1) or (a != 1 and b == 1)):
    print("NO")
if(a == 1 and b == 1):
    print("YES")