def array_front9(nums):
  size = len(nums)
  if size > 4:
    size = 4
    
  for i in range(size):
    if(nums[i] == 9):
      return True
  return False