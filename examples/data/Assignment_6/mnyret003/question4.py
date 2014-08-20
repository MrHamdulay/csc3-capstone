# A program that takes in a list of marks and output a histogram representation of the marks.
# Retselisitsoe Monyake
# 23/04/2014

# get marks from user
A=input("Enter a space-separated list of marks:\n")
marks=A.split()
one=0
twO=0
two=0
three=0
F=0
for i in marks:
    if eval(i)<50:
        F+=1
    elif 50<=eval(i)<60:
        three+=1
    elif 60<=eval(i)<70:
        two+=1
    elif 70<=eval(i)<75:
        twO+=1
    elif eval(i)>=75:
        one+=1
        
print("1 |"+"X"*one)
print("2+|"+"X"*twO)
print("2-|"+"X"*two)
print("3 |"+"X"*three)
print("F |"+"X"*F)

        
    

    


            
