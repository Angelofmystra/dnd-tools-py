import random

def d6(sides, faces):
	n = 0
	for i in range(sides):
		n += random.randint(1, faces)
	return n

def room():
	n = d6(1,6)
	m = d6(1,6)
	if n==1 or n == 2:
		print ("monster in room")
		if m == 1 or m == 2 or m == 3:
			print ("treasure present")
	else:
		print ("empty")	
		if m == 1:
			print ("treasure present")

room()