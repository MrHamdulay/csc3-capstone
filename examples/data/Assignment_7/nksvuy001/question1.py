"""program to print out list of strings without any duplicates
vuyolwethu nkosi
27 april 2014"""

def lists():
    #create empty string
    strings=[]
    #get list of strings from user
    string=input("Enter strings (end with DONE):\n")
    #create list
    while string!="DONE":
        strings.append(string)
        string=input("") #allows you to keep adding after pressing enter key
    
    print("\nUnique list:")
        
#create second list and put in the words in the first list but without the duplicate
    mylist=[] #create second list
    for j in strings: #going through list
        if j not in mylist: #if word is not in the list
            print(j) #print the word
            mylist.append(j) #then add this word in my new list
            #therefore if it finds the word in the new list, it will not print it
        #else:
         #   print("\n".join(strings))
lists()