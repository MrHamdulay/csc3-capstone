# Dalise Steynfaard
# STYDAL001
# Assignment 3, question 3
# March 2014

msg = input("Enter the message:\n")
r = eval(input("Enter the message repeat count:\n"))
ft = eval(input("Enter the frame thickness:\n"))

o_msg = '|'*ft + ' ' + msg + ' ' + '|'*ft
out_frame = '+' + '-'*(len(o_msg)-2) + '+'
in_frame = '|' + '+' + '-'*(len(out_frame)-4) + '+' + '|'

if r > 0 and ft > 0:
    print(out_frame)
    for i in range(ft-1,0,-1):
        print('|'*(ft-i) + '+' + '-'*(len(msg)+2*i) + '+' + '|'*(ft-i))
    for k in range(r):
        print(o_msg)
    for i in range(ft-1):
        print('|'*(ft-i-1) + '+' + '-'*(len(msg)+2*i+2) + '+' + '|'*(ft-i-1))    
    print(out_frame)
