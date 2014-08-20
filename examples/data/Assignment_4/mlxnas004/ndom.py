def ndom_to_decimal(a):
    a = str(a)
    power = len(a)-1
    multiplier=0
    for i in a:
        fact=(int(i)*(6**power))
        multiplier+=fact
        power-=1
    #print(multiplier)
    return multiplier

def decimal_to_ndom(a):
    int(a)
    if a >= 6**5:
        five1=a//7776
        five=a%7776
    elif a < 6**5:
        five=a
        five1=0
    
    if five >= 216:
        if a > 7776:
            four1=five//216
            four=five%216
        else:
            four1=a//216
            four=a%216
    elif five<216:
        four=five
        four1=0
    if four >= 36:
        if a > 216:
            three1=four//36
            three=four%36
        else:
            three1=a//36
            three=a%36 
    elif four<36:
        three=four
        three1=0
                
    if three >= 6:
        if a > 36:
            two1=three//6
            two=three%6
        else:
            two1=a//6
            two=a%6
    elif three<6: 
        two = three
        two1=0
    if two >= 1:
        if a > 6:
            one1=two
            one=two%1
        elif a<=6:
            one1=two
            #print(one1)
            one=a%2
    elif two<1:
        one1=0
        #print(one1)
    
    #print(three1)
    #print(two1)
    #print(one1)
    final= (five1*10000)+(four1*1000)+(three1*100)+(two1*10)+(one1*1)
    return final
decimal_to_ndom(112)
    
def ndom_add(a,b):
    a = ndom_to_decimal(a)
    b = ndom_to_decimal(b)
    answer=int(a)+int(b)    
    answer1= decimal_to_ndom(answer)
    
    #print(answer1)
    return answer1
    
def ndom_multiply(a,b):
    a = ndom_to_decimal(a)
    b = ndom_to_decimal(b)
    answer=int(a)*int(b)
    answer2= decimal_to_ndom(answer)
    return answer2
    #print(answer1)
    
    
    

    
        

    