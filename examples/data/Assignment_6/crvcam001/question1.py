# question1.py
# prints a list of names right-aligned by the longest name user inputs
# camilla craven
# 22 april 2014

first = input("Enter strings (end with DONE):\n")  # prompts user for list of names (DONE when finished)

if first == "DONE": # if user inputs "DONE" immediately
    List = [] # empty list
    
else:
    List = [first] # adds name to list
    length = len(first) # calculates length of first name
    string = ""
    
    while string != "DONE": # indefinite loop until "DONE" is entered
        string = input() # user inputs more names
        hello = List.append(string) # adds new name to list
        
        length2 = len(string) # calculates length of name entered
        if length2 > length: # if new length older than previous length calculated
            length = length2 # length is now equal to newest max length
        
    List.remove("DONE") # removes word "DONE" from list

print()
print("Right-aligned list:")

for name in List: # for all names in list
    print(name.rjust(length)) # print list right-aligned by max length calculated