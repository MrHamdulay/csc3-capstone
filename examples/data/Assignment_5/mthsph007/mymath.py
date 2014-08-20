""" Sphiwe Muthembi
Student no: MTHSPH007
 Assignment 5 - Question 3 <MYMATH> """

def get_integer(opt):
    if opt == "n":
        
        ans= input("Enter n:\n")
        
        while not ans.isdigit()  : 
            ans= input("Enter n:\n")
        ans= eval(ans)
        return ans
    elif opt == "k":
        
        kans= input("Enter k:\n")
        
        while not kans.isdigit():
            kans= input("Enter k:\n")
        kans = eval(kans)
        return kans

    
def calc_factorial(val):
    factorial = 1

    for i in range(1,val+1):
        factorial*= i
    return factorial
    

#get_integer(n)    
#n= get_integer("n") 
#k= get_integer("k")
#calc_factorial(n)    
