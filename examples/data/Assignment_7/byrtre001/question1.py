"""Create a unique list and get rid of any duplicates in the list
Trevor Byaruhanga
03 May 2014"""
#Create an empty list
list=[]
#Create another list, this will be the unique list
unique = []
print ('Enter strings (end with DONE):')

logic=False
while logic== False:
    strings= input('')
    if strings!='DONE':
        list.append(strings)
    elif strings=='DONE':
        logic=True
        break    
    
#once logic is true, if the items already exist in the list, don't add it to the unique list   
if logic==True:
    print()
    print('Unique list:')
    for i in list:
        if not i in unique:
            unique.append(i)
        
#print the new unique list
    for i in unique:
        
        print (i)    

    
    