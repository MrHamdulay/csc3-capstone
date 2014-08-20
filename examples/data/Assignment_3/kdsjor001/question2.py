height=eval(input('Enter the height of the triangle:\n'))
i=1
space=height-1
g=1
while g<=height:
    print (' '*space+i*('*'))
    i+=2
    space-=1
    g+=1