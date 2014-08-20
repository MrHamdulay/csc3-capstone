"""Sizwe Sibiya
SBYSIZ002: 21 Apr 2014
Right aligne a list of nams"""

#create a list with the names entered by the user
name = input('Enter strings (end with DONE):\n')
strings  = []
strings.append(name)

while name != 'DONE':
         name = input('')
         strings.append(name)
#Making the word with maximum length the aligner of the others    
strings.remove('DONE')   
a = 0         
for item in strings :
         x = len(item)
         if x > a :
                  a=x
print("")                  
print('Right-aligned list:')                  
for i in strings:                  
         r = '{0: >'+str(a)+'}'
         print( r.format(i))