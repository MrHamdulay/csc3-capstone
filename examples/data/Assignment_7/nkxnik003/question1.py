#Nikhil Jiten Naik
#NKXNIK003
#ComSci Assignment 7
#Question 1
#02/05/2014

def list_new():

    print("Enter strings (end with DONE):") #Enter an array
    entries = input()
    listEntries = [] 
    while entries != "DONE":
        listEntries.append(entries)
        entries = input()
    
    newList = []            
    for i in listEntries:       #Takes out entries which are duplicates
        if i not in newList:
            newList.append(i)
            
    print("\nUnique list:") #Prints the new List with no duplicates
    for i in newList:
        print(i)
        
if __name__=="__main__":
    list_new()