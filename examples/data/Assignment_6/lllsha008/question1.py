#Shaylan Lalloo
#Right aligns words

print('Enter strings (end with DONE):')

myword = ''

totwords = []

while True:
    myword = input()
    if myword == 'DONE':
        break
    totwords.append(myword)
    #reads input until sentinel is reached

print()
print('Right-aligned list:')
mylong = 0
for i in totwords:
    mylong = max(mylong, len(i))
#find longest word

for i in totwords:
    print(' ' * (mylong - len(i)) + i)
#output the spaces to make it th length of longest
    
