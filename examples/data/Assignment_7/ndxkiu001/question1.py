#Kiuran Naidoo
#Assignment 7
#Question 1
#27 April 2014

inputString = input("Enter strings (end with DONE):\n")#Get Input
words =[] #List to store unique words

while inputString != "DONE":
    if inputString not in words: #Add word to list if it is not in the list yet
        words.append(inputString)
        inputString=input("") #Get next input word
    else: #Get next input if the word is alread in the list
        inputString =input("")
        
print()
print("Unique list:") #Print output
for x in words:
    print(x)
    


    
