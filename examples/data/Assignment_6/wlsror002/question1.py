def main():
    width=0
    List=[]
    x=input('Enter strings (end with DONE):\n')
    while x != 'DONE' and x != 'Done' and x != 'done':
        List.append(x)
        x=input('')
        
    for i in List:
        x=len(i)
        if x > width:
            width=x
            
    print('\nRight-aligned list:')
    for i in List:
        print(i.rjust(width))
        
main()