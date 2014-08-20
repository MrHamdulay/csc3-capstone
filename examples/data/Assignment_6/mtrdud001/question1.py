"""Left aligning words input by the user
Dudley Mutero
4/24/14"""

def calculating():#this functions calculates the word with the biggest number of characters and stores it for alignment purposes
    listwords=[]
    c=0    #number of letters in the longest string
    print ("Enter strings (end with DONE):\n")
    a="start"
    while a != "DONE": #loop to continue collecting data from user till "DONE"
        a=input()    
        if a != "DONE": 
            listwords.append(a)
        b=0 
        d=len(a) #checking word length is greater than the global longest word
        if d>c:
            c=d
            
    print ("Right-aligned list:")
    for i in  listwords: #printing right alligned
        print (" "*(c-len(i)),i,sep="")
calculating()
        