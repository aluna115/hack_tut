print("Adios, World!")

import math

def median(input):
  n = len(input)
  if n % 2 == 1:
    mid = input[math.floor(n/2)]
  else:
    mid_num = [n/2, n/2 - 1]
    mid = mean(mid_num)
  return mid



