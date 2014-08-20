#program to calculate vectors in 3D
#kiyarah pillay
#23 april 2014
import math
vector_A=(input("Enter vector A:\n"))
vector_B=(input("Enter vector B:\n"))                                                                                                                          
a=vector_A.split()
b=vector_B.split()
ans=[]
#create loop, temporary a and b values for this addition calculation
for i in range (3):
    temp_a= eval(a[i])
    temp_b=eval(b[i])
    ab=temp_a + temp_b
#add each new value of a+b to existing list of addition
    ans.append(ab)
print ("A+B =", ans)
#equate the answer to 0, values will now be stored cumulatively in ans2
ans2=0
#create another loop for another set of temporary values of a and b when they undergo multiplication
for i in range (3):
    temp_a2=eval(a[i])
    temp_b2=eval(b[i])
    ab2=temp_a2*temp_b2
    ans2=ans2+ab2

print ("A.B =", ans2)
#help from vula, square and square rooted
ansa_total= eval(a[0])**2 + eval(a[1])**2 + eval(a[2])**2
print ("|A| = " , '%0.2f' %(math.sqrt(ansa_total)) ,sep='')
ansb_total= eval(b[0])**2 + eval(b[1])**2 + eval(b[2])**2
print ("|B| = " , '%0.2f' %(math.sqrt(ansb_total)) ,sep='')







