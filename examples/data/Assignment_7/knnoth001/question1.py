'''Program that prints list of unique string of a string in the same order
Othniel KONAN
KNNOTH001
2014/04/27
'''
#VARIABLES
unik_list = []

#PROMPT THE USER TO ENTER A STRING
st = input('Enter strings (end with DONE):\n')
while st != 'DONE':
    if not st in unik_list:             #If it's a new string 
        unik_list.append(st)            #Add it to the unique list
    st = input()                        #Ask the user again
    
print('\nUnique list:')

#PRINT THE LIST
for l in unik_list:
    print(l)
    