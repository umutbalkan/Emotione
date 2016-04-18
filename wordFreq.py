import requests
from bs4 import BeautifulSoup
import operator

# break up into 3 functions
# find all words it use(a list of every single word)


# Extracts words from HTML page to text
def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, "html.parser")
    for title_text in soup.findAll('a', {'class': 'hdrlnk'}):
        content = title_text.string
        words = content.lower().split()
        #print (words) # Splitted text containing all of the words
        for each_word in words:
            word_list.append(each_word)

    clean_up_list(word_list) # Calls next function

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
    word_count = {}     # declaration of dictionary data type
    
    # This loop simply calculates the frequency of each word
    for word in clean_word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # sort & display it on the screen by ascending order.
    for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):
        print(value, key)

# HTML page for processing
start('https://bloomington.craigslist.org/search/apa')