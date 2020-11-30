import requests

res = requests.get('http://inventwithpython.com/page_that_does_not_exit')

try:
	res.raise_for_status()
except Exception as exc:
	print('There was a problem downloading the file:', exc)