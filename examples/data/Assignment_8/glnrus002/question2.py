#GLNRUS002
#aSSIGNMENT 8
#QUESTION 2
#COUNT NUMBER OF OCCURANCES OF DOUBLE PATTERNS
num=0#used for counting num o recurances

def counter(m):
    global num
    l=len(m)
    if l==1:#too short for comparing
        return num

    if (m[0]==m[1]):#if same
        num+=1
        counter (m[1::])#removes front character
    elif m[0]!=m[1]:#if not same
        counter(m[1::])     #still remove character     
    return num
######User interaction###########
msg=input("Enter a message:\n")
num=counter(msg)
print("Number of pairs:",num)