def ndom_to_decimal(a):
    hun=a//100
    ten=(a-100*hun)//10
    ans=(hun*36+ten*6+int(str(a)[-1]))
    return ans


def decimal_to_ndom(a):
    hun=a//36
    ten=(a-hun*36)//6
    ans=hun*100+ten*10+(a-hun*36-ten*6)%6
    return ans
 


def ndom_add(a,b):
    huna, hunb = a//100, b//100
    tena, tenb=(a-huna*100)//10, (b-hunb*100)//10
    
    doma=huna*36+tena*6+int(str(a)[-1])
    domb=hunb*36+tenb*6+int(str(b)[-1])
    add=(doma)+(domb)
    hunadd=add//36
    hunten=add-hunadd*36//6
    ans=(hunadd*100+(add-hunadd*36)//6*10+(add-hunadd*36-hunten*6)%6)
    return ans
   



def ndom_multiply(a,b):
    huna, hunb = a//100, b//100
    tena, tenb=(a-huna*100)//10, (b-hunb*100)//10
    
    doma=huna*36+tena*6+int(str(a)[-1])
    domb=hunb*36+tenb*6+int(str(b)[-1])
    add=(doma)*(domb)
    hunadd=add//36
    hunten=add-hunadd*36//6
    ans=(hunadd*100+(add-hunadd*36)//6*10+(add-hunadd*36-hunten*6)%6)
    return ans
    
