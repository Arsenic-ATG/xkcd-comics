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

	
	# TODO: Find the URL of the comic image. # TODO: Download the image.
	# TODO: Save the image to ./xkcd.
	# TODO: Get the Prev button's url.
print("Done")