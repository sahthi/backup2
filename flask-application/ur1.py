import urllib2

import sys



def fetch_data(url):

	try:

		w = urllib2.urlopen(url)

	except:

		print("Bad URL")

		sys.exit(100)

	data = w.read()

	
	return data



def fetch_word_count(url):

	data_s = fetch_data(url)



	lines = data_s.split("\n")



	word_count = {}



	for line in lines:

		for word in line.split():

			word_count[word] = word_count.get(word, 0)+1



	return word_count



if __name__ == "__main__":

	print(fetch_word_count("https://sixty-north.com/c/t.txt"))


