#WHTBAS001
#30-03-2014
#ASSIGNMENT 4
#QUESTION 2

def decimal_to_ndom(a):
    nu = a%6
    ns1 = (a//6)% 6
    ns2 = (a//36)% 6
    ns3 = (a//216) % 6
    nfinal = nu + ns1*10 + ns2*100 + ns3*1000
    return nfinal

def ndom_to_decimal(a):
    du = a%10
    ds1 = (a//10)% 10
    ds2 = (a//100)% 10
    ds3 = (a//1000) % 10
    dfinal = du + ds1*6 + ds2*36 + ds3*216
    return dfinal    
    
def ndom_add(a,b):
    aau = a%10
    aas1 = (a//10)% 10
    aas2 = (a//100)% 10
    aas3 = (a//1000) % 10
    aafinal = aau + aas1*6 + aas2*36 + aas3*216
    abu = b%10
    abs1 = (b//10)% 10
    abs2 = (b//100)% 10
    abs3 = (b//1000) % 10
    abfinal = abu + abs1*6 + abs2*36 + abs3*216
    adecad = aafinal + abfinal
    au = adecad%6
    as1 = (adecad//6)% 6
    as2 = (adecad//36)% 6
    as3 = (adecad//216) % 6
    afinaladd = au + as1*10 + as2*100 + as3*1000
    return afinaladd 
    
    
def ndom_multiply(a,b):    
    mau = a%10
    mas1 = (a//10)% 10
    mas2 = (a//100)% 10
    mas3 = (a//1000) % 10
    mafinal = mau + mas1*6 + mas2*36 + mas3*216
    
    mbu = b%10
    mbs1 = (b//10)% 10
    mbs2 = (b//100)% 10
    mbs3 = (b//1000) % 10
    mbfinal = mbu + mbs1*6 + mbs2*36 + mbs3*216
    
    mdecmul = mafinal*mbfinal
    meu = mdecmul%6
    mes1 = (mdecmul//6)% 6
    mes2 = (mdecmul//36)% 6
    mes3 = (mdecmul//216) % 6
    mfinalmul = meu + mes1*10 + mes2*100 + mes3*1000
    return mfinalmul