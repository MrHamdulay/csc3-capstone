#Author: NLXALE001
#Date: 30 April 2014
#Assignment 7


print ("Enter strings (end with DONE):\n")
word = ""
unique = []
while word != "DONE":
    word = input("")
    if word not in unique:
        unique.append(word)
print ("Unique list:")
for i in range (0, len(unique)-1):
    print (unique[i])