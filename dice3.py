#! /usr/bin/env python3
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
		print("empty")
		if m == 1:
			print ("treasure present")

def rollHMStats():
	print ("Str: "+str(d6(3,6))+"/"+str(d6(1,100)))
	print ("Dex: "+str(d6(3,6))+"/"+str(d6(1,100)))
	print ("Con: "+str(d6(3,6))+"/"+str(d6(1,100)))
	print ("Int: "+str(d6(3,6))+"/"+str(d6(1,100)))
	print ("Wis: "+str(d6(3,6))+"/"+str(d6(1,100)))
	print ("Cha: "+str(d6(3,6))+"/"+str(d6(1,100)))
	print ("Com: "+str(d6(3,6))+"/"+str(d6(1,100)))

rollHMStats()