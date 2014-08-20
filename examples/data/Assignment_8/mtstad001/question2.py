"""Fionna Mautsa
ass8 qstn2: checking for pairs
9th May"""
M=input("Enter a message:\n")
def pair(M,c):
    if len(M)==0 or len(M)==1:
        return c
    elif len(M)>1:
        if M[0]==M[1]:
            c+=1
            return pair(M[2:],c)
        elif M[0]!=M[1]:
            return pair(M[1:],c)
c=0

print("Number of pairs:",pair(M,c))