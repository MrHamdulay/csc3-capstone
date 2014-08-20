h = eval(input("Enter the hours:\n"))
m = eval(input("Enter the minutes:\n"))
s = eval(input("Enter the seconds:\n"))

if(h>24) :
    print("Your time is invalid.")

elif(m>60) :
    print("Your time is invalid.")
    
elif(s>60) :
    print("Your time is invalid.")
    
elif(h<0) :
    print("Your time is invalid.")
    
elif(s<0) :
        print("Your time is invalid.")
        
elif(m<0) : 
    print("Your time is invalid.")
    
else :
    print("Your time is valid.")