
#Dhriven Hamlall

def main():
    
    strings=[] #list
    d=input(("Enter strings (end with DONE):\n"))
    
    while d!="DONE":
        strings.append(d)
        d=input() #First list with duplicates
#=======================================================================================================        
    unique=[]
    for a in strings:
        if a not in unique: #will only put a word if doesn't exist in list yet 
            unique.append(a)
#=======================================================================================================    
    print()
    print("Unique list:")
    for z in unique:
        print(z)
#=======================================================================================================
main()
