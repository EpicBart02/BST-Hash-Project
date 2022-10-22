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
for text_file in [text_file1]:
    unique_words = get_unique_words(text_file)
    print ("the number of unique words in", text_file1, "is:", len(unique_words))
for text_file in [text_file2]:
    unique_words = get_unique_words(text_file)
    print ("the number of unique words in", text_file2, "is:", len(unique_words))


#2 use dictionary class to produce a Top 10 list of the 10 of the most frequently used words having a word latger than 4 






