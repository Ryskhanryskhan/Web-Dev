def lucky_sum(a, b, c):
  sum = 0
  if (a != 13):
    sum += a
  if (a != 13 and b != 13):
    sum += b
  if (a != 13 and b != 13 and c != 13):
    sum += c
  return sum;
