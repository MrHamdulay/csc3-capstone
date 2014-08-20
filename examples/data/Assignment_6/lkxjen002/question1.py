#A program that prints out a right-aligned list
#Created by: Jenna Lake
#Date: 25/04/2014

def align():
    list=[]
    t=True
    count=0
    c=input("Enter strings (end with DONE):\n")
    while t:
        if c=='DONE':
            break           #breaks out of the loop only in the sentinal 'DONE' is inputed
        else:
            list.append(c)  # add each new inputed string to the list
        count+=1
        c=input()
    x=0
    for i in list:
        if len(i)>x:
            x=len(i)        #finds the length of the longest word in the list
    newlist=[]
    for i in list:
        b=len(i)
        if b<x:
            diff=x-b        #checks for difference in length between i and longest and replaces the difference with blank-space
            newlist.append(" "*diff+i) #appends each new word(including blankspace) to a new list
        else:
            newlist.append(i)
    print("\nRight-aligned list:")
    for i in newlist:
        print(i)
align()
    
