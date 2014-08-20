#Assignment6 Question1
#List of strings aligned to the right
#Carissa Moodley

def main():
    #creating an empty list to store list of strings
    listofstrings=[]
    
    #prompting the user to input strings
    strings=input("Enter strings (end with DONE):\n")
    
    maxlength=0
    
    while strings!="DONE":
        
        #determine longest string
        if len(strings)>maxlength:
            maxlength=len(strings)
            
        #add string to list
        listofstrings.append(strings)
        strings=input()
        
    print()
    print("Right-aligned list:")    
    for i in (listofstrings):
        #right-align the list of strings
        print(i.rjust(maxlength))


main()
    