
"""Sithembiso Mashinini 
2014/04/25
vector computations"""


def main():
    import math#this allows us to use the sqrt 
    #this is empty list that  are going to filled by the user and loops i set up beneath
    A=[]
    B=[]
    C=[]
    summation=0
    x=input('Enter vector A:\n')#prompt 
    y=input('Enter vector B:\n')#prompt
    for i in x.split():#this ignores the space between the number 
        A.append(int(i))#the int function converts the string into a integer for computational purposes 
    for j in y.split():
        B.append(int(j))
    #print(A)
    #print(B)
    
 
    print('A+B =',[A[0]+B[0],A[1]+B[1],A[2]+B[2]])#i index each list beauase the components of addition multiplication are the same so adding the same components 
    print('A.B =',A[0]*B[0]+A[1]*B[1]+A[2]*B[2]) 
    print('|A| =',"%.2f" %round(math.sqrt(A[0]**2+A[1]**2+A[2]**2),2))
    print('|B| =',"%.2f" %round(math.sqrt(B[0]**2+B[1]**2+B[2]**2),2))
    
    

          
main()