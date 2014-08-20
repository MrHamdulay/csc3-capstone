'''This program prints out a list of given strings right-aligned
By Kouame Hermann KOUASSI: KSSKOU001
on 19 april 2014'''

def get_list():
    '''inputs and converts list of strings to and an array that is returns'''
    #avoid the prompt sentence to repeat many times 
    print('Enter strings (end with DONE):')
    list = []
    #iterate untile the user enters 'DONE'
    while True:
        x=input()
        #break the loop before storing 'DONE'
        if x == 'DONE':
                    break
        #store each entry into list to create an array of 
        list.append(x)
    #return the array created
    return list
        
        

def longest_str(list):
    '''returns the longest item within a list of string'''
    #assume the first string is the longest
    max_length = len(list[0])
    for i in list:
        length = len(i)
        #check if each string is longer or not than the longest and thereafter change max_length
        if length > max_length:
            max_length = len(i)
    return max_length

def display(list,max_length):
    '''prints out list of strings out righted aligned'''
    for i in list:
        print(' '*(max_length-len(i)),i,sep = '')
        

def main():
    '''main function that calls the above functions'''
    #get the list of words
    list = get_list()
    if list != []: #find the longest word if list not empty
        max_length = longest_str(list)
        #output the word right-aligned 
        print('\nRight-aligned list:')
        display(list,max_length)
    else:
        print('\nRight-aligned list:')
    

if __name__=="__main__":
    main()
    
    
    
        

        
    
    
