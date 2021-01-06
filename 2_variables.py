# To get python to remember things for us, we need to give things names.
# For example, say we want to find the total price of some cabbages and apples:
cabbagePrice = 10.05
cabbageAmount = 200
grandTotal = cabbagePrice * cabbageAmount

applePrice = 13.20
appleAmount = 342
grandTotal = grandTotal + (applePrice * appleAmount)
print("The grand total is {}".format(grandTotal))
# Here, we're still performing a simple multiplication, but you as the 
# programmer have a better understanding of what the code is trying to do.
# However, if you wanted to save time, you can call your variables whatever 
# you want. The following code does the same job:

cp = 10.05
ca = 200
gt = cp * ca

ap = 13.20
aa = 342
gt = gt + (ap * aa)
print("The grand total is {}".format(gt))

# But if you were genuinely adding apples and cabbages, and you want to show 
# your code to someone else, then the first example is much more readable. 
# Code is shared a lot around the internet so good variable names makes 
# sure everyone (including future you!) can read the code and understand 
# it too!
