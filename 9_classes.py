# Say we wanted to represent a more complex object in python. For example, a 
# cat:

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

# We use classes because it allows us to store a variety of related data and 
# functions under a single variable. This is a pattern of thinking called 
# 'object-oriented' programming. It may not be relevant for all problems, 
# but like functions, it is useful for breaking problems down or classifying 
# complicated objects. 

# Many people use object-oriented programming, so it's useful to learn what 
# it looks like when you're coding with it.
