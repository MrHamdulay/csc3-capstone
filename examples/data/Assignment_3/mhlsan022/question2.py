#SandyCris MAHLANGU
#MHLSAN022
#Struggled a bit, but it was worth it...
H=eval(input('Enter the height of the triangle:\n'))
def tri(H):
    c=1
    for i in range(H):
        print(' '*(H-(i+1)),'*'*c,sep="")
       
        c+=2

tri(H)    
    