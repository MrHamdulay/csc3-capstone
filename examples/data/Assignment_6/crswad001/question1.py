'''Wade Cresswell Question 1'''
print("Enter strings (end with DONE):")
l = []
a = ''
while a !='DONE': # while the user does not input DONE
    l.append(a) # add what the user inputs into the list
    a = input() # allow the user to input a name
l=l[1:] # do not include the first element as empty
maxl = 0
for i in l:
    if len(i)>maxl:
        maxl=len(i) # finds the maximum word length in the list
print()
print('Right-aligned list:')
for i in l:
    print(' '*(maxl-len(i)),i,sep='') # PLACES SPACES BEFORE EACH ELEMENT IN THE LIST AS NECESSARY DEPENDANT ON LENGTH OF ELEMENT

