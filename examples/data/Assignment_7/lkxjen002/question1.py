#A program that prints only the unique strings in a list
#created by:Jenna Lake
#date:3 May 2014

def get_string():
    list_unsort=[]
    a=True
    count=0
    c=input("Enter strings (end with DONE):\n")
    while a:
        if c=='DONE': #breaks with sentinal done
            break
        else:
            list_unsort.append(c) #appends each new string
        count+=1
        c=input()
        
#def filter_unique():
    newstring=[]
    for i in list_unsort:
        if i not in newstring: # checks if values are in new string, if already in newstring, current string is a duplicate and is ignored
            y=list_unsort.count(i)
            newstring.append(i)
#print_unique():
    print("\nUnique list:")
    for i in newstring:
        print(i)
get_string()