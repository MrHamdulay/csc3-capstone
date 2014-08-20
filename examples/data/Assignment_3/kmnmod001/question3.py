mess = input("Enter the message:\n") #asks user to enter message to be printed.
rep1 = eval(input("Enter the message repeat count:\n")) #asks user for the repeats for message entered.
thick = eval(input("Enter the frame thickness:\n")) #asks user for frame thickness.

def thickness():
    dash = len(mess)+2*thick
    for i in range(thick):
        print(i*'|', '+', dash*'-', '+', i*'|', sep='')
        dash-=2
thickness()

def message():
    for r in range(rep1):
        print('|'*thick, mess, '|'*thick, sep=' ')
message()
        

def thicknesss():
    dash = len(mess)+2
    for n in range(thick-1,-1,-1):
        print(n*'|', '+', dash*'-', '+', n*'|', sep= '')
        dash+=2
thicknesss()
        