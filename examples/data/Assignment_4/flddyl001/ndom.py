def decimal_to_ndom(a):
    i = 1
    string = ""
    while a//(6**i) > 0:
        i = i + 1
    expo = 6**(i-1)

    dig = round(a//expo)
    
    string = string + str(dig)
    
    a = a - (dig*expo)
    print(a)
    
decimal_to_ndom (455)
