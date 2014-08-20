#module mystery.py
x=eval(input("Enter the height of the triangle:\n"))
def a(par1,par2):
    gab=par1//2-1
    for i in range(0,par1,2):
        print(' '*gab,end='')
        print(par2*(i+1))
        gab=gab-1
def sq(H,char):
    for i in range(H):
        print(char*H)
if __name__ =='__main__':
    a(x*2,'*')
    
