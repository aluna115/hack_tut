print("Adios, World!")

import math

def mean(input):
  sum = 0
  for entry in input:
    sum += entry
  return sum / len(input)

my_list = [0, 1, 2, 3, 4, 5]
print(mean(my_list))

def median(input):
  n = len(input)
  if n % 2 == 1:
    mid = input[math.floor(n/2)]
  else:
    mid_num = [n/2, n/2 - 1]
    mid = mean(mid_num)
  return mid




