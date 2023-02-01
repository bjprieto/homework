# dnd3-savingthrow.py

# One of the core mechanics of D&D is the "saving throw". When certain
# events happen, you need to roll a d20 to figure out if you succeed or not.
# For example, you are walking across a frozen lake and it begins to crack
# underfoot. If you make a saving throw, you step aside. If you fail, you
# fall in. Some saving throws are more difficult than others. If the ice
# is very thick, the "difficulty class" (DC) may be only 5. This means you
# only need to roll a 5 or higher to succeed. However, if the ice is thin
# and has a DC of 15, you will need a roll of 15 or higher to succeed.
# Certain events may give you "advantage" or "disadvantage". For example,
# if you have a rope tied around your waist and a friend is instructed to
# pull you aside if anything bad happens, you could have "advantage". This
# allows you to roll two d20s and take the larger value. You may also have
# disadvantage, for example another "friend" pushes you from behind, causing
# you to stumble forward. In this case, you have "disadvantage" and must take
# the lower of two d20 rolls.

# Write a program that simulates saving throws against DCs of 5, 10, and 15.
# What is the probability of success normally or with advantage/disadvantage?
# Make a table showing the results.

import random

# Perform rolls and calculate averages
for dc in range(5, 16, 5):

	# Initialize variables
	n = 10**5
	reg_sum = 0 # Sum of straight/regular rolls
	adv_sum = 0 # Sum of advantage rolls
	dis_sum = 0 # Sum of disadvantage rolls
	
	for i in range(n):
		
		# Straight/regular roll
		
		# Perform roll
		roll1 = random.randint(1,20)
		
		# Passes DC?
		if roll1 >= dc: reg_sum += 1


		
		# Perform second roll
		roll2 = random.randint(1,20)
# 		print(roll1, roll2, end=' ') # roll check
		
		
		
		# Advantage
		
		# Apply advantage
		if roll1 >= roll2:   roll = roll1
		elif roll2 >= roll1: roll = roll2
		
		# Passes DC?
		if roll >= dc: adv_sum += 1
# 		print(roll, end=' ') # roll check
# 		print(adv_sum, end=' ') # sum check
		
		
		
		# Disadvantage
		
		# Apply disadvantage
		if roll1 <= roll2:   roll = roll1
		elif roll2 <= roll1: roll = roll2
		
		# Passes DC?
		if roll >= dc: dis_sum += 1
# 		print(roll) # roll check
# 		print(dis_sum) # sum check
	
	# Print averages
	print(dc, f'{reg_sum/n:.3f}', f'{adv_sum/n:.3f}',
	 	  f'{dis_sum/n:.3f}', sep='\t')

"""
python3 dnd3-savingthrow.py
5  0.800 0.960 0.640
10 0.550 0.797 0.302
15 0.300 0.510 0.090
"""
