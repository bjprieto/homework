# 31entropy.py

# Write a Shannon entropy calculator: H = -sum(pi * log(pi))
# The values should come from the command line
# Store the values in a new list

# Note: make sure the command line values contain numbers
# Note: make sure the probabilities sum to 1.0
# Note: import math and use the math.log2()

# Hint: try breaking your program with erroneous input

import math
import sys

# Convert list to just a list of probabilities
probs = [val for val in sys.argv[1:]]

# Check all entered probabilities are numbers
for val in probs:
	try:    float(val)
	except: raise ValueError(f'Could not convert {val} into a number.')

# # Test a variation
# for val in probs: assert(float(val))

# Convert list items to floating points
probs = [float(val) for val in probs]

# Check that entered probabilities sum to 1, else exit the program
assert(math.isclose(sum(probs), 1))

# Calculate Shannon entropy
sum = 0
for pi in probs: sum += (pi * math.log2(pi))
H = -sum

# Print results
print(f'{H:.3f}')

"""
Archived suboptimal code

# Revise below portion 

# Check that entered probabilities sum to 1 and calculate Shannon entropy,
# else exit program
if sum(probs) == 1:
	sum = 0
	for pi in probs: sum += (pi * math.log2(pi))
	H = -sum # Shannon entropy
else: raise ValueError(f'The entered probabilities do not sum to 1.')
"""

"""
python3 31entropy.py 0.1 0.2 0.3 0.4
1.846
"""
