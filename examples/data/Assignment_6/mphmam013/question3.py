"""assignment 6
question 3
21 april 2014
Mphuthi Mamorena"""

print("Independent Electoral Commission")
print("-"*32)

lists=[]
stringlist=input('Enter the names of parties (terminated by DONE):\n')
while stringlist!='DONE':
    lists.append(stringlist)
    stringlist=input()#getting a list

print()
print("Vote counts:")


dictionary={}# making a dictionary
if len(lists)!=0:
    for i in lists:
        number=lists.count(i)# counting the number of occurences in a list
        dictionary[i]=number# adding the item in a list to a dictionary  and i is the key

    for party in sorted(dictionary.keys()):
        space=10-(len(party)-1)
        print(party+' '*space+'-',dictionary[party])
    
        