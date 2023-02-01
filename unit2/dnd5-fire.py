# dnd5-fire.py

# Your party has just defeated an evil dragon and it's your time to pick loot.
# You can either have the ring of fire protection, which gives advantage on
# all fire saving throws, or the cloak of fire protection, which gives +3
# versus all fire saving throws. Which one is better? Make a program that
# simulates saving throw success at various DCs (1-20) for ring and cloak.

import random

# Initialize variables
n = 10**6

for dc in range(1, 21):

	# Initialize loop variables
	r_save = 0 # Sum of Ring of Fire Protection fire saves
	c_save = 0 # Sum of Cloak of Fire Protection fire saves
	
	for i in range(n):
	
		# Ring of Fire Protection
		
		# Perform rolls
		roll1 = random.randint(1,20)
		roll2 = random.randint(1,20)
		
		# Apply advantages
		if roll1 >= roll2: roll = roll1
		elif roll2 >= roll1: roll = roll2
		
		# Passes DC?
		if roll >= dc: r_save += 1
		
		
		
		# Cloak of Fire Protection
		
		# Perform roll and apply effect
		roll = random.randint(1,20)+3
		
		# Passes DC?
		if roll >= dc: c_save += 1
	
	# Print results	
	print(dc, f'{r_save/n:.4f}', f'{c_save/n:.4f}')
	

"""
python3 dnd5-fire.py
1 1.0000 1.0000
2 0.9975 1.0000
3 0.9900 1.0000
4 0.9775 1.0000
5 0.9601 0.9501
6 0.9376 0.9003
7 0.9102 0.8500
8 0.8776 0.8000
9 0.8401 0.7499
10 0.7975 0.6997
11 0.7503 0.6504
12 0.6978 0.6004
13 0.6400 0.5501
14 0.5772 0.5001
15 0.5094 0.4498
16 0.4373 0.3998
17 0.3597 0.3499
18 0.2777 0.3001
19 0.1899 0.2496
20 0.0976 0.2000
"""
