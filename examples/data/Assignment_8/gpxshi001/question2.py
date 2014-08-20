"""
-GPXSHI001
-Ass8
-Q2

"""


stuff=input("Enter a message:\n")

def pairing(stuff):
    
    if stuff=="":
        return 0
    
    elif(len(stuff)==1):
        return 0
    
    else:
        
        if stuff[0]==stuff[1]:
            stuff=stuff[2:]
            return 1+ pairing(stuff)
        
        else:
            return pairing(stuff[1:])
        
x= pairing(stuff)
print("Number of pairs: " +str(x))