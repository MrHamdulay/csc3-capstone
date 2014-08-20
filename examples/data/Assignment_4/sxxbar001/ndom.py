#Assignment 4
#Question 2
#Barry Su
#2 April 2014

import math

def ndom_to_decimal(num):
    step_1=num//100
    multiply_36=step_1*36
    divide_100=num-(step_1*100)
    step_2=divide_100//10
    if step_1==0 and step_2==0:
        output=num-4*(step_2 -1)
        return output
    
    if step_1==0:
        output2=num-4*step_2
        return output2
    
    if step_1>0:    
        step_3=step_2*4
        start=divide_100-step_3
        start_num=multiply_36+start
        return start_num

    
def decimal_to_ndom(num):
    base_6=0
    step_1=num//36
    difference=step_1*36
    new_num=num-difference
    step_2=new_num//6
    difference_4=step_2*4
    base_6_Number=step_1*100+new_num+difference_4
    return base_6_Number

def ndom_add(a,b):
    ConvertA=ndom_to_decimal(a)
    ConvertB=ndom_to_decimal(b)
    NewNum=ConvertA + ConvertB
    output=decimal_to_ndom(NewNum)
    return output
    
    
def ndom_multiply(a,b):
    ConvertA=ndom_to_decimal(a)
    ConvertB=ndom_to_decimal(b)
    NewNum=ConvertA*ConvertB
    output=decimal_to_ndom(NewNum)
    return output