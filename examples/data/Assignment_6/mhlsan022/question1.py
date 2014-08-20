''' This program prompts a user to enter a list of names and right-aligns them.
Sandile Christopher Mahlangu
21 April 2014'''

def right_justified_list():
    '''This function prints a given list in a right justified manner'''
    #List where the names will be kept
    names=[]

    #Requesting the names
    name_request=input('Enter strings (end with DONE):\n')

    #Adding the name in to the list:
    names.append(name_request)

    while 'done' not in names and "DONE" not in names: #While the user hasn't made an input of done 

        name_request=input('')
        names.append(name_request)

    #Loop to print the names in the list
    names.remove(names[-1]) #Removing done from the list
    
    
    #finding the length of the longest string in the list
    max=0
    for j in names:
        if len(j)>max:
            max=len(j)
    print('\nRight-aligned list:')

    for i in range(len(names)):
        print(names[i].rjust(max)) 
    

    
if __name__=='__main__':        
    right_justified_list()