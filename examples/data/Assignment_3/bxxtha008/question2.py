#question2.py
#Outeur: Thabiso Beau
#Datum: 24 Maart 2014
#Program om area van driehoek te kry

Tri_height = eval(input("Enter the height of the triangle: "))
for i in range(Tri_height+1):
    print (" " * (Tri_height), i*"*",(i-1)*("*"),sep="")
    Tri_height -= 1