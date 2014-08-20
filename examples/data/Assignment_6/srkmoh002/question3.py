# Najeeb Sirkhoth
# SRKMOH002
# question3.py
# Assignment 6



print("Independent Electoral Commission")
print("--------------------------------")

# Create empty list    
namelist = []


# While loop which appends names to list
name = input("Enter the names of parties (terminated by DONE):\n")
while not name == "DONE":                                         # Sentinel is "DONE"
    namelist.append(name)
    name = input("") 
    
namelist.sort()                #Sort names in alphabetical order

dictionary = {}                #Empty Dictionary
for name in namelist: 
    dictionary[name] = dictionary.get(name,0) + 1       #add name count to dictionary
    
print("\nVote counts:")

keys = list(dictionary.keys())                         #Create list of names
keys.sort()                                            #Sort list of names
for i in range(len(keys)):
    print("{0:10} - {1}".format(keys[i], dictionary[keys[i]])) 
    
          
    
    
    
