# program with list of names but terminates but includes sentinel "DONE".
#strings are then right alligned.


# get input
m=input ("Enter a space-separated list of marks:\n")

#split marks into a list
marks = m.split (" ")
#setting counters to 0
fail = 0
three = 0
ltwo = 0
utwo = 0
first = 0

#loop through the list
for m in marks:
#increment counters for the correct grade.
    if eval(m) >= 0 and eval(m) <50:
        fail+=1
    
    elif eval(m)>=50 and eval(m)  <60:
        three+=1
    elif eval(m)>=60 and eval(m)<70 :
        ltwo+=1
    elif eval(m)>=70 and eval(m) <75:
        utwo+=1
    elif eval(m)>=75:
        first+=1
        
print("1 |"+ first*"X")
print("2+|"+ utwo*"X")
print("2-|"+ ltwo*"X")
print("3 |"+ three*"X")
print("F |"+ fail*"X")



                
    
    

