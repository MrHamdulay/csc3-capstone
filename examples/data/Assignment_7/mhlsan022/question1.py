'''This program removes duplicates in a provided list and prints the list in order
Sandile Christopher Mahlangu
29 April 2014'''


def get_list():
    '''This function gets a list from the user'''
    the_list=[]
    user_input=input('Enter strings (end with DONE):\n')
    the_list.append(user_input)
    
    #while the user has not entered an input of done the ask for more inputs
    while 'DONE' not in the_list:
        user_input=input('')
        the_list.append(user_input)

    return the_list[:-1] #Return the list the user has input except for the last input which is 'DONE'

def remove_duplicates(the_list):
    '''This function removes duplicates in a provided list'''
    new_list=[]
    for item in the_list:#Making a new list with no duplicates from the original list
        if item not in new_list:
            new_list.append(item)
    
    print('\nUnique list:')
    for item_print in new_list: #Printing the list without duplicates
        print(item_print)
        

if __name__=='__main__':
    #Calling the fuctions
    remove_duplicates(get_list())
