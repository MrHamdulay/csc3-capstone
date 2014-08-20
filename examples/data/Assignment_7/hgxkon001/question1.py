#Konrad Hugo
#Assignment seven question 1
#30/04/2014

print("Enter strings (end with DONE):")
print()
stop='DONE' #sentinel word
list_uniq=[]
user_input=input('') 
while user_input != stop: #sentinel loop with sentinel=DONE
    if user_input not in list_uniq: #limits the list contents/inputs to non-duplicates
        list_uniq.append(user_input) 
    user_input=input('') #Allows continuous input until sentinel word inserted
if user_input == stop: #Once break word inputed stop the blank prompts
    print("Unique list:")
    for i in list_uniq: #loop that Prints each word of the list individually under one another
        print(i)
    
        
        
        
    

    