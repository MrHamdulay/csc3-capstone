#Question 1: Right align an inputted list
#Galya Wolov
#23 April 2014

#get a list
listed=[]
string= input('Enter strings (end with DONE):\n')
print()
while string != 'DONE':
    listed.append(string)
    string= input("")
#find maximum length of list
long = ""
for i in range(len(listed)):
    if(len(long) < len(listed[i])):
        long = listed[i]
        


#align right to the largest string length
print('Right-aligned list:')
for i in listed :
    if(i == long):
        print(long)
    else:
        print(' '*(len(long)-len(i)) + i) #provides the right alignment for each word for the maximum 

