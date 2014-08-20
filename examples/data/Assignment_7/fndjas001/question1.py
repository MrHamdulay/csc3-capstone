"""A program to take in a list and print out a new list with no duplicates
Jason Findlay
30/04/2014"""

word=input("Enter strings (end with DONE):\n")
word_lst=[]
word_lst2=[]

#Populate list of words
while word!="DONE":
    word_lst.append(word)
    word=input()

#Populate new list of words with no repetition
for i in word_lst:
    if not i in word_lst2:
        word_lst2.append(i)
        
#Print output
print()
print("Unique list:")
for i in word_lst2:
    print(i)
