#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Pilusa
#
# Created:     08/03/2014
# Copyright:   (c) Pilusa 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    import math
    print('Approximation of pi:',round(math.pi,3))
    r=eval(input('Enter the radius:\n'))
    area=(math.pi)*r**2
    print('Area:',round(area,3))



if __name__ == '__main__':
    main()
