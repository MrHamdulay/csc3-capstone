"""Tofunmi Olagoke
OLGMOF001
23rd April 2014
Printing the right alignment"""

def main():
    #entering strings"
    y=print('Enter strings (end with DONE):')
    names= []
    
    #adding the input into a list
    while True:
        inp=input('')
        names= names+[inp]
     
    #sentinel "DONE"
        if inp=="DONE":
            break
        
    #moves the input to the right 
    length=[]
    for i in names[0:-1]:
        y=len(i)
        length = length+[y]   
        
    #printing the output
    print()
    print("Right-aligned list:")    
    
    for i in names[0:-1]:
        print(" "*((max(length))-(len(i)))+i)

    
main()