npairs=0
def nrepeat(s):
    global npairs
    
    if len(s)<2:
        return(npairs)
    
    if s[0]==s[1]:
        npairs+=1
        return(nrepeat(s[2:]))
    
    else:
        return(nrepeat(s[1:]))
    
s=input("Enter a message:\n")
print("Number of pairs:",nrepeat(s))
    
