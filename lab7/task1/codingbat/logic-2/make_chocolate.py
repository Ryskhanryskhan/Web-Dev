def make_chocolate(small, big, goal):
 if (big >= goal / 5 and small >= goal % 5):
  return goal % 5
 if (big <= goal / 5 and small >= goal - big * 5):
  return goal - big * 5
 return -1