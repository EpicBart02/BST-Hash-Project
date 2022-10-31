from dataclasses import dataclass
from turtle import right
from typing import Any


# The BstMap class is a binary search tree based implementation of
# a map (or dictionary). It works for any type of values and for
# all types keys that are comparable ==> we can compare keys using
# the operators < and >.


# The Node class is responsible for most of the work.
# Each call to the BstMap class is just delegated to the
# root node which starts a recursive sequence of calls to
# handle the request. Notice: All Node methods are recursive.
@dataclass
class Node:
    key: Any = None         # the key
    value: Any = None       # the value
    left: Any = None        # left child (a Node)
    right: Any = None       # right child (a Node)

    def put(self, key, value):

        if key < self.key:
            if self.left == None:
                self.left = Node(key, value)   #If it reaches an empty node, it creates a node with the input key and value
            else:
                self.left.put(key, value)    #If the node isnt empty, the key moves down and restarts until it finds an empty node
        elif key > self.key:#The same thing but in the right side of the tree 
            if self.right == None:
                self.right = Node(key, value)
            else:
                self.right.put(key, value)
        if key == self.key:                 #If the key is the same, override the current value with the input value
           self.value = self.value + 1


    def to_string(self):
        this_node = ""     #Create an empty string to hold the data
        if self.left is not None:
            this_node += self.left.to_string()                       #Take the left most node
        this_node += "(" + self.key + ","  + str(self.value) + ")"   #Add it to the string
        if self.right is not None:
                this_node += self.right.to_string()   #Take the right node and go back to
        return this_node                              #the start and check if it has a left node

    def count(self):
        count = 1                    #Literally the same as to_string function
        if self.left is not None:    #but instead of adding key and value to a string
            count += self.left.count() #it adds 1 to the counter 
        if self.right is not None:
            count += self.right.count()
        return count

    def get(self, key):
         if key < self.key:
            if self.left == None:     #If the node doesnt exist, return None
                return "None"
            else:
                return self.left.get(key)  #Somewhat same as the last function
         if key > self.key:                #but instead of printing, searches for the key node
            if self.right == None:
                return "None"         #If the node doesnt exist, return None
            else:
                return self.right.get(key)
         if key == self.key:          #If the key found itself in the tree, print its value
            return self.value

    def max_depth(self):
        if self.left is not None:
            left_depth = self.left.max_depth()   #If there is a node, the depth increases depending on how low down the node is in the map
        else:
            left_depth = 0                       
        if self.right is not None:
            right_depth = self.right.max_depth()
        else:
            right_depth = 0
        return max(left_depth, right_depth) + 1       #Print the maximum depth between the two sides of the map, if right is higher
                                                      #it gets printed, vice versa

    def count_leafs(self):
        if self.left == None or self.right == None:
            return 1
        return self.left.count_leafs() + self.right.count_leafs()

    # We do a left-to-right in-order traversal of the tree
    # to get the key-value pairs sorted base on their keys
    def as_list(self, lst):
        node = (self.key, self.value)
        if self.left is not None:
            lst.extend(self.left.as_list([]))
        lst.append(node)
        if self.right is not None:
            lst.extend(self.right.as_list([]))
        return lst
      


# The BstMap class is rather simple. It basically just takes care
# of the case when the map is empty. All other cases are delegated
# to the root node ==> the Node class.
#
# The class below is complete ==> not to be changed
@dataclass
class BstMap:
    root: Node = None

    # Adds a key-value pair to the map
    def put(self, key, value):
        if self.root is None:    # Empty, add first node
            self.root = Node(key, value, None, None)
        else:
            self.root.put(key, value)

    # Returns a string representation of all the key-value pairs
    def to_string(self):
        if self.root is None:     # Empty, return empty brackets
            return "{ }"
        else:
            res = "{ "
            res += self.root.to_string()
            res += "}"
            return res

    # Returns the current number of key-value pairs in the map
    def size(self):
        if self.root is None:
            return 0
        else:
            return self.root.count()

    # Returns the value for a given key. Returns None
    # if key doesn't exist (or map is empty)
    def get(self, key):
        if self.root is None:
            return None
        else:
            return self.root.get(key)

    # Returns the maximum tree depth. That is, the length
    # (counted in nodes) of the longest root-to-leaf path
    def max_depth(self):
        if self.root is None:
            return 0
        else:
            return self.root.max_depth()

    # Returns a leaf node count. That is, the number of nodes 
    # with no children
    def count_leafs(self):
        if self.root is None:
            return 0
        else:
            return self.root.count_leafs()

    # Returns a sorted list of all key-value pairs in the map.
    # Each key-value pair is represented as a tuple and the
    # list is sorted on the keys ==> left-to-right in-order
    def as_list(self):
        lst = []
        if self.root is None:
            return lst
        else:
            return self.root.as_list(lst)
