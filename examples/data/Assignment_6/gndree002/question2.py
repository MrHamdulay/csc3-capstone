A = input("Enter vector A:\n")
B = input("Enter vector B:\n")
A=A.split(" ")
B=B.split(" ")
type(A[0])
for i in range(0,3,1):
    A[i]=int(A[i])
    B[i]=int(B[i])
print("A+B = [",A[0]+B[0],", ",A[1]+B[1],", ",A[2]+B[2],"]",sep='')
print("A.B =",(A[0]*B[0])+(A[1]*B[1])+(A[2]*B[2]))
Art = ((A[0]**2)+(A[1]**2)+(A[2]**2))**(1/2)
Brt = ((B[0]**2)+(B[1]**2)+(B[2]**2))**(1/2)
print("|A| = %0.2f"%round(Art,2))
print("|B| = %0.2f"%round(Brt,2))