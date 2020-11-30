def main():
	print('Enter your details: ')
	print()
	input('Press Enter to continue... ')

	name = input('Your name: ')
	level = input('Your level')
	girlfriendName = input('Girlfriend name: ')

	details(name, level, girlfriendName)


def details(myName, myLevel, myGirl):
	print('My name is', myName)
	print('I am in', myLevel)
	print('She bears', myGirl)

main()

