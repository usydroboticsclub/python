# Say we want to store a lot of numbers at a time. We could use a lot of 
# variables:
print("Input number 1:")
var1 = input()

print("Input number 2:")
var2 = input()

print("Input number 3:")
var3 = input()

print("Input number 4:")
var4 = input()

# You can see how it's getting a little tedious. Instead, we can create a 
# list of variables under the same name to do the same thing:

print("Use a list instead to take input!")
listOfNumbers = []
currentPosition = 1

while (len(listOfNumbers) < 5):
  print("Input number "+str(currentPosition)+":")
  currentPosition = currentPosition + 1
  listOfNumbers.append(input())

# Another advantage of lists is that we can manipulate them in different ways:

print("Numbers in reverse order:")

currentPosition = len(listOfNumbers)
while (currentPosition > 0):
  currentPosition = currentPosition - 1
  print(listOfNumbers[currentPosition])
 
# (You may hear other programmers calling this an 'array'. Python likes to call
# it a List. I usually call these things arrays. But this is a python tutorial 
# so I'm going easy on you.)

# Also, you may have noticed that we started from 0 instead of 1 when we were 
# considering our list. This is because in most _real_ programming languages, 
# arrays/lists start at 0.