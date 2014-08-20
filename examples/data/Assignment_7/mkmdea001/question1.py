def rem_dup():
    #create an empty list 
    lis=[]
    #initialise a count 
    count=1
    #get input from user 
    x=input('Enter strings (end with DONE):\n')
    #as ong as input is not DONE  add the inputs to the list 
    while x != 'DONE':
        #if input is not in list then add it otherwise do nothing 
        if x not in lis:
            lis.append(x)
        x=input('')
        #accumulate count
        count+=1
        
    print()
    print('Unique list:\n',end='')
    #iterate throught the loop and print the string in the list 
    for i in lis:
            print(i)   
rem_dup()