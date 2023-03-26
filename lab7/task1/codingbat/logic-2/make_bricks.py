def make_bricks(small, big, goal):
  if (big >= goal / 5 and small >= goal % 5):
     return True
  if (goal - big * 5 <= small and goal - big * 5 > 0):
     return True
  else:
     return False