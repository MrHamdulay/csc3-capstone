#20 April 2014  
#Assignment 6, Question 1, program to right align entered words
#LYLJON002

string = ''                     #string input
length = 0                      #length to right align to                
wordlist = []                   #variable for list

print("Enter strings (end with DONE):\n")

while string != "DONE": 
        string = input("")
        wordlist.append(string)           #add inputted strings to the list              
        if len(string) > length: 
                length = len(string)            #find longest word's length

print("Right-aligned list:")

x = len(wordlist) - 1                           #loop variable creation

for j in range(0, x): 
        print(" "*(length-len(wordlist[j])) + wordlist[j])      #output right aligned