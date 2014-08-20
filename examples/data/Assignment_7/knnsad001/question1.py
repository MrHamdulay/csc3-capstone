#program to print list of strings without duplicates
#KNNSAD001
#Assignment 7
#program to code 2048 game

memory = []
#inputting list of words to be used :
words=input("Enter strings (end with DONE):\n")  #uses DONE as sentinel
memory.append(words)

#this while loop will allow for inputs :

while words != "DONE":
    words = input("")
    memory.append(words)
memory.remove("DONE")
    
#creating unique list using a loop
#unique list is list of strings without duplicates

new_memory = []
new_words = ""
for i in memory:
    new_words == i
    if i in new_memory:
        continue
    else:
        new_memory.append(i)
        
print()
print("Unique list:")
for k in range(len(new_memory)):
    print(new_memory[k])
    
  #prints list without duplicates 