#Author: NLXALE001
#Date: 27 March 2014
#Assignment 3

h = eval(input("Enter the height of the triangle:\n"))
w = h*2
outstart = "{0: ^"
outend = "}"
out = outstart + str(w) + outend
star = 1
for x in range(0, h):
    prinstar = "*"*star
    print(out.format(prinstar))
    star = star+2