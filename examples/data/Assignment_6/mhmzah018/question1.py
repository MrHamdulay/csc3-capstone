"""Assignment 6 - question 1
Zaheer Mahmood
20-04-2014"""

#create list to store strings
group_words=[]
word = input("Enter strings (end with DONE):\n")
group_words.append(word)

#construct loop to accept inputs
while word != "DONE":
    word = input("")
    group_words.append(word)
    
        
#determine the longest item in the list
group_words.remove("DONE")
longest = 0
length=[]
for k in range(len(group_words)):
    length.append(len(group_words[k]))
            
    longest = max(length)
print()           
print("Right-aligned list:")
        
#Create loop to allow for justification

for i in range(len(group_words)):
    justify = group_words[i].rjust(longest)
    print(justify)
            
    
            
        
        