#A program to count the number of marks and draw a histogram
#F.J.Chigwaza
#24-04-2014

def marks():
    percent=input('Enter a space-separated list of marks:\n')
    marks=percent.split(' ')
    
    A=0
    B=0
    C=0
    D=0
    E=0
    
    for i in marks:
        if 0<=int(i)<50:
            E+=1
            
        if 50<= int(i)<60:
            D+=1
            
        if 60<= int(i)<70:
            C+=1
        if 70<= int(i)<75:
            B+=1
        if 75<=int(i)<=100:
            A+=1
            
    print('1'+' '+'|'+'X'*A)
    print('2+'+'|'+'X'*B)
    print('2-'+'|'+'X'*C)
    print('3'+' '+'|'+'X'*D)
    print('F'+' '+'|'+'X'*E)
        
marks()         
        
        
        
    
    
    
    