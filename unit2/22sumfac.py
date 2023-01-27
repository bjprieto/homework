# 22sumfac.py

# Write a program that computes the running sum from 1..n
# Also, have it compute the factorial of n while you're at it
# Use the same loop for both calculations

# Note: you may not import math or any other library

n = 5 # use this value for your computation

# Print n
print(n, end= ' ')

# Print running sum
sum = 0
for i in range(6):
	sum += i
print(sum, end=' ')

# Print factorial
fac = 1
for i in range(1, 6):
	fac *= i
print(fac)
"""
python3 22sumfac.py
5 15 120
"""
