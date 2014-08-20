#Assignment 3 Q2
#Charlie Shang  
#SHNHUA002

iHeight = eval(input('Enter the height of the triangle:\n'))
i=0
k=1
j = iHeight

for i in range(iHeight):
        print(('*'*k).rjust(j))
        j +=1
        k+=2
        
        