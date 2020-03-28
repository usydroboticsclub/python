# python
## 1 What is python?
Python is a programming language. You write code files, and then you can run the code files, and they'll do what you told them to do.

Just like Word reads `.docx` files, Python reads `.py` files; except instead of containing your essay, `.py` files contain instructions that tell Python what you want it to do.

## 2 Installing python
If you want to install python, then go to the python website: https://www.python.org/downloads/

This tutorial was made so that you wouldn't have to install python yourself; but if you want to learn how to install packages, you'll need to install python anyway. So we recommend that you do go and install python sometime soon!

For now, let's use this online python version here: https://repl.it/languages/python3

## 3 Hello world!
Let's start with a programmer's classic: Hello World! Type this into the python script window on the LEFT:
```python
print("Hello world!")
```
Now press run up the top. You should see the window on the right (the output window) say "Hello world!" 
## 4 Variables in python
You can also print other things, like numbers:
```python
print (5)
print (2+7)
print (33*4)
```
But python can help you do much more than just calculator work. To do this, it needs to be able to remember things. Let's look at an example:

```python
print("Type a number:")
num1 = input()

print("Type another number:")
num2 = input()

print("The sum is:")
print(num1+num2)
```

Now hit run. On the window on the right, you should be prompted to enter two numbers. See if the program works as you'd expect.

So what did we do here? We asked python to remember two numbers that we typed in, and then add them. Now you can run this program multiple times without changing the code, and it'll run just fine. 

## 5 Control structures in python
Now we've figured out how to get our program to do one thing. But sometimes you want your program to do multiple things. For example:
```python
print("Type a number:")
num1 = input()

if (num1 == 5):
  print("You typed 5!")
else:
  print ("You didn't type 5!")
```
Using this `if`, you've steered your program down one set of commands if `num1` is 5, and a different set of commands if `num1` is not 5. Since you're controlling your program's flow, statements like `if` are called **control structures**.

What other control structures can we use? Here's another one:
```python
print("Type a number:")
num1 = input()

while (num1>0):
  print (num1)
  num1 = num1 - 1

print ("blastoff!")
```
Guess what this program is going to do? Run it, I'll let you find out.

Notice that in python, you need to push forward (a.k.a. indent) the commands that are inside of your control structures, so that python knows which commands are affected by the control structure and which ones arent.

Using these control structures you can make very complicated things. 
## 6 Lists in python
Say we want to store a lot of numbers at a time. We could use a lot of variables:
```python
print ("Input number 1:")
var1 = input()

print ("Input number 2:")
var2 = input()

print ("Input number 3:")
var3 = input()

print ("Input number 4:")
var4 = input()
```
You can see how it's getting a little tedious. Instead, we can create a list of variables under the same name to do the same thing:
```python
listOfNumbers=[]
currentPosition=0
while currentPosition>10:
  print ("Input number "+str(currentPosition)+":")
  listOfNumbers[currentPosition] = input()
  currentPosition=currentPosition+1
print ("Numbers in reverse order:")

while currentPosition>0:
  currentPosition=currentPosition-1
  print(listOfNumbers[currentPosition])
 
```
(You may hear other programmers calling this an 'array'. Python likes to call it a List. I usually call these things arrays. But this is a python tutorial so I'm going easy on you.)

Also, you may have noticed that we started from 0 instead of 1 when we were considering our list. This is because in most real programming languages, arrays/lists start at 0.

## 7 Types in python
Different variables can have different types. For example:
```python
p=5
print (type(p))

p=2.5
print(type(p))

p="hello world"
print(type(p))

p=[]
print(type(p))
```
This concept is important because sometimes when performing operations, you may not get the results you want. For example, try these, one line at a time:
```python
print (5+5)

print ("5"+"5")

print ("5"+5)

print(20/5)

print (2/5)

print (2.0/5)
```
You can also convert between types if necessary.
```python
print("5"+5)
print("5"+str(5))
print(int("5")+5)
```

## 8 Dictionaries in python
A dictionary in real life allows you to look up the meaning of a word. For example, 'cat' means 'a small domesticated creature'. In python, if you want to do so, you can use a dictionary.
```python
meaningDictionary={}
sizeDictionary={}

meaningDictionary["apple"] = "A fruit"
sizeDictionary["apple"] = 5

meaningDictionary["cabbage"] = "A vegetable"
sizeDictionary["cabbage"] = 10

meaningDictionary["tomato"] = "Widely contested"
sizeDictionary["tomato"] = 5

print("Tomato means "+ meaningDictionary["tomato"])

print("What would you like to look up?")
query = input()
print("The size of " + query + " is "+ str(sizeDictionary["tomato"]))
```

## 9 Functions in python
Sometimes a problem may be too big to do in one go. If so, you may want to break it into chunks. To do this, you can use functions.

```python
def printNnumbers(n):
  temp = 0
  stringOut=""
  while (temp<n):
    stringOut = stringOut + str(temp)
    temp=temp+1
  print (stringOut)

print ("Let's make a triangle! Input size:")
size=input()
temp=0
while (temp<size):
  printNnumbers(temp)
  temp=temp+1
```
Functions are also useful because:
- You can copy functions between programs without changing them, so you don't have to type up the functions each time
- You can use other people's functions without typing them up or understanding the nitty gritty of how they work

You may have noticed that I've used `temp` twice. The outside `temp` is different from the inside `temp`, because remember we want the function to behave the same way regardless of what environment it's in, so the inside `temp` is separate from the outside `temp`. This is called the `scope` of the variable.
## 10 Classes in python
Say we wanted to represent a more complex object in python. For example, a cat:
```python
class cat:
  def __init__(self):
      self.size=40
      self.color="blue"
      self.breed="persian"
  def meow(self):
      print ("meow! I am a " + self.color + ", " + self.breed + " cat.")

molly = cat()
jesse = cat()

print(molly.size)
jesse.breed = "tabby"
print(molly.breed)

molly.meow()
jesse.meow()
```

We use classes because it allows us to store a variety of related data and functions under a single variable. This is a pattern of thinking called 'object-oriented' programming. It may not be relevant for all problems, but like functions, it is useful for breaking problems down or classifying complicated objects. 

Many people use object-oriented programming, so it's useful to learn what it looks like when you're coding with it.

## 11 Libraries in python
We don't have to re-code everything from scratch when there are plenty of programmers around and the cost of copying code is second-to-none. For convenience's sake, people provide work they've already done as libraries of functions.

To use other peoples' libraries, we need to tell our code to care about them. It doesn't automatically care about every library because there are a lot of libraries out there. Let's use the `math` library, which contains some useful functions:

```python
import math

print(math.cos(math.pi/2))
print(math.sin(math.pi/6))
```
If you tried the last two commands without the preceding `import math`, you would likely get an error like this:
```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'math' is not defined
```
So if you need to use a library, make sure to `import` it!

## 10 Go conquer the world!
I hope we've made clear some fundamental concepts in programming for you to consider. Programming is immensely useful for creating the behaviours required in robotics; so this will be a useful first step. 

If you want extra practice, why not try and code the following things:
- A program that outputs triangular numbers
- A program that outputs prime numbers
- A program that simulates a projectile's motion
- A program that tells you the time

Happy coding!


