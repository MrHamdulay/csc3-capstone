
def create_grid(arr):
    
    for i in range(4):
        arr.append([0,0,0,0])
        
    return arr



def check_won (arr):
    flag=False
    
    for row in range(4):
        
        for col in range(4):
            
            if(arr[row][col]>=32):
                flag=True
    return flag




def copy_grid(arr):
    
    arr2=[['','','',''],['','','',''],['','','',''],['','','','']]
    for row in range(4):
        for col in range(4):
            arr2[row][col]=arr[row][col]
            
    return arr2




def check_lost(arr):
    flag=True
    for row in range(4):
        
        for col in range(4):
            
            if(grid[row][col]==0):
                flag=False
            if(col<3 and arr[row][col]==arr[row][col+1]):
                flag=False
            if(row<3 and grid[row][col]==grid[row+1][col]):
                flag=False
    
    return flag




def grid_equal (arrA, arrB):
    flag=False
    if(arrA==arrB):
        flag=True
    return flag




def print_grid(arr):
    
    print("+--------------------+")
    
    for row in range(4):
        print("|",end="")
        
        for col in range(4):
            if(arr[row][col]==0):
                print("{:<5}".format(" "),end="")
            else:
                print("{:<5}".format(arr[row][col]),end="")
                
        print("|",end="")    
        print("")
    print("+--------------------+")
    
    
    
