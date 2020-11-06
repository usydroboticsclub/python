# If someone asked you to add '5' and 'potato', you'd probably get confused.
# In computing, this concept is called types. Different variables can have 
# different types. For example:

p=5
print (type(p))

p=2.5
print(type(p))

p="hello world"
print(type(p))

p=[]
print(type(p))

# This concept is important because sometimes when performing operations, 
# you may not get the results you want. For example, try these, one line 
# at a time, by un-commenting them (remove the #):

# print (5+5)
# print ("5"+"5")
# print ("5"+5)
# print(20/5)
# print (2/5)
# print (2.0/5)

# You can also convert between types if necessary.

# print("5"+5)
# print("5"+str(5))
# print(int("5")+5)