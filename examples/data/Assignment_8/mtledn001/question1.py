'''Sewagodimo Matlapeng
Palindrome with recursion
06 May 2014'''
check = True
name =input('Enter a string:\n')
back = name
def pali(name):
    
    global check
    
       
    #if check == False:
        #print(check)    
    if name == '' or len(name)==1:
        if check== True:
            print('Palindrome!')
    elif name[0]!=name[-1]:
        #print(name[-1::-1])
        print('Not a palindrome!')
    else: 
        #print(name[-1], end='')
        return pali(name[1:-1])
pali(name)