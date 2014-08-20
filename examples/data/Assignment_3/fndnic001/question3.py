#Cool frame for a message
def top(thickness):
    j=''
    n=len(mess)+2*thickness
    for i in range(thickness):
        print(j+'+'+n*'-'+'+'+j)
        n=n-2
        thickness-=1
        j+='|'
        
def message(mess):
    for i in range(repeat):
        print(thickness*'|',mess,thickness*'|')
        
def bottom(thickness):
    n=len(mess)+2
    for i in range(thickness):
            print('|'*(thickness-1)+'+'+n*'-'+'+'+'|'*(thickness-1))
            n=n+2
            thickness=thickness-1
            

    
if __name__=="__main__":
    mess1=input("Enter the message:\n")    
    mess=str(mess1)
    repeat=eval(input("Enter the message repeat count:\n"))
    thickness=eval(input("Enter the frame thickness:\n"))
    top(thickness)
    message(mess)
    bottom(thickness)

    


