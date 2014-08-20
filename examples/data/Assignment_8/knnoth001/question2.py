'''[Recursion] Count the number of double letter in a string
Othniel KONAN
2014/05/03'''


def double(st,k):
    if len(st)>1:                       #set the break point when the string is only one character
        if st[0]==st[1]:                #check if the two first are equal
            k+=1                        #append the counter if we found a double letter
            double(st[2:],k)            #we continue to check for others double letter in the string not including the two first
        else:
            double(st[1:],k)            #we continue to check for others double letter in the string not including the first
    else:
        print('Number of pairs:',k)

st=input('Enter a message:\n')
double(st,0)                            #set the counter to zero