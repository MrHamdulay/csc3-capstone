def frame(s, repeat, thick):
    width = len(s) + thick*2
    height = repeat + thick
    cnt = 0
    for i in range(thick):              # top of frame
        
        print("|"*cnt, "+", "-"*(width-i*2), "+", "|"*cnt, sep="")  
        cnt += 1
        
    for i in range(repeat):             # middle

        print("|"*cnt, " ", s, " ", "|"*cnt, sep="")
    
    cnt-=1
    for i in range(thick-1, -1, -1):    # Bottom of frame

        print("|"*cnt, "+", "-"*(width-i*2), "+", "|"*cnt, sep="")
        cnt-=1

if __name__ == '__main__':
    m = input("Enter the message:\n")
    r = eval(input("Enter the message repeat count:\n"))
    t = eval(input("Enter the frame thickness:\n"))
    frame(m, r, t)
