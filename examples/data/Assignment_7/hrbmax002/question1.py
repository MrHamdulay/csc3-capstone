"""QUESTION 1, Assignment 7, MAX HERBERSTEIN"""

print ("Enter strings (end with DONE):")
list1 = []
user_input = ""
sentinal = "DONE"
print ()

while user_input!=sentinal :
    user_input = input()
    list1.append(user_input)
    
print ("Unique list:")

    
    
new_list = []

for i in (list1):
    if i not in new_list:
        new_list.append(i)
        
for i in range(len(new_list)-1) :
    print (new_list[i])