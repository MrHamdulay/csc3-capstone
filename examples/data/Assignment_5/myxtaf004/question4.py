"""Graphs a function
Tafadzwa Moyo
14 April 2014"""

eq=input("Enter a function f(x):\n") #Gets equation
terli=[] #list of terms
coli=[] #list of coeffients
x='' 
p=0
for i in eq: #Splits the equation into terms and puts them in a list

    if i!="+" and i!="-":
        x+=i
    else:
        if p!=0:
            terli.append(x)
        if i=="+" and i!=eq[-1]:
            x='+'
        elif i=="-" and i!=eq[-1]:
            x='-'
    p+=1
terli.append(x) #Adds last term to the lists of terms
x=''
for i in terli: #Removes the variable and only leaves coeffient
    if i.find("x")==0:
        coli.append('1')    
    elif i.find('x')!=-1:
        coli.append(i[:i.find('x')])
    else:
        coli.append(i)
graph="" #empty graph string
#Makes a string of the graph
b=0
if len(coli)==2:
    b=int(coli[1])
for i in range(10, -11, -1):
    for a in range(-10, 11):
        if i==int(coli[0])*a+b:
            graph+="o"
        elif a==0 and i==0:
            graph+="+"
        elif a==0:
            graph+="|"
        elif i==0:
            graph+="-"
        else:
            graph+=" "
    graph+="\n"
print(graph)
