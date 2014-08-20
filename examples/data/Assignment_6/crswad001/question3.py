'''Wade Cresswell Question 3'''
print("Independent Electoral Commission\n--------------------------------")
print("Enter the names of parties (terminated by DONE):")
l = []
a = ''
while a !='DONE': # while the user does not input DONE
    l.append(a) # add what the user inputs into the list
    a = input() # allow the user to input a name
l=l[1:] # do not include the first element as empty
sl =[]
for i in l:
    if i not in sl:
        sl.append(i) #creates a list with only unique names
sl.sort()
count=0
print()
print('Vote counts:')
for i in sl:
    count = l.count(i)
    print("{:<10}".format(i)+" -",count)

    