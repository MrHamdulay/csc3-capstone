#program that prints a list of strings without a reat of a string
#TLSSOH001 Sohail Tulsi
#1 April 2014

# create empty string
str = [] 

#ask user to enter strings
str_add=input('Enter strings (end with DONE):\n')

#add only words that have not been repeated before 
while str_add != 'DONE': 
# so thatt the process ends when user types DONE
    if not str_add in str:
        str.append(str_add)
    str_add= input('')     
#ask user to enter more list entries

#random space
print('')
#print each item on the list on a new line
print('Unique list:')
for i in range(len(str)): #run for loop so that each string will be printed on a new line
    print(str[i])