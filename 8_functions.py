# Sometimes a problem may be too big to do in one go. If so, you may want to 
# break it into chunks. To do this, you can use functions.

def printNnumbers(n):
  temp = 0
  stringOut=""
  while (temp<n):
    stringOut = stringOut + str(temp)
    temp=temp+1
  print (stringOut)

print ("Let's make a triangle! Input size:")
size=int(input())
temp=0
while (temp<size):
  printNnumbers(temp)
  temp=temp+1

# Functions are also useful because:
# - You can copy functions between programs without changing them, so you 
# don't have to type up the functions each time
# - You can use other people's functions without typing them up or 
# understanding the nitty gritty of how they work

# You may have noticed that I've used `temp` twice. The outside `temp` is 
# different from the inside `temp`, because remember we want the function to 
# behave the same way regardless of what environment it's in, so the inside 
# `temp` is separate from the outside `temp`. This is called the `scope` 
# of the variable.