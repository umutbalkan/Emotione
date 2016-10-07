import urllib
from bs4 import BeautifulSoup
import operator


# Extracts words from HTML page to text
def start(url):
	word_list = []
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html, "html.parser")

	# kill all script and style elements
	for script in soup(["script", "style"]):
		script.extract()		

	# get text
	text = soup.get_text()


	# break into lines and remove leading and trailing space on each
	lines = (line.strip() for line in text.splitlines())
	# break multi-headlines into a line each
	chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
	# drop blank lines
	text = '\n'.join(chunk for chunk in chunks if chunk)

	#print  "#*****************#" + "\nHTML to TEXT conversion of given URL" + '\n"#*****************#"'
	print (text)

	# get words from TEXT
	#for word in text:
	#	words = word.lower()
	#	word_list.append(words)
		#for each_word in words:
		#	word_list.append(each_word)

	print word_list
	#clean_up_list(word_list) # Calls next function

# Cleans word list from unsignificant symbols and words.
def clean_up_list(word_list):
    clean_word_list = []
    for word in word_list:
        # These variables clears data from symbols and unsignificant words
        symbols = "!@#$%^&*()_+|{}:<>?-=\[]\";',./'1234567890"
        nonsense = ["and", "the", "for", "an", "is", "are"]
        for i in range(0, len(symbols)):            # Clears symbols
            word = word.replace(symbols[i], "")     # Replace that word with empty string
        for i in range(0, len(nonsense)):           # Clears nonsense words
            word = word.replace(nonsense[i], "")    # Replace that word with empy string
        if len(word) > 0:
            # if word is not empty string than append it to the clean_word_list
            clean_word_list.append(word) 
        #print (clean_word_list) # Cleaned version of text containing all of the words

    create_dictionary(clean_word_list) # Calls next function

# Creates key-value pairs of each word
def create_dictionary(clean_word_list):
    word_count  = {}     # declaration of dictionary data type
    
    # This loop simply calculates the frequency of each word
    for word in clean_word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    print "#*****************#" + "\nWord Frequency" + "\n#*****************#"
    # sort & display it on the screen by ascending order.
    for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):
        print(value, key)


# HTML page for processing
start('http://www.theguardian.com/world/2016/apr/22/brussels-bomber-najim-laachraoui-identified-isis-jailer-foreign-hostages')