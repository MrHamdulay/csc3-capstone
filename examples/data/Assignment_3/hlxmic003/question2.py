# Michaela Heale
# Assignment 3 Question 2

h = eval(input("Enter the height of the triangle:\n"))

#EmptyPlaceHolder
star = ""
w = h+(h-1)
gap = w//2
for z in range(0,w,2):
    star = star + "" + (" "*gap) +"*"*(z+1)+"\n"
    gap-=1
    
print(star)
#OhMyGodAFuckingTriangle
#ImSoHipster
    
    