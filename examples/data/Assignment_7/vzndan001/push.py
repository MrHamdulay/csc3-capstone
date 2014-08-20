"""pushing tiles in different directions
danica van der zandt
2 may 2014"""


#merge grid values upwards
def push_up (grid):
    for j in range(0,4):
        temp_list=[]
        for i in range(0,4):
            temp_list.append(grid[i][j])
       
        for k in range(0,4):
            if temp_list[k]=="0":
                del temp_list[k]
                temp_list.append("0")
                
        for m in range(0,3):
            if temp_list[m]==temp_list[m+1]:
                temp_list[m]=temp_list[m]+temp_list[m+1]
                del temp_list[m+1]
                temp_list.append("0")
                
        for i in range(0,4):
            grid[i][j]=temp_list[i]
            
def push_down (grid):
    """merge grid values downwards"""
    for j in range(0,4):
        temp_list=[]
        for i in range(0,4):
            temp_list.append(grid[i][j])
        temp_list=temp_list[::-1]
          
        for k in range(0,4):
            if temp_list[k]=="0":
                del temp_list[k]
                temp_list.append("0")
                   
        for m in range(0,3):
            if temp_list[m]==temp_list[m+1]:
                temp_list[m]=temp_list[m]+temp_list[m+1]
                del temp_list[m+1]
                temp_list.append("0")
                   
        temp_list=templist[::-1]        
        for i in range(0,4):
            grid[i][j]=temp_list[i]
            

def push_left (grid):
    """merge grid values left"""

def push_right (grid):
    """merge grid values right""" 