import random

def dice(sides, faces):
	n = 0
	for i in range(sides):
		n += random.randint(1, faces)
	return n

def rollAbility():
    return dice(3, 6)

def rollPercentile():
    return dice(1, 100)

Str = rollAbility()
StrP = rollPercentile()
Dex = rollAbility()
DexP = rollPercentile()
Con = rollAbility()
ConP = rollPercentile()
Int = rollAbility()
IntP = rollPercentile()
Wis = rollAbility()
WisP = rollPercentile()
Cha = rollAbility()
ChaP = rollPercentile()
Com = rollAbility()
ComP = rollPercentile()

print("Str: " + str(Str) + "/" + str(StrP))
print("Dex: " + str(Dex) + "/" + str(DexP))
print("Con: " + str(Con) + "/" + str(ConP))
print("Int: " + str(Int) + "/" + str(IntP))
print("Wis: " + str(Wis) + "/" + str(WisP))
print("Cha: " + str(Cha) + "/" + str(ChaP))
print("Com: " + str(Com) + "/" + str(ComP))

