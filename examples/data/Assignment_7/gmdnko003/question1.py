'''Program where list of strings is outputted with no duplicates
Nkosi Gumede
30 April 2014'''
# 1)Ask user to input strings and store them in a list
# 2)If the same word appears in the list more than once, don't store it
# 3)Output the new list under the title 'Unique list:'

listed=[]
x= input("Enter strings (end with DONE):\n")
#Add items to list, remove the items already in the list
while x!="DONE":
    if x not in listed:
        listed.append(x)
    x=input("")
#Now for the output
print("")
print("Unique list:")
for i in listed:
    print(i)