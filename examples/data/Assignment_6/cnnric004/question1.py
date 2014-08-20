userInput = input("Enter strings (end with DONE):\n")
A = []
length = 0
stringsInputed = False
while(userInput!="DONE"):
    A.append(userInput)
    length+=1
    userInput = input("")
    stringsInputed = True

print("\nRight-aligned list:")
if(stringsInputed):
    maxLength = len(A[0])
    for i in range(1,len(A)):
        if(len(A[i])>maxLength):
            maxLength = len(A[i])
    for j in range(len(A)):
        print(" "*(maxLength-len(A[j])),A[j],sep="")