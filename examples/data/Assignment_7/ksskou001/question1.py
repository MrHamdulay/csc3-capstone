''' This program prints out a list of string without duplication
By Kouame KOUASSI: KSSKOU001
On 27 april 20144'''

#Define two empty lists to store lists of strings
the_list = []
compare_list = []
#print the prompt sentence separately to avoid repetion in the loop
x = print('Enter strings (end with DONE):')
#iterate indefinitely to get string
while True:
    x = input() 
    #End the iteration when string entered is 'Done'
    if x == 'DONE':
        break
    #otherwise append the string to the list to be printed
    else:
        #check if string already stored to avoid duplication
        if x not in compare_list:
            the_list.append(x)
            #add the string to the list of comparison
            compare_list.append(x)
print('\nUnique list:')    
for i in the_list:
    print(i)