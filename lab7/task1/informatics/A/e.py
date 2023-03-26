
s = 109
v = int(input())
t = int(input())

res = 0
if(v > 0): res = (v * t)
else:  
    res = (-v * t) % 109
    res = 109 - res

print(res % 109) 