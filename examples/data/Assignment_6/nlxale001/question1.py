#Author:NLXALE001
#Date:22 April 2014
#Assignment 6

#create empty variables and input words into lists
list_of_words = []
current = ""
print ("Enter strings (end with DONE):\n")
while current!="DONE":
    current = input("")
    list_of_words.append(current)

#count to find max length of line
maxi = 0
for i in list_of_words:
    if len(i)>maxi:
        maxi = len(i)

del list_of_words[-1]
space = 0
print ("Right-aligned list:")
for j in list_of_words:
    space = maxi - len(j)
    print (" "*space, j, sep="")