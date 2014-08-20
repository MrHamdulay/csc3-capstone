"""Assignment 6
question 1
20 april 2014
Mphuthi Mamorena"""

# getting a list from a user
list=[]
stringlist=input('Enter strings (end with DONE):\n')
while stringlist!='DONE':
    list.append(stringlist)
    stringlist=input()
print()
    
# FIND THE LENGTH OF THE longest string

maxlength=0
for i in range(len(list)):
    if len(list[i])>maxlength:
        maxlength=len(list[i])

    
# list to print as a column 
print("Right-aligned list:")
if len(list)!=0:
    for i in list:
        print("{0:>{1}}".format(i,maxlength))
