import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

try:
	res.raise_for_status()

	playFile = open('RomeoAndJuliet.txt', 'wb')
	for chunk in res.iter_content(100000):
		playFile.write(chunk)
	playFile.close()

except Exception as e:
	print('Error encountered:', e)

