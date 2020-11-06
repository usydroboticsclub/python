# We don't have to re-code everything from scratch when there are plenty of 
# programmers around and the cost of copying code is second-to-none. For 
# convenience's sake, people provide work they've already done as libraries 
# of functions.

# To use other peoples' libraries, we need to tell our code to care about 
# them. It doesn't automatically care about every library because there are 
# a lot of libraries out there. Let's use the `math` library, which contains 
# some useful functions:

import math

print(math.cos(math.pi/2))
print(math.sin(math.pi/6))

# What if we comment out the `import math?` 
# If you tried the last two commands without the preceding `import math`, 
# you would likely get an error like this:

#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#NameError: name 'math' is not defined

# So if you need to use a library, make sure to `import` it!

# We can also import other files we write ourselves as libraries. Check out
# helper.py, and see if you can predict what this code does.

import helper

help_me("now")
