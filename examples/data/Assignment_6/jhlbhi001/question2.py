import math
#get numbers
a=input("Enter vector A:\n")
b=input("Enter vector B:\n")
vectora=a.split(" ")
vectorb=b.split(" ")
va = vectora
vb = vectorb
#perform operation
addition=[]
answer=0
for i in range (len(vectora)):
    x=(vectora[i]+"+"+vectorb[i])
    x=eval(x)
    addition.append(x)
print("A+B =",addition)
for i in range(len(vectora)):
    y=(vectora[i]+"*"+vectorb[i])
    y=eval(y)    
    answer+=y
print("A.B =",answer)    
#sqaureroot



def sqr(list1):
    answer2 = 0
    for c in range(len(list1)):
        
        x = ("("+list1[c]+')**2')
        x = eval(x)
        answer2 += x
    y = math.sqrt(answer2)
    po = '{0:.2f}'.format(y)
    return(po)

norma = sqr(va)

print("|A| =",norma)

normb = sqr(vb)

print("|B| =",normb)