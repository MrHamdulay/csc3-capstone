# Kieran Reilly, RLLKIE001
# functions of Ndom conversions and basic arithmatic
# 31/03/03

def decimal_to_ndom(a):
    baseTen = a
    out = ""
    
    
    devident = int(baseTen/6)
    remainder = baseTen - (devident*6)
    out = ""+str(remainder)
    
    length = len(str(baseTen))
    for i in range(length):
        newDevident = int(devident/6)
        remainder = devident - (newDevident*6)
        if remainder != 0:
            out = str(remainder) + out
        devident = newDevident
        ndom = int(out)
    return ndom
          

def ndom_to_decimal(a): 
    ndom = a
    length = len(str(ndom))
    baseTen = 0.0
    
    baseTen = float(str(ndom)[0])
    
    for i in range(1, length):
        baseTen = (baseTen*6)+int(str(ndom)[i])
    baseTen = int(baseTen)
        
    return baseTen
    
    
def ndom_add(a,b):
    ndomA, ndomB = a, b
    
    baseTenA = ndom_to_decimal(ndomA)
    baseTenB = ndom_to_decimal(ndomB)
    
    sumNdom = baseTenA + baseTenB
    finalNdom = decimal_to_ndom(sumNdom)
    
    return finalNdom
    
    
def ndom_multiply(a,b):
    ndomA, ndomB = a, b
    
    baseTenA = ndom_to_decimal(ndomA)
    baseTenB = ndom_to_decimal(ndomB)
    
    multiply = baseTenA*baseTenB
    multiply = decimal_to_ndom(multiply)
    
    return multiply


if __name__ == "__main__":
    choice = input("Choose test: \n")
    length = len(choice)
    
    print("calling function")
    if length <= 5:
        if choice[0] == "d":
            a = choice[2:]
            print("called function")
            print(ndom_to_decimal(int(a)))
            
        if choice[0] == "n":
            a = choice[2:]
            print("called function")
            print(decimal_to_ndom(int(a)))
    if length > 5: 
        if choice[0] == "a":
            char, a, b = choice.split()
            print("called function")
            print(ndom_add(int(a),int(b)))
        if choice[0] == "m":
            char, a, b = choice.split()
            print("called function")
            print(ndom_multiply(int(a),int(b)))