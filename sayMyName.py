#This program prints out your name N times, where N is the first 2 digits of your SID
import math

name = input("Your name: ")
SID = input("Your SID: ")

length_of_SID = len(SID)
first_two_digits_SID = int(SID)//(pow(10,length_of_SID - 2))

for i in range(first_two_digits_SID):
    print(name)
