def uniquestr():
    string=[]
    list_string=input('Enter strings (end with DONE):\n')
    while list_string != 'DONE':
        if list_string not in string:
            string.append(list_string) 
        else :
            pass
        list_string=input('')
    
    print()
    print('Unique list:') #Printing the unique list
    for i in string :
        print(i)
uniquestr()