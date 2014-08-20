#Thembekile Dubazana
#Assignment 4 Ndom Conversion

def ndom_to_decimal(num):
        Sum=0
        i=0
        num=str(num)
        while i < len(num)-1:
                if i==0:
                        dig=int(num[i])
                        Sum=dig*6+Sum
                        i=i+1
                else:
                        dig=int(num[i])
                        Sum=Sum+dig
                        Sum=Sum*6
                        i=i+1       
        Fdig= int(num[-1])
        FSum=Sum+Fdig
        return FSum

def decimal_to_ndom (num):
        newnum=""
        rang=len(str(num))+1
        for i  in range(rang):
                dig=str(round(num%6,1))
                newnum=newnum+dig
                num=num//6
        revnum=newnum[::-1]
        return revnum

def ndom_add(num1,num2):
        num1=str(num1)
        num2=str(num2)
        k=len(num1)-1
        j=len(num2)-1
        Sum=""
        carry=0
        for i in range(3):
                digit=int(num1[k])+int(num2[j])+carry
                if digit < 6:
                        Sum+=str(digit)
                        k-=1
                        j-=1
                else:
                        digit1=str(digit+4)
                        Sum+=digit1[1]
                        carry=int(digit1[0])
                        k-=1
                        j-=1
        Sum=Sum[::-1]
        if Sum[0]=="0":
                Sum=Sum.replace(Sum[0],"")        
        return Sum        

def ndom_multiply(num1,num2):
        num1,num2=str(num1),str(num2)
        k,j=len(num1)-1,len(num2)-1
        mult1,mult2=0,0
        for i in range(len(num1)):
                mult1+=int(num1[i])*(6**k)
                k-=1
        for m in range(len(num2)):
                mult2+=(int(num2[m])*(6**j))
                j-=1
        num=mult1*mult2
        result=str(decimal_to_ndom (num))
        if result[0]=="0":
                result=result.replace(result[0],"")
        return result
        
    