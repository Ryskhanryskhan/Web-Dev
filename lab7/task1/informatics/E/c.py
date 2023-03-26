def xor(a, b):
    if(a == b):
        return False
    else:
        return True
    
ele = list(map(int, input().split()))

if(xor(ele[0], ele[1])):
    print(1)
else:
    print(0)