"""Tofunmi Olagoke
29 April 2014
Programme that removes dupicate inputs"""

def main():
    #entering strings"
    y=print('Enter strings (end with DONE):')
    words= []
    
    #adding the input into a list
    while True:
        inp=input('')
        words= words+[inp]
     
    #sentinel "DONE"
        if inp=="DONE":
            break
        
    #moves the input to the right 
    newlist=[]
    for i in words[0:-1]:
        if i not in newlist:
            newlist=newlist+[i]
    print()
    print("Unique list:")        
    for x in newlist:
        print (x)
main()