"""ndom to decimal/decimal to ndom convertor
ringo shima
4/a/14"""

def ndom_to_decimal(num): #prompts user for input without asking "enter num"
    #give values a starting point
    ans = 0 
    numStr = "" #empty string of number
    
    
    if num < 1000:
        numStr = str(num) #converts num to str value
        if len(numStr) == 3: #checks numbers from 100-999
            ans = ans +(eval(numStr[0])*36) + (eval(numStr[1])*6) + (eval(numStr[2])*1)
            #print(ans) #test with 900
        elif len(numStr) == 2:
            ans = ans + (eval(numStr[0])*6) + (eval(numStr[1])*1)
            #print(ans) test with 20
        elif len(numStr) == 1:
            ans = ans + (eval(numStr[0])*1)
            #print(ans) 
        return ans


def decimal_to_ndom(num):
    ans = 0
    numStr = ""
    a = 1
    b = 1
    c = 1
    
    if num < 1000:
        numStr = str(num)
        if len(numStr) == 3: #use 196 ans = 524
            a = num // 6 #196/6=32...
            aRem = num % 6 #rem = 4
            b = a // 6 #32/6=5...
            bRem = a % 6 #rem = 2
            c = b // 6 # 5/6=0...
            cRem = b % 6 #rem = 5
            ans = str(cRem) + str(bRem) + str(aRem) # 5+2+4 (decimal value)
            #print (ans)
    
        elif len(numStr) == 2: #90 ans=230
            a = num // 6 #90/6 = 15..
            aRem = num % 6 #rem = 0
            b = a // 6 # 15/6 = 2..
            bRem = a % 6 #rem = 3
            ans = str(b) + str(bRem) + str(aRem) #2+3+0
            if int(ans) < 100:
                ans = str(bRem) + str(aRem) #writes numbers 014-099 as 14-99
            #print (ans)            
        
        elif len(numStr) == 1:
            if num < 6:
                aRem = num % 6   
                ans = str(aRem)
            else:
                aRem = num % 6   
                ans ='1' + str(aRem)                     
            #print(ans)
    return ans

def ndom_add (num1, num2):
    num1 = ndom_to_decimal(num1)
    num2 = ndom_to_decimal(num2)
    ans = num1 + num2
    ans = decimal_to_ndom(ans)
    return ans

def ndom_multiply (num1, num2):
    ans = 0
    num1 = ndom_to_decimal(num1)
    num2 = ndom_to_decimal(num2)
    ans = num1 * num2
    ans = decimal_to_ndom(ans)
    return ans