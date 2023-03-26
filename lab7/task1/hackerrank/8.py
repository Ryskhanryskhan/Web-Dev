import math 

a = int(input())
b = int(input())

c = math.sqrt(a * a + b * b)

m = c / (2 * b)

print(round((m * 180)/3.14))