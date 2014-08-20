import math
vectA = [] # empty list to store vector A
vectB = [] # empty lis to store vector B

A = input('Enter vector A:\n') #propmt to enter vector(components separated by space)
co_ordsA = A.split() #splits single string entry into 3 components
for i in range(len(co_ordsA)): #to iterate through 3 string components of 'co-ords'
    vectA.append(eval(co_ordsA[i])) #appends numeric value of each component to list 'vectA'
B = input('Enter vector B:\n') #same process for vector B
co_ordsB = B.split()
for j in range(len(co_ordsB)):
    vectB.append(eval(co_ordsB[j]))

def vect_add(vectA,vectB): #function for vector addition
    vectC = [] #empty string to store added vector components
    for a in range(len(vectA)): #to iterate through components of vector A
        for b in range(len(vectB)): #nested loop to iterate through components of vector B
            if a == b: #when sequence number of iterations are equal
                vectC.append(int(vectA[a])+int(vectB[b])) #adds components of A and B at same sequence number and appends value to components in vector C
            else:
                continue #continue iterating until sequence numbers are equal again
    txt_line = '{0}+{1} = {2}'.format('A','B',vectC)
    print(txt_line) 

def dot_prod(vectA,vectB): #function for dot product of 2 vectors
    vectD = [] 
    for a in range(len(vectA)):
        for b in range(len(vectB)):
            if a == b:
                vectD.append(int(vectA[a])*int(vectB[b])) #same process as for addition function except multiplying like components
            else:
                continue
    dot_product = 0
    for x in range(len(vectD)): #loop to add components in vector D
        dot_product += (vectD[x])
    txt_line = '{0}.{1} = {2}'.format('A','B',dot_product)
    print(txt_line)

def normA(vectA): #normalisation function for vector A
    normal = 0
    for x in range(len(vectA)): #loop to square components in vector
        normal += (vectA[x])**2
        norm_fin = math.sqrt(float(normal)) #takes square root of sum of squared components
    txt_line1 = '|{0}| = {1:.2f}'.format('A',norm_fin)
    print(txt_line1)

def normB(vectB):
    normal = 0
    for x in range(len(vectB)):
        normal += (vectB[x])**2
        norm_fin = math.sqrt(float(normal))        
    txt_line2 = '|{0}| = {1:.2f}'.format('B',norm_fin)
    print(txt_line2) #same process as for vector A normalisation
            
vect_add(vectA,vectB)
dot_prod(vectA,vectB)
normA(vectA)
normB(vectB)

#NOTE: tried to have one function for normalisation, but when vectA = vectB, print statement which was meant to be |B| became |A|.