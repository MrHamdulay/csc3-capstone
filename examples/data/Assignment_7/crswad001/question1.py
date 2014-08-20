'''Wade Cresswell'''
print("Enter strings (end with DONE):") 
x = input() #GETS THE INPUT FROM THE USER
list= []
unlist = []
while x!='DONE':
    list.append(x)
    x=input() #ADDS ALL ELEMENTS TO THE LIST UNLESS THE WORD DONE IS INPUT

for i in list:
    if i not in unlist:
        unlist.append(i) #ADDS THE ITEM TO THE UNIQUE LIST IF IT IS NOT ALREADY IN THE LIST
print()
print('Unique list:')
for i in unlist:
    print(i) #PRINTS THE UNIQUE LIST