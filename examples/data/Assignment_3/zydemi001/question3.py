def main():
    m = input("Enter the message:\n")       #m = message
    r = eval(input("Enter the message repeat count:\n"))   #r = repeat count
    t = eval(input("Enter the frame thickness:\n"))      #t = frame thickness
    e = len(m) + 2*t
    
    for i in range (0,t):
        print("|"*i, "+", "-"*e, "+", "|"*i, sep="")
        e = e-2
    for j in range(0,r):
        print("|"*t, m, "|"*t)
    for k in range(t,0,-1):
        print("|"*(k-1), "+", "-"*(e+2), "+", "|"*(k-1), sep="")
        e = e+2

main()