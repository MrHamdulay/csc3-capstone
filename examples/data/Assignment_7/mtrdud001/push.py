"""Adding, subtracting and merging 4x4 grid
Dudley Mutero
1/5/14"""

def push_up (grid):
    """merge grid values upwards"""
    for row in range (4):
        temp_list=[]
        list1=[]
        for col in range (4):
            if grid[col][row]==0:#taking out non zero terms in the list from the grid and putting them in my new list1
                continue
            else:
                list1.append(grid[col][row])
        for i in range (4-len(list1)):
            list1.append (0)#adding back the zero terms; htus putting the xero terms at the end of list1
        for count in range (3): #checking if adjacent terms are equal and thus 
            if list1[count]==list1[count+1]:
                list1[count]+=list1[count+1] 
                list1[count+1]=0
        for m in range(4):#transferring values in list1 to temp list for further procesing
            if list1[m]!=0:
                temp_list.append(list1[m])
        for j in range (4-len(temp_list)):#adding zeros at end of the row
            temp_list.append(0)
        for g in range(4): #returning the new merged numbers back to original grid
            grid[g][row]=temp_list[g]
            
            
def push_down (grid):
    """merge grid values downwards"""
    for row in range (4):
            temp_list=[]
            list1=[]
            for col in range (4):
                if grid[col][row]==0:#taking out non zero terms in the list from the grid and putting them in my new list1
                    continue
                else:
                    list1.append(grid[col][row])
            for i in range (4-len(list1)):
                list1.append (0)#adding back the zero terms; htus putting the xero terms at the end of list1
            for count in range (3,0,-1): #checking if adjacent terms are equal and thus 
                if list1[count]==list1[count-1]:
                    list1[count]+=list1[count-1] 
                    list1[count-1]=0
            for m in range(4):#transferring values in list1 to temp list for further procesing
                if list1[m]!=0:
                    temp_list.append(list1[m])
            for j in range (4-len(temp_list)):#adding zeros at end of the row
                temp_list.insert(0,0)
            for g in range(4): #returning the new merged numbers back to original grid
                grid[g][row]=temp_list[g]    

def push_left (grid):
    """merge grid values left"""
    for row in range (4):
        temp_list=[]
        list1=[]
        for col in range (4):
            if grid[row][col]==0:
                continue #taking out non zero terms in the list from the grid and putting them in my new list1
            else:
                list1.append(grid[row][col])
        for i in range (4-len(list1)):
            list1.append (0)#adding back the zero terms; htus putting the xero terms at the end of list1
        for count in range (3): #checking if adjacent terms are equal and thus 
            if list1[count]==list1[count+1]:
                list1[count]+=list1[count+1] 
                list1[count+1]=0
        for m in range(4):#transferring values in list1 to temp list for further procesing
            if list1[m]!=0:
                temp_list.append(list1[m])
        for j in range (4-len(temp_list)):#adding zeros at end of the row
            temp_list.append(0)
        for g in range(4): #returning the new merged numbers back to original grid
            grid[row][g]=temp_list[g]    
            
def push_right (grid):
    """merge grid values right"""
    for row in range (4):
        temp_list=[]
        list1=[]
        for col in range (4):
            if grid[row][col]==0: #taking out non zero terms in the list from the grid and putting them in my new list1
                continue
            else:
                list1.append(grid[row][col])
        for i in range (4-len(list1)):
            list1.append (0)#adding back the zero terms; htus putting the xero terms at the end of list1
        for count in range (3): #checking if adjacent terms are equal and thus 
            if list1[count]==list1[count+1]:
                list1[count]+=list1[count+1] 
                list1[count+1]=0
        for m in range(4):#transferring values in list1 to temp list for further procesing
            if list1[m]!=0:
                temp_list.append(list1[m])
        for j in range (4-len(temp_list)):#adding zeros at end of the row
            temp_list.insert(0,0)
        for g in range(4): #returning the new merged numbers back to original grid
            grid[row][g]=temp_list[g]    
