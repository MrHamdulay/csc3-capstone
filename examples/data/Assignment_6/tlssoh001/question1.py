#program to align lists from the right
#Sohail Tulsi TLSSOH001
#23 April 2014

#add variables to string
sr = []
str_add= input('Enter strings (end with DONE):\n')

while str_add != 'DONE':
    sr.append(str_add)
    str_add= input('')
    
#find lenght of longest string
long = 0
for i in range(0,len(sr)):
    if len(sr[i]) > long:
        long= len(sr[i])
#align from the right of longest string
print(' ')      
print('Right-aligned list:')
for i in range(0,len(sr)):
    print(' '*(long-len(sr[i])),sr[i],sep='')
    
    