"""Yonela Ford
30 April 2014
grid merging routines"""


"""merge grid values upwards"""
def push_up (grid):

#create a list with the column and append this list with column entries
    for a in range(4):
        column= []                                                        
        for j in range(4):
            column.append(grid[j][a]) 
        #take out all entries of 0 or entries that are not integers in the list
        for i in range(4):
            for b in column:
                if type(b) != int or b==0:
                    column.remove(b) 
        #add onto list of column until len(column)==4
        for s in range(4-len(column)):
            column.append(0)
        #make a new list
        new_column= []                                                    
        while column!= []:
            if len(column)>1:
                #onto the new list, add the first item on column list and the second if the first and second items are the same
                if column[0] == column[1]:
                    new_column.append(column[0]+column[1])       
                    column= column[2:]                               
                else:
                    new_column.append(column[0])                      
                    column= column[1:]                               
            else:
                 #append new_column with last entry of column 
                new_column.append(column[0])                         
                #slice column from index 1 till the end 
                column= column[1:]                                   
        while len(new_column)>1:
            if new_column[0] == 0:
                new_column= new_column[1:]                           
            else: break
        #add onto new_column with values of 0 until len(new_column)=4    
        for k in range(4-len(new_column)):
            new_column.append(0)  
        #fill up column of grid with the related values in new_column                                         
        for j in range(4):
            grid[j][a] = new_column[j]                                     

"""merge grid values downwards"""
def push_down (grid):
    
    for k in range(4):
        column= []                                                        
        for l in range(4):
            column.append(grid[l][k])                                      
        column.reverse()                                                   
        for a in range(4):
            for x in column:
                if type(x) != int or x==0:
                    column.remove(x)                                      
        for s in range(4-len(column)):
            column.append(0)                                               
        new_column= []                                                    
        while column!= []:
            if len(column)>1:  
                if column[0] == column[1]:
                    new_column.append(column[0]+column[1])       
                    column= column[2:]                               
                else:
                    new_column.append(column[0])                      
                    column= column[1:]                               
            else:
                new_column.append(column[0])                         
                column= column[1:]                                   
        while len(new_column)>1:
            if new_column[0] == 0:
                new_column= new_column[1:]                           
            else: break
        for d in range(4-len(new_column)):
            new_column.append(0)                                          
        for j in range(4):
            grid[3-j][k] = new_column[j] 
            
"""merge grid values left"""
def push_left (grid):
    #make a new list and add onto it the column entries of the grid
    for d in range(4):
        column = []                                                        
        for j in range(4):
            column.append(grid[d][j]) 
        #remove all entries of 0 or non-integer entries in column                                   
        for t in range(4):
            for g in column:
                if type(g) != int or g==0:
                    column.remove(g)  
        #attach column with values of 0 until len(column)=4                                    
        for s in range(4-len(column)):
            column.append(0)                                               
        new_column = []                                                    
        while column != []:
            if len(column)>1: 
                #onto the new list, add the first item on column list and the second if the first and second items are the same
                if column[0] == column[1]:
                    new_column.append(column[0]+column[1])       
                    column = column[2:]                               
                else:
                    #append new_column with entry at index 0 of column
                    new_column.append(column[0])                      
                    column = column[1:]                               
            else:
                #append new_column with last entry of column
                new_column.append(column[0])                          
                column = column[1:]                                   
        while len(new_column)>1:
            if new_column[0] == 0:
                new_column = new_column[1:]                           
            else: break
        #append new_column with values of 0 until len(new_column)=4        
        for k in range(4-len(new_column)):
            new_column.append(0) 
        #fill row of grid with corresponding entries in new_column                                          
        for j in range(4):
            grid[d][j] = new_column[j]   
            
"""merge grid values right"""    
def push_right (grid):
     #make a new list and add onto it the column entries of the grid
    for i in range(4):
        column = []                                                        
        for j in range(4):
            column.append(grid[i][j])                                      
        column.reverse() 
        #delete all entries of 0 or non-integer entries in column                                                 
        for r in range(4):
            for l in column:
                if type(l) != int or l==0:
                    column.remove(l)  
        #append column with values of 0 until len(column)=4                                    
        for s in range(4-len(column)):
            column.append(0)                                               
        new_column = []                                                    
        while column != []:
            if len(column)>1:  
                if column[0] == column[1]:
                #onto the new list, add the first item on column list and the second if the first and second items are the same
                    
                    new_column.append(column[0]+column[1])       
                    column = column[2:]                              
                else:
                    new_column.append(column[0])                      
                    column = column[1:]                               
            else:
                new_column.append(column[0])                          
                column = column[1:]                                   
        while len(new_column)>1:
            if new_column[0] == 0:
                new_column = new_column[1:]                           
            else: break  
        #append new_column with values of 0 until len(new_column)=4       
        for k in range(4-len(new_column)):
            new_column.append(0)  
        #fill row of grid with corresponding entries in new_column                                        
        for j in range(4):
            grid[i][3-j] = new_column[j]                                   

