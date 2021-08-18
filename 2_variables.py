# To get python to remember things for us, we need to give things names.
# For example, say we want to find the total price of some cabbages and apples:
cucumberPrice = 2.25
cucumberAmount = 350
GST = 1.1
grandTotal = cucumberPrice * cucumberAmount * GST

mandarinPrice = 1.15
mandarinAmount = 675
grandTotal = grandTotal + (mandarinPrice * mandarinAmount * GST)
print("The grand total is {}".format(grandTotal))
# Here, we're still performing a simple multiplication, but you as the 
# programmer have a better understanding of what the code is trying to do.
# However, if you wanted to save time, you can call your variables whatever 
# you want. The following code does the same job:

cp = 2.25
ca = 350
GST = 1.1
gt = cp * ca * GST

mp = 1.15
ma = 675
gt = gt + (mp * ma * GST)
print("The grand total is {}".format(gt))

# But if you were genuinely adding apples and cabbages, and you want to show 
# your code to someone else, then the first example is much more readable. 
# Code is shared a lot around the internet so good variable names makes 
# sure everyone (including future you!) can read the code and understand 
# it too!
