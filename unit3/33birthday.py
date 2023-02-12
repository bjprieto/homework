# 33birthday.py

# You may have heard of the 'birthday paradox' before
# https://en.wikipedia.org/wiki/Birthday_problem
# Write a program that simulates it
# Make the number of days and the number of people command line arguments

# Hint: make the problem smaller to aid visualization and debugging

# Variation: try making the calendar a list
# Variation: try making the birthdays a list

import sys
import random

# Initialize general variables
days = int(sys.argv[1])
ppl = int(sys.argv[2])
k = 4.5                # exponent for easy modification of run number
n = int(10**k)         # runs
hit = 0                # number of instances of shared birthdays

# Calculate birthday-sharing probability

# Variation 1: Calendar List
for i in range(n):

	# Initialize variables
	cal = [0]*days
	# print(cal) # check

	# Generate birthdays
	for person in range(ppl):
		bday = random.randint(0, days-1)
		cal[bday] += 1
		# print(bday) # check
	
	# print(cal) # check
	
	# Tally instances of shared birthdays per iteration
	for day in cal:
		if day == 2: 
			hit += 1
			break
	
# Variation 2: Birthday list
# for i in range(n):
# 
# 	# Initialize variables
# 	bdays = []
# 
# 	# Generate birthdays
# 	for person in range(ppl):
# 		bday = random.randint(1, days+1)
# 		bdays.append(bday)
# 
# 	bdays.sort()
# 	# print(bdays) # check
# 	
# 	
# 	for bday in range(len(bdays)-1):
# 		if bdays[bday] == bdays[bday+1]:
# 			hit += 1
# 			break
	
# Print results
print(f'{hit/n:.3f}')

"""
python3 33birthday.py 365 23
0.571
"""

