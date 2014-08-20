'''Program to print out right-aligned strings
Daniel M. Tamale
2014-04-21'''

'''To ask for input and store as list'''
string=input ('Enter strings (end with DONE):\n')
strings=[]
while True:
    if string=='DONE':
        break
    strings.append(string)
    string=input('')
print('')

'''To right align the list'''
lengths=[]
for i in strings:
    lengths.append(len(i))
    
'''To print right aligned strings'''
if lengths:
    b=str(max(lengths))
    print ('Right-aligned list:')
    a='{0:>'+b+'}'
    for j in strings:
        print(a.format(j))
        
else:
    print ('Right-aligned list:')