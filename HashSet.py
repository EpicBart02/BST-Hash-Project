
from dataclasses import dataclass
from typing import List


@dataclass
class HashSet:
    buckets: List[List] = None
    size: int = 0

    def init(self):
        self.size = 0
        self.buckets = [[] for i in range(8)] #Create the initial buckets

    # Computes hash value for a word (a string)
    def get_hash(self, word):
        return (sum([ord(c) for c in word]) % self.bucket_list_size())  #Return the hash of the word % the bucket sizr

    # Doubles size of bucket list
    def rehash(self):
        temp_buckets = self.buckets #Save the old buckets so they dont get deleted
        self.buckets = [[] for i in range(self.bucket_list_size() *2)] #Create buckets double the len of the previous one
        self.size = 0
        for bucket in temp_buckets:   #re-add the old buckets
            for word in bucket:
                self.add(word)

    # Adds a word to set if not already added
    def add(self, word):
        hash_value = self.get_hash(word)
        if word not in self.buckets[hash_value]:    #If the word isnt in the buckets, put it in
            self.buckets[hash_value].append(word)
            self.size += 1
        if self.size == self.bucket_list_size(): #If the bucket is full, rehash
            self.rehash()

    # Returns all elements of the set in a list
    def to_list(self):
        return sum(self.buckets, [])  #Self explanitory

    # Returns a string representation of the set content
    def to_string(self):
        return "{ " + " ".join(self.to_list()) + " }" 

    # Returns current number of elements in set
    def get_size(self):
        return self.size

    # Returns True if word in set, otherwise False
    def contains(self, word):
        return word in self.buckets[self.get_hash(word)]

    # Returns current size of bucket list
    def bucket_list_size(self):
        return len(self.buckets)

    # Removes word from set if there, does nothing
    # if word not in set
    def remove(self, word):
        hash_value = self.get_hash(word)
        if word in self.buckets[hash_value]: #Removing the word if its in the bucket
            self.buckets[hash_value].remove(word)
            self.size -= 1  #Decreasing the self.size by one since we removed it from the bucket

    # Returns the size of the bucket with most elements
    def max_bucket_size(self):
        return max([len(bucket) for bucket in self.buckets])

    # Returns the ratio of buckets of lenght zero.
    # That is: number of zero buckets divided by number of buckets
    def zero_bucket_ratio(self):
        return self.buckets.count([]) / self.bucket_list_size()