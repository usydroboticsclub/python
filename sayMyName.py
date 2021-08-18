name = input("Please enter your name: ")
SID = input("Please enter your SID: ")

firstTwoDigits = int(SID[0] + SID[1])

for i in range(firstTwoDigits):
    print(name)
    
    # This line can be used to check the number of times is correct
    # print("Iteration ", i+1)