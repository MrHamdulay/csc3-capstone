""""program to create list of words that are not repeated-assignment 7 question1
author : Divan Jagers
27 April 2014"""
x=input("Enter strings (end with DONE):\n") #prompts the user to input words,using DONE as a sentinel
o_list=[] #creates an original list
while x != "DONE":    # a loop that iterates as long as the input value is not "DONE"
    o_list.append(x)     #appends to the original list
    x=input("")
n_list=[]                #creates a new unique empty list
for item in range(len(o_list)):        #loop that adds items to new list if not already in list
    if o_list[item] not in n_list:
        n_list.append(o_list[item])
print()
print("Unique list:")     #prints out the new unique list
for i in range(len(n_list)):
    print(n_list[i])
