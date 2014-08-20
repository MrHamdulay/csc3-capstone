'''Enter a space-separated list of marks:
12 23 34 45 56 67 78 89 90
1 |XXX
2+|
2-|X
3 |X
F |XXXX

fail < 50%
50% <= 3rd < 60%
60% <= lower 2nd < 70%
70% <= upper 2nd < 75%
1st >= 75%


'''

marks = input("Enter a space-separated list of marks:\n").split(" ")

one = 0
twoplus = 0
twomin = 0
three = 0
EFF = 0

for i in range(len(marks)):
    if 100 >= eval(marks[i]) >= 75:
        one += 1
    elif eval(marks[i]) >= 70: 
        twoplus += 1
    elif eval(marks[i]) >= 60:
        twomin +=1
    elif eval(marks[i]) >= 50: 
        three += 1
    elif eval(marks[i]) >= 0: 
        EFF += 1
        
print("1 |","X"*one,sep="")
print("2+|","X"*twoplus,sep="")
print("2-|","X"*twomin,sep="")
print("3 |","X"*three,sep="")
print("F |","X"*EFF,sep="")
    
    
    
