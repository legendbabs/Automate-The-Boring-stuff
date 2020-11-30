# import logging
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s-%(levelname)s-%(message)s')

# logging.debug('Student details:')
# logging.debug('=================')
# def student_details(first_name, last_name, age):
# 	logging.debug('My name is', first_name, last_name)
# 	logging.debug('I am', age, 'years old.')

# student_details('Tunde', 'Muhamed', '29')

import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s-%(levelname)s-%(message)s')

logging.debug('Start the program.')
def factorial(num):
	logging.debug(f'Start of factorial of {num}.')
	total = 1
	for i in range(1, num+1):
		total *= i
		logging.debug(f'i is {i}: total is {total}')
	logging.debug('End of factorial.')

	return total

print('Factorial:', factorial(5))
logging.debug('End of program.')
