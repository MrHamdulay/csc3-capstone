#Rorisang Moseli
#April 2014
#Question, Assignment 7



#Construct
words = []
printed = []

#Enter list
print ("Enter strings (end with DONE):")

while True:
    word = input("")
    if word == "DONE":
        break 
    words.append(word)      
    
#Unique list
print ("")
print ("Unique list:")
for i in range(len(words)):
    if words[i] not in printed:
        print (words[i])
        printed.append(words[i])