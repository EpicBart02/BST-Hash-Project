from collections import Counter
import BstMap as bst
import HashSet as hset


map = bst.BstMap()
words = hset.HashSet()
words.init()


text_file1 = 'brian_13525_words.txt'
text_file2 = 'newspaper_15179625_words.txt'

#Calculate what needs to be hashed in this method
def hashing(file): 
    f = open(file, 'r', encoding='utf-8') 
    for word in f:
        word = word.strip('.,!";()[]')
        words.add(word.lower())
    print("The number of unique words in", file, "is", words.get_size())
    print("The max bucket size for", file, "is", words.max_bucket_size())
    print("The zero bucket ratio for", file, "is", words.zero_bucket_ratio())

#2 use dictionary class to produce a Top 10 list of the 10 of the most frequently used words having a word latger than 4 
def open_file(file):
    f = open(file, 'r', encoding='utf-8')
    for word in f:
        word = word.strip('.,!";()[]')
        map.put(word.lower(), 1)
    print("The number of tree nodes is:" , map.size())
    print("The max depth is" , map.max_depth() , "and the number of leaf nodes are" , map.count_leafs())
    print("The top 10 most frequently used words in", file, "are", map.top_10())

open_file(text_file1)
print()
hashing(text_file1)
print()
open_file(text_file2)
print()
hashing(text_file2)
