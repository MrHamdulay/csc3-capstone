'''Ednecia Matlapeng
30 April 2014
Unique list'''
mylist = []
myword = input('Enter strings (end with DONE):\n')
output = ''
while myword!='DONE':
     
     if output.find(' '+myword+' ')==-1:
          mylist.append(myword)
     output+=' ' +myword+' '
     myword = input('')
print('\nUnique list:')
#print(mylist) tP SEE HOW THE LIST LOOKS
for  i in mylist:
     print(i)
