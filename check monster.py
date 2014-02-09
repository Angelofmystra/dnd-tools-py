import random

def d6(sides, faces):
 n = 0
 for i in range(sides):
  n += random.randint(1, faces)
 return n
x = d6(1,6)
print(x)

if x == 1 or x == 2:
 print("Monster in Room")

else:
 print("Empty")