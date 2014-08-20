#Dhriven Hamlall

line2d=[]
decision=False

for i in range(9):
    line=input()
    line1d=[]
    for j in range(9):
        
        line1d.append(line[j])
    line2d.append(line1d)    #9*9 grid
    


for k in range(9):
#col = 1, k is the col here
    colList = [ ]
    for i in range(len(line2d)):
        colList += [ line2d[i][k] ]
        
        for i in range(len(colList)-1):
            if (colList[i]==colList[i+1]):
                decision=True
                
                
#if decision:
#    print("Invalid")               


        
    #elif (colList[0]==colList[len(colList)-1]):
    #    print("Invalid")
    

#row = 1
#rowList = [ ]

for j in range(9):
    rowList = line2d[j]
    
    for i in range(8):
        if (rowList[i]==rowList[i+1]):
            decision=True
#===========================================================================            
#if decision:
#    print("Invalid")
#===========================================================================  



                
#print(x1)
      
#============================================================================

x1=[]  
for i in range(3):
    for j in range(3):
        x1.append(line2d[i][j])
#print(x1)
for i in range (8):
    if x1[i]==x1[i+1]:
        decision=True
        
#if decision:
#    print("Invalid upper left end")
    
#=====================================================================
x2=[]  
for i in range(3):
    for j in range(3,6):
        x2.append(line2d[i][j])
#print(x2)       
for i in range (8):
    if x2[i]==x2[i+1]:
        decision=True
        
#if decision:
#    print("Invalid upper middle ")
        
#=======================================================================
x3=[]  
for i in range(3):
    for j in range(6,9):
        x3.append(line2d[i][j])
#print(x3)       
for i in range (8):
    if x3[i]==x3[i+1]:
        decision=True
        #print("Invalid upper right end")    
    
#==========================================================================================
x4=[]  
for i in range(3,6):
    for j in range(3):
        x4.append(line2d[i][j])
#print(x4)
for i in range (8):
    if x4[i]==x4[i+1]:
        decision=True
        #print("middle left end")
        
if line2d[1][5] == line2d[2][4]:decision=True
if line2d[0][6] == line2d[2][8]:decision=True
        
#========================================================================================
x5=[]  
for i in range(3,6):
    for j in range(3,6):
        x5.append(line2d[i][j])
        
#print(x5)
for i in range (8):
    if x5[i]==x5[i+1]:
        decision=True
        #print("middle middle")
        

        
#========================================================================================
x6=[]  
for i in range(3,6):
    for j in range(6,9):
        x6.append(line2d[i][j])
        
#print(x6)
for i in range (8):
    if x6[i]==x6[i+1]:
        decision=True
        #print("middle right end")
        
#========================================================================================
x7=[]  
for i in range(6,9):
    for j in range(0,3):
        x7.append(line2d[i][j])
                
#print(x7)
for i in range (8):
    if x7[i]==x7[i+1]:
        decision=True
        #print("bottom left end")
#===================================================================
        
x8=[]  
for i in range(6,9):
    for j in range(3,6):
        x8.append(line2d[i][j])
                        
#print(x8)
for i in range (8):
    if x8[i]==x8[i+1]:
        decision=True
        #print("middle end")
        
#========================================================================

x9=[]  
for i in range(6,9):
    for j in range(6,9):
        x9.append(line2d[i][j])
                        
#print(x9)
for i in range (8):
    if x9[i]==x9[i+1]:
        decision=True
        #print("bottom left end")
        
if decision==True:
    print("Sudoku grid is not valid")
else:
    print("Sudoku grid is valid")