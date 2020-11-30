'''
Whenever I search a topic on Google, I don’t look at just one search result
at a time. By middle-clicking a search result link (or clicking while holding
ctrl), I open the first several links in a bunch of new tabs to read later.
I search Google often enough that this workflow—opening my browser,
searching for a topic, and middle-clicking several links one by one—is
tedious. It would be nice if I could simply type a search term on the command
line and have my computer automatically open a browser with all
the top search results in new tabs. Let’s write a script to do this.
'''

# Step 1: Get the Command Line Arguments and Request the Search Page

import requests, sys, webbrowser, bs4

print('Googling...')
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Step 2: Find All the Results
soup = bs4.BeautifulSoup(res.text)
# print(soup.prettify())
linkElems = soup.select('.r a')

# Step 3: Open Web Browsers for Each Result
numOpen = min(5, len(linkElems))

for i in range(numOpen):
	webbrowser.open('http://google.com' + linkElems[i].get('href'))