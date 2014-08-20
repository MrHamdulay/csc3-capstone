#triangle
#Tofunmi Olagoke
#OLGMOF001
height=eval(input("Enter the height of the triangle:\n"))
FTri=height-1
STri=1
TTri=0

while FTri>=0 and STri<=height and TTri<=(height-1):
    print(" "*FTri,"*"*STri,"*"*TTri, sep="")
    FTri=FTri-1
    STri=STri+1
    TTri=TTri+1
    

