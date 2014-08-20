""" Bella Gorham
marks
20/04/2014"""

values = input("Enter a space-separated list of marks:\n")
marks = values.split()


one = []
twoplus=[]
twominus=[]
three=[]
F=[]
for i in marks:
    i = eval(i)
    if i < 50:
        F.append(i)
    elif 50<=i < 60:
        three.append(i)
    elif 60 <= i < 70 :
        twominus.append(i)
    elif 70 <= i < 75 :
        twoplus.append(i)
    elif i >= 75:
        one.append(i)

display = "1 |{0}\n2+|{1}\n2-|{2}\n3 |{3}\nF |{4}"


Fx= len(F)*"X"

onex = len(one)*"X"
twoplusx=len(twoplus)*"X"
twominusx=len(twominus)*"X"
threex=len(three)*"X"

print(display.format(onex,twoplusx,twominusx,threex,Fx))

        
        

        
    
