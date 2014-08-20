def decimal_to_ndom(ndom):
        decimal = ""
        decimal = str(ndom//36)
        if decimal == "0":
                decimal = ""
        ndom = ndom%36
        decimal += str(ndom//6)
        if decimal == "0":
                decimal = ""
        ndom = ndom%6
        decimal += str(ndom)
        
        return decimal
def ndom_to_decimal(num):
        decimal = 0
        if len(str(num))==3:
                y=(eval(str(num)[0]))*36
                decimal=y
                num2=(eval(str(num)[1]))*6
                decimal+=num2
                num3=(eval(str(num)[2]))
                decimal+=num3
                return decimal

        elif len(str(num))==2:
                num2=(eval(str(num)[0]))*6
                decimal+=num2
                num3=(eval(str(num)[1]))
                decimal+=num3
                return decimal
        
        else:
                decimal = num
                return decimal

def ndom_add(a,b):
        first_no=ndom_to_decimal(a)
        second_no=ndom_to_decimal(b)
        answer=first_no+ second_no
        answer=decimal_to_ndom(answer)
        return answer
def ndom_multiply(a,b):
        first_no=ndom_to_decimal(a)
        second_no=ndom_to_decimal(b)
        answer=first_no*second_no
        answer=decimal_to_ndom(answer)
        return answer