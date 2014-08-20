# Najeeb Sirkhoth
# SRKMOH002
# question1.py
# Assignment 6

# Program which allows user to enter list of strings
# Prints out strings right-aligned with longest string


# Create empty list    
userList = []



# While loop which appends users' strings to list
string = input("Enter strings (end with DONE):\n")
while not string == "DONE":                           # Sentinel is "DONE"
    userList.append(string)
    string = input("")

  
    
# Method for finding list-item with maximum length
if len(userList) > 0:
    length = len(userList[0])                             # Intially set item 1 as having maximum length
    for i in range(len(userList)):                        # Then assess length of next item 
        if length < len(userList[i]):
            length = len(userList[i])                     # keeping track of any increase in length
        else:    
            length = length
        


# Print each list item
print("\nRight-aligned list:")
if len(userList) > 0:
    for i in range(len(userList)):
        print((" ")*(length-len(userList[i]))+userList[i])   
        
        # Use max length as field width
        # Use difference between max length and length item[i] to establish number of empty spacing 
    
              
    
    
    
    
    