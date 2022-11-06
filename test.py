
import BstMap as bst
import random
import HashSet as hset
bucket = hset.HashSet()
bucket.init()


file = 'brian_13525_words.txt'

names = ["Ella", "Owen", "Fred", "Zoe", "Adam", "Ceve", "Adam", "Ceve", "Jonas", "Ola", "Morgan", "Fredrik", "Simon", "Albin", "Jonas", "Amer", "David"]


word = open(file, 'r', encoding="utf-8")
words = []
words.extend(word)
new_word = []
for l in range(900):
    element = random.choice(words)
    new_word.append(element)
for i in new_word:
    bucket.add(i)
print(bucket.max_bucket_size())
print(bucket.zero_bucket_ratio())