def no_teen_sum(a, b, c):
  sum = 0
  if (a < 13 or a > 19):
      sum += a
  if (b < 13 or b > 19):
      sum += b
  if (c < 13 or c > 19):
      sum += c
  return sum + fixTeen(a) + fixTeen(b) + fixTeen(c)
  
def fixTeen(n):
    if (n == 15 or n == 16):
      return n
    else:
      return 0