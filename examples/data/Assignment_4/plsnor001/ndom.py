#-------------------------------------------------------------------------------
# Name:        ndom
# Purpose:
#
# Author:      Pilusa
#
# Created:     02-04-2014
# Copyright:   (c) Pilusa 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------


def decimal_to_ndom(num):
    count36=0
    count6=0
    count5=0
    while True:
        if num>=6 and num<36:
                num=num-6
                count6+=1
        elif num>=36:
                num=num-36
                count36+=1
        elif num<6 and num>=0:
                count5=num
                break
        else:
                print('invalid number')
                break


    if count36>=1:
        return str(count36)+str(count6)+str(count5)

    elif count6>=1:
        return str(count6)+str(count5)

    else:
        return str(count5)

def ndom_to_decimal (num):
    a=str(num)
    d=[]
    for i in a:
        d+=i
    if len(d)==3:
        k=int(d[0])*36+int(d[1])*6+int(d[2])

    elif len(d)==2:
        k=int(d[0])*6+int(d[1])

    else:
        k=(d[0])


    return k

def ndom_add (num1, num2):
    num1=ndom_to_decimal (num1)
    num2=ndom_to_decimal (num2)
    num=num1+num2
    result=decimal_to_ndom(num)
    return result


def ndom_multiply (num1, num2):
    num1=ndom_to_decimal (num1)
    num2=ndom_to_decimal (num2)
    num=num1*num2
    result=decimal_to_ndom(num)
    return result



if __name__ == '__main__':
    decimal_to_ndom(num)
