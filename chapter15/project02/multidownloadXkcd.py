import requests, os, bs4, threading

os.makedirs('xkcd', exist_ok=True)

def downloadXkcd(startComic, endComic):
	for urlNumber in range(startComic, endComic):
		# Download the page
		print(f'Downloading page http://xkcd.com/{urlNumber}')
		res = requests.get(f'http://xkcd.com/{urlNumber}')
		res.raise_for_status()

		soup = bs4.BeautifulSoup(res.text)

		comicElem = soup.select('#comic img')
		if comicElem == []:
			print('Could not find comic image')
		else:
			comicUrl = comicElem[0].get('src')
			# Download the image
			print(f'Downloading the image {comicUrl}')
			res = requests.get(comicUrl)
			res.raise_for_status()

			# Save the image to ./xkcd.
			imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
			for chunk in res.iter_content(100000):
				imageFile.write(chunk)
			imageFile.close()

# Create and start the Thread objects.
downloadThreads = []
for i in range(0, 1400, 100):
	downloadThread = threading.Thread(target=downloadXkcd, args=(i, i+99))
	downloadThreads.append(downloadThread)
	downloadThread.start()

# Wait for all threads to end.
for downloadThread in downloadThreads:
	downloadThread.join()
print('Done.')

