"""Thrianka Naidoo
NDXTHR005
assigment8,q2"""

m = input("Enter a message:\n")#input for user

def Pairs(m):
    if m=="":                  #stopping condition1
        return 0
    elif(len(m)==1):           #stopping condition2
        return 0
    else:
        if m[0]==m[1]:
            m=m[2:]
            return 1+Pairs(m)
        else:
            return Pairs(m[1:])
        
new_m = Pairs(m)               #gets valus
print("Number of pairs:",new_m)