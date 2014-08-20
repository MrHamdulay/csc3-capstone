import math

va=input("Enter vector A:\n")
a=va.split(" ")
vb=input("Enter vector B:\n")
b=vb.split(" ")

def addi():
    one=int(a[0])+int(b[0])
    two=int(a[1])+int(b[1])
    three=int(a[2])+int(b[2])
    
    print("A+B = ["+str(one)+", " + str(two)+", " +str(three)+"]")

def pro():
    one=int(a[0])*int(b[0])
    two=int(a[1])*int(b[1])
    three=int(a[2])*int(b[2])    
    
    pro=one+two+three
    
    print("A.B = "+str(pro))
    
    
def nor():
    one=(int(a[0]))**2
    two=(int(a[1]))**2
    three=(int(a[2]))**2
    
    nor=one+two+three
    norm=(math.sqrt(nor))
    
    print("|A| = {0:.2f}".format(norm))
    
    one1=(int(b[0]))**2
    two2=(int(b[1]))**2
    three3=(int(b[2]))**2
    
    norr=one1+two2+three3
    normm=(math.sqrt(norr))
    
    print("|B| = {0:.2f}".format(normm))
    
addi()
pro()
nor()

