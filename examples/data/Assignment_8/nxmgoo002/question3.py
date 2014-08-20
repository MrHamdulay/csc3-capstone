'''this programm prints the next of letter of each letter in a sentence
Nxumalo Goodman
09 May 2014'''

def move(w):
    if w == '':
        return w # if the is the nothing in the string it prints nothing
    elif not  96 < ord(w[0]) < 123:
        return w[0] +  move(w[1:]) #if the given input is not a small letter it passes it
    elif w[0] == ' ':
        return w[0] +  move(w[1:]) #if there is a space in the string it passes string and do recursion
    elif w[0] == 'z':
        return chr(97) +  move(w[1:]) #if the string is 'z' then it returns 'a'
    #recursion step
    else:
        return chr(ord(w[0])+1) + move(w[1:])

#prompt the user to enter the string    
w = input('Enter a message:\n')
move(w)
print('Encrypted message:')
print(move(w))