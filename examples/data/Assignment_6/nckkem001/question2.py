"""Program to perform calculations with supplied vectors.
Kemeshan Naicker
23 April 2014"""

def vector_calc():
    
    #Prompt user for vectors
    vA=input("Enter vector A:\n")
    vB=input("Enter vector B:\n")
    #Convert supplied vectors to 3-item lists and convert items in list to integers.
    vA=vA.split()
    vB=vB.split()
    for i in range(3):
        vA[i]=eval(vA[i])
        vB[i]=eval(vB[i])
    #Perform addition calculation.
    addv=[]
    for i in range(3):
        addv.append(vA[i]+vB[i])
    print("A+B =",addv)
    #Perform dot calculation.
    dot = 0
    for i in range(3):
        dot+=vA[i]*vB[i]
    print("A.B =",dot)
    #Perform absolute value calculations.
    addsqrsA=0
    addsqrsB=0
    for i in range(3):
        addsqrsA+=vA[i]**2
        addsqrsB+=vB[i]**2
    print("|A| = {0:0.2f}".format(addsqrsA**(1/2)))
    print("|B| = {0:0.2f}".format(addsqrsB**(1/2)))
        
if __name__=="__main__":
    vector_calc()