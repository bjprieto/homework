# dnd1-elementaladept.py

# You are a mage with the Fire Bolt spell. This does 1d10 damage, or 5.5
# points of damage on average. If you have the Elemental Adept feat, damage
# rolls of 1 become 2. How much more damage do you do on average if you are
# an Elemental Adept? Simulate by rolling dice a million times.

## Initialize modules and variables
import random
n = 10**6

## Vanilla Fire Bolt

# Sum of Fire Bolt damage
dmg_vfb = 0 

# Calculate average damage
for i in range(n):
	dmg = random.randint(1,10)
	dmg_vfb += dmg

# Average Fire Bolt damage
avg_vfb = dmg_vfb/n
# print(avg_vfb) # check


## Elemental Adapt Fire Bolt
	
# Sum of Fire Bolt damage with Elemental Adapt
eafb_dmg = 0 

# Calculate average damage
for i in range(n):
	dmg = random.randint(1,10)
	if dmg == 1: dmg = 2
	eafb_dmg += dmg

# Average Elemental Adapt Fire Bolt Damage
avg_eafb = eafb_dmg/n
# print(avg_eafb) # check


## Compare averages by difference
print(f'{avg_eafb - avg_vfb:.1f}')

"""
python3 dnd1-elementaladept.py
0.1
"""
