# A program that takes in a list of strings and removes duplicates
# Retselisitsoe Monyake
# 27 April 2014

# an empty list 
mylist = []
# a function to place strings into the list
def lis():
    n=input("Enter strings (end with DONE):\n")
    while n!="DONE":
        mylist.append(n)
        n=input("")
lis()
print()
# an empty list to record the new list
mylist2=[]
# a function to remove duplications in list
def remov():
    for name in mylist:
        while name not in mylist2:
            mylist2.append(name)
    for i in mylist2:
        print(i)
print("Unique list:")
remov()
