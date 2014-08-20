"""question 1
clare walker
19 april"""
print("Enter strings (end with DONE):")
#initiate list
words =[]
#get values
while True:
    word = input("")
    if word == "DONE":    #to exit loop
        
        break
    else:
        words.append(str(word)) # add word to list of words
        
# find longest word
maxi = 0
for i in range(len(words)):
    word = words[i]
    if len(word)>maxi:
        maxi = len(word)
    else:
        continue
print()
#print list in colomn size 'maxi'
print("Right-aligned list:") 
for i in range(len(words)):
    print((maxi-len(words[i]))*' '+words[i])