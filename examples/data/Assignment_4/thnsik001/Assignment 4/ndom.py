"""assignment4
question2
THNSIK001"""

def ndom_to_decimal(a):
    dec=0
    if a<6:
        dec = a
    else:
        ndom = a
        while ndom>=36:
            ndom = ndom-36
            dec+=100
        else:
            dec += ndom        
        while ndom>=6:
            ndom = ndom-6
            dec+=10
        else:
            dec += ndom
    print(dec)
    
def decimal_to_ndom(b):
    ndom=0
    if b<6:
        ndom = b
    else:
        dec = b
        while dec>=100:
            dec = dec-100
            ndom+=36
        while dec>=10:
            dec = dec-10
            ndom+=6
        else:
            ndom += dec
    print(ndom)    
    
def ndom_add(a,b):
    sumu=0
    sumt=0
    sumh=0
    bunit = b%10
    
    aunit = a%10
    
    if(aunit+bunit)<6:
        sumu = aunit + bunit
    else:
        sumu = aunit + bunit - 6
        sumt=10
    aten = a%100 - aunit
    bten = b%100 - bunit
    if(sumt+aten+bten)<40:
        sumt += aten + bten
    elif(sumt+aten+bten)>40:
        sumt = sumt + aten + bten -60
        sumh = 100       
    ahun = a- a%100
    bhun =b- b%100
    sumh += ahun + bhun
print(sumh+sumt+sumu)
    
def ndom_multiply(a,b):
    aunit = a%10
    bunit=b%10
    aten=a%100 - aunit
    bten = b%100 - bunit
    ahun = a - a%100
    bhun = b - b%100
    uprodu=aunit*bunit
    uprodt =aunit*bten
    uprodh =aunit*bhun
    tprodu =aten*bunit
    tprodt =aten*bten
    tprodh =aten*bhun
    hprodu =ahun*bunit
    hprodt =ahun*bten
    hprodh =ahun*bhun
    if(uprodu)>6:
        uprodt+=uprodu//6
        uprodu=uprodu%6
    if(uprodt>60):
        uprodh+=uprodt//60
        uprodt=uprodt%60
    if(tprodu)>60:
        tprodt+=tprodu//60
        tprodu=tprodu%60
    if(tprodt>600):
        tprodh+=uprodt//600
        tprodt=trodt%600 
    uprod = uprodu+uprodt+uprodh
    tprod = tprodu + tprodt+ tprodh
    hprod = hprodu+hprodt+hprodh
    ndom_add(uprod,tprod)
        