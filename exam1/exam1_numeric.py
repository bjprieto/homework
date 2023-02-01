# Numeric Program

# Initialize variables
m = 1
n = 20
k = 1

# Generate numbers and label properties
for i in range (m, n+1, k):
	
	# Check is divisible by 3
	is_div3 = False
	if i%3 == 0: is_div3 = True
	
	# Check is square
	is_sq = False
	for sq in range(i):
		if sq == i**0.5:
			is_sq = True
			break
	
	# Check is prime
	is_prime = False
	if i >= 3:
		is_prime = True
		for div in range(2, i):
			if i%div == 0: 
				is_prime = False
				break
			
	# Print results
	print(i, end='')
	if is_div3 == True: print('@', end='')
	if is_sq == True: print('#', end ='')
	if is_prime == True: print('*', end='')
	print('')