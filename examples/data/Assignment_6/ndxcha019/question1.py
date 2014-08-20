#question 1
#luke naude
#2014-4-23

name_string=[]
string_length=[]
x=''

#tell the user what to do
print('Enter strings (end with DONE):')

#get the names
x=input()
while x != 'DONE':
    name_string.append(x)
    string_length.append(len(x))
    x=input() 

#length of longest word
LongestWord=max(string_length)

#print the names
print('\nRight-aligned list:')    
for i in name_string:
    print(' '*(LongestWord-len(i)),i,sep='')
    #print('{0:>x}'.format(i))
    