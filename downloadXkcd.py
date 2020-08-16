#! python3

# downloadXkcd.py - Downloads every single XKCD comic.

import requests, os, bs4
url = 'http://xkcd.com' 		# starting url
os.makedirs('xkcd')		# create a file to place all the downloads

while not url.endswith("#"):
	# Download the page.
	print("Downloading the page ... ")
	res = requests.get(url)
	res.raise_for_status()

	soup = bs4.BeautifulSoup(res,'lxml')

	# Find the URL of the comic image.
	comic_element = soup.select('#comic img')
	if comic_element == []:
		print("No comic image found!!..")
	else
		comic_image_url = comic_element[0].get('scr')
		# download the image
		print("Downloading the imgae %s .. " %(comic_image_url))
		res = requests.get(comic_image_url)
		res.raise_for_status()

	# TODO: Save the image to ./xkcd.
	# TODO: Get the Prev button's url.
print("Done")