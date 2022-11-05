
### About Markdown

Markdown is an easy-to-use plain text formatting syntax created by John Gruber.

To write a text in Markdown you need a Markdown editor. Fortunately VS Code comes with an easy-to-use Markdown editor. Hence, open a markdown file (.md file) in VS code and press ``preview`` in the upper right corner and you will see the Markdown code side-by-side with a view showing the rendered text.

To get started using Markdown we suggest that you open the file you are currently reading (ProjectTemplate.md), or (better) [this file](https://homepage.lnu.se//staff/jlnmsi/python/2021/Macdown.zip), in a Markdown editor and compare the rendered result with the given markdown code. Then Google various markdown tutorials to understand markdown symbols that are not obvious from the given examples. A few examples:

Python code markup:

```python
def max(a,b):
	if a > b:
		return a
	else:
		return b
```

Inserting images (using HTML markup):

<img src="http://homepage.lnu.se/staff/jlnmsi/python/2020/cos_sin.png" width="400"/>


This is a table with left- , center-, and right-allgned columns:

| Left Aligned  | Center Aligned  | Right Aligned |
|:------------- |:---------------:| -------------:|
| col 3 is      | some wordy text |         $1600 |
| col 2 is      | centered        |           $12 |
| zebra stripes | are neat        |            $1 |

The left- and right-most pipes (`|`) are only aesthetic, and can be omitted. The spaces don’t matter, either. Alignment depends solely on `:` marks in the lines under the column titles.

## Regarding the report template

The template below is in English. Feel free to write your report in Swedish or English. 

We expect each team to present their report as their README.md in the Gitlab repository.

Try to be short and precise. We expect more than 2000, but less than 4000, words. 

Assume that the reader knows about Python. Give a reference and explain techniques introduced that we havn't presented in the course.

In what follow we give you the **mandatory report headlines** and brief comments about what we expect each section to contain. Make sure to remove our comments (and the Markdown intro above) in your final report.


************************

# Mini-project report 
Members: Sedra Altunji and Abdul Rahman Racheed
Program: CTMAT and NGDPV	
Course: 1DT901 and 1DV501
Date of submission: 2022-11-06


## Introduction  

This project, mini-project, is a part of the course 1DT901 and it is a project in algorithms and data structures. In this project, three different tasks are going to be solved. Task 1 is Count unique words 1, in this task the number of unique words will be counted from the files ’life of brain’ and ’swedish_news_2020’ with the help of Python set class. Also, in task 1, the ten most frequently used words having a length larger than 4 in each file have to be produced with the help of Python dictionary class. 
Task 2, Implementing data structures, 
The last task, Count unique words 2

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
- For the hash based word set (HashSet), present (and explain in words):
 	* Python code for function ``add``, how to compute the hash value, and rehashing.
 	* Point out and explain any differences from the given results in ``hash_main.py``
 	
- For the BST based map (BstMap), present (and explain in words):.
Firstly, the code for ``put``, The only way i can explain it is that i based the BST sorting based on the key, the letters. 
[Left side]: If the input key is less then the current key on the Tree, ```if key < self.key:```, it moves LEFT of that current Node. If the space is empty, the list created a new node and put the input key and its value inside of that node. 
```python
if self.left == None:
    self.left = Node(key, value)
```
But if there already was a node in that slot, the input key moves down one space in the Tree and the current key becomes that left node we were talking about earlier, the input key travels down until it finds an empty space it fits in. 
[Right side]: The right side of the tree is essentially the same as the left, but instead of it letting trough lower valued keys, it only lets the keys who are higher then the current key trough. The node travels down the same way as before though. To put it simply, it works exactly same way as the the left side, but takes in the higher values instead of lower values.

The code for ``max_depth`` was not very difficult once you understood the recursive methods of the BST. I recursively go down the tree and grab the value of the current node. Not the value as in key, value, but as in how far down it is in the tree. So each time we move, we grab the node's value.
In the end we ta
* Point out and explain any differences from the given results in ``bst_main.py``.

## Part 3: Count unique words 2

This part was very easily solved by using sort. Firstly i created two methods within the BstMap.py file. top_10 and my_sort. My sort took in a tuple and returned the second element within it. So instead of returning the key, it returned the value.```return t[1]```. after that i sorted all the words from lowest to highest, and reversed the order of the list by using ```reverse=True``` and printed the first 10 elements in the reversed list. the output are the 10 words that came up most frequently in the file.
The code looks something like this
```python
return sorted(self.as_list([]), key=my_sort, reverse=True)[:10]
```
Also in part3.py, i set the minimum len of the word to 5 and over because its not allowed to have words with a len of 4 or less as stated in the project instructions. 

The top 10 most frequent words in Life if brian are, Brian, Centurion, Crowd, Mother, right, Crucifixion, Pilate, pontius, Crowd and Rogers. The output is the same in part 1.

And lastly the top 10 most frequent words in Swe news are as stated: säger, under, kommer, efter, eller, också, andra, finns, sedan and lastly procent. The output is the same in part 1.

* What is the bucket list size, max bucket size and zero bucket ratio for HashSet, and the total node count, max depth and leaf count for BstMap, after having added all the words in the two large word files? (Hence, eight different numbers.)
* Explain how max bucket size and zero bucket ratio can be used to evaluate the quality of your hash function in HashSet. What are optimal/reasonable/poor values in both cases?
* Explain how max depth and leaf count can be used to evaluate the efficiency of the BstMap. What are optimal/reasonable/poor values in both cases?


## Project conclusions and lessons learned
We separate technical issues from project related issues.
### Technical issues 
The most time consuming part by far was the BST map. Binary search trees were a whole new experience from anything we've encountered before. This was a structured way to store information like we havent seen before in programming. Working on it without having the faintest idea how they work was not an option. We had to thoroughly research about binary search trees and how they worked. The more we read, the more complicated it was. But once we learned about recursive functions everything became clearer. Working with recursive methots simplified our learning experience with BST maps quite significantly. Also it became much more fun. So Id say working with binary search trees when we had no idea what it was in the beginning was the most difficult part of the project.

- What lessons have you learned? What should you have done differently if you now were facing a similar problem.
The most important lesson is most likely not to look at code as an explanation, but just a watered down solution. For example, reading code about recursive methods did not help me at all. I was just as confused as i was coming into it. 
Reading and understanding what im working with fundamentally helped way more in my work. Looking at code does not do anything to teach us how it works, just what the solution COULD be. And we did not like that so researching how it fundamentally worked was the best decision we made. And we're sure to bring that with us in later studies aswell. Looking at solutions does not teach us anything, but understanding the methods and how it fundamentally works teaches us quite a lot.

- How could the results be improved if you were given a bit more time to complete the task.
The results would probably be cleaner. Easier to read code, more time efficient and all in all better code. Of course you dont always have time but in this hypothetical scenario, i would probably say the outcome wouldve been a cleaner result.

### Project issues
- Describe how your team organized the work. How did you communicate? How often did you communicate?
We communicated every day or every other day. We were very active on telling eachother how far we've gotten and what we've done and implemented.

- For each individual team member: 
 	* Describe which parts (or subtasks) of the project they were responsible for. Consider writing the report as a separate task. Try to identify main contributors and co-contributors.
	Abdul was the main contributor for the BST maps and part 3 while Sedra was the main contributor for the hashing and part 1. Ofcourse we both worked on everything together but we tried splitting up the work in the beginning. Every update time we talked we explained what we implemented and what didnt work. And we tried solving tj
 	* Estimate hours spend each week (on average)
 - What lessons have you learned? What should you have done differently if you now were facing a similar project.



