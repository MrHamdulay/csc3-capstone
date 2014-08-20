"""Mark Histogrammer"""
#Liam Brodie
#BRDLIA004
#21/4/2014

print("Enter a space-separated list of marks:")
marks = input("")
marks = marks.split(" ")

failcount   = 0
thirdcount  = 0
min2count   = 0
plus2count  = 0
Fcount      = 0

for i in marks:
    if eval(i) < 50:
        failcount += 1
    if 50 <= eval(i) < 60:
        thirdcount +=1
    if 60 <= eval(i) < 70:
        min2count += 1
    if 70 <= eval(i) < 75:
        plus2count += 1
    if 75 <= eval(i) <= 100:
        Fcount += 1 
        
print("1 |"+ "X"*Fcount)
print("2+|"+ "X"*plus2count)
print("2-|"+ "X"*min2count)
print("3 |"+ "X"*thirdcount)
print("F |"+ "X"*failcount )