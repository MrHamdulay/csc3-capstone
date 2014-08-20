#luke naude
#program to create a unique list
#30-4-2014



string_list=[]
def get_input():
    x=input('Enter strings (end with DONE):\n')
    '''getting the input'''
    while x != 'DONE':
        if x not in string_list:    
            string_list.append(x)
            x=input()
        else:
            x=input()
        
def give_output():
    '''printing string inputs that were not repetitions'''
    print('\nUnique list:')
    for i in string_list:
        print(i)
        
        
get_input()
give_output()