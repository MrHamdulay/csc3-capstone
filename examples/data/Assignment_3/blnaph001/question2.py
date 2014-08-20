
def a(par1,par2):
    gap=par1//2-1
    for i in range(0,par1,2):
        print(' '*gap,end='')
        print(par2*(i+1))
        gap=gap-1
        
        #if gap==1:
            #gap=0
if __name__ =='__main__':
    i=eval(input('Enter the height of the triangle:\n'))
    a(i*2,'*')