"""MArk counter
Luveshen Pillay
4/22/2014"""

#Get string and form list
scorestring=input("Enter a space-separated list of marks:\n")
d=scorestring.split()

#Count number of grades
f,su,sl,t,fa=0,0,0,0,0
for num in d:
    num=eval(num)
    if num >= 75:
        f=f+1
        
    elif 70 <= num < 75:
        su=su+1
        
    elif 60 <= num < 70:
        sl=sl+1
        
    elif 50 <= num < 60:
        t=t+1
        
    else:
        fa=fa+1
        
print("1 |"+"X"*f)
print("2+|"+"X"*su)
print("2-|"+"X"*sl)
print("3 |"+"X"*t)
print("F |"+"X"*fa)