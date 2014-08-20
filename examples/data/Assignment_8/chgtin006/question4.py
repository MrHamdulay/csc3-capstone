
def reverse(leng):
    number=str(leng)
    if len(number)==1:
        return number
    else:
        return number[-1]+reverse(number[:-1])

def check_equality(leng):
    num=reverse(leng)
    newnum=eval(num)
    if leng==newnum:
        True
    
counter =1
def prime(leng):
    answer=False
    if counter== leng:
        answer=True
    if leng==0 or leng==1:
        False
    if leng

    