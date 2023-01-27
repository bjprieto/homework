# dnd4-deathsaves.py

# Death saves are a little different than normal saving throws. If your
# health drops to 0 or below, you are unconscious and may die. Each time it
# is your turn, roll a d20 to determine if you get closer to life or fall
# deeper into death. If the number is less than 10, you record a "failure".
# If the number is 10 or greater, you record a "success". If you collect 3
# failures, you "die". If you collect 3 successes, you are "stable" but
# unconscious. If you are unlucky and roll a 1, it counts as 2 failures.
# If you're lucky and roll a 20, you gain 1 health and have "revived".
# Write a program that simulates death saves. What is the probability one
# dies, stabilizes, or revives?

import random

# Initialize variables
n = 10**6
die_chance = 0
save_chance = 0
revive_chance = 0

for i in range(n):
	
	# Initialize variables
	revive = 0
	save = 0
	death = 0
	
	# Roll death saves until achieving a result
	while save < 3 and death > -3 and revive != 1:
		roll = random.randint(1,20)
		if roll == 20: revive = 1
		elif roll == 1: death -= 2
		elif roll >= 10: save += 1
		else: death -= 1
		# print(roll, death, save, revive, sep='\t')

	# Keep track of each result
	if death <= -3: die_chance += 1
	if save == 3: save_chance += 1
	if revive == 1: revive_chance += 1


# Print results
print('die:', f'{die_chance/n:.3f}')
print('stabilize:', f'{save_chance/n:.3f}')
print('revive:', f'{revive_chance/n:.3f}')	

"""
python3 dnd4-deathsaves.py
die: 0.405
stabilize: 0.414
revive: 0.181
"""
