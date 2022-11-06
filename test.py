import BstMap as bst
import random
map = bst.BstMap()
words = ["Abraham", "Corey", "Ella", "Gray", "James", "Lorry", "Night", "Porrige", "Ramsay", "Ulric"]
for l in range(20):
    lord = random.choice(words)
    map.put(lord, 1)

print(map.max_depth())
print(map.count_leafs())