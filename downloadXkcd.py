#! python3

# downloadXkcd.py - Downloads every single XKCD comic.

import requests, os, bs4
url = 'http://xkcd.com' 		# starting url
os.makedirs('xkcd',exist_ok = True)		# create a directory to store all the downloads

while not url.endswith("#"):
	# Download the page.
	print("Downloading the page ... ")
	res = requests.get(url)
	res.raise_for_status()
	try:
		soup = bs4.BeautifulSoup(res.text,'lxml')
	except bs4.FeatureNotFound:  # lxml is not installed
		soup = bs4.BeautifulSoup(res.text,'html.parser')

	# Find the URL of the comic image.
	comic_element = soup.select('#comic img')
	if comic_element == []:
		print("No comic image found!!..")
	else:
		comic_image_url = comic_element[0].get('src')
		# download the image
		print("Downloading the image %s .. " %(comic_image_url))
		res = requests.get('http:' + comic_image_url)
		res.raise_for_status()

		# Save the image to ./xkcd.
		file = open( os.path.join('xkcd',os.path.basename(comic_image_url)) , 'wb')
		for chunk in res.iter_content(10000):
			file.write(chunk)
		file.close()

	# Get the Prev button's url.
	prev_link = soup.select('a[rel="prev"]')[0]
	url = 'http://xkcd.com' + prev_link.get('href')

print("Done")
