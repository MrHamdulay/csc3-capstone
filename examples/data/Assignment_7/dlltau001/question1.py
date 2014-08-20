#Assignment 7
#Question1
#Tauriq Dolley

#take in a list and output in same order without repetitions
    
    
words = []
new_words = []
    
words.append(input("Enter strings (end with DONE):\n"))
while 'DONE' not in words:
    words.append(input(""))
    
for i in words:
    if i not in new_words:
        new_words.append(i)
        
print()
print("Unique list:")

for i in range(len(new_words) - 1):
    print(new_words[i])
    
        
    