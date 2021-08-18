# A dictionary in real life allows you to look up the meaning of a word. 
# For example, 'cat' means 'a small domesticated creature'. In python, if 
# you want to do so, you can use a dictionary.

meaningDictionary = {}
sizeDictionary = {}

meaningDictionary["roof"] = "the top covering of a building"
sizeDictionary["roof"] = 10000000

meaningDictionary["bookshelf"] = "a shelf on which books can be stored"
sizeDictionary["bookshelf"] = 0.5

meaningDictionary["painting"] = "a painted picture"
sizeDictionary["painting"] = 23.45

print("What would you like to look up? Choose between roof, bookshelf or painting.")
query = input()
print("The meaning of " + query + " is: "+ str(meaningDictionary[query]) + ", and its size is: " + str(sizeDictionary[query]))
