def close_far(a, b, c):
  if (abs(a - b) <= 1 and abs(c - b) >= 2 and abs(a - c) >= 2):
    return True
  if (abs(a - c) <= 1 and abs(b - a) >= 2 and abs(b - c) >= 2):
    return True
  return False