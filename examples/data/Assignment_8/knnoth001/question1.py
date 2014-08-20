'''Check if a string is a Palindrome using recursion
Othniel KONAN
KNNOTH001
2014/05/04'''

def palin(st):
    if len(st)>1:                           #set the breaking point when there is less than one character in the string
        if st[0] == st[len(st)-1]:          #If the first letter is the same as the last one
            palin(st[1:len(st)-1])          #we go to check for the rest of the string
        else:
            print('Not a palindrome!')    
    else:
        print('Palindrome!')

st=input('Enter a string:\n')
palin(st)