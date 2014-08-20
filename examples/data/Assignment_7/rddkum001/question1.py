""" To create a unique list
Kumaran Reddy
30 April 2014 """

Word=input("Enter strings (end with DONE):\n")
Words=[]
while Word != "DONE": #To get the list of words
    Words.append(Word)
    Word=input('')
UList=[] #Create new list to allow for alteration
for i in Words:
    if i in UList:
        continue #To skip the word if it already exists
    else:
        UList.append(i)
print(' ')
print("Unique list:")
for i in UList:
    print(i)