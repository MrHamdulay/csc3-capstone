"""Vector calculations
20/4/12
Luveshen Pillay"""
# Get VEctor A
a=input("Enter vector A:\n")
Veca=a.split()
Veca_list=[]
for dimension in Veca:
    a=eval(dimension)
    Veca_list.append(a)
    
# Get vector B
b=input("Enter vector B:\n")
Vecb=b.split()
Vecb_list=[]
for dimension in Vecb:
    c=eval(dimension)
    Vecb_list.append(c)

# vector addition
Vecadd=[]    
for i in range(len(Vecb_list)):
    d=Veca_list[i]+Vecb_list[i]
    Vecadd.append(d)
    
print("A+B =",Vecadd)

# vector multiplication
Vecmultp=0
for i in range(len(Vecb_list)):
    d=Veca_list[i]*Vecb_list[i]
    Vecmultp+=d
    

print("A.B =",Vecmultp)

# vector normalisation
normA=0
for item in Veca_list:
    sq=item**2
    normA+=sq
    anorm=normA**0.5
print("|A| = {0:0.2f}".format(anorm))
    
normB=0
for item in Vecb_list:
    sq=item**2
    normB+=sq
    bnorm=normB**0.5
print("|B| = {0:0.2f}".format(bnorm))
    
