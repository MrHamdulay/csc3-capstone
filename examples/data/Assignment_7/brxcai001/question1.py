#Program where the user can enter a list of strings and these strings are then printed in the same order but without duplicates.
#BRXCAI001
#2 MAY 2014



#Create an empty list.
strings = []

#Get a list of strings that stops getting strings when DONE is enetered.
string = input("Enter strings (end with DONE):\n")

while string != "DONE":
    strings.append(string)
    string = input("")

#Create a new empty list.
new_list = ''

#Print space before "unique list" title.
print()

#Print title before loop.
print("Unique list:")

#Print the strings from the first list in the second list but only if they have not already been printed.
for string in strings:
    if string not in new_list:
        print(string)
        new_list = new_list + string 
    
    

        
    
        
        
    
        
   

