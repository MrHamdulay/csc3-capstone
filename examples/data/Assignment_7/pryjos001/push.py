def push_up(grid):
    import copy
    new_grid=copy.deepcopy(grid)
    for i in range (4): #goes through each column
        for j in range(4): #goes through each value in each column
            if new_grid[j][i]==0:
                side_list=[] #Create new list in which to place column to be edited
                
                for n in range (4):
                    x=new_grid[n][i]
                    side_list.append(x)
                
                for x in range(len(side_list)-1,-1,-1): #Check through values in side_list
                    if side_list[x]==0:
                        del side_list[x] #If zero, delete it from list
                        side_list.append(0) #add zero to end to list if a value is deleted
                print(side_list)

                
                for val in range(4):
                    new_grid[val][i]=side_list[val]
                break
    return (new_grid)