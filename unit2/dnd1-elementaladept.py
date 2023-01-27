# dnd1-elementaladept.py

# You are a mage with the Fire Bolt spell. This does 1d10 damage, or 5.5
# points of damage on average. If you have the Elemental Adept feat, damage
# rolls of 1 become 2. How much more damage do you do on average if you are
# an Elemental Adept? Simulate by rolling dice a million times.


import random

# Vanilla Fire Bolt average calculator
dmg_vfb = 0 # Sum of Fire Bolt damage

for i in range(10**6):
	dmg = random.randint(1,10)
	dmg_vfb += dmg
avg_vfb = dmg_vfb/(10**6)
# print(avg_vfb)

# Elemental Adapt Fire Bolt average calculator
eafb_dmg = 0 # Sum of Fire Bolt damage with Elemental Adapt

for i in range(10**6):
	dmg = random.randint(1,10)
	if dmg == 1: dmg = 2
	eafb_dmg += dmg
avg_eafb = eafb_dmg/(10**6)
# print(avg_eafb)


# Calculate and print difference of averages
print(f'{avg_eafb - avg_vfb:.1f}')
"""
python3 dnd1-elementaladept.py
0.1
"""
