# Now, we don't just want our computer to be able to do preset calculations - 
# we want it to respond to different situations; otherwise we might as well 
# do the maths using just a calculator!

# We can do this using inputs.

print("Type your name:")
name = input()
print("Your name is "+name+". I hope that isn't surprising.")

# Now hit run. On the window on the right, you should be prompted to enter 
# your name. See if the program works as you'd expect.

# A caveat for python is that all inputs are `string` type (`string` is a 
# fancy computer term for 'word'). That means, we need to convert our inputs 
# to numbers if we want to make a calculator.

print("Type a number:")
num1 = int(input())

print("Type another number:")
num2 = int(input())

print("The sum is:")
print(num1+num2)

# So what did we do here? We asked python to remember two numbers that we 
# typed in, and then add them. Now you can run this program multiple times 
# without changing the code, and it'll still produce the sum each time.

