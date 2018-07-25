import urllib.request

def read_text():
	quotes = open("/home/eva/Desktop/motivation.txt")
	contents_of_the_file = quotes.read()
	print(contents_of_the_file)
	quotes.close()
	check_profanity(contents_of_the_file)


def check_profanity(text_to_check):
	connection = urllib.request.urlopen("http://www.dyl.com/profanity?q="+text_to_check)
	output = connection.read()
	print(output)
	connection.close()
read_text()