# question1.py
# author: bxtnaa002
# assignment 7

words = [] 
word = input("Enter strings (end with DONE):\n") # create a list containing words and DONE is inputed to terminate the growth of the list
while word != "DONE":
        words.append(word)
        word = input("")

unique = [] #create a new list 
for word in words: #loop through all the words in the list created from inputed words
        if word not in unique: #if the word does not already appear in the new list, add it
                unique.append(word)
        else: #else if it does already appear, continue to the next word
                continue
        
print("\nUnique list:") 
print("\n".join(unique)) #print the new list containing the words appearing only once.