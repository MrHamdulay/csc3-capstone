#Assignment 6 - Question 1
#Right-alignment of a list of strings
#Author: Aidan de Nobrega DNBAID001
#19/04/2014

list_of_strings = []

stringinput = input("Enter strings (end with DONE):\n")
while stringinput != "DONE": #sentinel - not included in list
    list_of_strings.append(stringinput)   
    stringinput = input() #prompted to add strings until sentinel

print("\nRight-aligned list:")
    
longest_string = 0
for string in list_of_strings:
    if len(string) > longest_string: 
        longest_string = len(string) #finds longest string
    
for string in list_of_strings:
        diff = longest_string - len(string) #calculates number of spaces
        print (" "*diff + string) #right-aligns according to longest
        
    

  
    
    