# PROGRAM TAKING LIST OF MARKS AND OUTPUTING A HISTOGRAM
# Sandisha Budhal
# BDHSAN003


list_marks=input("Enter a space-separated list of marks:\n") #ASK USER TO INPUT MARKS
mrks=list_marks.split() #splitting
ONE=0
TWO=0
Two=0
THREE=0
F=0
for i in mrks:
    if eval(i)<50:
        F+=1
    
    elif 50<=eval(i)<60:
        THREE+=1
    
    elif 60<=eval(i)<70:
        Two+=1
    
    elif 70<=eval(i)<75:
        TWO+=1
    
    elif eval(i)>=75:
        ONE+=1
        
print("1 |"+"X"*ONE)

print("2+|"+"X"*TWO)

print("2-|"+"X"*Two)

print("3 |"+"X"*THREE)

print("F |"+"X"*F)

        
    

    


            
