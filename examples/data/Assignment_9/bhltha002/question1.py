from math import sqrt
def info():
    X=input("Enter the marks filename:\n")
    X=open(X,"r")
    Y={}
    for line in X:
        name,marks=line.split(",")
        Y[name]=marks
    return Y

def sum(Y):
    Z=list(Y.values())
    sum=0.0
    for item in Z:
        value=eval(item)
        sum+=value
    return sum

def mean(sum,Y):
    S=Y.values()
    mea = sum/(len(S))
    return mea
def devi(mea,Y):
    F=Y.values()
    sumdev=0.0
    for j in F:
        num=eval(j)
        dev= num - mea
        sumdev=sumdev + dev * dev
    return sqrt(sumdev/(len(F)-1))
def main():
    data = info()
    sume=sum(data)
    Ave=mean(sume,data)
    stard=devi(Ave,data)
    mean_Sd=Ave-stard
    
    for low in data.values():
        mark=eval(low)
        if mark<mean_sd:
            
            
        
    


                
                
        
    


     
 
    
        
  

        