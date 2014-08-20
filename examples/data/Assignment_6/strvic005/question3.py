"""program to count numer of party votes 
vicky stark
23 april 2014"""

print("Independent Electoral Commission\n"+"-"*32)

list_of_words=[]
name=input("Enter the names of parties (terminated by DONE): \n")

while name!='DONE':
    list_of_words.append(name)
    name=input('')

list_of_words.sort()  
counters= {} #start with an empty dictionary
    
for name in list_of_words:
    if not name in counters: #check if word is in dict
        counters[name]=0
    counters[name]+=1

y=sorted(counters.keys()) #sort keys into alphabetical order

print("\nVote counts:")
#print results
for name in y:
    print("{0:10}".format(name), '-', counters[name])