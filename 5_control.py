# Now we've figured out how to get our program to do one thing. But sometimes
# you want your program to do multiple things. For example:

print("Type a number:")
num1 = int(input())

if (num1 < 25):
  print("Your number is less than 25")
else:
  print("Your number is greater or equal to 25")

# Using this `if`, you've steered your program down one set of commands if 
# `num1` is 5, and a different set of commands if `num1` is not 5. Since 
# you're controlling your program's flow, statements like `if` are called 
# 'control structures'.

# What other control structures can we use? Here's another one:
print("Type a number:")
num1 = int(input())
print("Okay, let's see who can count to {} first! Ready?".format(num1))
print("Type Y to start.")
answer = input()

num2 = 0

if (answer == "Y"):

  while (num2 <= num1):
    print(num2)
    num2 = num2 + 1

  print("Beat you!")

else:

  print("You fool! Type Y next time.")

# Guess what this program is going to do? Run it, I'll let you find out.

# Notice that in python, you need to push forward (a.k.a. indent) the commands
# that are inside of your control structures, so that python knows which 
# commands are affected by the control structure and which ones arent.

# Using these control structures you can make very complicated things. 