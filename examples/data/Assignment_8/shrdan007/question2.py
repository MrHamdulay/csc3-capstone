# counts the number of pairs of repeated characters in a string
# Danielle Sher

x = input("Enter a message:\n")

def count_pairs(x, count1 = 0):
   
    if x == x[-1] or x == "":
        print("Number of pairs:", end = ' ')
        return count1 
    if x[0] == x[1] and len(x) > 2:
        
        return count_pairs(x[2:], count1 + 1)
    
    if x[0] == x[1] and len(x) == 2:
        return count_pairs(x[-1], count1 + 1)
        
       
    else:
        return  count_pairs(x[1:], count1 + 0)
    
   
    
    
   
print (count_pairs(x))