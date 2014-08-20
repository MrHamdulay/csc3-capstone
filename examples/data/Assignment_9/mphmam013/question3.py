"""Mphuthi Mamorena
assignment 9
question 3"""


#input values 

lines = []
for i in range(9):
    line = input()
    lines.append(line)


# make a 2-d array
newlist=[]

for i in range(len(lines)):
    nolist=[]
    for f in range(len(lines[i])):
        nolist.append(lines[i][f])
    newlist.append(nolist)#adding a list to list
    
# determining the validity horizontally
def horizontal(newlist):
    valid=True
    m=0
    for i in range(len(newlist)):
        for f in range(len(newlist[i])):
            if newlist[i].count(newlist[i][f])>1:
                valid='para'
    return valid

# determining the validity vertically

def vertical(newlist):
    valid=True
    m=0
    nlis=[]
    for i in range(len(newlist)):
        while m<len(newlist[i]):
            nlis.append(newlist[i][m])
            for j in range(len(nlis)):
                if nlis.count(nlis[j])>1:
                    valid='para'
        m+=1
    return valid   

            
def in3grid(newlist):
    valid=False
    sm1=[]
    for i in range(3):
        sm1.append(newlist[i][:3])
    
    sm2=[]
    for i in range(3):
        sm2.append(newlist[i][3:6])
    
    sm3=[]
    for i in range(3):
        sm3.append(newlist[i][6:9]) 
        
    sm4=[]
    for i in range(3,6):
        sm4.append(newlist[i][:3])
        
    sm5=[]
    for i in range(3,6):
        sm5.append(newlist[i][3:6]) 
        
    sm6=[]
    for i in range(6,9):
        sm6.append(newlist[i][6:9])
        
    sm7=[]
    for i in range(6,9):
        sm7.append(newlist[i][:3])   
    
    sm8=[]
    for i in range(6,9):
        sm8.append(newlist[i][3:6])   
        
    sm9=[]
    for i in range(6,9):
        sm9.append(newlist[i][6:9])
        
    if horizontal(sm1)==False or vertical(sm1)==False:
        valid='para'
    elif horizontal(sm2)==False or vertical(sm2)==False:
        valid='para'  
    elif horizontal(sm3)==False or vertical(sm3)==False:
        valid='para'    
    elif horizontal(sm4)==False or vertical(sm4)==False:
        valid='para'    
    elif horizontal(sm5)==False or vertical(sm5)==False:
        valid='para'   
    elif horizontal(sm6)==False or vertical(sm6)==False:
        valid='para'     
    elif horizontal(sm7)==False or vertical(sm7)==False:
        valid='para'     
    elif horizontal(sm8)==False or vertical(sm8)==False:
        valid='para' 
    elif horizontal(sm9)==False or vertical(sm9)==False:
        valid='para'     
    else:
        valid=True
    return valid

if horizontal(newlist)=='para':
    print("Sudoku grid is not valid")
elif vertical(newlist)=='para':
    print("Sudoku grid is not valid")
elif in3grid(newlist)=='para':
    print("Sudoku grid is not valid")
else:
    print("Sudoku grid is valid")
    
        
    
    
                    
        
           

    
            
            
                       
        
    



