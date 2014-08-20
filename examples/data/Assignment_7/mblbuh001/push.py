# push.py
# Name: Buhlebezwe
# Student Number: MBLBUH001
# Date: 30 April 2014

def push_up (grid):
    """merge grid values upwards"""
    for i in range(4):
        column_list = []                                                        #create column_list
        for j in range(4):
            column_list.append(grid[j][i])                                      #append column entries of grid to column_list
        for r in range(4):
            for l in column_list:
                if type(l) != int or l==0:
                    column_list.remove(l)                                       #remove all entries of 0 or non-integer entries in column_list
        for s in range(4-len(column_list)):
            column_list.append(0)                                               #append column_list with values of 0 until len(column_list)=4
        new_column_list = []                                                    #create new_column_list
        while column_list != []:
            if len(column_list)>1:  
                if column_list[0] == column_list[1]:
                    new_column_list.append(column_list[0]+column_list[1])       #append new_column_list with column_list[0]+column_list[1] if column_list[0] == column_list[1]
                    column_list = column_list[2:]                               #slice column_list from index 2 till the end
                else:
                    new_column_list.append(column_list[0])                      #append new_column_list with entry at index 0 of column_list
                    column_list = column_list[1:]                               #slice column_list from index 1 till the end
            else:
                new_column_list.append(column_list[0])                          #append new_column_list with last entry of column_list
                column_list = column_list[1:]                                   #slice column_list from index 1 till the end
        while len(new_column_list)>1:
            if new_column_list[0] == 0:
                new_column_list = new_column_list[1:]                           #slice new_column_list from index 1 till the end if 0 is the first entry,else break
            else: break     
        for k in range(4-len(new_column_list)):
            new_column_list.append(0)                                           #append new_column_list with values of 0 until len(new_column_list)=4
        for j in range(4):
            grid[j][i] = new_column_list[j]                                     #fill column of grid with corresponding entries in new_column_list

def push_down (grid):
    """merge grid values downwards"""
    for i in range(4):
        column_list = []                                                        #create column_list
        for j in range(4):
            column_list.append(grid[j][i])                                      #append column entries of grid to column_list
        column_list.reverse()                                                   #reverse column_list
        for r in range(4):
            for l in column_list:
                if type(l) != int or l==0:
                    column_list.remove(l)                                       #remove all entries of 0 or non-integer entries in column_list
        for s in range(4-len(column_list)):
            column_list.append(0)                                               #append column_list with values of 0 until len(column_list)=4
        new_column_list = []                                                    #create new_column_list
        while column_list != []:
            if len(column_list)>1:  
                if column_list[0] == column_list[1]:
                    new_column_list.append(column_list[0]+column_list[1])       #append new_column_list with column_list[0]+column_list[1] if column_list[0] == column_list[1]
                    column_list = column_list[2:]                               #slice column_list from index 2 till the end
                else:
                    new_column_list.append(column_list[0])                      #append new_column_list with entry at index 0 of column_list
                    column_list = column_list[1:]                               #slice column_list from index 1 till the end
            else:
                new_column_list.append(column_list[0])                          #append new_column_list with last entry of column_list
                column_list = column_list[1:]                                   #slice column_list from index 1 till the end
        while len(new_column_list)>1:
            if new_column_list[0] == 0:
                new_column_list = new_column_list[1:]                           #slice new_column_list from index 1 till the end if 0 is the first entry,else break
            else: break
        for k in range(4-len(new_column_list)):
            new_column_list.append(0)                                           #append new_column_list with values of 0 until len(new_column_list)=4
        for j in range(4):
            grid[3-j][i] = new_column_list[j]                                   #fill column of grid with corresponding entries in new_column_list

def push_left (grid):
    """merge grid values left"""
    for i in range(4):
        column_list = []                                                        #create column_list
        for j in range(4):
            column_list.append(grid[i][j])                                      #append column entries of grid to column_list
        for r in range(4):
            for l in column_list:
                if type(l) != int or l==0:
                    column_list.remove(l)                                       #remove all entries of 0 or non-integer entries in column_list
        for s in range(4-len(column_list)):
            column_list.append(0)                                               #append column_list with values of 0 until len(column_list)=4
        new_column_list = []                                                    #create new_column_list
        while column_list != []:
            if len(column_list)>1:  
                if column_list[0] == column_list[1]:
                    new_column_list.append(column_list[0]+column_list[1])       #append new_column_list with column_list[0]+column_list[1] if column_list[0] == column_list[1]
                    column_list = column_list[2:]                               #slice column_list from index 2 till the end
                else:
                    new_column_list.append(column_list[0])                      #append new_column_list with entry at index 0 of column_list
                    column_list = column_list[1:]                               #slice column_list from index 1 till the end
            else:
                new_column_list.append(column_list[0])                          #append new_column_list with last entry of column_list
                column_list = column_list[1:]                                   #slice column_list from index 1 till the end
        while len(new_column_list)>1:
            if new_column_list[0] == 0:
                new_column_list = new_column_list[1:]                           #slice new_column_list from index 1 till the end if 0 is the first entry,else break
            else: break        
        for k in range(4-len(new_column_list)):
            new_column_list.append(0)                                           #append new_column_list with values of 0 until len(new_column_list)=4
        for j in range(4):
            grid[i][j] = new_column_list[j]                                     #fill row of grid with corresponding entries in new_column_list
    
def push_right (grid):
    """merge grid values right"""
    for i in range(4):
        column_list = []                                                        #create column_list
        for j in range(4):
            column_list.append(grid[i][j])                                      #append column entries of grid to column_list
        column_list.reverse()                                                   #reverse column_list
        for r in range(4):
            for l in column_list:
                if type(l) != int or l==0:
                    column_list.remove(l)                                       #remove all entries of 0 or non-integer entries in column_list
        for s in range(4-len(column_list)):
            column_list.append(0)                                               #append column_list with values of 0 until len(column_list)=4
        new_column_list = []                                                    #create new_column_list
        while column_list != []:
            if len(column_list)>1:  
                if column_list[0] == column_list[1]:
                    new_column_list.append(column_list[0]+column_list[1])       #append new_column_list with column_list[0]+column_list[1] if column_list[0] == column_list[1]
                    column_list = column_list[2:]                               #slice column_list from index 2 till the end
                else:
                    new_column_list.append(column_list[0])                      #append new_column_list with entry at index 0 of column_list
                    column_list = column_list[1:]                               #slice column_list from index 1 till the end
            else:
                new_column_list.append(column_list[0])                          #append new_column_list with last entry of column_list
                column_list = column_list[1:]                                   #slice column_list from index 1 till the end
        while len(new_column_list)>1:
            if new_column_list[0] == 0:
                new_column_list = new_column_list[1:]                           #slice new_column_list from index 1 till the end if 0 is the first entry,else break
            else: break          
        for k in range(4-len(new_column_list)):
            new_column_list.append(0)                                           #append new_column_list with values of 0 until len(new_column_list)=4
        for j in range(4):
            grid[i][3-j] = new_column_list[j]                                   #fill row of grid with corresponding entries in new_column_list