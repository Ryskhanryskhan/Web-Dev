def max_end3(arr):
  temp = 0 # temporary variable
  temp = arr[0]
  for i in range(int((len(arr)-1)/2)):  # iterate from 0
    if arr[i] <= arr[len(arr)-1-i]:
      temp = arr[len(arr)-1-i]
            
  for i in range(len(arr)):
    arr[i] = temp
        
  return arr