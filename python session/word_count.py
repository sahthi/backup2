from urllib.request import urlopen

def get_data(url):
	w = urlopen(url)
	data = w.read()
	data_s = str(data, "utf-8")

	return data_s

def get_word_count(url):
	data_s = get_data(url)
	count_words  = {}
	for line in data_s.split("\n"):
		for word in line.split():
			if word not in count_words:
				count_words[word] = 1
			else:
				count_words[word] = count_words[word]+1

	return count_words

if __name__ == "__main__":
	print("Word count dictionary:", get_word_count("http://sixty-north.com/c/t.txt"))
