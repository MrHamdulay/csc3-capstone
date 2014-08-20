  
def sq(H):
    X = 1
    for i in range(H,0,-1):
        print(" "*(i-1),"*"*X," "*(i-1),sep="")
        X+=2

if __name__=='__main__':
    H =eval(input("Enter the height of the triangle:\n"))
    sq(H)

   
   