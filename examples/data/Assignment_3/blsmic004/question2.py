# Draw triangle with given height
# Michele Balestra BLSMIC004
# 23 March 2014

height = eval(input("Enter the height of the triangle:\n"))
gap = height - 1
st = 1
for i in range(height):
    print(" " * gap, "*" * st, sep="")
    gap = gap - 1
    st = st + 2