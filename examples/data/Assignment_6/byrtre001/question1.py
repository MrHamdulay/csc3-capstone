"""Print list of strings right-aligned
Trevor Byaruhanga
20 April 2014"""



list=[]

print('Enter strings (end with DONE):')
logic=False
#while logic is false, ask the user to enter a list of strings. When the user enters done stop compiling the list.
while logic==False:
    strings=input('')
    if strings!='DONE':
        list.append(strings)
    elif strings=='DONE':
        logic=True
        break

if logic==True:
    print()
    print ('Right-aligned list:')
    if len(list)>=1:
        
#print the list of strings right aligned. With the alignment width being the longest item in the list.
        x= max(list, key=len)
        y=(len(x))
        for i in list:
            print("{0:>{1}}".format(i, y))
    else:
        print()
            
        
        
    



