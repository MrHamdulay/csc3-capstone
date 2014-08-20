# triaqngle of height h
# tarisai stephen kalinde
# klntar002

def triangle():
    H=eval(input("Enter the height of the triangle:\n"))
    stresk=1
    gaps=H-1
    for i in range(0,H):
        print(' '*gaps,'*'*stresk,sep="")
        stresk+=2
        gaps+=-1
        
        
triangle()        
        

       
             