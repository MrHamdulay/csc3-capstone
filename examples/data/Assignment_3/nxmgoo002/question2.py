def zwide():
    mina=eval(input("Enter the height of the triangle:\n"))
    for d in range(mina):
        nkosi="*"*(d+1)
        pho=" "*(mina-(d+1))
        good=pho+(d*"*")
        print(good+nkosi)
zwide()        
    