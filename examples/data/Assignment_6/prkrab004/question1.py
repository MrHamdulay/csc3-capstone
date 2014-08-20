#Assignment 6
#Question 1
#Rabia Parker
#Due Date: 25/04/14

#Creating a program to print a list of strings that is right-aligned with the longest string.


def list_string():
    List=[]
    string=input("Enter strings (end with DONE):\n")
    while string != 'DONE':
        List.append(string)
        string=input()
    
    longest=0
    for i in range(len(List)):
        if len(List[i]) > longest:
            longest = len(List[i])
       
    print("")
    print("Right-aligned list:")
    for j in List:
        j=j.rjust(longest)
        print(j)
    
        
    
    
list_string()

    
            