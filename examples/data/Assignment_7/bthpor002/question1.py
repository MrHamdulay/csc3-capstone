#A program that prints out a unique lists without duplicates 
#By Portia Buthelezi 


#create an empty string
x_list= []

#Let the user input strings 
x_string= input('Enter strings (end with DONE):\n')

#append the inputs to the list
while x_string !='DONE':
    x_list.append(x_string)
    x_string= input('')

#Creat new empty list
x_new_list=[]
    
for x_string in x_list:
    if x_string not in x_new_list:
        x_new_list.append(x_string)
    else:
        continue

print('\nUnique list:')    
for i in x_new_list:
    print(i)
    
    
