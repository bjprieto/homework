# 30stats.py

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median

# Hint: use sys.argv to get the values from the command line

# Note: you are not allowed to import any library except sys

import sys

# Initialize conditions
sum = 0
min = None
max = None

# Convert list to list of values
nums = [float(sys.argv[val]) for val in range(1, len(sys.argv))]

# Find minimum, maximum, and mean
for val in nums:
	
	# Find minimum
	if min == None: min = val
	elif val < min: min = val
	
	# Find maximum
	if max == None: max = val
	elif val > max: max = val
	
	# Take sum
	sum += val

mean = sum/len(nums)

# Find std deviation
sq_diff = 0 # sum of the difference of squares between nums values and mean
for val in nums: sq_diff += ((val**2) - (mean**2))
stdev = (sq_diff/(len(nums)))**0.5 

# Sort list and find middle position
nums.sort()
med_pos = (len(nums)/2) - 0.5
# print(med_pos) # check

# Find median based on middle position
if med_pos%1 == 0: 
	med = nums[int(med_pos)]
else:
	med_pos = int(med_pos)
	med = 0.5*(nums[med_pos] + nums[med_pos-1])

# Print results
print('Count:', f'{len(nums)}')
print('Minimum:', f'{min}')
print('Maximum:', f'{max}')
print('Mean:', f'{mean:.3f}')
print('Std. dev:', f'{stdev:.3f}')
print('Median:', f'{med:.3f}')

"""
python3 30stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""
