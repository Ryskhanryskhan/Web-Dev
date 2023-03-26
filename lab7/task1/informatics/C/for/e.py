x = int(input())

def getSum(x):
    sum = 0
    for digit in str(x):
        sum += int(digit)
    return sum

print(getSum(x))