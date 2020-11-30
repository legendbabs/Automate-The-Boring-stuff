# This program
# Calculate the product of the first 100,000 numbers.

import time

def main():
	startTime = time.time()
	prod = calcProd()
	endTime = time.time()

	# Display the time taken for the program 
	# to run
	print(f'The result is {len(str(prod))} digits long.')
	print(f'It took {endTime - startTime} second(s) to calculate.')


def calcProd():
	product = 1
	for i in range(1, 100000):
		product *= i
	return product

main()
