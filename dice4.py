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
		print ("monster in room", file=f)
		if m == 1 or m == 2 or m == 3:
			print ("treasure present", file=f)
	else:
		print("empty")
		if m == 1:
			print ("treasure present", file=f)

def rollHMStats():
	Str = str(d6(3,6))
	Dex = str(d6(3,6))
	Con = str(d6(3,6))
	Int = str(d6(3,6))
	Wis = str(d6(3,6))
	Cha = str(d6(3,6))
	Com = str(d6(3,6))

	StrP = str(d6(1,100))
	DexP = str(d6(1,100))
	ConP = str(d6(1,100))
	IntP = str(d6(1,100))
	WisP = str(d6(1,100))
	ChaP = str(d6(1,100))
	ComP = str(d6(1,100))

	print ("Str: "+Str+" / "+StrP, file=f)
	print ("Dex: "+Dex+" / "+DexP, file=f)
	print ("Con: "+Con+" / "+ConP, file=f)
	print ("Int: "+Int+" / "+IntP, file=f)
	print ("Wis: "+Wis+" / "+WisP, file=f)
	print ("Cha: "+Cha+" / "+ChaP, file=f)
	print ("Com: "+Com+" / "+ComP, file=f)

try:
    filename = input("enter filename here \n")+".txt"

except EOFError:
    filename = "default.txt"

f = open(filename, 'w')
rollHMStats()
f.close()