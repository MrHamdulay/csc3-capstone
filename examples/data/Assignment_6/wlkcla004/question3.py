"""question 3
clare walker
19 april 2014"""
# print intro
print("Independent Electoral Commission\n--------------------------------\nEnter the names of parties (terminated by DONE):")
word =""
words=[]
while True:   #create loop to get sequence
    word= input("")
    if word == "DONE":
        break
    else:
        words.append(str(word))
    

values=[] #create sequence to check and delete repetition
# add values to non repetitive sequence
for i in range(len(words)):
    if words[i] not in values:
        values.append(str(words[i]))
    else:
        continue
values.sort()    
print()
print("Vote counts:")
for i in range(len(values)):    #loop to print out counts and values
    print("{0:<10} - {1}".format(values[i], words.count(values[i])))
        
    
