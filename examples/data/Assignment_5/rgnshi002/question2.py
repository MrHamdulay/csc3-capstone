
#Shivam Ragoonaden
#Calculate change from a given cost and deposit

v = 1
w = 5
x = 10
y = 25   #Different coins
z = 100

Cost = eval(input("Enter the cost (in cents):\n"))

Sum = 0  #0 at the beginning as nothing has been deposited yet

while Sum < Cost:  
    #Input coins/notes
    inp = eval(input("Deposit a coin or note (in cents):\n"))
    Sum += inp  
else:
    #Do change
    change = Sum - Cost
    if change != 0:   #If there is any change to be given
        print("Your change is:")        
    #Split change into coins
    rest = change    #Initialise "rest of amount" as "change"
    
    r = change//z   
    if r != 0:   #Check if divisible by 100
        rs = str(r)
        print(rs + ' x $1')
        rest = change - r*z  #Take out the hundreds/thousands etc and leave only tens and units
        
    if rest != 0:  #Is there any change left
        r = rest//y
        if y != 0:
            rs = str(r)
            if r != 0:
                print(rs + ' x 25c')   #Repeat same for each coin:
                rest = rest - r*y            
                
    if rest != 0:
        r = rest//x
        if x != 0:
            rs = str(r)
            if r != 0:
                print(rs + ' x 10c')
                rest = rest - r*x   
                        
    if rest != 0:
        r = rest//w
        if w != 0:
            rs = str(r)
            if r != 0:
                print(rs + ' x 5c')
                rest = rest - r*w   
                                
    if rest != 0:
        r = rest//v
        if v != 0:
            rs = str(r)
            if r != 0:
                print(rs + ' x 1c')
                rest = rest - r*v                                 