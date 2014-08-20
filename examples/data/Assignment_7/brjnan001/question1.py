"""To remove repeated words in a given input
Nandani Birjanund
assignment 7 : Q1"""

words = []        #array created to store list                               
x = input("Enter strings (end with DONE): \n")   #User input                

while x != "DONE":      # loop to know when to stop        
       if x not in words: #checks if words are repeated
              words.append(x)   #if not equal then add to list
       x = input("")   #asks for input again

print()
print("Unique list:")  #headings for title
for i in words: #loop to display list values
       print(i) #prints i