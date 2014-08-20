"""Assignment 6 push module
merges adjacent tiles 
Shaheen Karodia
KRDSHA003"""



def push_up (grid):
    """merge grid values upwards"""
       
    for col in range(4):

        inter_list=[]  #intitlise the list where merging will take place
        for row in range(4):
            inter_list.append(grid[row][col])
            
        if inter_list.count(0) !=4:     #check that the list isnt just zeros
                 
            final_list=[] 
            while 0 in inter_list:
                inter_list.remove(0)    #remove all the 0s from the list
                
                
            while len(inter_list) >0:
                
                if len(inter_list)>1:
                    if inter_list[0]==inter_list[1]:   #checks if the first two items in the list are equal
                        final_list.append(2*inter_list[0])     #append the merged value to the new list
                        inter_list.remove(inter_list[0])     #remove both values from the inter_list
                        inter_list.remove(inter_list[0])
                    else:
                        final_list.append(inter_list[0])     # add first item to final_list
                        inter_list.remove(inter_list[0])     #remove first from the inter_list
                        
                if len(inter_list)==1:               #checks if there is one item left in interlist and adds it to final list
                    final_list.append(inter_list[0])
                    inter_list.remove(inter_list[0])
                    
            #ensure final_list has 4 items
            
            while len(final_list) <4:
                final_list.append(0)     #fill the rest of list with zeros
                    
          
            #replace values in original grid
            j=0
            for i in final_list:
                grid[j][col]=i
                j+=1                  
    return grid                               
                            
   

def push_down (grid):
    """merge grid values downwards"""
    for col in range(4):
        inter_list=[]  #intitlise the inter_list
        for row in range(3,-1,-1):
            inter_list.append(grid[row][col])
            
        if inter_list.count(0) !=4:     #check that the list isnt just zeros
                  
            final_list=[] 
            while 0 in inter_list:
                inter_list.remove(0)    #remove all the 0s from the list
                
                
            while len(inter_list) >0:
                
                if len(inter_list)>1:
                    if inter_list[0]==inter_list[1]:   #checks if the first two items in the list are equal
                        final_list.append(2*inter_list[0])     #append the merged value to the new list
                        inter_list.remove(inter_list[0])     #remove both values from the inter_list
                        inter_list.remove(inter_list[0])
                    else:
                        final_list.append(inter_list[0])     # add first item to final_list
                        inter_list.remove(inter_list[0])     #remove first from the inter_list
                        
                if len(inter_list)==1:               #checks if there is one item left in interlist and adds it to final list
                    final_list.append(inter_list[0])
                    inter_list.remove(inter_list[0])
                    
            #ensure final_list has 4 items
            
            while len(final_list) <4:
                final_list.append(0)     #fill the rest of list with zeros
          
                  
   
                      
                      
                    #replace values in original grid
            j=0
            final_list.reverse()
            for i in final_list:
                grid[j][col]=i
                j+=1                            
    
    return grid               
                   
                                    
                   

def push_left (grid):
    """merge grid values left"""
    for row in range(4):
        inter_list=[]  #intitlise inter_list
        for col in range(4):
            inter_list.append(grid[row][col])
            
        if inter_list.count(0) !=4:     #check that the list isnt just zeros
                                           
            final_list=[] 
            while 0 in inter_list:
                inter_list.remove(0)    #remove all the 0s from the list
                
                
            while len(inter_list) >0:
                
                if len(inter_list)>1:
                    if inter_list[0]==inter_list[1]:   #checks if the first two items in the list are equal
                        final_list.append(2*inter_list[0])     #append the merged value to the new list
                        inter_list.remove(inter_list[0])     #remove both values from the inter_list
                        inter_list.remove(inter_list[0])
                    else:
                        final_list.append(inter_list[0])     # add first item to final_list
                        inter_list.remove(inter_list[0])     #remove first from the inter_list
                        
                if len(inter_list)==1:               #checks if there is one item left in interlist and adds it to final list
                    final_list.append(inter_list[0])
                    inter_list.remove(inter_list[0])
                    
            #ensure final_list has 4 items
            
            while len(final_list) <4:
                final_list.append(0)     #fill the rest of list with zeros            
                                
             
                                
            #replace values in original grid
            j=0
            for i in final_list:
                grid[row][j]=i
                j+=1                                  

    return grid



def push_right (grid):
    """merge grid values right"""   
    for row in range(4):
            inter_list=[]  #intitlise inter_list
            for col in range(3,-1,-1):
                inter_list.append(grid[row][col])
                
            if inter_list.count(0) !=4:     #check that the list isnt just zeros
                                               
                final_list=[] 
                while 0 in inter_list:
                    inter_list.remove(0)    #remove all the 0s from the list
                    
                    
                while len(inter_list) >0:
                    
                    if len(inter_list)>1:
                        if inter_list[0]==inter_list[1]:   #checks if the first two items in the list are equal
                            final_list.append(2*inter_list[0])     #append the merged value to the new list
                            inter_list.remove(inter_list[0])     #remove both values from the inter_list
                            inter_list.remove(inter_list[0])
                        else:
                            final_list.append(inter_list[0])     # add first item to final_list
                            inter_list.remove(inter_list[0])     #remove first from the inter_list
                            
                    if len(inter_list)==1:               #checks if there is one item left in interlist and adds it to final list
                        final_list.append(inter_list[0])
                        inter_list.remove(inter_list[0])
                        
                #ensure final_list has 4 items
                
                while len(final_list) <4:
                    final_list.append(0)     #fill the rest of list with zeros            
                                    
                 
                                    
                #replace values in original grid
                j=0
                final_list.reverse()
                for i in final_list:
                    grid[row][j]=i
                    j+=1                                  
    
    return grid









    
    
