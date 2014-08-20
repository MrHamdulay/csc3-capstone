#program to print message enclosed in frame
#by nasreen

#input from user
msg = input("Enter the message:\n")
rpt = eval(input("Enter the message repeat count:\n"))
frm = eval(input("Enter the frame thickness:\n"))
length = (len(msg) + 2 + frm*2)
a = 0
b = (length -2)

#prints top of frame
for i in range(frm):
    print('|'*a, '+', '-'*b, '+', '|'*a, sep ='')
    a = (a+1)
    b = (b-2)
    
#prints message + sides of frame
for j in range(rpt):
    print('|'* frm, end = '')
    print (' '+msg, end ='')
    print(' '+'|' * frm)
    
#prints bottom of frame
c = (frm - 1)
d = (len(msg) +2)
for k in range(frm):
    print('|'*c, '+', '-'*d, '+', '|'*c, sep ='')
    c = (c-1)
    d = (d+2)