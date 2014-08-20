"""counting the number of pairs of repeated characters in a string
Elizabeth Cilliers
14/05/05"""

def npairs(string,position,pairs):
          
          if string=="":
                    print("Number of pairs:",count) #print zero if input is space
          
          elif (position+1) < len(string):
                    if string[position] == string[position+1]: #if adjacent letters are the same
                              
                              if (position+2) < len(string): #take into account any 3 adjacent letters that are the same
                                        if string[position] == string[position+2]:
                                                  position += 2  #move position an extra one to account for the third letter that is the same  
                                                  pairs += 1
                                                  
                                        else:
                                                  position += 1
                                                  pairs += 1
                                                  
                              else:
                                        position += 1 
                                        pairs += 1
                              npairs(string, position, pairs)             
                                        
                    else:
                              position += 1
                              npairs(string, position, pairs)      
          
          elif position == (len(string)-1):
                    print("Number of pairs:", pairs)
                                     
          else:
                    position += 1
                    npairs(string, position, pairs)         
            


string= input("Enter a message:\n") 
position=0
pairs=0

npairs(string, position, pairs) 
