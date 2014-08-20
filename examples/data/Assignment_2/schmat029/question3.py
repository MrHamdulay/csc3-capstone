#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Matthias
#
# Created:     07-03-2014
# Copyright:   (c) Matthias 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

import math

app = 2
term = 2
denominator = math.sqrt(2)

while term > 1.0:
    term = 2 / denominator
    app *= term
    denominator = math.sqrt(2 + denominator)

print("Approximation of pi:", round(app,3))
radius = eval(input("Enter the radius: \n"))
print("Area:", round(app * radius **2, 3))

if __name__ == '__main__':
    main()
