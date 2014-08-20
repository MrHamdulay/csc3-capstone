"""progress report
Lubalethu Dube
23 April 2014"""
def Mr_Histogram():
    #get marks
    x=(input("Enter a space-separated list of marks:\n"))
    the_list=x.split(" ")
    #find pass level
    f=0
    three=0
    two_n=0
    two_p=0
    one=0
    for i in range (1):
        for k in the_list:
            j=eval(k)
            if j<50:
                f+=1
            elif j>=50 and j<60:
                three+=1
            elif j>=60 and j<70:
                two_n+=1
            elif j>=70 and j<75:
                two_p+=1
            else:
                if j>=75:
                    one+=1
    print("1 |",("X")*one,sep="")
    print("2+|",("X")*two_p,sep="")
    print("2-|",("X")*two_n,sep="")
    print("3 |",("X")*three,sep="")
    print("F |",("X")*f,sep="")
    
            
        
            
        
        
    
Mr_Histogram()