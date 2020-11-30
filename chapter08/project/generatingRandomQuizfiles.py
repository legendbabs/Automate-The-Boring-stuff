'''
Say you’re a geography teacher with 35 students in your class and you want
to give a pop quiz on US state capitals. Alas, your class has a few bad eggs in
it, and you can’t trust the students not to cheat. You’d like to randomize the
order of questions so that each quiz is unique, making it impossible for anyone
to crib answers from anyone else.
'''

# Step 1: Store the Quiz Data in a Dictionary

import random, pprint
# The quiz data. Keys are states and values are their capitals.
capitals = {
'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 
'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 
'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'
} 

# print('STATE\t\t\t\t\t\t CAPITAL')
# print('=======================================')
# for k,v in capitals.items():
# 	print(k.ljust(18), '--->', v.rjust(15))

# Generate 35 quiz files.
# Step 2: Create the Quiz File and Shuffle the Question Order
for quizNum in range(35):
	quizFile = open(f'capitalsquiz{quizNum+1}.txt', 'w')
	answerKeyFile = open(f'capitalsquiz_answers{quizNum+1}.txt', 'w')

	# Write out the header for the quiz.
	quizFile.write('Name:\nDate:\nPeriod:\n\n')
	quizFile.write((' ' * 20) + 'State Capital Quiz Form' + str(quizNum+1))
	quizFile.write('\n\n')

	# Shuffle the order of the states.
	states = list(capitals.keys())
	random.shuffle(states)

	# Step 3: Create the Answer Options
	# Loop through all 50 states, making a question for each.
	for questionNum in range(50):
		# Get right and wrong answers.
		correctAnswer = capitals[states[questionNum]]
		wrongAnswers = list(capitals.values())
		del wrongAnswers[wrongAnswers.index(correctAnswer)]
		wrongAnswers = random.sample(wrongAnswers, 3)
		answerOptions = wrongAnswers + [correctAnswer]
		# Finally, the answers need to be randomized
		# so that the correct response isn’t always choice D.
		random.shuffle(answerOptions)

		# Step 4: Write Content to the Quiz and Answer Key Files
		# Write the question and the answer options to the quiz file.
		quizFile.write(str(questionNum+1) + '. ' + 'What is the capital of ' + states[questionNum] + '?' + '\n')

		for i in range(4):
			quizFile.write('ABCD'[i] + ' ' + answerOptions[i] + '\n')
		quizFile.write('\n')

		# Write the answer key to a file.
		answerKeyFile.write(str(questionNum+1) + '.' + 'ABCD'[answerOptions.index(correctAnswer)])

	quizFile.close()
	answerKeyFile.close()





