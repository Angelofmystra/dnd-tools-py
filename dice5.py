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

Str = d6(3,6)
Dex = d6(3,6)
Con = d6(3,6)
Int = d6(3,6)
Wis = d6(3,6)
Cha = d6(3,6)
Com = d6(3,6)

StrP = str(d6(1,100))
DexP = str(d6(1,100))
ConP = str(d6(1,100))
IntP = str(d6(1,100))
WisP = str(d6(1,100))
ChaP = str(d6(1,100))
ComP = str(d6(1,100))

def rollHMStats():
	print ("Str: "+str(Str)+" / "+StrP, file=f)
	print ("Dex: "+str(Dex)+" / "+DexP, file=f)
	print ("Con: "+str(Con)+" / "+ConP, file=f)
	print ("Int: "+str(Int)+" / "+IntP, file=f)
	print ("Wis: "+str(Wis)+" / "+WisP, file=f)
	print ("Cha: "+str(Cha)+" / "+ChaP, file=f)
	print ("Com: "+str(Com)+" / "+ComP, file=f)

def racesAvailable(Str):
	l = ["Male Dwarf", "Female Dwarf", "Male Elf", "Female Elf", "Male Gnome", "Female Gnome", "Male Gnomeling", "Female Gnomeling", "Male Half Elf", "Female Half Elf", "Male Halfling", "Female Halfling", "Male Half Orc", "Female Half Orc", "Male Half Ogre", "Female Half Ogre", "Male Pixie Fairy", "Female Pixie Fairy"]
	strMinFilter(l,Str)
	strMaxFilter(l,Str)
	dexMinFilter(l,Str)
	dexMaxFilter(l,Str)
	conMinFilter(l,Str)
	conMaxFilter(l,Str)
	intMinFilter(l,Str)
	intMaxFilter(l,Str)
	wisMinFilter(l,Str)
	wisMaxFilter(l,Str)
	chaMinFilter(l,Str)
	chaMaxFilter(l,Str)
	comMinFilter(l,Str)
	comMaxFilter(l,Str)	
	return l

def strMinFilter(l, Str):
	if Str < 1:
		l.remove("Male Pixie Fairy")
		l.remove("Female Pixie Fairy")
	if Str < 3:
		l.remove("Male Elf")
		l.remove("Female Elf")
		l.remove("Male Half Elf")
		l.remove("Female Half Elf")
	if Str < 6:
		l.remove("Male Gnome")
		l.remove("Female Gnome")
		l.remove("Male Gnomeling")
		l.remove("Female Gnomeling")
		l.remove("Male Halfling")
		l.remove("Female Halfling")
		l.remove("Male Half Orc")
	if Str < 8:
		l.remove("Male Dwarf")
		l.remove("Female Dwarf")
	if Str < 14:
		l.remove("Male Half Ogre")
		l.remove("Female Half Ogre")
	if Str < 18:
		l.remove("Female Half Orc")

def strMaxFilter(l,Str):

def dexMinFilter(l,Str):

def dexMaxFilter(l,Str):

def conMinFilter(l,Str):

def conMaxFilter(l,Str):

def intMinFilter(l,Str):

def intMaxFilter(l,Str):

def wisMinFilter(l,Str):

def wisMaxFilter(l,Str):

def chaMinFilter(l,Str):

def chaMaxFilter(l,Str):

def comMinFilter(l,Str):
	
def comMaxFilter(l,Str):





try:
    filename = input("enter filename here \n")+".txt"

except EOFError:
    filename = "default.txt"

f = open(filename, 'w')
rollHMStats()
l = racesAvailable(Str)
l.append("Male Human")
l.append("Female Human")
print(str(l), file=f)
f.close()