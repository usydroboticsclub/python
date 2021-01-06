# A dictionary in real life allows you to look up the meaning of a word. 
# For example, 'cat' means 'a small domesticated creature'. In python, if 
# you want to do so, you can use a dictionary.

meaningDictionary = {}
sizeDictionary = {}

meaningDictionary["apple"] = "A fruit"
sizeDictionary["apple"] = 5

meaningDictionary["cabbage"] = "A vegetable"
sizeDictionary["cabbage"] = 10

meaningDictionary["tomato"] = "Widely contested"
sizeDictionary["tomato"] = 5

print("Tomato means "+ meaningDictionary["tomato"])

print("What would you like to look up?")
query = input()
print("The size of " + query + " is "+ str(sizeDictionary[query]))
