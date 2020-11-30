'''
Say you have the boring task of finding every phone number and email
address in a long web page or document. If you manually scroll through
the page, you might end up searching for a long time. But if you had a program
that could search the text in your clipboard for phone numbers and
email addresses, you could simply press ctrl-A to select all the text, press
ctrl-C to copy it to the clipboard, and then run your program. It could
replace the text on the clipboard with just the phone numbers and email
addresses it finds.
'''

# Step1: Create a regex for phone numbers

import pyperclip, re

phoneRegex = re.compile(r'''
	(
	(\d{3}|\(\d{3}\))?              # area code
	(\s|-|\.)?                      # separator
	\d{3}                           # first 3 digits
	(\s|-|\.)?                      # separator
	\d{4}                           # last 4 digits
	(\s*(ext|x|ext.)\s*\d{2,5})?    # extension
	)
	''', re.VERBOSE
	)

# Step2: Create a regex for email address
emailRegex = re.compile(r'''
	(
	[a-zA-Z0-9._%+-]+      # username
	@                      # @ symbol
	[a-zA-Z0-9.-]+         # domain name
	(\.[a-zA-Z]{2,4})      # dot something

	)
	''', re.VERBOSE)

# Step 3: Find all the matches in the clipboard text
text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
	phoneNum = '-'.join([groups[1], groups[3], groups[5]])
	if groups[8] != '':
		phoneNum += ' x' + groups[8]
	matches.append(phoneNum)

for groups in emailRegex.findall(text):
	matches.append(groups[0])

if len(matches) > 0:
	pyperclip.copy('\n'.join(matches))
	print('Copied to clipboard.')
	print('\n'.join(matches))
else:
	print('No phone numbers or email address found.')




# phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# mo = phoneRegex.search('My number is: 070-332-6997')
# print(mo.groups())

