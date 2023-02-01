# dnd2-piercer.py

# If you have the "Piercer" feat, you may re-roll a damage die. You must
# take the new roll regardless if it was lower than the previous roll. Assume
# you have a weapon that does 1d8 damage. Clearly, you should re-roll any die
# with an initial roll of 1 damage. But what about higher rolls? Your friend
# Jorg re-rolls 1-5. But Gastin says that's too high and re-rolls 1-3.
# What is the optimal strategy? Simulate it.
# Make a table showing reroll threshold (use <=) and average damage.

import random

# Initialize variables
n = 10**6

# Generate table of reroll thresholds and average damages
for thresh in range(2,8):

	# Sum of damage
	sum = 0 
	
	# Perform re-rolls
	for i in range(n):
		roll = random.randint(1,8)
		# print(roll, end=' ') # check
		
		if roll <= thresh: roll = random.randint(1,8)
		# print(roll, end=' ') # check replaced roll
		
		sum += roll
		# print(sum) # check update
	
	# Print threshold with re-roll average
	print(thresh, f'{sum/n:.3f}')

"""
python3 dnd2-piercer.py
2 5.251
3 5.437
4 5.500
5 5.438
6 5.250
7 4.938
"""
