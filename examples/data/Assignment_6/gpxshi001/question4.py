#GPXSHI001
#ASS 6
#Q4
#MARK POINTS

def main():
    
    alles= input("Enter a space-separated list of marks:\n")
    
    proper= alles.split(" ")  #creates a list of strings from the marks that have been separated by a space
    marks= (len(proper))   # need to find len loop needs to iterate for
    R1=0   
    R2=0
    R3=0
    R4=0
    R5=0          #Created to multiply by X
    
    for i in range(marks):
        
        if (eval(proper[i])) < 50:
            R5+=1
            
        if (50 <=(eval(proper[i]))< 60):
            R4+=1
            
        if (60 <=(eval(proper[i]))< 70):
            R3+=1
            
        if (70 <= (eval(proper[i]))< 75):
            R2+=1
            
        if ((eval(proper[i]))>= 75):
            R1+=1
            
    print("1 |", "X"*R1, sep="")
    print("2+|", "X"*R2, sep="")
    print("2-|", "X"*R3, sep="")
    print("3 |", "X"*R4, sep="")
    print("F |", "X"*R5, sep="")
            
            
      
main()
        