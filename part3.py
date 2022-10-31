from collections import Counter
import BstMap as bst

map = bst.BstMap()

#Count unique words 1 
# 1 Count unique words using set class


def get_unique_words(text_file): 
    f = open(text_file, 'r', encoding='utf-8') 
    text = f.read()

    #cleaning
    text = text.lower()                 #convert the words to lower casre 
    words = text.split()                  #splite each word into a list 
    words = [word.strip('.,!";()[]') for word in words]         #clean the symbols in file
    words = [word.replace("'s", '') for word in words]          
    # change the type for the words, list --> set
    words = set(words)
    return words

text_file1 = 'brian_13525_words.txt'
text_file2 = 'newspaper_15179625_words.txt'


#2 use dictionary class to produce a Top 10 list of the 10 of the most frequently used words having a word latger than 4 
f = open(text_file1, 'r', encoding='utf-8')
for word in f:
    if len(word) > 4:
        map.put(word, 1)
print(map)