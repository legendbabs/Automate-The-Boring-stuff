'''
Here we’ve defined a boxPrint() function that takes a character, a width,
and a height, and uses the character to make a little picture of a box with
that width and height. This box shape is printed to the screen.
Say we want the symbol character to be a single character, and the width and
height to be greater than 2. We add if statements to raise exceptions if
these requirements aren’t satisfied. Later, when we call boxPrint() with various
arguments, our try/except will handle invalid arguments.
This program uses the except Exception as err form of the except statement
'''

def boxPrint(symbol, width, height):
	if len(symbol) != 1:
		raise Exception('Symbol must be a single character string.')
	if width <= 2:
		raise Exception('Width must be greater than 2.')
	if height <= 2:
		raise Exception('Height must be greater than 2.')

	print(symbol * width)
	for i in range(height-2):
		print(symbol + (' '*(width-2)) + symbol)
	print(symbol * width)

for sym, w, h in (('*', 4, 4), ('0', 20, 5), ('X', 1, 3), ('ZZ', 3, 3)):
	try:
		boxPrint(sym, w, h)
	except Exception as err:
		print('An Exception happened: ' + str(err))