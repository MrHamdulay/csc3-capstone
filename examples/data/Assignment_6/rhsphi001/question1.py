'''Phillip Ruhesi 
24/04/14
this program that prints out a list of strings right aligned by the longest string'''

strings=[]                                       #Creates empty list
#Asks user for input and adds input to the list strings
x=input('Enter strings (end with DONE):\n')
strings.append(x)
if x=='DONE':
    print('\nRight-aligned list:')
else:
    while x!='DONE':                                 #While loop ends when the word sentinel DONE is entered
        x=input('')
        strings.append(x)
    del strings[len(strings)-1]                         #Deletes the word DONE from the list
    long=len(max(strings, key=len))                  #finds the length of the longest word
    print('\nRight-aligned list:')                   # len(max(name of list, key=len)) key specifies that you want the maximum length
    for i in strings:
        spaces=long-len(i)                           #prints the words right aligned
        print(' '*spaces,end='')
        print(i)    

                                                           