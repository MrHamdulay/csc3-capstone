def menu()
print('Welcome to UCT BBS')
print('MENU')
print("(E)nter a message")
print('(V)eiw a message')
print('(L)ist files')
print('(D)isplay file')
print('e(X)it')
list = []
x= input('Enter your selection:\n')
if x=='X':
    print('Goodbye!')
elif x=='E':
    y = input('Please enter a message:\n')
    if x=='V':
        print(y)
elif x=='L':
    return list
elif x=='D':
    print(y)