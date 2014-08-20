"""Program to print out a list of strings right aligned
By JP Lanser
19 April 2014"""

#Prompt user for first string

string = input("Enter strings (end with DONE):\n")

#Set first string as the longest one

longest_string = len(string) 
#Create an empty list and add strings entered by the user to it
list_of_strings = []

#Use loop to keep prompting user for more strings until "DONE" is entered
while not string == "DONE":   
    if len(string) > longest_string:  #If the user enters a string that is longer than the current longest one then set this new one as longest 
        longest_string = len(string)
    list_of_strings.append(string) #Add the string to the list
    string = input()
    
    

print()
print("Right-aligned list:")
    #loop through the list and print all of the strings
for i in list_of_strings:
    print(" "*(longest_string - len(i)) , end="") #If the current string is shorter than the longest, print a certain number of spaces equal to the difference between the length of the longest and the current one. This will make sure that it is right aligned. 
    print(i)
       
        
        
        



