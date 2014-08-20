'''Text file formater
Sbongakonke Mlangeni
16 May 2014'''
filename = input('Enter:\n')
fob = open(filename,'r')
lines = fob.readlines
fob.close()

print(lines)