import math

Ax, Ay, Az = (int(a) for a in input("Enter vector A:\n").split(" "))
Bx, By, Bz = (int(b) for b in input("Enter vector B:\n").split(" "))
vector_add = [Ax + Bx, Ay + By, Az + Bz]
dot_product = Ax*Bx + Ay*By + Az*Bz
normA = math.sqrt(Ax**2 + Ay**2 + Az**2)
normB = math.sqrt(Bx**2 + By**2 + Bz**2)
print("A+B =", vector_add)
print("A.B =", dot_product)
print("|A| = {0:0.2f}".format(round(normA,2)))
print("|B| = {0:0.2f}".format(round(normB,2)))