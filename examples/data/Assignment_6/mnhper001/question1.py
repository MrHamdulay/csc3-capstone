#Author:Percival Munhuwaani
#Program:A program that prints the list of strings right-aligned
#Date:24/04/2014

def main():
    list_name=[] #creating a list to store the names as strings
    name=input("Enter strings (end with DONE):\n")
    while name!="DONE": #starting the loop
        list_name.append(name)
        name=input("")
        
    max_length=0 #initializing the strings with  the maximum length
    for name in list_name:
        if len(name)>max_length:
            max_length=len(name)
    print()        
    print("Right-aligned list:")
    for name in list_name: #iterating for every name in the list
        spaces=max_length-len(name)
        print(" "*spaces+name,sep="") #printing out the names right-aligned

main()


        