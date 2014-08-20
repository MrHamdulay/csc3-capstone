
def rep_char(c):
    if len(c) == 1:#Base case
        return 0
    elif  len(c) > 2 and c[0] == c[1] and c[0] == c[2] :
        return rep_char(c[2:]) + 1
    elif c[0] == c[1]:
        return rep_char(c[1:]) + 1
    else:
        return rep_char(c[1:])
        
print("Number of pairs:",rep_char(c= input("Enter a message:\n")))       
    
    