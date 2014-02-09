import random

def d6(sides, faces):
 n = 0
 for i in range(sides):
  n += random.randint(1, faces)
 return n
print d6(1,6)