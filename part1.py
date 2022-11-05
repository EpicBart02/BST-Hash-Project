from collections import Counter

#Count unique words 1 
# 1 Count unique words using set class


def get_unique_words(text_file): 
    f = open(text_file, 'r', encoding='utf-8') 
    text = f.read()
    #cleaning
    text = text.lower()                 #convert the words to lower casre 
    words = text.split()                  #split each word into a list 
    words = [word.strip('.,!";()[]') for word in words]         #clean the symbols in file          
    # change the type for the words, list --> set
    words = set(words)
    return words

text_file1 = 'brian_13525_words.txt'
text_file2 = 'newspaper_15179625_words.txt'


#2 use dictionary class to produce a Top 10 list of the 10 of the most frequently used words having a word latger than 4 

def top_10(file):
    f = open(file, 'r', encoding='utf-8')
    dct = {}                           #Create an empty set to store all the unique words that have a len over 4
    for word in f:
        if len(word) > 5:              #Tell the code that the minimum length of a word has to be 4 or more
            if word in dct:
                dct[word] += 1         #If a word is brought up for the first time, it gets a value of 1, else it gets +1
            else:
                dct[word] = 1
        else:
            False                      #If the len of the word is less then 4, it returns as false and doesnt get included in the dct
    return Counter(dct).most_common(10)

for text_file in [text_file1]:
    unique_words = get_unique_words(text_file)
    print ("the number of unique words in", text_file1, "is:", len(unique_words), "\nAnd the top 10 most used words are\n", top_10(text_file1))
for text_file in [text_file2]:
    unique_words = get_unique_words(text_file)
    print ("the number of unique words in", text_file2, "is:", len(unique_words), "\nAnd the top 10 most used words are\n", top_10(text_file2))

