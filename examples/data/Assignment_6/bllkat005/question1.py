# Kate Bell
# BLLKAT005
# 22 April 2014 

# Input strings from user, with "DONE" as the sentinel 
word = input("Enter strings (end with DONE):\n")
string_list = []
while not word == "DONE":
    string_list.append(word)    
    word = input("")
    
# Determine how long the longest string in the list is    
longest = 0
for i in string_list:
    if len(i) > longest:
        longest = len(i)

# print out strings in list, right-aligned 
print("\nRight-aligned list:")
for j in string_list:
    print(" "*(longest-len(j)),j,sep="")
    
    