"""Program to count the number of votes
By Tinashe Choga
25/04/2014"""
print("Independent Electoral Commission")
print("--------------------------------")
#creating list
names=[]
list=input("Enter the names of parties (terminated by DONE):\n")
while list!= "DONE":
    names.append(list)
    list=input("")
print()
print("Vote counts:")
counter = {}

# count words and add new words as they are encountered
for word in names:
    if not word in counter:
        counter[word] = 1
    else:
        counter[word] += 1
        
# print out counters
for word in sorted(counter):
    print (word+" "*(10-len(word)),"-",counter[word])
    
    
    
    
