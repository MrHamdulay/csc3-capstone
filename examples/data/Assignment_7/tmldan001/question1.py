'''Program where user can enter list of strings and strings are printed in same order
Daniel M. Tamale
TMLDAN001
2014-04-27'''

'''To enter words stored as strings'''
string=input ('Enter strings (end with DONE):\n')
strings=[]
while True:
    if string=='DONE':
        break
    strings.append(string)
    string=input('')
print('')

'''To reverse the list and check for repeated items'''
strings.reverse()

for i in strings:
    while strings.count(i)>1:
        strings.remove(i)
        
'''To print strings in same order without repeatition'''
strings.reverse()
print ('Unique list:')
for i  in strings:
        print (i)