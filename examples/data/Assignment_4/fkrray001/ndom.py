# Author : Rayaan Fakier FKRRAY001
# Date : 03 - 04 - 2014

def ndom_to_decimal(a):
    ndomstr = str(a)
    if len(ndomstr) == 3:
        thrd = int(ndomstr[2])
        scd = int(ndomstr[1]) * 6
        fst = int(ndomstr[0]) * 36
        dec = fst + scd + thrd
    elif len(ndomstr) == 2:
        scd = int(ndomstr[0]) * 6
        fst = int(ndomstr[1])         
        dec = fst + scd
    else:
        fst = int(ndomstr[0])        
        dec = fst
    return dec

def decimal_to_ndom(a):
    # Formula to convert to base 6
    plce = a // 6 
    u = a % 6
    plce2 = plce // 6
    t = plce%6
    plce3 = plce2 // 6
    h = plce2%6
    plce4 = plce3 // 6
    th = plce3%6
    ndom = str(th) + str(h) + str(t) + str(u) # Unedited ndom number
    for i in ndom:
        if int(i) == 0: # Removes initial unwanted 0's
            continue
        break # Breaks where i != 0 (so as to assign i the desired find value)
    ndom = ndom[ndom.find(i):] # Splices unwanted 0's
    return ndom

def ndom_add(a,b):
    addab = int(a) + int(b)
    
    plce = addab // 6 
    u = addab % 6
    plce2 = plce // 6
    t = plce%6
    plce3 = plce2 // 6
    h = plce2%6
    plce4 = plce3 // 6
    th = plce3%6
    ndomsum = str(th) + str(h) + str(t) + str(u) # Unedited ndom number
    for i in ndomsum:
        if int(i) == 0: # Removes initial unwanted 0's
            continue
        break # Breaks where i != 0 (so as to assign i the desired 'find' value)
    ndomsum = ndomsum[ndomsum.find(i):] 
    return int(ndomsum)

def ndom_multiply(a,b):
    def ndom_amul(a):
        plce = a // 6 
        u = a % 6
        plce2 = plce // 6
        t = plce%6
        plce3 = plce2 // 6
        h = plce2%6
        plce4 = plce3 // 6
        th = plce3%6
        ndoma = str(th) + str(h) + str(t) + str(u) # Unedited ndom number
        for i in ndoma:
            if int(i) == 0: # Removes initial wanted 0's
                continue
            break # Breaks where i != 0 (so as to assign i the desired find value)
        ndoma = ndoma[ndoma.find(i):]
        return int(ndoma)
    def ndom_bmul(b):
        plce = b // 6 
        u = a % 6
        plce2 = plce // 6
        t = plce%6
        plce3 = plce2 // 6
        h = plce2%6
        plce4 = plce3 // 6
        th = plce3%6
        ndomb = str(th) + str(h) + str(t) + str(u) # Unedited ndom number
        for i in ndomb:
            if int(i) == 0: # Removes initial unwanted 0's
                continue
            break # Breaks where i != 0 (so as to assign i the desired find value)
        ndomb = ndomb[ndomb.find(i):]
        return int(ndomb)
    ndommult = ndom_amul(a) * ndom_bmul(b)
    return ndommult
