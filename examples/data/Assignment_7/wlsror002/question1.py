def List():
    List=[]
    x= input('Enter strings (end with DONE):\n')
    while x != 'DONE' and x!= 'Done' and x != 'done':
        if x not in List:
            List.append(x)
        x=input('')
    return List
        
def main():
    x=List()
    print('\nUnique list:')
    for i in x:
        print (i)
        
main()