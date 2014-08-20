"""Shriya Roy
2 May 2014
program to get a unique list of numbers without repetition"""


def main():
    #inital empty lists
    strings=[]
    unique=[]
    #getting input from user
    y=input("Enter strings (end with DONE): \n")
    while y!="DONE":
        strings.append(y)
        y=input("")
    print()  
    print("Unique list:")
    for i in range(len(strings)):
         #if the strings are not in the list, append it to a new list
        if not strings[i] in unique:
            unique.append(strings[i])
            
        else: 
            continue
        #printing the list 
    for i in range (len(unique)):
        print (unique[i])
        
        
main()
        
            
            
    
    