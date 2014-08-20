"""Shriya Roy
23 April 2014
printing out a string"""



def main():
    #create an empty list
    names=[]
    #get input from user
    strings=input("Enter strings (end with DONE):\n")
    
    length_max=""
    #append the list
    while strings!= "DONE" :
        names.append(strings)
        strings=input("")
        
        #finding the maximum string
    count=0   
    for name in names:
        length=len(name)
        if length>count:
            count=length
        

        
    print()
    print("Right-aligned list:")
    
    #formatting and printing in a right-aligned list
    for name in names:
        output="{0:>{1}}".format(name,count)
        print(output)
        
main()
        