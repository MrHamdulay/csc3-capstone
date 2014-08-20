#A program that allows a user to enter a list of names and right-algn the longest  string
#Thembekani Gwegwana
#April 2014
def namess():
    names=[]#Creating a list called name
    maximum=0
    list_names=''
    list_names=input("Enter strings (end with DONE):\n")
    while list_names !='DONE':
        names.append(list_names) #Adding strings to the list
        list_names=input('')
    for i in range (len(names)):
        if len(names[i])> maximum :
            maximum=(len(names[i]))
    print()
    print('Right-aligned list:')

    for i in names:   
        print(' '*(maximum-(len(i))),i,sep='')
namess()        
    