#Creating unique list for input string
#romelon chetty(chtrom001)
# 27 april 2014

x=[] # empty list will be fill with inputs
string=input('Enter strings (end with DONE):\n') #ask for input from user
x.append(string) # attach input to created list
while string!='DONE': 
    string=input()        #ask for inputs uptil user inputs DONE
    x.append(string) # attach input to created list

del x[len(x)-1] #delete DONE from list x

unilist=[] # this list will be used to append to unique strings

for i in x:
    if i in unilist:
        continue         # checks if item is in the list if not it will append it to the new list
    else:
        unilist.append(i) 
        
print()
print('Unique list:')
for i in unilist:
    print(i) # prints each item in unique 
    