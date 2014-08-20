def upper_border(thck):
    space = '|'
    p = len(msg) + (2*thck)
    fill = '+' + '-'*p + '+'
    for i in range(thck):
        print((space*i) + '+' + '-'*p + '+' + (space*i))
        p-=2
        
def middle_portion(count):
    space = '|'
    for p in range(count):
        print(space*thck, msg, space*thck)
        
def lower_border(thck):
    space = '|'
    k = len(msg)+2
    fill = '+' + '-'*k + '+'
    c = 1
    for l in range(thck):
        print(space*(thck-c) + '+' + '-'*k + '+' + space*(thck-c))
        k+=2
        c+=1
        
        
msg  = input("Enter the message: \n")
count  = eval(input("Enter the message repeat count: \n"))
thck = eval(input("Enter the frame thickness: \n"))
upper_border(thck)
middle_portion(count)
lower_border(thck)