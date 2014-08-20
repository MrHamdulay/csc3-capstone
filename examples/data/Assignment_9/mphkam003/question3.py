"""progam to check weather a sudoku grid is valid
Kamogelo Mphela
11 may 2014"""
 
    
def twoD(k):
    """store input to 2d array"""
    real_list=[]
    for i in range(9):
        j = k[:9]
        k=k[9:]
        real_list.append(j)
    
    
    vertical = []
    y = 0
    h =0
    j = len(real_list[0])
    for k in range(len(real_list[0])):
        for i in range(len(real_list)):
            vertical.append(real_list[i][k])
        
    for p in range(len(real_list[0])):
        y += check_row(vertical[h:j])
        h += len(real_list[0])
        j += len(real_list[0])
        
    
    
    x=0
    for i in range(9):
        
        x+=check_row(real_list[i])
    
    if x + y  == 0:
        print("Sudoku grid is valid")
    else:
        print("Sudoku grid is not valid")    
    
def check_row(s):
    """return 0 if sudoku is valid horizontally else return 1"""
    
    if len(s)==1:
        return 0
    else:
        for i in range(1,len(s)):
            if s[0] == s[i]:
                return 1
        else:
            return check_row(s[1:])
        
def check_col(s):
    """return 0 if sudoku is valid vertically else return 1"""
    if len(s)==1:
            return 0
    else:
        for i in range(1,len(s)):
            if s[0] == s[i]:
                return 1
            else:
                return check_col(s[1:])        
    
            
            
w = []
v = []
for n in range(9):
    g =input("")
    w.append(g)
for i in w:
    for k in i:
        v.append(k)

twoD(v)    

            


