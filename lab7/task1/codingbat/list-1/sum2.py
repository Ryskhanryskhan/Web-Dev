def sum2(arr):
    sum = 0
    if len(arr) == 0:
        sum = 0
    elif len(arr) < 2:
        sum = arr[0]
    else:
        for i in range(2):
            sum += arr[i]
            
    return sum