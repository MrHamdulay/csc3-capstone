list_A=[]  #initialize list a 
print("Enter vector A:")

a=input()
a=a.split()
k=len(a)   
for i in range(k) :
    
    b=a[i]
    list_A.append(b)
    
    
list_B=[]

print("Enter vector B:")

a=input()
a=a.split()
k=len(a)

for i in range(k) :
    
    b=a[i]
    list_B.append(b)


list_C=list_A+list_B  #Performing addition to list_C

answer=[]

for i in range(0,3):
    
    b=eval(list_C[i]) + eval(list_C[i+3])
    answer.append(b)
    
    y = answer  #chnge to smaller name, output still the same
    
print("A+B","=",y)


ans=0    # dot product,  

for i in range (0,3):
    
    b=eval(list_C[i]) * eval(list_C[i+3])
    ans+=b
    
print("A.B","=",ans)


import math
answerA=0  
answerB=0

for i in range (0,3):
    
    b=eval(list_A[i])
    
    z=b*b 
    answerA+=z
    
    q=eval(list_B[i])   #here  
    e=q*q
    answerB+=e
    
result_a = math.sqrt(answerA)    #ans to result_a
result_b = math.sqrt(answerB)

result_a=round(result_a,2)
result_b=round(result_b,2)

form_ra="{0:.2f}".format(result_a)  #format specifiers, form_ra
form_rb="{0:.2f}".format(result_b)

print("|A|","=",form_ra)
print("|B|","=",form_rb)

    