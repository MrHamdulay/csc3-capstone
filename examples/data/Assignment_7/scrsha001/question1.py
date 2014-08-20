#Shaaheen Sacoor SCRSHA001
#27 April 2014
#Program to enter a list of items and have a unique list printed

def main():
    strings = input("Enter strings (end with DONE):\n")
    EnteredList =[] #Empty list
    while strings !="DONE":
        EnteredList.append(strings) #Adding strings to list
        strings = input("")
    print("\nUnique list:")
    repeats= [] #List for all repeated strings
    for i in range(len(EnteredList)): #Goes through list(EnteredList)
        if EnteredList[i] in repeats:
            print("",end="") #If string has already been accounted for then print nothing
        else:
            print(EnteredList[i]) # else print the string
        repeats.append(EnteredList[i]) #Adds to repeat list so it won't be used again
main()
    
    
        