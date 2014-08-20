words = input("Enter strings (end with DONE):\n")
#create array to hold words 
list = []
longestWord=0
#while user has not terminated the program, populate the array.
while words != "DONE":
    list.append(words)
    words=input("")
#Find the longest word in the array and set longestWord to that length    
for i in range (len(list)):
    
    if(len(list[i]))>longestWord:
        longestWord = (len(list[i]))
        

print()        
print ("Right-aligned list:")
#print out the list right aligned
for i in range (len(list)):
    
    print(list[i].rjust(longestWord))
       
       
    
