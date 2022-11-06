************************

# Mini-project report 
Members: Sedra Altunji and Abdul Rahman Racheed
Program: CTMAT and NGDPV	
Course: 1DT901 and 1DV501
Date of submission: 2022-11-06

## Introduction 
This project, mini-project, is a part of the courses 1DT901/1DV501 and it is a project in algorithms and data structures. In this project, three different tasks are going to be solved. Task 1, Count unique words 1, in this task the number of unique words will be counted from the files ‘life of brain’ and ‘swedish_news_2020’ with the help of Python set class. Also, in task 1, the ten most frequently used words having a length larger than 4 in each file have to be produced with the help of Python dictionary class. Task 2, Implementing data structures, in this assignment we will practice, Binary Search Trees (BST) and Hashing, which are techniques suitable for implementing dictionaries and sets.
The last task, Count unique words 2, same requirements as task 1, but this time should our hash based set and BST based map be used.


## Part 1: Count unique words 1
``life_of_brian`` had 2064 special/unique words while  ``swedish_news_2020`` had rougly 384000 words. We counted the special/unique words by simply using pythons built in sets. A set does not allow two of the same words to exist in the same set, so firstly we lower and split each word in the text files to get them prepared. And after that we place the words in a for loop to get rid of the special symbols by using ```word.strip()```
The code looks something like this.
```python
    text = text.lower()               
    words = text.split()                  
    words = [word.strip('.,!";()[]') for word in words]        
    words = set(words)
```
- The top 10 part of the code was quite easy to do. I firstly created a dictionary with keys, which are input words from each of the text files and in the beginning no word has a value. But everytome a word with over 4 characters shows up in the loop, it gains one to its value. If its the first time a word comes up in the loop, its value updates from None to 1.
```python
if word in dct:
                dct[word] += 1   
            else:
                dct[word] = 1
```
 And to get the top 10 values from the dictionary, i import a counter made for dictionaries and use it. Also i use a piece of code called ```most_common(10)``` that grabs the 10 most common words that come up in the files. The full line of code in the return looks like this. 
```Counter(dct).most_common(10)```

## Part 2: Implementing data structures
- Hashing, ```HashSet.py```
Computing the hash value takes place with the help of the function get_hash, which takes words as arguments, then it calculates and returns those hash value using ```ord(c)``` It then returns the numeric for each letter in a word and then sums all the values of the letters to get the hash value for each word in the string. 
```python
return sum([ord(c) for c in word]
```
For the add function, the hash value will be calculated at first, then we will go through all the buckets to find the position of the hash value and check if the given element exists, if not, it will be appended. Also when we do append a word in the buckets, we increase the self.size by one because we do increase bucket size by one.
```python
if word not in self.buckets[hash_value]:   
      self.buckets[hash_value].append(word)
      self.size += 1
```
If the bucket is full, we have to rehash it to increase its size. With rehashing, we mean to double the size of a bucket list when it is full. To do that, the old buckets must be saved first, so they don´t get deleted. ```temp_buckets = self.buckets``` Then, a bucket with double the len of the previous one must be created and at the same time we set ```self.size = 0``` so that when we add the words back the self size will be correct. At the end, re-adding the old bucket must be implemented.

- BST, ```BSTMap.py```
Firstly, the code for ``put``, The only way i can explain it is that i based the BST sorting based on the key, the letters. 
[Left side]: If the input key is less then the current key on the Tree, ```if key < self.key:```, it moves LEFT of that current Node. If the space is empty, the list created a new node and put the input key and its value inside of that node. 
```python
if self.left == None:
    self.left = Node(key, value)
```
But if there already was a node in that slot, the input key moves down one space in the Tree and the current key becomes that left node we were talking about earlier, the input key travels down until it finds an empty space it fits in. 
[Right side]: The right side of the tree is essentially the same as the left, but instead of it letting trough lower valued keys, it only lets the keys who are higher then the current key trough. The node travels down the same way as before though. To put it simply, it works exactly same way as the the left side, but takes in the higher values instead of lower values.

The code for ``max_depth`` was not very difficult once you understood the recursive methods of the BST. I recursively go down the tree and grab the value of the current node. Not the value as in key, value, but as in how far down it is in the tree. So each time we move, we grab the node's value.
In the end we return the highest value between left and right plus one to check the maximum depth of our tree. ```return max(left_depth, right_depth) + 1 ``` 
* Our BST map did not have any different outcomes since the binary tree can only be built one way. So the outcome will always be the same if its built the same way.
## Part 3: Count unique words 2

This part was very easily solved by using sort. Firstly, two methods within the BstMap.py file was created, top_10 and my_sort. My sort took in a tuple and returned the second element within it. Instead of returning the key, it returned the value.return t[1]. Thus, it was time to get all the words with the len over 5. We used filter and lambda to filter out all words with a len below 5.

```python
lst = filter(lambda x: len(x[0]) >5, lst)
```
After that, all the words were sorted from lowest to highest, and reversed the order of the list by using reverse=True and printed the first 10 elements in the reversed list. The output are the 10 words that came up most frequently in the file.
The code looks something like this:

```python
return sorted(lst, key=my_sort, reverse=True)[:10]
```
Also, in part3.py, minimum len of the word to 5 and over was set because it’s not allowed to have words with a len of 4 or less as stated in the project instructions.

The top 10 most frequent words in `life if brian`` are:
Brian, Centurion, Crowd, Mother, right, Crucifixion, Pilate, pontius, Crowd and Rogers. The output is the same as in part 1.

Lastly, the top 10 most frequent words in ``swe news_2020`` are as stated:
säger, under, kommer, efter, eller, också, andra, finns, sedan and procent. The output is the same in part 1 as well.


- BST and Hash values for the two text files
For the text file ```brian_13525_words.txt```, the bucket list size is 2079, the max bucket size stands at 16 and the zero-bucket ratio for HashSet is around 0.84. Now the results from the BST map, life_of_brian’s total node count is the exact same as the total bucket size. Its max depth is 28 while the total leaf count is 662.
For the second text file, ```newspaper_15179625_words.txt```, the bucket size stands at 384 501 words. Same goes for its total nodes in the BST. Max bucket size for it is 682 while zero bucket ratio stands at 0.99. The maximum depth is 83 and the leaf node count is 126 661.

* Explain how max bucket size and zero bucket ratio can be used to evaluate the quality of your hash function in HashSet. What are optimal/reasonable/poor values in both cases?

The larger max bucket size is, the worse the quality of the hash function in HashSet is. The reason is that it will take more time to add, contain and remove an element which is less efficient. We want to maintain the O(1) speed. This also means the more buckets filled the better. So a low zero bucket ratio is also optimal. To find the resonable values we decided on creating a list where we input 100 random words into a hash list and repeated that 5 times, increasing the word count by 200 each time we repeat, to see the average max bucket size and zero bucket ratio.

```python
for l in range(100):
    element = random.choice(words)
    new_word.append(element)
for i in new_word:
    bucket.add(i)
```


| Tries              | Max bct size    | Zero bkt ratio |
|:------------------ |:---------------:| --------------:|
| Try one(100)       |        3        |            0.52|
| Try two(300)       |        4        |            0.46|
| Try three(500)     |        5        |            0.58|
| Try four(700)      |        5        |            0.51|
| Try five(900)      |        7        |            0.48|

As you can see here, the max bucket size is increasing ever so slowly, and that is to be expected with such a large array of words, some words are bound to have the same hash value. The zero bucket ratio is fluctuating though. This is because everytime we rehash, we get many empty buckets in our list. So The zero bucket ratio stays fluctuating.

* Explain how max depth and leaf count can be used to evaluate the efficiency of the BstMap. What are optimal/reasonable/poor values in both cases?


The efficiency of a binary search tree depends ofcourse how its built and the insertion order of the keys or values. A balanced search tree is the most efficient tree, a tree that is built to be filled at each level and that has as low of a depth as possible. So if we got an array  The more leaf nodes the better. That is because the less levels there are in a binary tree, the faster it takes to search trough it. That is why a large maximum depth is not as time efficient as a balanced tree. 
A balanced tree has the same depth on the left and right side of the tree. So that would be the optimal value for max depth. A value that stays true for both the left and right side of the tree. Of course that is unelikely to happen in real binary trees. An unreasonable value is a tree with a very large max depth value. This is because it will take the tree more recursions to find the word its looking for. And for a resonable/normal value, i tried working with binary trees in ```test.py``` to try out different starigies. 

I created a list to keep track of the values and to check what the normal output for a randomized list of strings is. The first 5 tries i created a list with 10 different words and created a loop that took out a random word from the list and put it into a binary map. i Looped that around 20 times per session and the results i got were pretty similar.
```python
words = ["Abraham", "Corey", "Ella", "Gray", "James", "Lorry", "Night", "Porrige", "Ramsay", "Ulric"]
for l in range(20):
    lord = random.choice(words)
    map.put(lord, 1)

```

|     Tries     | Max depth       | Leaf count    |
|:------------- |:---------------:| -------------:|
| Try one       |        4        |              3|
| Try two       |        4        |              3|
| Try three     |        3        |              3|
| Try four      |        4        |              2|
| Try five      |        4        |              4|

As you can see, the first five tries similar. The max depth is slightly higher than the leaf count because of the small word choice and small tree size. But now im increasing the word sample size by grabbing ```life_of_brian's``` words. Now that our word list is much larger the differences are also bigger. So for each try in the next five tries, i will increase the word size by 10. Try 6 = 30 words, try 7 = 40 words and so on.
```python
word = open(file, 'r', encoding="utf-8")
words = []
words.extend(word)
for l in range(70):
    lord = random.choice(words)
    map.put(lord, 1)
```

|     Tries     | Max depth       | Leaf count    |
|:------------- |:---------------:| -------------:|
| Try six(30)   |        9        |             10|
| Try seven(40) |       10        |             12|
| Try eight(50) |       10        |             15|
| Try nine(60)  |       11        |             19|
| Try ten(70)   |       10        |             21|

So the reasonable values for max depth and count leaves differs depending on the list size and words available. But normally, a smaller list with a smaller list index equals larger max depth and smaller count leaves while a larger list with a larger selection of words equals a larger leaf count and smaller maximum depth.


## Project conclusions and lessons learned

In summary, the project is about algorithms and data structures. In this project we have solved three tasks and we have mainly used HashSet and BST. The lessons learned due to the project are the different algorithm techniques and what is HashSet and BST, plus how to use them in python. Also, this project made it easy for us to understand Python classes

### Technical issues 
The most time consuming part by far was the BST map and understanding what hashing and hash values are. Binary search trees were a whole new experience from anything we've encountered before. This was a structured way to store information like we havent seen before in programming. Working on it without having the faintest idea how they work was not an option. We had to thoroughly research about the subjects and how they worked. The more we read, the more complicated it was.
### Bst
But once we learned about recursive functions everything became clearer. Working with recursive methots simplified our learning experience with BST maps quite significantly. Also it became much more fun. So Id say working with binary search trees when we had no idea what it was in the beginning was the most difficult part of the project.
### Hashing
For hashing we did not have such luck. It took a very long time to actually understand how to get the hash value of a string. We learnt about ASCII and ord(). If we took the time to prematurely ask about hashing during the first few laboratories it wouldve taken us much less time to complete.

The most important lesson is most likely not to look at code as an explanation, but just a watered down solution. For example, reading code about recursive methods did not help me at all. I was just as confused as i was coming into it. 
Reading and understanding what im working with fundamentally helped way more in my work. Looking at code does not do anything to teach us how it works, just what the solution COULD be. And we did not like that so researching how it fundamentally worked was the best decision we made. And we're sure to bring that with us in later studies aswell. Looking at solutions does not teach us anything, but understanding the methods and how it fundamentally works teaches us quite a lot.

The results would probably be cleaner if we had more time. Easier to read code, more time efficient and all in all better code. Of course you dont always have time but in this hypothetical scenario, i would probably say the outcome wouldve been a cleaner result.



### Project issues
We communicated every day or every other day. We were very active on telling eachother how far we've gotten and what we've done and implemented.

- For each individual team member: 
Contributors and co-contributors?
Abdul was the main contributor for the BST maps and part 3 while Sedra was the main contributor for the hashing and part 1. Of course we both worked on everything together but we tried splitting up the work in the beginning. Every update time we talked we explained what we implemented and what didn’t work. And we tried solving it.
Estimate hours spend each week (on average)
About 3 hours every day so around 21 hours per week.(Abdul)
For me it took me around 20 hours each week. (Sedra)
What lessons have you learned? What should you have done differently if you now were facing a similar project.
As stated before, reading thouroughly about the subject is a great help. So I’ll be sure to bring that with me going forward in other projects. (Abdul)
If I’m facing a similar project, I would use every lab opportunity to get help on what I’m stuck on like git and the hash function. (Sedra)




* What lessons have you learned?
 As stated before, reading thouroughly about the subject is a great help. So ill be sure to bring that with me going forward in other projects. 

