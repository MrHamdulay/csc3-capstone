"""program for list of strings
tayla george
29 april 2014"""

print("Enter strings (end with DONE):\n") 
string =input() #getting the list from the user
strings = []
strings.append(string) #adding the strings to the list of strings

while string != "DONE":  #Done used as a sentinel
    string =input()
    strings.append(string)
    
strings.remove("DONE") #removing Done from the list of strings

print("Unique list:")

unique_list =[] 
for i in strings:
    if i not in unique_list: #printing the strings that were not already printed
        unique_list.append(i)
        
for i in unique_list:
    print(i)

        
    