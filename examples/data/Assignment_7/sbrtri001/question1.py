''' Assignment 7, question 1
List of names with duplicates removed
Tristan Subroyen
27 April 2014 '''

def names():
    ''' This function inputs a list of names into a list 
    (without allowing duplicates) and then prints the list '''
    
    # initialize variables to be used
    names = []
    name = ''
    nameCount = 0
    
    # print the input heading
    print("Enter strings (end with DONE):")
    
    while name != 'DONE': # while the user does not enter DONE (sentinel value)
        name = input() # name is user's input
        if name not in names: # if the name does not already exist in the list names
            names.append(name) # add the name to the list
            nameCount += 1 # increase nameCount
        else:
            name = '' # reset name value so that the while loop will continue

    names.remove('DONE') # remove DONE from the list
    nameCount = nameCount-1 # subtract one to compensate for removed DONE
    print('') # print a blank line
    print("Unique list:") # print output heading
    
    # print the unique list
    for i in range (nameCount):
        print(names[i])

if __name__ == '__main__':
    names()