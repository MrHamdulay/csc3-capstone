"""Assignment 7 , Question 1 
CHRIS BOLTON"""

print ("Enter strings (end with DONE):")
list_strings = []
user_input = ""
sentinal = "DONE"
print ()

while user_input!=sentinal :
    user_input = input()
    list_strings.append(user_input)
    
print ("Unique list:")

    
    
unique_list = []

for i in (list_strings):
    if i not in unique_list:
        unique_list.append(i)
        
for i in range(len(unique_list)-1) :
    print (unique_list[i])
            
            
            


            
        
            
    
    


