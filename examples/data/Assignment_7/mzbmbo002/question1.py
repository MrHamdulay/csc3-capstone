#Mbongeni Mazibuko
#MZBMBO002
#Assignment 7

def no_duplicates():
    '''function where strings are entered and then printed in the same order but without duplicates.'''
    lName= []
    name= ''
    print("Enter strings (end with DONE):")
    
    while name!='DONE':
        name= input('')
        if name not in lName and (name!='DONE'):
            lName.append(name)
            
    print()
    print('Unique list:')
    for s in lName:
        print(s)
        
if __name__=='__main__':
    no_duplicates()